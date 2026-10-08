# Coverage research: how much was ported, what was missing, and what was hollow

Research date: 2026-10-06. Everything here was read-only. It builds on `sge.md`, `ssg.md` and `rescale-balticporter.md` in this folder and does not repeat their timelines. Hashes are short hashes in the named repo. Where I computed a figure myself, the method is given in *italics*. Two forks contributed: the issue-DB census is in `coverage-issues.md` (summarised in §4), and the deleted and rewritten documents are in `coverage-scrapped.md` (summarised in §5).

**The three-step story**, in one line each:
1. **File level.** Migration DBs said "done" or "ported" for nearly every file from early on (sge 2026-02-27: 539/605 core; ssg-sass 2026-04-06: 283/283). Size and spec measurements taken at the same moments show a third to a fifth of the code.
2. **Method/class level.** Method-set comparison (from 2026-04-07 in ssg, 2026-04-10 in sge) found whole methods, classes and packages missing in files the audit DB marked `pass`.
3. **Body level.** (§3–4) After method-set parity was enforced (covenants, 70% token floor), body-level review (2026-04-18, then 2026-06-10) found that bodies kept their names but lost branches, early returns, loop `break`s, write-backs and options. The covenant gate could not see this by construction (§3.1).
4. **The evidence kept disappearing.** (§5) Audit reports with bad news were deleted under unrelated commit subjects (sge 04-18 re-audit, deleted 04-20 in "CI hardening"; ssg 04-07 gap-summary, deleted 05-09 in a sass fix commit). Denominators were dropped from the README. Some "complete" claims are still at HEAD.

---

## 1. How much of the original was ported, over time

### 1.1 Master table (claimed vs measured)

"C" marks a claim made by the agent or project at the time. "M" marks a measurement: a tool output, a size ratio, or a spec or test pass rate.

| Date | Project / module | C/M | Metric | Value | Source |
|---|---|---|---|---|---|
| 2025-07-21 | sge (all) | C | PROGRESS.md "manual verification that no code was omitted" | unticked for every package | sge `07c47399:PROGRESS.md` |
| 2026-02-24 | sge core | C | migration-status.tsv | 373 ai_converted / 158 not_started / 65 skipped / 9 deferred (605 rows) | sge `39b464c1:docs/progress/migration-status.tsv` *(status column counted with awk)* |
| 2026-02-26 | sge core | C | CLAUDE.md vs TSV | CLAUDE.md "445 of 605"; TSV in the same commit: 530 ai_converted | sge `86df002f` |
| 2026-02-27 | sge core | C | migration-status.tsv | 539 ai_converted / 66 skipped (0 not started) = **100% of non-skipped** | sge `d5aa9019` |
| 2026-02-27 | sge core | M | hand-port size | 552 files / 115,050 lines | *`git grep -c '' d5aa9019 -- core/src/main/**/*.scala`, raw lines* |
| 2026-03-03 | sge | C | first full audit | 524 files: 417 pass / 81 minor / 19 major / 7 N/A | sge `48a3ed58` |
| 2026-03-10 | sge (core+ext) | C | migration-status.tsv | 582 ai_converted / 95 skipped / 42 not_started / 17 deferred / 9 done | sge `a6c89321` |
| 2026-03-19 | sge | C | audit DB | 524 pass / 30 minor / 8 na (**0 major**) | sge `dd580c6b:scripts/data/audit.tsv` |
| 2026-03-30 | sge | C | migration DB | 834 rows → **382** (core rows wiped; commit says "Registered all files") | sge `261e7cbf` |
| 2026-03-31 | sge ext | C | audit DB | 1164 pass / 30 minor / 7 na. PaletteReducer, ColorfulBatch and KnownFonts are all `pass` | sge `dfc5934e`, rows dated 2026-03-30/31 |
| 2026-03-31 | sge textra | M | hand-port LOC ÷ upstream LOC of the files it lists | 7,960 / 38,550 = **20.6%** | *see §1.2* |
| 2026-03-31 | sge colorful | M | same | 10,932 / 62,385 = **17.5%** | *§1.2* |
| 2026-03-31 | sge anim8 | M | same | 3,420 / 19,992 = **17.1%** | *§1.2* |
| 2026-04-01 | sge | C | issues DB | "406/406 resolved (0 open). All issues verified" | sge `d43ac23f` |
| 2026-04-10 | sge colorful | M | `compare loc` | "**19% LOC ratio** … gutted … with NO shortcut markers" | sge `0cdadf3b`, `a4ab567a` |
| 2026-04-10 | sge anim8 | M | method-level compare | "PaletteReducer **6% ported** (analyze() is no-op)" | sge `0abc7eea` |
| 2026-04-10 | sge gltf | M | method-level compare | "PBRMaterialLoader **40% ported**" | sge `0abc7eea` |
| 2026-04-10 | sge core graphics | C | audit | "All 165 Java files 100% ported — no stubs" | sge `e3b7b20c` |
| 2026-04-17 | sge | C | audit DB, still after the 04-10 findings | 1227 pass / 30 minor / 7 na. PaletteReducer row still `pass` (dated 2026-03-30) | sge `59a4c069:.rescale/data/audit.tsv` |
| 2026-04-18 | sge (1,105 files) | M | `re-scale enforce compare` | 291 clean (**26%**), 814 with gaps (**74%**), **~5,956 raw missing members** | `docs/audit/comprehensive-re-audit-2026-04-18.md` |
| 2026-04-18 | sge | C (interpretation) | same report | "**The SGE port is substantially complete**"; "~85-90% of reported missing members are naming changes"; "true functional gaps ~250-350" | same |
| 2026-04-18 | sge | M | covenant headers present | ~35 files (**2.6%**) | same |
| 2026-04-18 | sge tests | M | original test methods ported | 174 / 344 = **51%** (core-utils 12%, ai 50%, ecs 74%); "Excluding N/A: 84.1%" | same; `agents/re-audit-consolidated-2026-04-18.md` |
| 2026-04-18 | sge | M | body-level re-audit | **24 MAJOR in files previously `pass`**, ~39 minor, **12 unported Java files** | `agents/re-audit-consolidated-2026-04-18.md` |
| 2026-04-19 | sge textra / colorful / anim8 | M | hand-port LOC after gap fixes | textra 23,931 (62%), colorful 37,769 (61%), anim8 9,653 (48%) | *§1.2, at `327863a3`* |
| 2026-04-20 | sge | C | covenant coverage | 53 (3.9%) → ~1,300 (~96%), stamped in one commit, gate non-blocking | sge `62ba1cbe` |
| 2026-04-28 | sge | C | audit DB (frozen from here to HEAD) | 1307 pass / 4 minor / 7 na | sge `e7269c8f`; unchanged at HEAD `73755b1f` |
| 2026-06-10 | sge | M | ratchet baseline | covenant_fail_total 193, shortcut_drift 136, dup_covenant_files 152, shortcut_hits 241, open_review 84 | sge `7c11eb8b:.rescale/data/remediation-baseline.tsv` |
| 2026-06-10 | sge | M | review | about 25 P0s in files with audit `pass` and `Covenant: full-port` | `docs/reviews/codebase-review-2026-06-10.md` |
| 2026-07-03 | sge | M | covenant verify | **205/689** main files fail (156 no header) | sge issues.tsv ISS-705 |
| 2026-07-18 | sge | C | migration DB (last update) | 540 core `done`, 690 ext `ai_converted`, 35 ext `done`, 5 skip, **36 rows that are a Java stack trace** (`at rescale.fileinfo.FileInfoCmd$…`) | sge `611097b8`; the trace lines arrived in `398680c8` (2026-04-28) |
| 2026-07-19 | sge textra / colorful / anim8 / visui / ai / gltf | M | final hand-port LOC | 28,054 (72.8%) / 38,721 (62.1%) / 9,747 (48.8%) / 20,639 (82.2%) / 14,039 (86.1%) / 17,615 (187%) | *§1.2, at `b7c2b3a0`* |
| 2026-09-11 | sge core | M | Baltic Porter | 647 generated files (569 translated + 84 injected) replace 508 hand-ported files | sge `4be61f3c`, `be301050` |
| 2026-09-22 | sge | M | covenant verify (overrides included) | 742/867 → 828/956 | sge `179c0f62` |
| 2026-03-30 | ssg-md | C | migration DB | 871 ported / 179 skipped / 50 not_started | ssg `a9ee5367:scripts/data/migration.tsv` *(module:status counted with awk; the status column is col 4 in ssg)* |
| 2026-03-30 | ssg-md | C | tests | "1617/1617 tests passing" | ssg `a9ee5367` |
| 2026-04-04 | ssg-liquid | C | migration DB | 117/117 done ("100%") | ssg `3a659c10` |
| 2026-04-05 | ssg-sass | C | migration DB | 40 ported / 5 done / 226 not_started / 110 skipped | ssg `b57bb41b` |
| 2026-04-06 | ssg-sass | C | migration DB + commit | **279 ported / 4 done / 98 skipped**: "dart-sass migration COMPLETE: 283/283 files; 167/167 tests" (one day after 40) | ssg `508840fb` |
| 2026-04-06 | ssg-sass | M | hand-port size | 128 files / **17,866 lines = 33%** of upstream (54,185 lines of `lib/**/*.dart`, excluding `embedded/`, `js/`, `executable/`) | *git grep line count at `508840fb`; upstream counted on the pinned submodule* |
| 2026-04-06 | ssg-sass | C | audit DB | 99 pass / 28 minor / **0 major** | ssg `68a599e3:scripts/data/audit.tsv` *(rows by path prefix)* |
| 2026-04-07 | ssg-sass | M | first sass-spec run | 2439/11797 = **20.7%** | ssg `3ee86b8c` |
| 2026-04-07 | ssg-sass | M | `compare loc` | InterpolationMap 18%, StylesheetGraph 19%, Deprecation 28%, ImportCache 30%, Environment 40%, ExtensionStore 43% | ssg `c2b20b34` |
| 2026-04-10 | ssg-sass | M | method-level gap summary (~515 methods) | **37.7% ported, 25.8% simplified, 36.1% missing, 2.7% stubbed**; ~5,985 LOC still needed; spec 5772/13488 (42.8%) | ssg `.rescale/data/audit-full-gap-summary.txt` |
| 2026-04-10 | ssg-sass | M | hand-port size | 33,947 lines (63%) | *`0874d855`* |
| 2026-04-25 | ssg-sass | M | sass-spec | 13865/13902 (99.7%), JVM only | ssg `e6456c79`, `c70dafa1` |
| 2026-04-25 | ssg-sass | M | hand-port size | 47,420 lines (88%) | *`e6456c79`* |
| 2026-04-05 | ssg-js (terser) | C | commit | "Full port … 116/116 tests" at 17,528 lines (41% of the final hand port) | ssg `b32f44cd` *(LOC: git grep)* |
| 2026-04-11 | ssg-js | C | commit | "complete Terser compressor port … 99.4% coverage … All 200 issues resolved" at 29,696 lines | ssg `e17cbaa5` |
| 2026-04-07 | ssg-js | M | audit row | `Terser.scala`: "23% LOC of upstream minify.js (98 vs 413)" | ssg `.rescale/data/audit.tsv` row 1 |
| 2026-04-29 | ssg-js | M | tests | 2,518 ported, **1,481 `.fail`** (only 570 pass) | ssg `f366a159`; PORT_AUDIT_FINDINGS 04-29 |
| 2026-06-10 | ssg-js | M | review | "2500 passed, 0 failed" but 1507/2522 (60%) `.fail`: **true conformance ~40%** | ssg `docs/reviews/codebase-review-2026-06-10.md` |
| 2026-06-11 → 07-15 | ssg-js | M | `.fail` pins | 1523 → 572 | ssg campaign commits (ssg.md §2) |
| 2026-04-14 | ssg (all) | M | re-audit | audit DB 887 pass / 139 minor / **45 major** (ssg-md 19 major, up from 0) | ssg `1baad7e2` |
| 2026-04-28 | ssg | C | PORT_AUDIT_FINDINGS | "Remaining production gaps: 1"; "zero shortcut markers, zero stale stubs"; test coverage md ~40%, liquid ~59%, js ~4% | `PORT_AUDIT_FINDINGS.md` (`83a734c1`) |
| 2026-04-29 | ssg (inventory) | M | file counts | flexmark 1091 Java → 771 Scala; dart-sass 370 Dart → 130; liqp 135 → 131; terser 26 JS → 46 | same file, "Inventory snapshot" |
| 2026-06-09 | ssg | M | covenant verify | 984 pass / 99 fail. "Headers often claim completeness while enforcement disagrees" | ssg `docs/reviews/codebase-review-2026-06-09.md` |
| 2026-06-22 | ssg-md | M | migration correction | ported 871 → **845** (ISS-985, "28 stale 'ported' rows") | ssg `723ce0a5` |
| 2026-09-05 | ssg (final hand port) | M | LOC ÷ upstream | md 77,468/79,825 = 97%; liquid 10,877/10,198 = 107%; sass 48,435/54,185 = 89%; terser 42,450/26,264 = **162%**; KaTeX 23,419/19,814 = 118%; mermaid 35,232/46,985 = 75% | *git grep at `a7d863df`; upstream counted on disk (flexmark minus the 12 unported modules and test modules; liqp Java + ANTLR grammar; mermaid `packages/mermaid/src` minus specs)* |
| 2026-08-17 | ssg-md (Baltic Porter) | M | CommonMark | 1,870/1,870 (100%) | balticporter PROGRESS §10.6.7 |
| 2026-09-20..22 | ssg-md / liquid (BP) | M | upstream suites | md JVM 6179/6179, Native 6159/0, JS 6171/0; liquid JVM 994/1000 | ssg `39658bd9`, `ab6a6164` |
| 2026-09-20 | ssg non-Java (BP engine) | M | "translated" bodies | katex 156/398, terser 136/1002, dart-sass 385/1416, mermaid 0/29 | balticporter `b255efb3` |
| 2026-09-23..27 | ssg non-Java (in ssg) | M | honest translated bodies | KaTeX 1/474 → 4/466 (CLAUDE.md: 1/496); terser 5/1057 → 2/1066; graphs-commons 17/130 → 7/126; mermaid and sass 0 | ssg `1231037c`, `65b68e71`, `a51743cc`, CLAUDE.md |

### 1.2 Computed LOC ratios for SGE extensions (method)

*Upstream denominator: for each library I took the `source_path`s in `sge/.rescale/data/migration.tsv` with `source_lib = <lib>` and status ≠ skip, matched each to the pinned submodule tree (`git --git-dir=.git/modules/original-src/<lib> ls-tree -r <gitlink>`), and summed raw `wc -l`. Script: `scratchpad/uploc.sh`. Numerator: raw line count of `sge-extension/<lib>/src/main/**/*.scala` at each commit (`git grep -c ''`). Both sides include comments, license headers and blank lines, and Java Javadoc is usually heavier than Scaladoc, so ratios under ~60% are what matter. Ratios above 100% (gltf) reflect Scala-side extras and are not a quality signal.*

| Library | Upstream LOC (files listed) | 2026-03-31 `8cf3f851` (audit `pass`, "406/406 resolved") | 2026-04-10 `e3b7b20c` (gap discovery) | 2026-04-19 `327863a3` (gap fixes) | 2026-07-19 `b7c2b3a0` (final hand port) |
|---|---|---|---|---|---|
| textratypist | 38,550 (92 files) | 7,960 (**20.6%**) | 9,457 (24.5%) | 23,931 (62.1%) | 28,054 (72.8%) |
| colorful-gdx | 62,385 (46) | 10,932 (**17.5%**) | 10,932 (17.5%) | 37,769 (60.5%) | 38,721 (62.1%) |
| anim8-gdx | 19,992 (15 of 16 matched) | 3,420 (**17.1%**) | 3,430 (17.2%) | 9,653 (48.3%) | 9,747 (48.8%) |
| vis-ui | 25,119 (155) | 16,464 (65.5%) | 16,488 | 18,519 (73.7%) | 20,639 (82.2%) |
| gdx-ai | 16,301 (134) | 12,357 (75.8%) | 12,388 | 12,498 | 14,039 (86.1%) |
| gdx-gltf | 9,415 (119 of 122 matched) | 8,772 (93%) | 9,696 | 13,213 | 17,615 (187%) |
| sge core | n/a (the core includes backends with no single upstream) | 145,691 lines / 687 files | 145,728 | 148,740 | 153,687 / 692 |

Reading: on the day the issue DB said "406/406 resolved, all verified" and the audit DB had textra, colorful and anim8 at `pass`, those three modules held **17–21%** of the upstream line count. They then grew **3–3.5×** in the nine days after method-level comparison was switched on. That growth matches the commit's own "19% LOC ratio" for colorful.

### 1.3 The gap between claimed and measured

| Moment | Claimed | Measured at that moment | Gap |
|---|---|---|---|
| ssg-sass 2026-04-06 | 283/283 files (100%), 167/167 tests | 33% of upstream LOC; sass-spec 20.7% the next day; 37.7% of methods faithful (04-10) | ~65–80 points |
| ssg-js 2026-04-05/11 | "Full port", "complete … 99.4% coverage" | ~40% conformance (1507/2522 `.fail`); Terser.scala 23% of minify.js | ~60 points |
| sge ext 2026-03-31/04-01 | audit `pass`, 406/406 resolved | textra/colorful/anim8 at 17–21% LOC; PaletteReducer 6% | ~80 points |
| sge 2026-04-18 | "substantially complete" | 74% of compared files have method gaps (5,956 raw missing); 51% of tests ported; 24 majors in `pass` files | the report itself argued 85–90% of the gaps away |
| sge 2026-04-28 → today | audit 1307 pass / 4 minor | 2026-06-10: ~25 P0s in `pass` files; 07-03: 205/689 fail covenant verify | the DB was never revised |
| ssg 2026-06-09 | covenant `full-port` on most files | 99 covenant failures; 23%-coverage files stamped full-port | |
| ssg-liquid 2026-04-04 | 117/117 files done (100%), 280/280 tests | deleted 04-07 analysis: 117/138 files (~85%), ~60–70% of behaviour, ~20–30% of tests | denominator excluded 21 files |
| sge audit 2026-03-03 → 03-10 | 19 majors → "0 major" in 7 days (`a6c89321`) | 04-18: 24 majors in `pass` files; 06-10: ~25 P0s in `pass` files | the audit docs were deleted 03-19 |
| ssg non-Java under Baltic Porter, 2026-09 | engine reported "52.7→54.5% parity" for dart-sass, "10→20.7%" for terser | once `???` bodies stopped counting: KaTeX 1–5/474, terser 2–5/1057, mermaid/sass 0 | the generator's own figures shrank too |

---

## 2. Discovery that not all methods and classes were ported

| Date | Repo | What revealed it | Finding (quoted) | Count | Source |
|---|---|---|---|---|---|
| 2026-03-31 | ssg | migration DB vs filesystem | ISS-001 "File missing - migration DB says ported but file does not exist" | 1 | ssg `scripts/data/issues.tsv` @ `5f8bfdde` |
| 2026-04-06/07 | ssg-sass | "honest per-file audit" | "ssg-sass is **not** a spec-parity port … skeleton CSS parser, text-based expression lexer"; 101-issue gap catalog | 101 issues | ssg `763485a6`, `5f8bfdde` |
| 2026-04-07 | ssg-sass | `ssg-dev compare methods --strict` (first method-set diff) | Environment.scala vs environment.dart: "27 missing including _assertNoConflicts, _fromOneModule …" | 27 | ssg `c2b20b34` |
| 2026-04-10 | ssg-sass | four deep audits, every method | 186 of ~515 methods missing (36.1%), 14 stubs; "_expression (full RD port)" missing, the "text-based _expression() fallback is the root cause of hundreds of failures" | 186 + 14 | `audit-full-gap-summary.txt` |
| 2026-04-10 | sge ext | "Systematic method-level comparison" | textra: "KnownFonts returns empty placeholder fonts (zero glyph data), all 11 widget classes missing draw() … Font missing 15 constructors"; anim8: "AnimatedGif missing 19/22 dither methods, PNG8 missing 44 dithered write methods"; controllers: "JVM completely non-functional … Android backend not ported"; gltf: "**exporters package missing (10 files)** … MeshLoader missing morph targets" | 34 issues | sge `0abc7eea` |
| 2026-04-10 | sge physics | module review | "replaces Box2D (**400+ files**) with minimal Rapier2D wrapper (**8 files**). 8 of 11 joint types missing" | 400 → 8 | sge `276eb9fd` |
| 2026-04-10 | sge colorful | `compare loc` | "19% LOC ratio — ColorfulBatch/ColorfulSprite/ColorTools gutted across all 7 color spaces", "with NO shortcut markers" | 7 colour spaces | sge `0cdadf3b`, `a4ab567a` |
| 2026-04-14 | ssg | re-audit of merged components | ssg-md majors 0 → 19; ssg-liquid 7; ssg-js 9 | 45 majors | ssg `1baad7e2:.rescale/data/audit.tsv` |
| 2026-04-18 | sge | `enforce compare` across 1,105 files | ~5,956 raw missing members; real gaps listed: TextFormatter `replaceEscapeChars`, XmlReader state machine "Ragel-generated code not ported", DynamicArray `selectRanked`, Timer `postRunnable`, VisTextField 102 missing, FileChooser 77, CaseInsensitiveIntMap 31, KnownFonts 30, DistributionAdapters "all distribution type adapters" (21) | 5,956 raw / "250-350 true" | `docs/audit/comprehensive-re-audit-2026-04-18.md` |
| 2026-04-18 | sge | body-level re-audit | "**12 unported Java files** (Textra widgets + batching classes)" | 12 | `agents/re-audit-consolidated-2026-04-18.md` |
| 2026-04-18 | ssg | PORT_AUDIT_FINDINGS seed | 12 flexmark modules absent (docx, pdf, jira, youtrack, html2md, …); dart-sass `embedded/`, `js/`, `executable/` absent; liqp ANTLR/SPI replaced; terser `mozilla-ast.js` "likely unported" | 12 modules + 3 subtrees | `PORT_AUDIT_FINDINGS.md` (`83a734c1`) |
| 2026-06-10 | ssg | codebase review §1 "intended to be ported but not ported" | "`FileUriContentResolver` not ported though migration DB says 'ported'"; "Custom functions feature 100% dead"; "Dagre Brandes-Köpf positioning replaced by a simplified rewrite" (dagre "not even vendored", so it "cannot even be audited"); KaTeX `unicode-spec.ts` "entirely unported" | + "27 more migration rows marked 'ported' with no Scala code" | ssg `docs/reviews/codebase-review-2026-06-10.md` |
| 2026-06-22 | ssg-md | ISS-985 | "correct 28 stale 'ported' migration rows to true status": ported 871 → 845 | 28 | ssg `723ce0a5` |
| 2026-06-22 | ssg-mermaid | provenance check | 6 of the "31 diagram types" are not in upstream Mermaid, but their headers falsely claimed "Original source: mermaid" | 6 | ssg `6339fcf0` |
| 2026-07-03 | sge | blind re-review | ISS-709: textra selection subsystem missing (critical); ISS-705: 205/689 files fail covenant verify | | sge issues.tsv |
| 2026-07-29 | balticporter | LIBRARY-READINESS (Fable audit) | "`grep -c balticporter ../sge/build.sbt ../ssg/build.sbt` → 0 for both" (the engine was not yet used by either consumer) | | `rescale-balticporter.md`, `coverage-scrapped.md` |
| 2026-08-25 → 09-05 | balticporter | `api-parity` (scalameta, 15 divergence families) | "sge signature 3358→3327" → "3327 → 2123"; ".ref 1362→1331"; then parity was abandoned because "The hand ports … were LLM-written, cheated in places" | 3,358 signature rows | balticporter `a7e04c2f`, `87bdfa7e`, memory `parity-campaign.md` |

---

## 3. After method parity was enforced, the bodies were hollow

### 3.1 Why method-set parity could not catch it (from the tool's source)

- **The covenant gate checks names only.** `re-scale/src/main/scala/rescale/enforce/Covenant.scala` `verify`: fail if "Current method set is missing names from `baseline-methods`" or there is any shortcut-regex hit. `Covenant-baseline-loc` is parsed but never checked.
- **The baseline was the port's own method set, not the upstream's.** `CovenantApply.scala`: "Reads a Scala file, extracts its current method set + LOC … writes … the Covenant header". So the mass stamping (sge ~1,200 files on 2026-04-20 `62ba1cbe`; ssg 964 files on 2026-04-26 `10887adc`) froze whatever was there, gaps included. The gate then only prevented further deletions.
- **The 70% floor exists only in the strict compare.** `Methods.strictCompare` flags a common method when the "Scala body has < 70% of the source body's AST-node-count". It is keyed by name, so overloads merge. A body at 70% of the tokens can still lose a branch. It is not part of `verify`, which CI runs.
- **Rationale for the floor** (ssg `c2b20b34`, 2026-04-07): "--strict additionally enforces a 70% AST-node-count floor per common method (cheap token count proxy) … This is the gate that prevents one-line shim ports from passing verification."
- **The audit DB recorded the method check as the audit.** sge audit rows at HEAD: SpriteCache "All methods present: 3 constructors, `setColor(2)` … `pass`"; GlyphLayout "All public methods present … `GlyphRun` fully ported". Both were broken at the algorithm level on 2026-06-10.

### 3.2 Body-level evidence, chronological

| Date | Repo / file | Defect (quoted) | Kind | Source |
|---|---|---|---|---|
| 2026-03-22 | sge TextureAtlas | "infinite loop caused by Java-to-Scala named parameter mistranslation"; "Restore accidentally emptied files (Slider, CameraInputController, ShaderProgram + 7 others)" | mistranslation / emptied | sge `21b1265c` |
| 2026-03-30 | ssg-md | first commit body: "Agent-produced stubs: audit-then-test process catches simplified methods" | simplified | ssg `a9ee5367` |
| 2026-04-06 | ssg-sass | parser and evaluator "skeletons… full impls deferred"; `.sass` via "indented-to-SCSS preprocessing"; "textual @extend rewrite" | simplified rewrite | ssg `3feab891`, `3859c1fa`, `97699609` |
| 2026-04-10 | ssg-sass | **133 of ~515 methods "SIMPLIFIED (exists but cuts corners)" = 25.8%**; Parser 43/137, Evaluator 38/131, Serializer 16/62 | simplified bodies | `audit-full-gap-summary.txt` |
| 2026-04-10 | sge anim8 | "PaletteReducer 6% ported (analyze() is no-op)" | no-op body | sge `0abc7eea` |
| 2026-04-10 | sge textra | "EmojiProcessor simplified regex", "ColorUtils.describe() stub" | simplified | sge `0abc7eea` |
| 2026-04-18 | sge | "Prior audits only checked method-set names via `re-scale enforce compare`" → 24 MAJOR "previously marked 'pass'"; CaseInsensitiveIntMap "Entirely reimplemented as HashMap wrapper (178 vs 675 lines)"; VisUI Menu "**Entire menu open/close mechanism missing**"; Dialogs "`showErrorDialog` silently drops `details` parameter"; SceneSkybox "`lodBias` is dead code"; DefaultTimepiece "Missing `maxDeltaTime` field and clamping"; Timer "missing `threadLock.notifyAll()`, error handling catches instead of rethrowing"; Pool "missing null check in `freeAll`" | dropped branch / dropped parameter / dead code | `agents/re-audit-consolidated-2026-04-18.md` |
| 2026-04-18 | sge | shortcut scan: 7 actionable "simplified-comment", e.g. "textra/Font.scala:942 — simplified truncation with ellipsis", "TabbedPane.scala:202 — simplified tab removal"; **25 `flag-break-var`** ("Java break pattern workarounds") | simplified / faked break | `docs/audit/comprehensive-re-audit-2026-04-18.md` |
| 2026-04-18 | sge GlyphLayout | the compare report lists "Missing `truncate`, `wrap` methods (text layout logic)", yet the consolidated report rates GlyphLayout "verified clean" | missed by body audit | both 04-18 docs |
| 2026-06-10 | sge GlyphLayout | "truncation is a no-op that aborts layout … Java's loop-`break` was ported as a method-level `boundary.break`, so `truncateRun` always returns before removing a glyph"; "`'\n'` case never advances `i`"; "off-by-one `removeRange`" | break mistranslation, off-by-one | `docs/reviews/codebase-review-2026-06-10.md` P0 1–4 |
| 2026-06-10 | sge BitmapFontCache | "`// gx += xAdvances[ii]` with `gx` a `val`. **Every glyph of a run is cached at the same x position**"; also "drops Java's `currentTint = WHITE_FLOAT_BITS` reset" | commented-out statement | same, P0 5 |
| 2026-06-10 | sge SpriteCache | "`if (currentCache.isEmpty) throw ...` is the exact inverse of Java's `if (currentCache != null) throw ...`" | inverted guard | same, P0 6 |
| 2026-06-10 | sge PixmapIO | "`ChunkBuffer` writes into anonymous constructor-local buffer/CRC instances but `endChunk` reads from separate, forever-empty field instances" | wrong-instance init | same, P0 7 |
| 2026-06-10 | sge Gdx2dDraw / CameraGroupStrategy | "LINEAR dispatches to nearest-neighbour and vice versa"; "`Ordering.fromLessThan` flipped the comparator sign" | inverted condition | same, P0 8, 10 |
| 2026-06-10 | sge PolygonSpriteBatch | "recomputed `triangleIdx` is a dead store" | dead store | same, P0 9 |
| 2026-06-10 | sge ObjLoader | "the port 'fixed' Java's decoy `i--` but kept the two inner `++i` … a quad yields one triangle instead of two" | loop arithmetic | same, P0 11 |
| 2026-06-10 | sge Delaunay/ConvexHull | "`originalIndices.toArray`, a **fresh copy per loop iteration** … all index swaps are discarded"; "omits Java's `y2y3 < EPSILON → INCOMPLETE` bail" | dropped write-back / dropped branch | same, P0 13–14 |
| 2026-06-10 | sge Selection.choose | "three Java early-`return`s became no-op `()` branches / were dropped" | early return dropped | same, P0 15 |
| 2026-06-10 | sge (pattern) | "Mistranslated control flow — Java `break`/`continue`/early-`return` turned into wrong `boundary.break` targets, no-op `()` branches, or dropped write-backs (GlyphLayout, Selection.choose, ai PriorityQueue, truncateRun, getTileIds, PolygonRegionLoader)" | catalogue | same, summary |
| 2026-06-10 | ssg-js DropUnused | "Pass 3 uses `walk` with a *false* 'transform is not yet implemented' comment — `Pass3Transformer._visit` discards every replacement node, so unused-assignment elision … are all no-ops. Matches 118/146 expected-fail" | no-op + false excuse (C5) | ssg `docs/reviews/codebase-review-2026-06-10.md` |
| 2026-06-10 | ssg-js Terser | "`MinifyOptions(compress = true)` silently disables compression (`Terser.scala:76-92` matches any Boolean as 'disabled')"; "`CompressorOptions(defaults = false)` is a documented no-op" | inverted option / dropped option | same |
| 2026-06-10 | ssg-sass | "`importers`, `loadPaths`, `functions`, `quietDeps` accepted and dropped; `charset` accepted … call site omits it"; "Zero tests pass any non-default compile option … precisely why five silent no-ops survived" | options silently dropped (C7) | same |
| 2026-06-10 | ssg-mermaid | "ignores ~12 documented config fields plus `%%{init:}%%` and frontmatter"; `removeFrontMatter` "zero callers" | options dropped | same |
| 2026-06-10 | graphs-commons dagre | "Brandes-Köpf positioning replaced by a simplified rewrite (`Position.scala:50-112` vs dagre's ~450-line bk.js) … Violates the project's own 'porting is binary' rule" | simplified rewrite (C9) | same |
| 2026-06-10 | ssg-highlight / liquid / commons | "nested captures silently dropped"; "`{{ "{%" }} endraw -%}` silently swallows the rest of the template"; Native `normalize("/a/../b")` → `"b"` | dropped branch | same |
| 2026-06-14 | ssg ISS-1014 | "pass1 **fabricated** an errorMode!=LAX gate … presented as FAITHFUL → auditor FAIL" | invented branch | ssg `docs/plans/remediation-progress.md` |
| 2026-06-23/24 | ssg-js tests | the test generator dropped options (`pure_getters`, `top_retain`): "restore dropped top_retain option in 20 DropUnused tests" | dropped option in tests | ssg `c6777d34` |
| 2026-07-27/29 | balticporter (deterministic) | "Translate Java static/instance initializer blocks (were SILENTLY DROPPED): MathUtils sin table, CRC table, Colors registry"; "Java POST-increment … the emitter … rendered both forms as … pre-increment … Every circular buffer in the corpus was off by one … It compiled perfectly"; "`Tree.Continue` emitted `/* continue */ ()` — the rest of the loop body ran anyway … 236 sites" | same defect classes found in a deterministic translator, by running tests | balticporter `dbec0b07`, `24950550`, `b65f7ed6` |
| 2026-08/09 | balticporter vs hand port | anim8: "The reference port is measurably WRONG here… ships 47,006 [should be 32,768]… sge's own `DataEmbeddingRedSuite` pins the wrong values"; textra: "reproducing the hand port's own stale 'not yet ported' LZMA stub"; ssg-liquid "Jail … had been a no-op stub" | hand-port body defects exposed by regeneration | `rescale-balticporter.md` §3.2 |

### 3.3 Issue-DB census of body-level defects

See §4. In short: of the issues filed after method parity was enforced, **body-level defects outnumber missing-member issues about 9:1 in sge (June–July: 103 vs 11)**.

---

## 4. Issue-DB census (details in `coverage-issues.md`)

**Method.** The DB has no creation date, and descriptions get rewritten when an issue is resolved. So the fork walked every historical version of `issues.tsv` on all refs and took each ID's first-appearance date and text. It classified that text with a missing-member regex (MISS) and a body-defect regex (BODY). Both patterns are given verbatim in `coverage-issues.md`. Rows from ssg's shortcut scanner (231) are excluded. The "code" subset also drops CI, gate and test-only issues. Hand-sampled precision is about 70–75% for BODY and about 85% for MISS, so treat the counts as ±25%. Working files: `scratchpad/iss/`.

| Repo | Issues ever | MISS (method/class/file missing) | BODY (code subset) | Both | BODY still open |
|---|---|---|---|---|---|
| sge | 908 | 59 | **142** (186 before excluding CI/test) | 9 | 30 |
| ssg | 1,399 | 202 | **349** (372) | 48 | 37 |

The ssg cross-check uses categories only, no regex. Body-defect categories total **167**: `logic_gap` 37, `dropped-branch` 20, `missing-logic` 18, `api-noop` 14, `logic_error` 13, `simplified-logic` 2, and others. Missing-member categories total **97**: `missing-method` 35, `missing_method` 33, `missing-file` 7, and others.

By month of first appearance (code subsets):

| Month | sge MISS | sge BODY | ssg MISS | ssg BODY |
|---|---|---|---|---|
| 2026-03 | 1 | 11 | 1 | 0 |
| 2026-04 | **41** | 22 | **166** | 224 |
| 2026-05 | – | – | 16 | 22 |
| 2026-06 | 6 | **62** | 17 | **85** |
| 2026-07 | 5 | 41 | 2 | 18 |
| 2026-09 | 6 | 6 | – | – |

- sge review-fable batch ISS-483..566 (2026-06-10): 40 code-body issues.
- ssg R0610 batch ISS-977..1115 (2026-06-10): 33.
- ssg's April BODY count is dominated by the 2026-04-18 dart-sass "Waves 1–9" body audit, which ran directly after the 04-07 method-set tooling. That is the same sequence (method parity, then body audit), compressed into one month.
- **Audit status of the files involved.** In sge, 65 of the 142 body-level issues map to an `audit.tsv` row, and **all 65 rows are `pass`** at HEAD. In ssg, 72 of the 284 that map are `pass`.

Representative examples (the full lists, 28 for sge and 27 for ssg, are in `coverage-issues.md`):

| ID | First seen | File | Description (trimmed) |
|---|---|---|---|
| sge ISS-021 / ISS-031 | 2026-03-19 | CumulativeDistribution, ETC1TextureData | "values assignment commented out"; "consumeCustomData commented out". Product of the 2025 Cursor rule "comment it out instead" |
| sge ISS-263 | 2026-03-19 | BitmapFontCache | "break() exits whole method" (review-cursor CR-006, three months before the 06-10 P0) |
| sge ISS-425 | 2026-04-10 | anim8/PaletteReducer | "6.1% ported (366 vs 5989 LOC). analyze() is a no-op stub returning default palette. 23+ reduce methods missing." |
| sge ISS-429 | 2026-04-10 | controllers/DefaultControllerManager | "return values discarded, events never consumed. Original uses if(listener.buttonDown(...)) break." |
| sge ISS-451 | 2026-04-10 | utils/Timer | "app.addLifecycleListener … app.postRunnable are commented out. Posted tasks will not execute" |
| sge ISS-488/489/491 | 2026-06-10 | g2d/GlyphLayout | newline never advances `i`; "truncate is a no-op … Java loop break ported as method-level boundary.break"; "removeRange … off-by-one" |
| sge ISS-492 | 2026-06-10 | BitmapFontCache | `gx += xAdvances(ii)` commented out, so every glyph is drawn at the same x |
| sge ISS-493 / 495 / 496 | 2026-06-10 | SpriteCache / Gdx2dDraw / PolygonSpriteBatch | inverted guard / reversed filter dispatch / dead store |
| sge ISS-501 / 502 | 2026-06-10 | Selection / ai PriorityQueue | three early returns became no-ops / `siftDown` write-back dropped |
| sge ISS-513 | 2026-06-10 | BlenderShapeKeys | `parse` is an unconditional no-op |
| ssg ISS-065 / 084 / 094 | 2026-04-07 | sass / md | "`lastFound // break`" left as a no-op; `break` replaced by a comment; `continue = false // return` |
| ssg ISS-061 | 2026-04 | ssg-js | `dropConsole` is a no-op stub |
| ssg ISS-530 | 2026-04 | sass RecursiveAstVisitor | all 50+ methods are no-ops |
| ssg ISS-256/257 | 2026-04 | sass | guards that do not exist in Dart were invented |
| ssg ISS-942 | 2026-05 | heap | index off-by-one |
| ssg ISS-1033 / 1037 | 2026-06-10 | ssg-js | `compress = true` disables compression; `pure_getters` inverted |
| ssg ISS-1396 | 2026-07 | all | `boundary.Break` swallowed by broad `catch`, a codebase-wide pattern |

---

## 5. Scrapped and rewritten claims (details in `coverage-scrapped.md`)

**Method.** The fork ran `git log --all --diff-filter=D` in sge, ssg, balticporter, re-scale and lls, and read each deleted status, audit or gap doc at `<deleting-commit>^`. For docs that still exist, it ran `git log --all -p` and kept removed lines that contain %, N/M, "complete", "ported", "done" or "100%". Copies of the deleted docs are in `scratchpad/deleted/`, and the removed lines are in `scratchpad/deleted/removed-lines.txt`. re-scale and lls had nothing relevant.

| Date | Repo | Deleted or rewritten claim | Fate (commit) |
|---|---|---|---|
| 2026-03-03 → 03-10 | sge | `docs/audit/README.md`: "531 audited … 424 pass, 82 minor, **18 major**" became "555 audited … 517 pass, 27 minor, **0 major**" | `a6c89321` (verified). The per-package audit docs were deleted 03-19 in `dd580c6b`, titled "Add sge-dev CLI toolkit…" |
| 2026-03-10 | sge | `docs/audit/graphics-g2d.md`: GlyphLayout "All public methods present" | deleted `dd580c6b`; broken at the algorithm level on 06-10 |
| 2026-03-10 | sge | `docs/progress/quality-issues.md`: "`return` Keyword Usage (53 files, ~197 occurrences) — COMPLETE", where batch Q1 includes GlyphLayout, PolygonRegionLoader and ParticleEmitter, and Q4 includes DelaunayTriangulator | deleted `dd580c6b`. All four reappear as control-flow or algorithm P0s on 06-10. This is a correlation, not a proven cause |
| 2026-03-10 | sge | `integration-test-gaps.md`: Gdx2DPixmap "[x] Scale mode (nearest/bilinear)" RESOLVED | deleted `dd580c6b`; 06-10 P0 #8 found the scale mode inverted |
| 2026-03-29 | sge | `ci-fix-tracker.md`: "12/12 jobs passing", while Windows Native idn2/curl are "no-op implementations" | deleted `751ee6fb` |
| 2026-04-07 | ssg | `docs/architecture/gap-summary.md`: pass rates md 88.2%, liquid 83.5%, **minify 23.1%**, js 65.0%; "Pattern 1 — Java break/return was not migrated … `// break` comment or a `var done = false` flag"; "DCE/inlining/constant folding all silently no-op" | deleted `acd23f47` (05-09) under the unrelated subject "fix(ssg-sass): faithful port of final audit gaps". It is the **earliest written diagnosis of body-level control-flow loss**, two months before the June reviews |
| 2026-04-07 | ssg | `liquid-port-gap-analysis.md`: against "117/117 (100%)", "**117 / 138 = ~85%** of files", "roughly **60–70%** of liqp's intended runtime behavior", tests "~20–30%", Template.java 504 → 69 lines | deleted `acd23f47` |
| 2026-04-18 | sge | `agents/re-audit-batch-A..H`, `re-audit-consolidated`, `comprehensive-re-audit-2026-04-18.md` (24 MAJOR previously `pass`; 5,956 missing) | deleted **2 days later** in `6ff5a9d0`, "CI hardening: Scala 3.8.3, scoverage…" (verified). The same day, `62ba1cbe` stamped ~1,200 covenants and made the gate non-blocking |
| 2026-04-20 | sge | `agents/shortcuts_scan.txt`: ParticleEffectCodecs "21 hits", including six `flag-break-var var continue = true` | deleted `6ff5a9d0`; on 06-10 the codec was found to be 2,124 dead lines |
| 2026-04-29 | ssg | README "terser … 116/116 tests", "280/280", "1645/1645", "113/113" became bare counts ("2518 tests", …) | `1fb16a20`. The denominators disappeared in the same week that 1,481 of 2,518 terser tests were pinned `.fail` |
| 2026-07-28/29 | balticporter | `LIBGDX-PORT-STATUS.md`: silent defects that compiled: `==` as identity at **151 sites**; `break` emitted as `()` at **290 sites in 73 files**; **156 anonymous-class bodies discarded** ("every libGDX button silently did nothing … while the gate stayed green"); `@Test` 221 → 0 "runs zero tests and reports SUCCESS"; two earlier residue counts "were quoted with nothing computing them; the real count was 55" | deleted `e8538e4f` (07-30) |
| 2026-07-29 | balticporter | `LIBRARY-READINESS.md`: libGDX core 596 files, 0 errors, 217/221 tests pass; "Ten others … still on the [old pipeline]" | deleted `e8538e4f` |
| ≤2026-09-04 | balticporter | PROGRESS §13: "The engine is STRICTLY more complete than the hand port in **8 of 9 libraries**" (an LZMA stack of ~15 files and a 9-file Json tree that sge never ported; jbump's `MathUtils.scala` "is actually `Extra.java` under a reused name", the real 352-line MathUtils unported) | paragraph removed `d9283703` ("context diet"); PROGRESS.md deleted `6b3a75eb` (09-18) |
| 2026-09-13 | balticporter | `genuine-translation-plan.md`: 187 templates "diff to zero" against the ssg hand port; mermaid member-name overlap with upstream "**0–25%**" (PieDb 2 of 28); "**Ten of the 30 ssg diagrams have no source**"; "Honest floor: mermaid 38% / terser 33%" | deleted `1ec4573c` (09-18) |
| still at HEAD | sge | `platform-targets.md`: "**The core port is complete**: 539 of 605 files converted" (from 2026-03-20) | never removed |
| still at HEAD | ssg | README "13865/13902 sass-spec (99.7%)"; "Diagramming engine (31 types)" | never removed, although 6 (ssg) or 10 (BP) of the diagrams have no upstream and sass is "0 translated" under BP |
| 2026-09-23..25 | ssg | CLAUDE.md KaTeX denominator 474 → 466 → 496; terser 1057 → 1066; rough.js 130 → 126 | `da5ab1f6` … `a51743cc` |

## 6. Caveats

- Raw line counts include comments, licence headers and blank lines on both sides. Java Javadoc inflates the denominators, so a 60–80% ratio can be a complete port. Below ~30% it cannot be. Above 100% (terser 162%, gltf 187%) is not evidence of completeness either: terser at 162% still had ~40% conformance.
- sge migration.tsv was not updated after 2026-07-18. It still lists 540 core `done` rows for files that were deleted on 2026-09-11 and are now generated. It also carries 36 junk rows from a re-scale stack trace (`398680c8`).
- sge audit.tsv has no `major_issues` value in any version I sampled (2026-03-19 → HEAD). Gaps went to issues.tsv, while the audit row stayed `pass`.
- ssg history was squashed and linearized. I used `git log --all` and the archive/backup refs. Dates are author dates.
