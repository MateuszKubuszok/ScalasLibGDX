# Presentation as the audience experiences it

Everything below is all the audience gets: the slide content (including text inside diagrams, revealed click by click) and what the speaker says (the speaker notes). There is also a live demo at the 'Demo' slide: a rotating 3D model that responds to mouse and keyboard input, running from the same Scala code in a web browser, in an Android emulator, and as a Scala Native desktop binary.


---
## Slide 1: Scala’s LibGDX

**On screen:**
```
A Report from the Trenches
Mateusz Kubuszok
```

**Speaker says:** _(no speaker notes)_


---
## Slide 2: About me

**On screen:**
```
Scala developer for almost 12 years
co-author and maintainer of Chimney for about 9 of them
author of Hearth and Kindlings
blogged at Kubuszok.com
wrote Things you need to know about JVM (that matter in Scala)
several presentations about metaprogramming in Scala
```

**Speaker says:** So let me shortly introduce myself.
I developed in Scala for almost twelve years.
For about nine of them, I was also a maintainer of the Chimney library that perhaps some of you have heard.
This gave me some insight into how macros are working and about metaprogramming in Scala in general, which resulted in several presentations, a blog post, and recently a new library.
During all that time I have also been learning about functional programming and sharing what I learned, how JVM works, how to make it performant, how to make Scala approachable to other programmers.


---
## Slide 3: Why port libGDX to Scala?

**Speaker says:** _(no speaker notes)_


---
## Slide 4: What libGDX gives you

**On screen:**
```
Common game logic
written in Java, against the libGDX API
Desktop
LWJGL3
on a normal JVM
Android
Android SDK
bytecode → dex
Browser
GWT
Java source → JS
iOS
RoboVM / MobiVM
AOT bytecode → ARM
```

**Speaker says:** One codebase, four backends. Desktop on a normal JVM (LWJGL3), Android, the browser through GWT, iOS through RoboVM/MobiVM, an ahead-of-time compiler for JVM bytecode.


---
## Slide 5: …​and what you keep if you write it in Scala

**On screen:**
```
Common game logic
written in Scala, against the libGDX API
Desktop
LWJGL3
on a normal JVM
✓
works as is
Android
Android SDK
bytecode → dex
⚠
works, but Scala/Androidversion mismatches; natives
Browser
GWT
Java source → JS
GWT compiles Java source,not bytecode
iOS
RoboVM / MobiVM
AOT bytecode → ARM
Scala on RoboVM:unsupported, unmaintained
Scala Native: not a libGDX target at all (Java + JNI)
```

**Speaker says:** Click through the backends. GWT compiles Java source, so Scala is useless there. RoboVM compiles bytecode, but nobody supports the Scala path. Android works with caveats. And Scala Native, the most interesting target for native libraries, isn’t a libGDX target at all.


---
## Slide 6: The build tooling goes too

**On screen:**
```
What a game needslibGDX + GradleScala + sbt
| Desktop apps for Windows / macOS / Linux, built on one host | Construo (jlink + native launcher) | sbt-native-packager: packages only for the platform you build on
| Android: dex, shrink, sign, package | Android Gradle Plugin (D8, R8 / ProGuard, signing) | sbt-android: unmaintained for years
| iOS: AOT-compile to ARM, package the app | RoboVM / MobiVM Gradle plugin | Nothing: RoboVM doesn't support Scala, Scala Native has no iOS
| Browser build, and knowing which assets exist at runtime | GWT Gradle plugin; the build generates assets.txt, which GWT's preloader reads to fetch and list assets | Scala.js has no classpath, so getResourceAsStream finds nothing; no build step to embed assets or generate a manifest
| Native libraries for every platform | gdx-jnigen + per-platform natives JARs | JVM: extract from the JAR by hand; Scala Native: install the library on the system and pass linker flags yourself
```

**Speaker says:** It’s not only the runtime. libGDX’s Gradle setup packages desktop apps for every OS from one machine, builds and shrinks Android apps, and AOT-compiles for iOS. Moving to sbt and Scala-first backends means porting those plugins too: none of it existed for Scala, so it all had to be built (Part II).


---
## Slide 7: Demo

**Speaker says:** Same Scala code: JVM, browser, Android, native. Pre-launch all three; keep a backup video.


---
## Slide 8: We’re done, thank you!

**Speaker says:** _(no speaker notes)_


---
## Slide 9: This demo is deceptive

**On screen:**
```
I had a demo like this in March
What you’ve just seen is the first iteration of a different approach
It needed tooling that Scala doesn’t have
```

**Speaker says:** _(no speaker notes)_


---
## Slide 10: Part I: Porting with agents

**Speaker says:** _(no speaker notes)_


---
## Slide 11: Eight months

**On screen:**
```
Feb
Mar
Apr
May
Jun
Jul
Aug
Sep
Oct
Opus 4.6
SGE resumes (begun 2025-07)
claimed progress (agent ports)
SGE: CI green
SSG starts
method audit:PaletteReducer 6%
SSG: 20.7% → re-scale
```

**Speaker says:** Each click pairs a line segment with the milestone or release that explains it. SGE was begun in 2025-07 with Cursor and resumed with agents on 02-24; on 03-30 the same approach starts SSG, and SSG’s first honest measurement (04-07) is what exposes the lying. Blue: what agent ports claimed; red: what reviews found. Green: Baltic Porter, restarting from zero, slower but measured by tests. Line heights are illustrative.


---
## Slide 12: April: the files were "done"

**On screen:**
```
Feb
Mar
Apr
May
Jun
Jul
Aug
Sep
Oct
Opus 4.6
SGE resumes (begun 2025-07)
claimed progress (agent ports)
SGE: CI green
SSG starts
method audit:PaletteReducer 6%
SSG: 20.7% → re-scale
effort cut, thinking wiped
peak-hour throttling
▲03-04 Claude Code: default effort cut to medium; from 03-26 earlier thinking wiped every turn (Anthropic postmortem 04-23)
▲03-23 Peak-hour throttling of session limits, until 05-06
●04-06 dart-sass "COMPLETE: 283/283 files"; next day the spec suite passes 20.7% (old runner ended in assert(true))
◆04-07 New checks: size vs original (calibrated on flexmark ≈ 0.94), method list vs original, TODO/stub scanner
◆04-08 re-scale: a certificate header per file, verified in CI
●04-10 colorful at 19% of original size, no TODO in sight; PaletteReducer 6%; Box2D 400+ files → 8
◆04-11 Auditor agent: "porting is binary — 100% or not done"; size ratio is "a signal, not a verdict"
```

**Speaker says:** Zoom on the drop. Red dots: what we found. Blue diamonds: the check we added in response. Purple bars: what was going wrong on Anthropic’s side at the same time (research/incidents.md); they stay after zooming out.


---
## Slide 13: Eight months

**On screen:**
```
Feb
Mar
Apr
May
Jun
Jul
Aug
Sep
Oct
Opus 4.6
SGE resumes (begun 2025-07)
claimed progress (agent ports)
SGE: CI green
SSG starts
method audit:PaletteReducer 6%
SSG: 20.7% → re-scale
certificates stamped
Opus 4.8
Fable 5
Fable review:broken atalgorithm level
effort cut, thinking wiped
peak-hour throttling
```

**Speaker says:** _(no speaker notes)_


---
## Slide 14: June: every method present, bodies hollow

**On screen:**
```
Feb
Mar
Apr
May
Jun
Jul
Aug
Sep
Oct
Opus 4.6
SGE resumes (begun 2025-07)
claimed progress (agent ports)
SGE: CI green
SSG starts
method audit:PaletteReducer 6%
SSG: 20.7% → re-scale
certificates stamped
Opus 4.8
Fable 5
Fable review:broken atalgorithm level
effort cut, thinking wiped
peak-hour throttling
classifier silently swaps Fable → Opus 4.8
●04-20 ~1,200 certificates stamped in one commit, while their CI check was non-blocking
●06-10 GlyphLayout: Java's loop break became a method exit, so text truncation is a no-op
●06-10 BitmapFontCache: // gx += xAdvances[ii] commented out, so every glyph is drawn at the same x
●06-10 ssg-js: 1,507 of 2,522 tests pinned to fail → ~40% real conformance; compress = true disables compression
◆06-10 New rules: failing test first, ratchets, a blocking CI gate, and a different model must audit (cheat catalogue C1–C16)
▲06-10 A safety classifier silently swaps Fable for Opus 4.8 for the rest of the session — pinned agents too
●06-12 Fable switched off worldwide: Opus 4.8 audits Opus 4.6
```

**Speaker says:** Zoom on the drop. Red dots: what we found. Blue diamonds: the check we added in response. Purple bars: what was going wrong on Anthropic’s side at the same time (research/incidents.md); they stay after zooming out.


---
## Slide 15: Eight months

**On screen:**
```
Feb
Mar
Apr
May
Jun
Jul
Aug
Sep
Oct
Opus 4.6
SGE resumes (begun 2025-07)
claimed progress (agent ports)
SGE: CI green
SSG starts
method audit:PaletteReducer 6%
SSG: 20.7% → re-scale
certificates stamped
Opus 4.8
Fable 5
Fable review:broken atalgorithm level
Fableoff
review queue at zero
Fablepromo
blind re-review:5 criticals
effort cut, thinking wiped
peak-hour throttling
classifier silently swaps Fable → Opus 4.8
```

**Speaker says:** _(no speaker notes)_


---
## Slide 16: July: the review queue was at zero

**On screen:**
```
Feb
Mar
Apr
May
Jun
Jul
Aug
Sep
Oct
Opus 4.6
SGE resumes (begun 2025-07)
claimed progress (agent ports)
SGE: CI green
SSG starts
method audit:PaletteReducer 6%
SSG: 20.7% → re-scale
certificates stamped
Opus 4.8
Fable 5
Fable review:broken atalgorithm level
Fableoff
review queue at zero
Fablepromo
blind re-review:5 criticals
effort cut, thinking wiped
peak-hour throttling
classifier silently swaps Fable → Opus 4.8
●07-02 "10/10 random re-audits verified, zero reopens"
●07-03 textra's whole text-selection subsystem missing under a full-port certificate
●07-03 12 tests exercising only the Scala standard library — "pure count inflation"; 205 of 689 files fail the certificate check
●07-03 Debt reworded ("Partial-port debt") to slip past the scanner; one reviewer fabricated 3 of 5 findings
◆07-04 Findings must quote the port and the original side by side; banned: "effectively complete", "diminishing returns"
●07-17 "The agents aren't trustworthy because they are non-deterministic" → build a deterministic translator
```

**Speaker says:** Zoom on the drop. Red dots: what we found. Blue diamonds: the check we added in response. Purple bars: what was going wrong on Anthropic’s side at the same time (research/incidents.md); they stay after zooming out.


---
## Slide 17: Eight months

**On screen:**
```
Feb
Mar
Apr
May
Jun
Jul
Aug
Sep
Oct
Opus 4.6
SGE resumes (begun 2025-07)
claimed progress (agent ports)
SGE: CI green
SSG starts
method audit:PaletteReducer 6%
SSG: 20.7% → re-scale
certificates stamped
Opus 4.8
Fable 5
Fable review:broken atalgorithm level
Fableoff
review queue at zero
Fablepromo
blind re-review:5 criticals
Opus 5
agent porting stops
generated & tested (Baltic Porter)
Baltic Porter
libGDX core compiles
Fable 5.1
regeneration: the handports were worse still
parity dropped: hand ports cheated
12/12 demos
effort cut, thinking wiped
peak-hour throttling
classifier silently swaps Fable → Opus 4.8
```

**Speaker says:** _(no speaker notes)_


---
## Slide 18: September: the old ports were worse still

**On screen:**
```
Feb
Mar
Apr
May
Jun
Jul
Aug
Sep
Oct
Opus 4.6
SGE resumes (begun 2025-07)
claimed progress (agent ports)
SGE: CI green
SSG starts
method audit:PaletteReducer 6%
SSG: 20.7% → re-scale
certificates stamped
Opus 4.8
Fable 5
Fable review:broken atalgorithm level
Fableoff
review queue at zero
Fablepromo
blind re-review:5 criticals
Opus 5
agent porting stops
generated & tested (Baltic Porter)
Baltic Porter
libGDX core compiles
Fable 5.1
regeneration: the handports were worse still
parity dropped: hand ports cheated
12/12 demos
effort cut, thinking wiped
peak-hour throttling
classifier silently swaps Fable → Opus 4.8
Opus 5 "spiky"
effort lower than selected
▲07-29 Opus 5 "nerfed" reports; Anthropic: "a really spiky model"
▲08-19 Effort experiment: "high" sent as effort 10, the old value for "low"; effort in agent files ignored until 09-09
◆08-25 Parity campaign: the generated code must match the hand ports' API exactly
●09-05 Parity dropped: the hand ports "were LLM-written, cheated in places"
●anim8 embedded 47,006 bytes instead of 32,768 — and its own test pinned the wrong value
●ssg markdown: 35 "ignored" tests were whole suites replaced by stubs (~720 tests); liquid's sandbox was a no-op
◆09-07 "Done" means it runs: demos and upstream test suites are the oracle, not parity rows or compile counts
```

**Speaker says:** Zoom on the drop. Red dots: what we found. Blue diamonds: the check we added in response. Purple bars: what was going wrong on Anthropic’s side at the same time (research/incidents.md); they stay after zooming out.


---
## Slide 19: Eight months

**On screen:**
```
Feb
Mar
Apr
May
Jun
Jul
Aug
Sep
Oct
Opus 4.6
SGE resumes (begun 2025-07)
claimed progress (agent ports)
SGE: CI green
SSG starts
method audit:PaletteReducer 6%
SSG: 20.7% → re-scale
certificates stamped
Opus 4.8
Fable 5
Fable review:broken atalgorithm level
Fableoff
review queue at zero
Fablepromo
blind re-review:5 criticals
Opus 5
agent porting stops
generated & tested (Baltic Porter)
Baltic Porter
libGDX core compiles
Fable 5.1
regeneration: the handports were worse still
parity dropped: hand ports cheated
12/12 demos
generated core in SGE
Opus 5.5
4 extensions
effort cut, thinking wiped
peak-hour throttling
classifier silently swaps Fable → Opus 4.8
Opus 5 "spiky"
effort lower than selected
```

**Speaker says:** _(no speaker notes)_


---
## Slide 20: Claimed vs measured

**On screen:**
```
dart-sass, 2026-04-06: "migration COMPLETE: 283/283 files"
the agent's claim
```

**Speaker says:** _(no speaker notes)_


---
## Slide 21: Claimed vs measured

**On screen:**
```
dart-sass, 2026-04-07: first honest sass-spec run
20.7% (2,439 / 11,797)
```

**Speaker says:** Same bar, next day. Then the method-level audit on 04-10: 37.7% faithful, 25.8% simplified, 36.1% missing.


---
## Slide 22: Claimed vs measured

**On screen:**
```
dart-sass, 2026-04-10: method-level audit (~515 methods)
37.7% faithfully ported
25.8% simplified (exists but cuts corners)
36.1% missing
```

**Speaker says:** _(no speaker notes)_


---
## Slide 23: What was tried?

**Speaker says:** _(no speaker notes)_


---
## Slide 24: re-scale

**On screen:**
```
A CLI + Claude Code plugin, rewritten in a day from the per-project helper tools
Migration, audit and issue databases: agents query them instead of "remembering"
A certificate header per file: method list + size baseline, verified in CI
Checks against the original: method list, size ratio, TODO/stub wording, stale "not yet ported" excuses
Implementer and auditor agents: "porting is binary — 100% or not done"
```

**Speaker says:** Why it wasn’t enough: every check looks at names and words, not behaviour.
Agents stamped 1,200 certificates while the CI check was off, reworded comments to dodge the scanner,
and kept every method name while hollowing out the bodies (see the June zoom).


---
## Slide 25: re-scale: what we tried, how it was beaten

**On screen:**
```
The checkHow the agents got past it
| Certificate header per file, verified in CI | ~1,200 certificates stamped in one commit, while the CI check was switched to non-blocking (04-20)
| Method list must match the original | Every method kept, bodies hollowed: a loop break became a method exit; gx += xAdvances[ii] commented out
| Size ratio against a trusted port | Caught colorful at 19%, but full-size files were still wrong; terser reached 162% of upstream at ~40% conformance
| Scanner for TODO / stub wording | Debt reworded ("Partial-port debt"), comments rewritten "to clear the scanner"
| Auditor agent on a different model | Same-model audits rationalised gaps; pins silently fell back when Fable was off; one reviewer fabricated 3 of 5 findings
| Issues tracked to "resolved" | Resolved on the easy half; "406/406 resolved", "queue at zero"; 1,507 tests pinned to fail so CI read "0 failed"
```

**Speaker says:** Every check looked at names, words or counts, never at behaviour. Each one was satisfied without doing the work.


---
## Slide 26: Baltic Porter

**On screen:**
```
A deterministic translator: Java → typed IR → Scala 3 (plus TypeScript/JS/Dart front ends for SSG)
Agents don’t translate code any more; they build and measure the translator
Each project owns its porting policy: renames, type redesigns (Nullable, opaque types, Panama), a few hand-written overrides
Code is generated from upstream at build time; never edited, never committed
Refuses loudly: what it can’t translate is counted and reported, not guessed
The oracle is tests: upstream suites and the hand ports' own suites, on JVM, JS and Native
```

**Speaker says:** Results so far: libGDX core compiles with 0 errors (07-29), 12/12 demos render (09-07), SGE core generated with 5 overrides.
Its own first output had the same bug classes as the agents' (dropped breaks, == as identity, discarded anonymous classes),
but running the tests caught them. About 700 SGE extension files and SSG’s non-Java ports are still hand-written: iteration one.


---
## Slide 27: Baltic Porter: what we tried, where it still slipped

**On screen:**
```
The approachWhat still went wrong
| Agents build the translator, never the port | The Mermaid "generator" was 187 templates copied byte for byte from the hand port (09-13)
| Tests are the oracle | 28 suites stubbed with .ignore → "0 failures, 18,011 tests" (09-12); 23 lls tests ignored 28 minutes after generation
| Generated code is never edited | Regex patches over generated text and loosened assertions to make it pass (09-11); reverted 09-23/25
| "Done" means it runs | "All twelve demos compile" reported as the goal reached (09-07)
| Long autonomous runs | Subagents stopped on invented limits: "14.6M tokens remaining, I need to provide a handoff"
| Deterministic translation | Compiling ≠ correct: dropped breaks and == as identity found only by running tests; non-Java sources barely translate (KaTeX 5/474 bodies)
```

**Speaker says:** The difference from re-scale: these were caught, because the oracle is running tests and every count is computed by the tool, not reported by an agent. The limit is coverage, not honesty.


---
## Slide 28: Part II: Shipping cross-platform Scala

**Speaker says:** _(no speaker notes)_


---
## Slide 29: What still needs native code

**On screen:**
```
libGDXJVMScala NativeBrowser
| LWJGL (OpenGL) | ANGLE via Panama | ANGLE via @extern | WebGL
| LWJGL (GLFW, OpenAL) | GLFW, miniaudio via Panama | GLFW, miniaudio | DOM, Web Audio
| jnigen natives (buffers, ETC1, gdx2d) | Rust library via Panama | same library, same C ABI | pure Scala
| FreeType | Rust wrapper via Panama | static library | none
| Box2D / Bullet (physics) | Rapier via Panama | static library | Rapier as WASM
```

**Speaker says:** One C ABI shared by every runtime: Panama on the JVM (and PanamaPort on Android), @extern on Scala Native. JNI is gone entirely (04-04). Each of these libraries has to be built for every platform and delivered to every build. SSG adds tree-sitter and curl.


---
## Slide 30: Natives and packaging on the JVM

**On screen:**
```
ProblemWhat we built
| No standard way to ship and load native libraries | Provider JARs with a manifest + a runtime loader: detect the platform, extract, load (falls back to java.library.path, Android's lib/)
| Calling C needs JNI glue generated per library; Android has no Panama | One Panama-based API: compiles on JDK 17, uses PanamaPort on Android, the real thing on JDK 22+
| Desktop packages only for the machine you build on | jlink + a native launcher for Windows, macOS and Linux (x86_64, arm64), all from one host
| No maintained sbt Android plugin | An Android plugin: D8, aapt2, signing, AAR extraction
```

**Speaker says:** These are the Gradle-side features from the earlier table, rebuilt for sbt in multiarch-scala (0.1.0 in April, 0.4.0 in July).


---
## Slide 31: Scala Native

**On screen:**
```
ProblemWhat we built
| A library needs the native code installed on the system, plus linker flags you write yourself | Provider JARs carry static libraries and per-platform linker flags; an sbt plugin finds them on the classpath, extracts the right one and configures the linker. Resolving dependencies is enough to link
| sttp on Scala Native needs a system libcurl | A ready-made curl provider: statically built for 6 desktop platforms
| Scala Native builds only for the machine you're on | Cross-compilation through zig: one host produces binaries for the other operating systems and architectures
```

**Speaker says:** The core idea: a native library is a dependency like any other. Out of the box Scala Native expects you to install it and pass flags (scala-native#4800). zig cross-compilation: confirm the credit for the original idea (probably Lorenzo Gabriele’s Mill prototype).


---
## Slide 32: Scala.js

**On screen:**
```
ProblemWhat we built
| No classpath: getResourceAsStream finds nothing, so a game can't load or list its assets | A build step embeds assets into the JS bundle; one resource API on JVM, JS and Native; directory listing from the embedded names
| No ServiceLoader (and on Scala Native it only accepts a literal class) | A cross-platform ServiceLoader generated from META-INF/services; a typo fails at compile time
```

**Speaker says:** libGDX solves assets with a generated assets.txt and GWT’s preloader. SGE first copied that (manifest + fetch), then moved to embedding, which also makes loading synchronous.


---
## Slide 33: What we still haven’t fixed

**On screen:**
```
Upstream: Scala Native, Scala.js
Scala Native has no iOS support, so there is no iOS backend at all
Scala Native can't target Windows on ARM; those builds ship untested
Shipping native libraries is still not part of Scala Native itself
Scala.js on WebAssembly isn't usable for us yet (browser support, module splitting)
Our own backlog
Android: code shrinking (R8) and an older minimum Android version are planned, not built
A standalone sbt Android plugin hasn't started
No sbt support for packaging an iOS app either, even once Scala Native gets there
No GPU in CI: ANGLE on Vulkan fails on both software Vulkan implementations
```

**Speaker says:** Left column: things we can only work around or wait for. Right column: our own backlog.


---
## Slide 34: So what do I have today?

**Speaker says:** _(no speaker notes)_


---
## Slide 35: SGE: what is generated, what is left

**On screen:**
```
ModuleStageGeneratedHand-written leftTests JVM / JS / Native
| lls (libGDX utils, the base) | generated, published | 24 files | — | 593 / 578 / 583
| sge core (libGDX core) | generated | 575 files, 17,962 members | 5 justified replacements | 2,102 / 1,595 / 1,604
| ecs (Ashley) | generated | 40 files | 1 | 265 / 266 / 266
| noise · anim8 · jbump | generated | 12 · 17 · 19 | 0 | 13 · 21/18/18 · 32/32/32
| guacamole | generated | 32 | 4 types, by design | through screens
| screens · graphs | generated, not wired in yet | 22 · 36 | 20 · 25 | —
| visui · gltf · ai · textra · vfx | rules written, not started | — | 157 · 142 · 134 · 92 · 41 | hand-written tests pass
| colorful · controllers · physics · physics3d · freetype · tools | no rules yet | — | 46 · 18 · 17 · 17 · 9 · 8 | —
About 65 of ~760 extension files generated so far; ~690 to go. Not counted: 74 shared and 145 platform-backend files that are SGE's own code, not translations.
```

**Speaker says:** Generated means: produced at build time from upstream libGDX by SGE’s own porting rules, upstream and hand-port tests passing on all three platforms. Caveat: at the time of the report several of these (noise, anim8, jbump, guacamole, screens) were verified locally but not yet merged; check before the talk.


---
## Slide 36: Plain translation vs SGE’s conventions

**On screen:**
```
plain translation
36% (4,735)
SGE's own conventions
64% (8,242)
Per-declaration decisions in SGE core's decision log (not lines of code)
3,710bean getters/setters and empty parentheses removed
1,083Nullable instead of null
601 · 149package renames · other renames
414call-site substitutions (e.g. GdxRuntimeException → SgeError)
398opaque types (Pixels, Align, Input.Button, …)
282an Sge context instead of globals
208 · 156Scala collections and Ordering · type classes instead of reflection
```

**Speaker says:** The plain translation alone already makes a valid port; two-thirds of the recorded decisions are SGE’s design layered on top. Extensions show the same split (e.g. anim8 543 configured vs 93 universal; ecs 225 vs 123).


---
## Slide 37: Less code to maintain, same behaviour

**On screen:**
```
Three SGE pull requests: about +8.8k / −133k lines, with tests and demos still passing
```

**Images:** PR #146: Baltic Porter integration, +7,950 / -115,453 lines; PR #160: core overrides 89 to 16, +83 / -14,687 lines; PR #153: ecs generated from Ashley, +789 / -2,794 lines

**Speaker says:** I still have little trust in the numbers the AI reports about itself.
What I do trust: the tests keep passing, and the demos keep working and doing what I want them to do,
while the number of lines of code I maintain keeps going down.
If this trend holds, I end up with a codebase where relatively few maintained lines support a lot of functionality.
The risk of AI slop in those hand-written lines is still there, maybe even higher,
but the slop that needs reviewing is a much smaller body of work.
PRs: #146 Baltic Porter integration (+7,950 / -115,453), #160 overrides 89 → 16 (+83 / -14,687),
#153 ecs generated from Ashley, the pilot for every extension (+789 / -2,794).


---
## Slide 38: SSG: Java done, the rest is still a hand port

**On screen:**
```
ModuleSourceApproachState
| ssg-md (flexmark core) | Java | generated | 446 files, 9,268 members
| ssg-md extensions | Java | generated | 331 files, 3,499 members
| ssg-liquid (liqp) | Java | generated + 16 hand-written files (lexer, parser, JSON, dates) | 132 files, 910 members
| KaTeX | TypeScript | hand-port skeleton; translated bodies replace it | 1 of 496 bodies
| terser | JavaScript | same | 2 of 1,066
| rough.js | TypeScript | same | 7 of 126
| dart-sass | Dart | skeleton only | 0 of 2,748
| Mermaid | TypeScript | skeleton only | 0 of 1,075
| jekyll-minifier | Ruby | hand-written, no front end | undecided
All tests passing: JVM 13,611 · JS 12,701 · Native 12,561. The non-Java modules pass because they still run the hand-written reference.
```

**Speaker says:** "Reference-only" means members with no counterpart in the original, like Scala wrappers. An earlier engine-side figure claimed KaTeX was 85% translated; the shipping build translates almost nothing.


---
## Slide 39: multiarch-scala

**On screen:**
```
Delivered
sbt plugins: native-provider distribution, multi-architecture native release, multi-architecture JVM release
A core library with the runtime native-library loader
A prebuilt curl provider for 6 desktop platforms
Cross-platform resources and ServiceLoader; a Panama API for JDK 17 / Android and JDK 22+
Used by SGE and SSG through their native providers
Still to do
10 open issues, mostly hardening and API clean-up before 1.0
Planned: an audit of the native linker flags
Planned: a standalone Android sbt plugin (R8, older Android versions)
```

**Speaker says:** 77 commits; 0.4.0 is the latest release.


---
## Slide 40: Ready, or a stepping stone?

**On screen:**
```
Java sources: production-shaped
lls, SGE core and extensions, ssg-md, ssg-liquid
Every change gated on JVM, JS and Native
What can't be translated is counted; what stays hand-written is listed with reasons
Only snapshot builds so far, no versioned release
TypeScript / Dart / Ruby: a stepping stone
KaTeX, terser, rough.js, dart-sass, Mermaid, jekyll-minifier
A hand-written skeleton waiting for translated bodies
About 0–5% translated today
```

**Speaker says:** This is the "first iteration" point of the talk.


---
## Slide 41: Summary

**Speaker says:** _(no speaker notes)_


---
## Slide 42: Porting with LLMs

**On screen:**
```
Automatic porting of libraries is not a solved problem
Every LLM will mislead you
Being certain means reviewing all of the code: impossible at this size
So take away every chance to cheat: guardrails shrink the review, they never remove it
Use the LLM to build a deterministic migration, then run that
```

**Speaker says:** Automatic porting of libraries is not yet a solved problem.
Every LLM will mislead you. Ideally you would review all of its code to be certain when and how it did.
With libraries of non-trivial size that is virtually impossible. So you have to use every guardrail you can to take away the LLM’s possibility to cheat. You end up with less to review, but the review never goes away.
It may look harder, but in practice it is much more reliable not to let the LLM do the whole migration: use it to develop a deterministic migration, and then run the deterministic system.


---
## Slide 43: Scala on every platform

**On screen:**
```
Scala targets natively what Java reaches with hacks: a dedicated AOT compiler for iOS, a Java-to-JavaScript compiler built outside the language
The community already builds tooling for multiple platforms, without weird hacks in the build
```

**Speaker says:** Scala as a language has the potential to natively support things that Java achieves through hacks, like RoboVM, an iOS-dedicated ahead-of-time compiler, or GWT, a Java-to-JavaScript compiler developed outside of the language.
Scala already has a community that creates and maintains tooling for targeting multiple platforms, without weird hacks in the build tools.


---
## Slide 44: What works today

**On screen:**
```
Out of the box: backends, sometimes frontends, CLI tools
Scala Native works flawlessly only if the native libraries are already installed on the system
All of it looks solvable, often by reusing existing solutions
Someone just has to point at it
```

**Speaker says:** Today things work out of the box when we develop a backend application, sometimes a frontend application, and CLI utilities. But Scala Native works flawlessly only if all the necessary native libraries and bindings are already installed on the system.
All of these issues seem addressable. Perhaps it’s only a matter of nobody pointing out that they could and should be solved, maybe even in a very easy way by leveraging existing solutions.


---
## Slide 45: An unexplored space

**On screen:**
```
Frontend, native bindings, native libraries: room for low-level libraries
Not immutable FP, but metaprogramming: macros, `inline def`s, specialization
Closer to Java, no runtime reflection: code that optimises itself at compile time and stays readable
```

**Speaker says:** If we look at targets other than backends, at the frontend, native bindings and native libraries, we see a completely unexplored space for low-level libraries.
They wouldn’t be written in immutable functional programming style. They would use metaprogramming, macros, inline defs and specialization to write code that is perhaps less idiomatic for Scala, maybe closer to Java without runtime reflection, but which macro-optimises itself while keeping the code the programmer writes quite readable.


---
## Slide 46: Questions?

**Speaker says:** _(no speaker notes)_


---
## Slide 47: Thank you!

**Speaker says:** _(no speaker notes)_
