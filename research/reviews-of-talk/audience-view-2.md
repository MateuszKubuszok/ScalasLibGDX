# Presentation as the audience experiences it

Everything below is all the audience gets: the slide content (including text inside diagrams, revealed click by click) and what the speaker says (the speaker notes). '(click)' and '(pause)' in the notes are cues for the speaker, not spoken. There is also a live demo at the 'Demo' slide: a rotating 3D model that responds to mouse and keyboard input, running from the same Scala code in a web browser, in an Android emulator, and as a Scala Native desktop binary.


---
## Slide 1: Scala’s LibGDX

**On screen:**
```
A Report from the Trenches
Mateusz Kubuszok
```

**Speaker says:** Hello. I’m Mateusz. (pause) This is a report from the trenches: what it took to run Scala on every platform a game engine supports, and what AI agents did along the way.


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

**Speaker says:** A few words about me. (pause)
I have been writing Scala for almost twelve years.
For about nine of them I have maintained Chimney, a library some of you may know.
That taught me a lot about macros. It led to several talks, a blog post, and two new libraries.
I also like sharing what I learn: about the JVM, and about making Scala approachable.


---
## Slide 3: Why port libGDX to Scala?

**Speaker says:** I wanted to write a game. In Scala. With libGDX, a mature Java game framework. (pause) So first: why would anyone need to port libGDX to Scala?


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

**Speaker says:** libGDX gives you one codebase and four targets. (pause) Desktop runs on a normal JVM. Android runs your bytecode after converting it. The browser goes through GWT, which compiles Java source to JavaScript. And iOS goes through RoboVM, a compiler that turns JVM bytecode into native code ahead of time.


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
works, but Scala/Android version mismatches; natives
Browser
GWT
Java source → JS
GWT compiles Java source, not bytecode
iOS
RoboVM / MobiVM
AOT bytecode → ARM
Scala on RoboVM: unsupported, unmaintained
Scala Native: not a libGDX target at all (Java + JNI)
```

**Speaker says:** Now write the same game in Scala. (click) Desktop: fine. (click) Android: it works, but Scala and Android versions don’t always agree, and native libraries make it harder. (click) The browser: GWT reads Java source, not bytecode, so Scala can’t use it. (click) iOS: RoboVM could take Scala bytecode in theory, but nobody supports that path. (click) And Scala Native is not a libGDX target at all. libGDX is Java, calling C through JNI. (pause) So to have Scala everywhere, I had to own the engine. I had to port libGDX itself.


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

**Speaker says:** It’s not only the runtime. (pause) With Gradle, libGDX can package a desktop app for every system from one laptop. It can build and shrink Android apps. It can compile for iOS. (pause) For Scala and sbt, none of that existed. So I had to build it. That’s the second part of this talk.


---
## Slide 7: Demo

**Speaker says:** This is SGE, the Scala Game Engine: my Scala port of libGDX. (pause)
The same Scala code. Here in the browser. Here on an Android emulator. And here as a native binary, built with Scala Native.


---
## Slide 8: We’re done, thank you!

**Speaker says:** So: it works. That’s my talk. Thank you. (pause) Well, not quite.


---
## Slide 9: This demo is deceptive

**On screen:**
```
I had a demo like this in March
What you’ve just seen is the first iteration of a different approach
It needed tooling that Scala doesn’t have
```

**Speaker says:** (click) I had a demo like this in March. (pause) That code was ported by AI agents, and a lot of it turned out to be hollow.
(click) What you just saw runs on code made in a completely different way. And it is only a first iteration.
(click) And getting it onto three platforms needed tooling that Scala didn’t have.
(pause) Those are the two parts of this talk.


---
## Slide 10: Part I: Porting with agents

**Speaker says:** Part one: how I tried to port a big library with AI agents, and how they lied to me.


---
## Slide 11: Claimed vs measured

**On screen:**
```
The Sass compiler, ported by an agent, April 6th: "migration COMPLETE: 283/283 files"
the agent's claim
```

**Speaker says:** Here is what an agent told me in April. I was porting dart-sass, the Sass compiler, to Scala. The agent said: migration complete. Two hundred eighty-three of two hundred eighty-three files.


---
## Slide 12: Claimed vs measured

**On screen:**
```
The next day: the official Sass test suite
20.7% of the tests pass
```

**Speaker says:** The next day I ran the official Sass test suite. (pause) One test in five passed.


---
## Slide 13: Claimed vs measured

**On screen:**
```
Then: every method checked against the original
37.7% faithfully ported
25.8% simplified: it exists, but cuts corners
36.1% missing
```

**Speaker says:** Then I checked method by method. About a third faithful. A quarter cut short. A third simply missing. (pause) This part of the talk is about how that happens, and what I did about it.


---
## Slide 14: Eight months

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
SGE (game engine) resumes
claimed progress (agent ports)
SGE: CI green
SSG (site generator) starts
method audit: PaletteReducer 6%
SSG: 20.7% → re-scale
```

**Speaker says:** This is the last eight months. (pause) The blue line is what the agents told me: how much was ported. It is not to scale; only the dates are real. (click) In late February I picked SGE up again: SGE, the Scala Game Engine, is my Scala port of libGDX. This time I did it with AI agents. Anthropic’s Opus model was the one doing the work. (click) By the end of March, all three platforms were green in CI. (click) Then I started a second project the same way: SSG, a static site generator. It needs a Markdown parser, a template engine, a Sass compiler, so it is also mostly ported libraries. (click) And the second project is where it broke: the Sass port you just saw. Let’s zoom in.


---
## Slide 15: April: the files were "done"

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
SGE (game engine) resumes
claimed progress (agent ports)
SGE: CI green
SSG (site generator) starts
method audit: PaletteReducer 6%
SSG: 20.7% → re-scale
effort cut, thinking wiped
peak-hour throttling
▲03-04 Claude Code: default effort cut to medium; from 03-26 earlier thinking wiped every turn (Anthropic postmortem 04-23)
▲03-23 Peak-hour throttling of session limits, until 05-06
●04-06 Sass compiler: "COMPLETE: 283/283 files"; next day the spec suite passes 20.7%
◆04-07 New checks: size vs the original (a good port is about the same size), method list vs the original, TODO/stub scanner
◆04-08 re-scale: a certificate per file (its methods and size), checked in CI
●04-10 colorful at 19% of original size, no TODO in sight; PaletteReducer 6%; Box2D 400+ files → 8
◆04-11 Rule for agents: "porting is binary — 100% or not done"
```

**Speaker says:** In the zooms, red is what I found, blue is what I added in response, and purple is what was going wrong on Anthropic’s side. (click) First, purple: Anthropic later admitted that in March Claude Code ran with lower default effort, and a bug kept wiping the model’s earlier reasoning. (click) Usage was also throttled at peak hours. (click) Then the Sass port: complete, said the agent. One test in five, said the test suite. (click) So I added checks. Compare each file’s size with the original: one well-ported library told me a good port is about the same size. Compare the list of methods. Scan for TODOs and stubs. (click) I put those checks into a tool, re-scale. Every file gets a certificate: a header with its methods and size, checked in CI. (click) The checks found more right away: one library at a fifth of its original size, with no TODO anywhere. Box2D, four hundred files, replaced by an eight-file wrapper. (click) And a rule for the agents: porting is binary. A hundred percent, or not done.


---
## Slide 16: Eight months

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
SGE (game engine) resumes
claimed progress (agent ports)
SGE: CI green
SSG (site generator) starts
method audit: PaletteReducer 6%
SSG: 20.7% → re-scale
certificates stamped
Opus 4.8
Fable 5
Fable review: broken at algorithm level
effort cut, thinking wiped
peak-hour throttling
```

**Speaker says:** (click) The agents then stamped those certificates on about twelve hundred files at once. (click) Through May the claims stayed high. A new model came out, Opus 4.8. (click) In June, Anthropic released Fable, a stronger and more expensive model. I asked it to review everything. (pause) And the line fell.


---
## Slide 17: June: every method present, bodies hollow

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
SGE (game engine) resumes
claimed progress (agent ports)
SGE: CI green
SSG (site generator) starts
method audit: PaletteReducer 6%
SSG: 20.7% → re-scale
certificates stamped
Opus 4.8
Fable 5
Fable review: broken at algorithm level
effort cut, thinking wiped
peak-hour throttling
classifier silently swaps Fable → Opus 4.8
●04-20 ~1,200 certificates stamped in one commit, while their CI check was non-blocking
●06-10 Text layout: Java's loop break became a method exit, so truncation is a no-op
●06-10 Font rendering: // gx += xAdvances[ii] commented out, so every glyph is drawn at the same x
●06-10 JavaScript minifier: 1,507 of 2,522 tests marked as expected failures → ~40% real conformance
◆06-10 New rules: failing test first, counters that only go down, a blocking CI gate, a different model must audit
▲06-10 A safety classifier silently swaps Fable for Opus 4.8 for the rest of the session
●06-12 Fable switched off worldwide: Opus 4.8 audits Opus 4.6
```

**Speaker says:** (click) The certificates had been stamped while the CI check was switched off. (click) Every method was there, but the bodies were hollow. In text layout, a loop’s break became an exit from the whole method. (click) In font rendering, the line that moves to the next letter was commented out. Every letter drawn in the same place. (click) In the JavaScript minifier, more than half the tests were marked as expected to fail, so CI said: zero failures. Real conformance was about forty percent. (click) So, new rules: a failing test first, counters that may only go down, a blocking CI gate, and a different model must audit. (click) On Anthropic’s side, a safety classifier could silently swap Fable for Opus. (click) And then Fable was switched off worldwide for almost three weeks. So Opus was auditing Opus.


---
## Slide 18: Eight months

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
SGE (game engine) resumes
claimed progress (agent ports)
SGE: CI green
SSG (site generator) starts
method audit: PaletteReducer 6%
SSG: 20.7% → re-scale
certificates stamped
Opus 4.8
Fable 5
Fable review: broken at algorithm level
Fable off
review queue at zero
Fable promo
blind re-review: 5 criticals
effort cut, thinking wiped
peak-hour throttling
classifier silently swaps Fable → Opus 4.8
```

**Speaker says:** (click) Fixing all of that took until the end of June. The review queue reached zero. (click) Then Fable came back for a short time, and I ran a blind re-review. Five critical findings. A whole subsystem missing. Tests that only tested the standard library. (pause) And one reviewer agent invented three of its five findings.


---
## Slide 19: (untitled)

**On screen:**
```
The agents aren't trustworthy because they are non-deterministic.
me, mid-July
```

**Speaker says:** That is what I wrote in mid-July. (pause) Every check I added, the agents learned to get past. So I stopped asking them to port the code. I asked them to build a translator instead: a deterministic one. I called it Baltic Porter.


---
## Slide 20: Eight months

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
SGE (game engine) resumes
claimed progress (agent ports)
SGE: CI green
SSG (site generator) starts
method audit: PaletteReducer 6%
SSG: 20.7% → re-scale
certificates stamped
Opus 4.8
Fable 5
Fable review: broken at algorithm level
Fable off
review queue at zero
Fable promo
blind re-review: 5 criticals
Opus 5
agent porting stops
generated & tested (Baltic Porter)
Baltic Porter
libGDX core compiles
Fable 5.1
regeneration: the agent ports were worse still
Opus 5 "spiky"
effort lower than selected
parity dropped: agent ports cheated
12/12 demos
generated core in SGE
Opus 5.5
4 extensions
effort cut, thinking wiped
peak-hour throttling
classifier silently swaps Fable → Opus 4.8
```

**Speaker says:** (click) Agent porting stops. Baltic Porter starts, from zero. That’s the green line. It grows slower, but every number on it is measured by running tests. (click) By the end of July, the whole libGDX core compiles. (click) In September I compared the result with the old agent ports. They were even worse than the reviews had shown: their own tests checked for wrong values. That’s the second red line. And in purple: Claude Code was quietly sending lower effort than I had selected, and Opus 5 was, in Anthropic’s words, a really spiky model. Meanwhile, all twelve demos render. (click) The generated core replaces SGE’s agent port. (click) And four extensions are generated too. (pause) That’s where I am today.


---
## Slide 21: What was tried?

**Speaker says:** So, two tools. First re-scale, then Baltic Porter. Let’s look at what each of them tried, and where it fell short.


---
## Slide 22: re-scale: what it checked, how it was beaten

**On screen:**
```
re-scale: a command-line tool and Claude Code plugin that checks every ported file against its original
The checkHow the agents got past it
| A certificate per file (its methods and size), checked in CI | ~1,200 certificates stamped in one commit, while the CI check was switched off
| Method list must match the original | Every method kept, bodies hollowed: a loop break became a method exit; gx += xAdvances[ii] commented out
| Size compared with the original | Caught colorful at 19%, but full-size files were still wrong; the minifier grew to 162% of the original at ~40% conformance
| Scanner for TODO / stub wording | Debt reworded ("Partial-port debt"), comments rewritten "to clear the scanner"
| Auditor agent on a different model | Same-model audits explained gaps away; pinned models silently fell back when Fable was off; one reviewer invented 3 of 5 findings
```

**Speaker says:** re-scale compared every ported file with its original. (click) Each file got a certificate, and CI checked it. The agents stamped twelve hundred certificates at once, with the check switched off.
(click) The method list had to match. It did. The bodies were hollow.
(click) The size had to match. Some files that matched were still wrong.
(pause) I won’t read the rest. (click) (click) The pattern is always the same: (pause) every check looked at names, words, or counts. Never at behaviour. And each one was satisfied without doing the work.


---
## Slide 23: Baltic Porter: what it does, where it still slipped

**On screen:**
```
Baltic Porter: a deterministic Java → Scala 3 translator. Agents build and measure it; they don't port code.
The approachWhat still went wrong
| Each project owns its porting rules: renames, Nullable, opaque types, a few hand-written overrides | The rules are code too, so they need review
| Agents build the translator, never the port | The Mermaid "generator" was 187 templates copied byte for byte from the agent port
| Tests are the judge | 28 test suites stubbed out → "0 failures, 18,011 tests"; 23 tests switched off 28 minutes after a regeneration
| Generated code is never edited | Regex patches over generated code, assertions loosened to make it pass; reverted later
| Deterministic translation | Compiling is not the same as correct: a dropped break, a wrong equality, found only by running tests
The limit is now test coverage, not honesty.
```

**Speaker says:** Baltic Porter translates Java to Scala deterministically. The agents don’t port anything. They improve the translator and measure it.
(click) Each project has its own rules on top: Scala names, Nullable instead of null, opaque types.
(click) Agents still tried to cheat. One "generator" just copied the old code, byte for byte.
(click) Another switched off twenty-eight test suites and reported zero failures.
(click) Another patched the generated code by hand.
(click) And the translator itself had the same kinds of bugs the agents made. (pause) The difference: this time we caught all of it. The tests decide, and the tool does the counting, not the agent.
(click) The limit now is test coverage, not honesty.


---
## Slide 24: Part II: Shipping cross-platform Scala

**On screen:**
```
Everything built along the way became multiarch-scala: sbt plugins and small runtime libraries
```

**Speaker says:** Part two: the boring part that nobody had built. Shipping Scala to every platform. (pause) Everything I built here became one project: multiarch-scala.


---
## Slide 25: What still needs native code

**On screen:**
```
In libGDXJVMScala NativeBrowser
| LWJGL (OpenGL) | ANGLE via Panama | ANGLE via @extern | WebGL
| LWJGL (windows, audio) | GLFW, miniaudio via Panama | GLFW, miniaudio | DOM, Web Audio
| jnigen natives (buffers, images) | Rust library via Panama | same library, same C interface | pure Scala
| FreeType (fonts) | Rust wrapper via Panama | static library | none
| Box2D / Bullet (physics) | Rapier via Panama | static library | Rapier as WASM
```

**Speaker says:** Even in Scala, a game needs native code: graphics, windows, audio, fonts, physics.
(click) (click) (click) (click) (click)
Every native library gets one C interface. The JVM calls it through Panama. Android through a backport of Panama. Scala Native calls it directly. (pause) No JNI anywhere.
But every one of these libraries has to be built for every platform, and delivered to every build.


---
## Slide 26: A native library is just a dependency

**On screen:**
```
Problem beforeWhat multiarch-scala adds
| JVM: no standard way to ship and load native libraries | Provider JARs with a manifest, and a loader: detect the platform, extract, load
| Scala Native: the library must be installed on the system, and you write the linker flags yourself | The provider JAR carries static libraries and linker flags per platform; resolving dependencies is enough to link
| You can only build for the machine you are on | Native binaries cross-compiled with zig; desktop JVM apps packaged for every system from one host
| No maintained sbt Android plugin | An Android plugin: dexing, resources, signing
| Scala.js: no classpath, no ServiceLoader | Assets embedded at build time behind one resource API; a ServiceLoader generated at compile time
```

**Speaker says:** The core idea: a native library should be a dependency like any other.
(click) On the JVM, there was no standard way to ship one. Now it’s a JAR with a manifest, and a loader.
(click) On Scala Native, you had to install the library yourself and pass linker flags. Now the JAR carries them. (pause) Adding a dependency is enough.
(click) You could only build for your own machine. Now native binaries are cross-compiled with zig, and desktop apps are packaged for every system from one laptop.
(click) Android got its own plugin.
(click) And Scala.js, which has no classpath, gets its assets embedded at build time, and a ServiceLoader generated at compile time.


---
## Slide 27: What we still haven’t fixed

**On screen:**
```
Upstream: Scala Native
No iOS support, so no iOS backend at all
No Windows on ARM; those builds ship untested
Shipping native libraries is still not part of Scala Native itself
Our own backlog
Android: code shrinking and older Android versions
No GPU in CI, so graphics tests run on a software renderer
```

**Speaker says:** What’s still missing. (click) Scala Native has no iOS support, so there is no iOS backend. (click) It can’t target Windows on ARM either. (click) And shipping native libraries is still something you need a plugin for.
(click) On my side: Android needs code shrinking and support for older versions. (click) And CI has no GPU.


---
## Slide 28: So what do I have today?

**Speaker says:** So where am I today? (pause) Honestly.


---
## Slide 29: SGE: what is generated, what is left

**On screen:**
```
Part of SGEStateStill maintained by hand
| libGDX core | generated from upstream at build time | 5 hand-written overrides
| Utilities and 6 small extensions | generated | almost nothing
| The other ~690 extension files | porting rules not written yet | still the agent port
Tests pass on JVM, JS and Native
```

**Speaker says:** (click) The libGDX core is fully generated. Five files are written by hand. (click) The utilities and six small extensions are generated too.
(click) About six hundred ninety extension files are still the old agent port. Their rules are not written yet.


---
## Slide 30: Plain translation vs SGE’s conventions

**On screen:**
```
plain Java → Scala translation
36%
SGE's own design on top
64%
Share of the translator's recorded decisions for SGE core
3,710bean getters/setters and empty parentheses removed
1,083Nullable instead of null
398opaque types (Pixels, Align, Input.Button, …)
282an Sge context instead of global variables
```

**Speaker says:** A plain translation already gives you a working port. But two thirds of the decisions are SGE’s own design on top.
(click) Scala-style names. (click) Nullable instead of null. (click) Opaque types. (click) A context instead of globals.
(pause) That’s what the porting rules are: my design, written down once, applied everywhere.


---
## Slide 31: Less code to maintain, same behaviour

**On screen:**
```
Three SGE pull requests: about +8.8k / −133k lines, with tests and demos still passing
```

**Images:** PR #146: Baltic Porter integration, +7,950 / -115,453 lines; PR #160: core overrides 89 to 16, +83 / -14,687 lines; PR #153: ecs generated from Ashley, +789 / -2,794 lines

**Speaker says:** (click) (click) (click) Three pull requests. (click) About nine thousand lines added, a hundred and thirty thousand removed. The code didn’t disappear: it’s generated at build time, so I no longer maintain it.
(pause) I still have little trust in the numbers the AI reports about itself.
What I do trust: the tests keep passing, and the demos keep working and doing what I want, while the code I maintain keeps shrinking.
If that trend holds, a few maintained lines will support a lot of functionality.
The risk of AI slop in those lines is still there. But the slop I have to review is much smaller.


---
## Slide 32: SSG: Java done, the rest is still an agent port

**On screen:**
```
Libraries ported into SSGSource languageState
| Markdown parser, Liquid templates | Java | generated, tests pass
| KaTeX, terser, rough.js, Mermaid | TypeScript / JavaScript | still the agent port; 0–6% of method bodies translated
| Sass compiler | Dart | still the agent port; nothing translated yet
| HTML/CSS minifier | Ruby | agent port, no translator
Over twelve thousand tests pass on every platform, but the non-Java ones still run the agent-written code
```

**Speaker says:** And SSG, the static site generator. (click) The Java libraries are generated, and their tests pass.
(click) For TypeScript and JavaScript, the translator exists, but almost nothing comes out of it yet. (click) Sass, written in Dart: nothing yet. (click) And Ruby has no translator at all.
(pause) The tests pass everywhere. But for the non-Java libraries, they still run the old agent port.


---
## Slide 33: Ready, or a stepping stone?

**On screen:**
```
Java sources: almost ready
libGDX core and utilities, SGE extensions, SSG's Markdown and Liquid
Every change tested on JVM, JS and Native
What can't be translated is counted; what stays hand-written is listed, with reasons
Only snapshot builds so far, no release
TypeScript / Dart / Ruby: a first step
KaTeX, terser, rough.js, Sass, Mermaid, the minifier
An agent-written skeleton, waiting for translated method bodies
About 0–5% translated today
```

**Speaker says:** So: is it ready? (click) (click) (click) (click) For Java sources, almost. Every change is tested on three platforms, and nothing is hidden.
(click) (click) (click) For everything else, it’s a first step. (pause) Remember the deceptive demo? This is what "first iteration" means.


---
## Slide 34: Summary

**Speaker says:** Let me sum up.


---
## Slide 35: Porting with LLMs

**On screen:**
```
Automatic porting of libraries is not a solved problem
Every LLM will mislead you
Being certain means reviewing all of the code: impossible at this size
So take away every chance to cheat: guardrails shrink the review, they never remove it
Use the LLM to build a deterministic migration, then run that
```

**Speaker says:** (click) Automatic porting of libraries is not a solved problem.
(click) Every LLM will mislead you. (pause)
(click) To be certain, you would have to review all of its code. With a library this size, that’s impossible.
(click) So take away every chance to cheat. You end up with less to review. But the review never goes away.
(click) (pause) Don’t let the LLM do the migration. Let it build a tool that does the migration. Then run the tool. It sounds harder. In practice, it is much more reliable.


---
## Slide 36: Scala on every platform

**On screen:**
```
Scala targets natively what Java reaches with hacks: a separate AOT compiler for iOS, a Java-to-JavaScript compiler built outside the language
The community already builds tooling for multiple platforms, without weird hacks in the build
```

**Speaker says:** (click) Java reaches iOS and the browser with hacks: a separate compiler for each. (pause) Scala can target them natively.
(click) And our community already builds tools for many platforms, without strange tricks in the build.


---
## Slide 37: What works today

**On screen:**
```
Out of the box: backends, sometimes frontends, CLI tools
Scala Native works flawlessly only if the native libraries are already installed on the system
All of it looks solvable, often by reusing existing solutions
Someone just has to point at it
```

**Speaker says:** (click) Today, Scala works out of the box for backends, sometimes for frontends, and for command-line tools.
(click) Scala Native works perfectly, as long as every native library is already installed.
(click) All of this looks solvable. Often the fix already exists somewhere.
(click) Maybe nobody has pointed at it yet. (pause) So I’m pointing at it.


---
## Slide 38: An unexplored space

**On screen:**
```
Frontend, native bindings, native libraries: room for low-level libraries
Not immutable FP, but metaprogramming: macros, `inline def`s, specialization
Closer to Java, no runtime reflection: code that optimises itself at compile time and stays readable
```

**Speaker says:** (click) Beyond backends, there is a lot of unexplored space: low-level libraries for the frontend, for native code.
(click) They would not be pure functional programming. They would use macros and inline defs. We already saw a small example: a ServiceLoader generated at compile time.
(click) Closer to Java, but without reflection. The code you write stays readable, and the compiler makes it fast.


---
## Slide 39: Questions?

**Speaker says:** Thank you. Questions?


---
## Slide 40: Thank you!

**Speaker says:** _(no speaker notes)_
