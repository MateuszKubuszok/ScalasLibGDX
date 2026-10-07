# LLS (Low Level Scala): history, evolution, and tooling gaps

Repo: `/Users/dev/Workspaces/kubuszok/lls` (github.com/kubuszok/lls), 92 commits, 2026-05-14 to 2026-09-27.
Artifacts: `com.kubuszok %% lls`, `lls-io` (from 0.3.0), `lls-port` (from 0.3.0-50 snapshot). Scala 3, JVM + Scala.js + Scala Native.
Companion report: `natives-multiarch.md`, which covers SGE natives, multiarch-scala, and sbt-kubuszok. This report does not repeat it.
Sources: lls/sge/ssg/balticporter/sbt-kubuszok/multiarch-scala git history; `lls/CLAUDE.md`, `lls/README.md`, `lls/.rescale/data/issues.tsv`,
`lls/docs/plans/2026-07-lls-io.md`; `FABLE5_PLANNING_ROADMAP.md`; Claude memories (balticporter `lls-port-decision.md`,
`post-green-progress.md`, `parity-campaign.md`, `multiarch-scala-target.md`; sge `campaign-state.md`, `remediation-progress.md`);
and the prompt log `prompts.txt`. The prompt log only starts on 2026-06-18, after the history wipe, so there is no prompt record of the May creation.

---

## 1. What LLS is and what was extracted

### 1.1 Definition
From `README.md`: "Cross-platform (JVM, Scala.js, Scala Native) low-level utilities for Scala 3, focused on avoiding allocations,
boxing, and reflection." It also says: "This library extracts and optimizes core data structures originally ported from libGDX to
Scala 3 as part of SGE … The goal is to provide these structures as a standalone, dependency-free library usable by any Scala 3
project — not just game engines."

Packages: `lowlevel` (Nullable, MkArray, ArrayView), `lowlevel.util` (collections, Eval, Resource, Sort, Select),
`lowlevel.math` (MathUtils), `lowlevel.io` (lls-io), `lowlevel.port` (lls-port).

### 1.2 Pre-history inside SGE
These types lived in SGE as `sge.utils.*` and `sge.math.*`:
- `Nullable`, `ObjectMap`, `Eval`, `Resource` arrived with SGE's first commit, `e1aff235` (2025-07-01), "Initial project: convert audio, files, math, input, net, utils from LibGDX Java to Scala 3".
- `Nullable` was hardened in `2195dc22` (2025-08-31), "Fix Nullable for nested nullable safety".
- `MkArray` and `DynamicArray` came in `39b464c1` (2026-02-24). SGE migrated onto `DynamicArray` in `d5aa9019` (2026-02-27).

### 1.3 The extraction (2026-05-14 to 2026-05-17)

| Date | Commit | What |
|---|---|---|
| 2026-05-14 | lls `3d0fc4a` | "Initial project setup, port from SGE, and benchmarks module": Scala 3.8.3 projectmatrix, CI on 6 JVM + 5 Native + 1 JS platforms, Maven Central. It ported **16 files** from SGE and renamed the namespaces (`sge.utils/math → lowlevel.util/math`): Nullable, MkArray, Eval, Resource, DynamicArray, ArrayMap, ObjectMap, ObjectSet, OrderedMap, OrderedSet, MathUtils, Sort, TimSort, ComparableTimSort, Select, QuickSelect. It also brought 7 test files and replaced `SgeError.InvalidInput` with `IllegalArgumentException`. A JMH module (`lls-bench`, 8 benchmark classes) came with it. 8,989 lines added. |
| 2026-05-14 | `4c31094` | "Eliminate boxing via sealed MkArray hierarchy and inline specialization". It added `OfInts`, `OfLongs` and similar final subclasses, the `MkArray.withResolved` polymorphic-function pattern, inline predicates, and MkArray threading through Sort, TimSort, Select and QuickSelect. |
| 2026-05-14 | `72c0664` | Tests for Nullable, Eval, Resource, MkArray and MathUtils. |
| 2026-05-14 | `eb0ccfc` | **ArrayView**, a new lls-only type: an opaque type over `Array[A]` with type-level booleans and all methods inline. The commit quotes "zipWithIndex foreach 12.6x faster, filter+map 2.0x faster" against the stdlib at size 10000, with 49 tests. |
| 2026-05-15 | `d3a9582` | Added `Nullable.Null` and `toOption` "for SSG". CI moved from Java 17 to Java 25 because 17 was "unavailable on windows-11-arm runners". |
| 2026-05-15 | sge `85b0a8a3` | "Migrate from bundled utilities to lls library": 884 files changed, −10,085 lines. SGE adopted `leanView` (ArrayView) in hot paths, removed the test suites now in lls, and added an lls skill (`/guide-lls-types`). |
| 2026-05-16 | ssg `45e5494b` | **Second consumer**: "Migrate Nullable from ssg-commons/ssg-liquid to lls (lowlevel.Nullable)". |
| 2026-05-16 | lls `0715651`, **tag 0.1.0** | "Replace manual plugin setup with sbt-kubuszok". lls adopted sbt-kubuszok on the day the plugin was created (sbt-kubuszok `a59e2d0`). |
| 2026-05-17 | sge `01b50507` | Bumped lls from SNAPSHOT to 0.1.0. Packaging docs were disabled because "scaladoc crashes on Scala 3.8.3". |

**What was *not* extracted:** no buffers and no natives. `BufferUtils`, ETC1, gdx2d and the Panama/Rust layer stayed in SGE (`sge.platform.*`) and in
multiarch-scala; see natives-multiarch.md §1. LLS is the pure-Scala, zero-dependency bottom layer. The extracted set is the
libGDX utilities collections (Array → `DynamicArray`, ObjectMap/Set, OrderedMap/Set, ArrayMap), sorting and selection, `MathUtils`, and
SGE's own design types (`Nullable`, `MkArray`, `Eval`, `Resource`). The canonical mapping table is `sge/docs/contributing/type-mappings.md`
§"Types Extracted to lls".

### 1.4 Why a separate library
- **Reuse across projects.** SSG (the static-site generator) needed the same `Nullable` within a day (`d3a9582` "for SSG", ssg `45e5494b`).
  `sge/CLAUDE.md:169` says: "Shared zero-allocation types extracted from `sge.utils.*`. Changes to `lowlevel.*` types go to lls, not sge."
- **Performance engineering in isolation.** The extraction was immediately followed by the boxing-elimination and ArrayView work, plus a JMH
  module, none of which existed in SGE.
- **Platform-neutral home.** In July, lls was chosen over a new repo or multiarch for shared path/file code because it "already hosts the
  shared `lowlevel.*` types both repos consume, has a working release pipeline (tag → `sbt ci-release`), and a Windows CI matrix that
  ssg lacks" (`docs/plans/2026-07-lls-io.md` §1.1).
- **API as a contract.** `lls/CLAUDE.md` says: "sge and ssg depend on it, so its public API is a contract." MiMa was enabled through sbt-kubuszok.

---

## 2. Everything done with LLS

### 2.1 Phase A: hand-written library, maintenance and the sbt 2 move (May to June)
- 2026-05-22 `511dac2`: refactored onto sbt-kubuszok 0.2.0.
- June: dependency bumps from Scala Steward and Dependabot (munit, scalafmt, Scala 3.8.4 in `a02093b` on 06-06, and Actions).
- **ISS-686, a critical cross-repo bug.** On 2026-06-19, SGE's new FrameBuffer coverage found that `DynamicArray.foreach`, `exists`, `find`, `count`,
  `forall` and `indexWhere` crashed with `ClassCastException: [Ljava.lang.Object; cannot be cast to [L<Bound>;` whenever the backing array was `Object[]`
  and the element type had a non-AnyRef bound. "This … blocked every sge FrameBuffer build (GLFrameBuffer.build:302)."
  The fix was lls `547e624` (2026-06-19): `withResolved` witnesses `B = AnyRef` in its ref and fallback branches, plus `DynamicArrayAbstractRefTest`.
  The bug had been "hidden by the zero-test gap" (sge memory `remediation-progress.md`). SGE could not land its suite until lls was released,
  because "sge CI resolves lls 0.1.0 from a REMOTE" (sge `campaign-state.md`). sge closed it on 2026-06-21 (`bf1d6fdf`: "FrameBuffer CCE fixed by lls 0.2.0").
- 2026-06-20 `22aef5c`, `3c7eb08`, `902002a`, `0447d63`: **migration to sbt 2.0** with sbt-kubuszok 0.2.3, released as **0.2.0** (tag on `0447d63`).
  The `build.sbt` comments document the friction (see §3).
- 2026-06-29 `e151311`: committed Claude settings that disable the session-URL/attribution footer (#66504).

### 2.2 Phase B: lls-io (July)
- 2026-07-01: plan written in the "Fable-5 planning window" (`FABLE5_PLANNING_ROADMAP.md` Topic 1). It went through an Opus dry-run gate on 2026-07-02
  (`37b6c34`: "fix 4 dry-run-gate defects … gate verdict EXECUTABLE") and got a drive-lift addendum the same day (`3fab5ad`, ssg ISS-1383 evidence).
- 2026-07-03, executed in steps:
  - `df0c5b5` L1: shared POSIX-string `FilePath` with UNC and drive rules.
  - `32e18c3` L2: `FileOps`, JVM/Native platform implementations, and the nio bridge.
  - `e14b5f9` L3: the Scala.js `FileOps` on Node.
  - `87b6d99`: gate fixes.

  The roadmap reports "452 tests green ×3 platforms, audit PASS incl. mutations + 33/33 ssg-suite mapping".
- **Tag 0.3.0 on 2026-07-07**: "lls 0.3.0 — add lls-io module (cross-platform FilePath + FileOps for JVM/JS/Native, ported from ssg-commons)".
  This is the **last tagged release**.
- **Adoption never happened.** The plan required ssg's `ssg.commons.io` to become a deprecated shim (§1.2, step S1) and SGE to delegate (G1).
  Today neither ssg nor sge references `lowlevel.io` (`git grep` returns empty). ssg kept fixing its own copy: ISS-1384 JS/Native drive-lift, and
  `180d961a` (2026-09-21) "java.nio.file.Path is ssg.commons.io.FilePath throughout". On 2026-09-16 the user asked: "Isn't FileHandle defined in lls, in a cross-platform way?"

### 2.3 Phase C: the move to Baltic Porter (September)
**Decision (2026-09-05).** Prompt: "Make lls as baltiporter artifact, usafle first, and use that to find order the first items of the ladder, then use
lls as basis for the rest of libgdx porting". On 2026-09-06: "Let's cover all utilities, but let's also enrich them with APIs added by lls".
The Balticporter memory `lls-port-decision.md` records it: "lls becomes a corpus port … generated from libGDX's 12 utils/math sources … five
hand-written originals Nullable, MkArray, ArrayView, Eval, Resource stay hand-written". The rationale: the gdx retarget tables ("10 rewrite variants,
~437 boundary rows") were "a hand-maintained shadow of lls's redesign". The bar was later relaxed under the demo goal: "lls's own design stands
(MkArray type class, Nullable, final, factories)". `parity-campaign.md` frames the whole effort: "The hand ports (sge, lls) were LLM-written, cheated
in places", the deadline is **Scala Days 2026 (12–13 Oct)**, and the order is "**lls FIRST** … the base beneath the rest of the port."

Balticporter work on lls (2026-09-05/06):

| Commit | Change |
|---|---|
| `c1955af7` | census port: "100 errors, api-parity 868 rows … lls suite 149 compile errors" |
| `88470116` | L0: 19 files, "149 -> 0 JVM errors; the first ladder artifact compiles" |
| `b8a9a2ba` | rung experiments on nullable and ordering |
| `96144a35` | "enrichment rung (lls's added members …) + lls-diff differential suite -- 282 members, diff 191/189/2" |
| `5f2b4a75` | ElementWitnessTransform, the MkArray-style array type class |
| `ec62c3f1` | narrowed to "the 12 files the real lls declares (K43 CLOSED)" |
| `564e877e` | "THE LADDER written — 15 rungs on the lls base" |

lls was used to order the ladder by measurement.

**Integration into the lls repo (2026-09-11).** Prompt at 13:33: "in lls repositody make a branch … make lls store submodule to libgdx … configure sbt there to
use balticporter to generate lls implementation and tests … compilation and tests should pass".
- `6cc2226` (14:15) "integrate Baltic Porter as sourceGenerator for the twelve ported libGDX sources": libGDX became a submodule (`original-src/libgdx` @ 4b4d2c4)
  and `project/BalticPorterGen.scala` was added. **−5,385 lines** of hand-ported code. Main compiles on all three platforms (6 hand-written + 24 generated files), but
  "Test Compile has 265 errors".
- `e25a29c` (14:43, 28 minutes later) "fix: adapt lls test suite for machine-ported API — 265->0 compile errors, 132 pass / **23 ignored**". It rewrote the tests to the
  libGDX spellings: `first→head`, `JInt` bounds, `Nullable` returns, inclusive `removeRange`, and exception types. It added `.ignore` to 23 tests "for known
  generated-code limitations": primitive-backed sort/equals CCE, "Abstract-ref Object[]-backed foreach/exists/find: **same CCE regression**" (the ISS-686 regression
  tests from June), and opaque primitive keys.

**CI hardening (2026-09-15).** Commits `6ef40af` through `cc8d301`, roughly 14 of them. The user objected to a workaround (prompt 2026-09-15 09:45): "lls - if lls-bench is incompatible, it should be fixed rather
than ignored! it goes against all good practices and our principles with this whole work!". The ignore attempt `1b8b095` was reverted (`a75fda7`) and the bench was fixed properly (`ba37bfb`).
At 17:17 the user asked: "Spawn an agent dedicated to fixing lls build, it should pass locally before pushing on CI". `630d0db` fixed JS TimSort and Native Windows UNC (§3).

**Discovery of the 23 hidden ignores (2026-09-19).** It started with a defect report (`efa28e1`, ISS-004: `DynamicArray[Int].sort` threw CCE). Engine fix `ac4ca83f` followed, then lls `52e2a99`.
`post-green-progress.md` Update 5 records: "**lls had 23 tests marked `.ignore` by an earlier agent ("machine-ported has the bug") hiding all of this — un-ignored, all pass**".
The KEY LESSON recorded there: "an `inline def` added by the lls policy is compiled INTO THE CALLER". lls snapshot 0.3.0-42 broke 15 sge tests with `Object[] cannot be cast
to String[]`, and `consumers-check` had "compiled sge against the OLD published lls and missed this". Fixes:
- Engine `971be58b`: "inline members never cast the backing array … (lls: 23 ignored tests run again, **570 -> 593 passing**; sge against the new lls: 15 failed -> 0)".
- lls `1459e14` (2026-09-19): removes all 23 `.ignore` markers.
- Balticporter `ebfea845`: consumers-check now builds each consumer against the previous one's freshly published artifact.

Engine issue #26 notes a remaining counting gap: "consumers that generate at build time get no findings report at all."

**Performance verification (2026-09-18/19).**
- Balticporter memory F: the parked javap test showed "ALL FOUR README claims fail". The generated `foreach` became a plain `def f(g: T => Unit)`.
- Fixes: engine `7b370c93` and `9271fd72` (inline-with-inline-function), lls `aa86c5c` "The README's overhead claims, checked against bytecode". This added `OverheadClaimsSuite` (javap -c) and a README downgraded to "what holds".
- JMH, hand-written vs generated on one machine (ISS-002): "113 rows same, 42 faster, 34 slower; the large regressions (traversals through iterators up to 34x, boxed Int lookups 2.5x) fixed". Fixed by engine `6736bd10`, `dae0bbc7`, `e589702b` and lls `bd1425b`; benchmarks restructured in `550b886`.

**Policy ownership (2026-09-21).** Prompt: "Goal is to make baltipcorter library agnostic … for ssg/sge/lls to make updates to their config without publishig a new balticporter artifact."
- `e62014a`: `lls-port`, the porting policy (`LlsMigrate`, `LlsEnrich`, `LlsPrimitiveArrays`, `GdxCoreClasspath`; 759 lines), moved into lls.
- `b485fe9`: compiled into the meta-build, "generated code byte-identical, 24 files".
- `4a43cc0`: published as a JVM module that sge's port extends.
- Balticporter `7d65fd6e` / `74c286af` (2026-09-22) deleted the corpus copies: "279 files, 47253 lines" and "248 files, 87993 lines".
- One incident: the user's lls checkout "vanished and was re-cloned"; 13 local branches were restored from `.balticporter/lls-local-branches.bundle`.

**Pin bumps (2026-09-24 to 2026-09-27).** `d48c5fe` through `d32ce62` bump `balticporter-engine` and republish `lls-port`.
- `4e632c1`: "lls-port must be republished against it before sge pins it".
- Balticporter `d7b5cf4e`: "sge #155 NoSuchMethodError on lls-port after PortManifest gained a parameter".
- `ca78e90e` pin: "owned T* binds through the element's ClassTag on Scala.js".

**Agent infrastructure (2026-09-18).** `9f4e529` added `CLAUDE.md` working rules, the Balticporter Claude Code plugin with a push hook that requires `verifyLocal`, and the re-scale issue table.
The issue table had 3 entries carried over from older notes, 2 of which were obsolete (the rest of ISS-001…006 were filed afterwards). The current rule: "Never edit a generated file, and never patch a hand-written file to fit a generated defect."

### 2.4 Releases and consumer pins

| Version | Date | Content |
|---|---|---|
| 0.1.0 | 2026-05-16 | extraction + MkArray/ArrayView + sbt-kubuszok |
| 0.2.0 | 2026-06-20 | ISS-686 fix + sbt 2.0 |
| 0.3.0 | 2026-07-07 (tag) | lls-io |
| 0.3.0-45-g1459e14-SNAPSHOT | 2026-09-19 | first generated release used by sge (sge `c5c6915a`) |
| 0.3.0-50-ged7e53f-SNAPSHOT | 2026-09-21 | publishes lls-port (sge `7ff6ddc6`: "0 differing lines over 657 files") |
| 0.3.0-57-gd32ce62-SNAPSHOT | 2026-09-27 | current ssg pin (`ssg/project/Versions.scala:26`); sge pins -50 |

There has been **no tagged release since 0.3.0**. The generated lls exists only as snapshots, because lls-port and the generator depend on a `balticporter-engine` *SNAPSHOT* (`project/plugins.sbt`).

Today the repo has 7 hand-written main files (ArrayView, MkArray, Nullable, Collections, Eval, ObjectArrays, Resource), 24 generated files, and 21 test files.
Tests stand at about 593 JVM / 578 JS / 583 Native with 0 ignored (memory, 2026-09-21).

---

## 3. Tooling gaps hit while building LLS, and where they went

LLS has no native code, so it fed **no feature directly into multiarch-scala**: multiarch-scala has no lls references beyond a note in a plan
(`docs/plans/2026-07-native-flags-and-collisions.md:560`). LLS sits on the other side of the same rule. The memory `multiarch-scala-target.md` (2026-08-14) says
"platform-divergent JDK families" (ServiceLoader, JNI loading) go to multiarch-scala, while pure-Scala portable code goes to lls. lls-io is the
borderline case: file I/O differs per platform, but it was solved in pure Scala on Node `fs` and java.nio, so it went to lls instead (Topic 1).
The gaps LLS hit were absorbed by **sbt-kubuszok** (build), **Baltic Porter** (codegen workarounds), and lls's own `build.sbt`:

| Gap | Evidence | Where handled | Status |
|---|---|---|---|
| Boilerplate of cross-building JVM/JS/Native (projectmatrix, publishing, MiMa, CI aliases) | lls `0715651` on the same day as sbt-kubuszok `a59e2d0` (2026-05-16) | sbt-kubuszok | resolved |
| sbt 1 to sbt 2 move: plugins must cross-build, `Def.uncached`, SNAPSHOT-publish guard | sbt-kubuszok `5229a2f` (2026-06-20); lls `22aef5c` | sbt-kubuszok 0.2.3 | resolved |
| sbt 2 `test` is incremental and machine-cached, so "a CI run that begins with `clean` can still report 'No tests to run' and pass vacuously" | `build.sbt` `fullTests` rewrites to `testFull` | lls build.sbt (local workaround) | worked around |
| sbt 2 + scoverage + `fork := true`: `scoverage-data` dir is not pre-created, so every test crashes with FileNotFoundException | `0447d63` | lls build.sbt | worked around |
| sbt 2 launcher defaults to a thin client whose server "keeps the first step's environment" | `1452fc6` (2026-09-18) | CI wrapper `--server` | worked around |
| sbt 2 build dialect drops structural refinements; sbt-welcome has no sbt 2 build | `build.sbt` comments | lls build.sbt | worked around |
| Scala Native: scalacheck pulls test-interface 0.5.8 against 0.5.12, a strict eviction error on sbt 2 | `build.sbt` `evictionErrorLevel := Warn` | lls build.sbt | worked around |
| Scaladoc crashes: Scala 3.8.3 packageDoc (sge `01b50507`), DottydocRunner on JDK 25 (`5ccaa08`) | | docs skipped | **unresolved upstream** |
| GitHub windows-11-arm runners lack JDK 17 | `d3a9582` | JDK 25 in CI | worked around |
| **Scala.js miscompiles named `boundary.break`/`return` across nested while loops** into a JS `break` that exits only the inner loop, giving `ArrayIndexOutOfBoundsException: -1` in TimSort merges | lls `630d0db` (post-gen patch), engine `17ee4e6b` (ControlThrowable sentinel), patch removed in `2a0cc49` | Baltic Porter | worked around; **no upstream Scala.js issue filed** (none referenced in any repo) |
| **Scala Native java.nio on Windows does not preserve UNC prefixes** through `Paths.get`/`toString` | `630d0db` | lls-io `FilePathNio` reconstructs from `getRoot`; tests skip via `nioSupportsUnc` | worked around; **unresolved upstream** |
| Scala 3 `inline` + arrays: an inlined typed local reifies a whole-array `CHECKCAST` at the call site (ISS-686; again in generated code, 2026-09-19) | `547e624`, engine `971be58b` | lls design rule "read via `mk0.get(mk0.castArray(raw: Any …), i)` with NO typed array local" | resolved by convention; it is a language property |
| Scala.js varargs `T*` need a ClassTag | `77316f1` | engine `ca78e90e` | resolved |
| Scala 3.9: "3.8.4 cannot read 3.9.0-built classes" (TASTy); sbt 2.0.8 compiles `project/` with 3.8.4, and Baltic Porter runs in the meta-build | balticporter memory (D) | lls branch `scala-3.9.0`, local only | **unresolved**: lls stays on 3.8.4 |
| sbt eviction across two engine hashes via lls-port | balticporter memory: "fix = `VersionScheme.Always`" | | partially |

About **scala-newtype-compat and refined-compat**: neither references lls. The only overlap is build policy. On 2026-07-01 the user ruled that lls "is already ported to sbt 2, it uses scala 3.8.4, so it
needs JDK17 anyway", while JDK-11-tested libraries stay on sbt 1 (`scala-steward-pinning.md`).

### Still unresolved (as of 2026-10-06)
- **ISS-006**: generated `ObjectMap`, `ObjectSet`, `OrderedMap` and `OrderedSet` keep Java's `Object` bound, so `ObjectMap[Int, Int]` needs boxed `java.lang.Integer`. "API and allocation regression"
  relative to the hand-written lls.
- **ISS-005**: small-size JMH gaps, e.g. "ObjectMap.foreachEntry 2.4x, OrderedSet.foreach 2.2x … at 100 elements".
- **ISS-003**: a filtered or zipped `ArrayView` for-comprehension still allocates. The README was corrected to say so.
- **ISS-001**: every API divergence from Java needs a recorded justification.
- No tagged release since 0.3.0. The generated lls depends on an engine SNAPSHOT.
- lls-io is published but **adopted by neither ssg nor sge**.
- Scala 3.9 migration is blocked by the TASTy/meta-build constraint.
- Upstream bugs (Scala.js labelled break, SN Windows UNC nio, scaladoc on JDK 25) are worked around locally, with no upstream reports found.
