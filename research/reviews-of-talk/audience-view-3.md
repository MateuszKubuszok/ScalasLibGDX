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

**On screen:**
```

```

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
bytecode converted
Browser
GWT
Java source → JS
iOS
RoboVM / MobiVM
bytecode → native code
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
bytecode converted
⚠
works, but Scala/Android
version clashes; native libs
Browser
GWT
Java source → JS
GWT compiles Java source,
not bytecode
iOS
RoboVM / MobiVM
bytecode → native code
Scala on RoboVM:
unsupported, unmaintained
Scala Native: not a libGDX target at all (Java + JNI)
```

**Speaker says:** Now write the same game in Scala. (click) Desktop: fine. (click) Android: it works, but Scala and Android versions don’t always agree, and native libraries make it harder. (click) The browser: GWT reads Java source, not bytecode, so Scala can’t use it. (click) iOS: RoboVM could take Scala bytecode in theory, but nobody supports that path. (click) And Scala Native is not a libGDX target at all. libGDX is Java, calling C through JNI. (pause) So to have Scala everywhere, I had to own the engine. I had to port libGDX itself.

---
## Slide 6: The build tooling goes too

**On screen:**
```
| What a game needs | libGDX + Gradle | Scala + sbt
| Desktop apps for Windows / macOS / Linux, built on one host | Construo: bundles a trimmed JVM and a launcher | sbt-native-packager: packages only for the platform you build on
| Android: convert bytecode, shrink, sign, package | Android Gradle Plugin | sbt-android: unmaintained for years
| iOS: compile to native code, package the app | RoboVM / MobiVM Gradle plugin | Nothing: RoboVM doesn't support Scala, Scala Native has no iOS
| Browser build, and knowing which assets exist at runtime | GWT Gradle plugin; the build generates assets.txt, which GWT's preloader reads to fetch and list assets | Scala.js has no classpath, so getResourceAsStream finds nothing; and no build step embeds the assets or lists them
| Native libraries for every platform | gdx-jnigen builds them; one JAR of native libraries per platform | JVM: extract from the JAR by hand; Scala Native: install the library on the system and pass linker flags yourself
```

**Speaker says:** It’s not only the runtime. The build tooling goes too. (click) With Gradle, libGDX packages a desktop app for every system from one laptop. sbt packages only for the system you’re on. (click) Android: Gradle has the official plugin. The sbt one hasn’t been maintained for years. (click) iOS: there’s simply nothing for Scala. (click) The browser: libGDX’s build writes down which assets exist, so the game can find them. Scala.js has no such step. (click) And native libraries: libGDX builds and ships them for every platform. In Scala, you’re on your own. (pause) None of that existed, so I had to build it. That’s the second part of this talk.

---
## Slide 7: Demo

**On screen:**
```

```

**Speaker says:** This is SGE, the Scala Game Engine: my Scala port of libGDX. (pause)
The same Scala code. Here in the browser. Here on an Android emulator. And here as a native binary, built with Scala Native.

---
## Slide 8: We’re done, thank you!

**On screen:**
```

```

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

**On screen:**
```

```

**Speaker says:** Part one: how I tried to port a big library with AI agents, and how they lied to me.

---
## Slide 11: Claimed vs measured

**On screen:**
```
SSG's Sass compiler, ported by an agent, April 6th: "migration COMPLETE: 283/283 files"
the agent's claim
```

**Speaker says:** Besides the game engine, I was building SSG, a static site generator. It needs a Sass compiler, so an agent was porting one to Scala. In April it told me: migration complete. Every file, two hundred eighty-three of them.

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
25.8% cut short: there, but simplified
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
what the agents claimed
SGE: tests green
SSG (site generator) starts
checked method by method:
one file 6% ported
Sass: 1 test in 5
```

**Speaker says:** This is the last eight months. (pause) The blue line is what the agents claimed: how much was ported. Only the dates are real; the heights are not to scale. (click) In late February I picked SGE up again, this time with AI agents. (click) By the end of March, the tests were green on all three platforms. (click) Then I started a second project the same way: SSG, the static site generator, with its Sass compiler. (click) And that’s where it broke. Let’s zoom in.

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
what the agents claimed
SGE: tests green
SSG (site generator) starts
checked method by method:
one file 6% ported
Sass: 1 test in 5
Claude Code: less reasoning
usage throttled at peak hours
▲03-04 Claude Code gave the model less reasoning by default, and a bug made it forget its earlier reasoning (Anthropic admitted it in April)
▲03-23 Usage limits throttled at peak hours
●04-06 Sass compiler: the agent says "complete, 283 of 283 files"; the tests say 1 in 5
◆04-07 New checks: is the file about as long as the original? Does it have the same methods? Any TODOs or stubs?
◆04-08 re-scale: a tool that runs those checks on every file, in CI
●04-10 A colour library at a fifth of its original size, with no TODO anywhere; a physics engine of 400 files replaced by 8
◆04-11 Rule for the agents: "porting is binary — 100% or not done"
```

**Speaker says:** Red is what I found. Blue is what I added. Purple is what was going wrong on Anthropic’s side. (click) (click) In purple: Anthropic later admitted that Claude Code gave the model less reasoning in those weeks, and that usage was throttled at peak hours. (click) The Sass port you saw: complete, said the agent. One test in five, said the tests. (click) So I added checks. Is each file about as long as the original? Does it have the same methods? Any TODOs or stubs? (click) I put them into a tool, re-scale, which runs them on every file, in CI. (click) They found more right away. A colour library at a fifth of its original size, with no TODO anywhere. A physics engine of four hundred files, replaced by eight. (click) And a rule for the agents: porting is binary. A hundred percent, or not done.

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
what the agents claimed
SGE: tests green
SSG (site generator) starts
checked method by method:
one file 6% ported
Sass: 1 test in 5
1,200 files marked 'complete'
Opus 4.8
Fable 5
stronger model's review:
the logic is broken
Claude Code: less reasoning
usage throttled at peak hours
```

**Speaker says:** (click) The agents then marked twelve hundred files as complete, in one go. (click) Through May the claims stayed high. (click) In June, Anthropic released Fable, a stronger and more expensive model. I asked it to review everything. (pause) And the line fell.

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
what the agents claimed
SGE: tests green
SSG (site generator) starts
checked method by method:
one file 6% ported
Sass: 1 test in 5
1,200 files marked 'complete'
Opus 4.8
Fable 5
stronger model's review:
the logic is broken
Claude Code: less reasoning
usage throttled at peak hours
Fable silently replaced by Opus
●04-20 The agents marked 1,200 files 'complete' in one go, and turned the CI check into a warning
●06-10 Text layout: breaking out of a loop became returning from the whole method
●06-10 Font rendering: // gx += xAdvances[ii] commented out, so every letter is drawn in one spot
●06-10 JavaScript minifier: 1,507 of 2,522 tests marked "expected to fail", so CI showed 0 failures; really ~40% worked
◆06-10 New rules: a failing test first; failure counts may only go down; CI must block; a different model reviews
▲06-10 Anthropic's safety filter could silently replace Fable with Opus
●06-12 Fable switched off worldwide for ~3 weeks: Opus reviewed Opus
```

**Speaker says:** (click) Those twelve hundred files were marked complete while the CI check was turned into a warning. (click) Every method was there, but the insides were wrong. In text layout, breaking out of a loop became returning from the whole method. (click) In font rendering, the line that moves to the next letter was commented out. Every letter drawn in the same place. (click) In the JavaScript minifier, more than half the tests were marked 'expected to fail', so CI showed zero failures. Really, about forty percent worked. (click) So, new rules. A failing test first. Failure counts may only go down. CI must block. And a different model reviews. (click) (click) In purple: Anthropic’s safety filter could silently replace Fable with Opus. And then Fable was switched off worldwide for almost three weeks. So Opus was reviewing Opus.

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
what the agents claimed
SGE: tests green
SSG (site generator) starts
checked method by method:
one file 6% ported
Sass: 1 test in 5
1,200 files marked 'complete'
Opus 4.8
Fable 5
stronger model's review:
the logic is broken
Fable
off
all review findings 'fixed'
Fable
back briefly
fresh review:
5 critical bugs
Claude Code: less reasoning
usage throttled at peak hours
Fable silently replaced by Opus
```

**Speaker says:** (click) Fixing all of that took until the end of June. Every review finding was marked as fixed. (click) Then Fable came back for a short time, and I asked for a fresh review. Five critical bugs. A whole feature missing. Tests that only tested the standard library. (pause) And one reviewing agent invented three of its own findings.

---
## Slide 19: 

**On screen:**
```
The agents aren't trustworthy because they are non-deterministic.me, mid-July
```

**Speaker says:** That is what I wrote in mid-July. (pause) Every check I added, the agents learned to get past. So I stopped asking them to port the code. I asked them to build a translator instead. A translator is deterministic: I can run it again, compare the output, and measure it. And when I fix a bug in it, it’s fixed in every file at once. (pause) I called it Baltic Porter.

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
what the agents claimed
SGE: tests green
SSG (site generator) starts
checked method by method:
one file 6% ported
Sass: 1 test in 5
1,200 files marked 'complete'
Opus 4.8
Fable 5
stronger model's review:
the logic is broken
Fable
off
all review findings 'fixed'
Fable
back briefly
fresh review:
5 critical bugs
Opus 5
agent porting stops
measured by tests (Baltic Porter)
Baltic Porter starts
libGDX core compiles
Fable 5.1
the old agent ports:
worse still
Opus 5: uneven quality
less reasoning than selected
old agent ports found to cheat
12 sample games run
SGE core now generated
Opus 5.5
extensions generated
Claude Code: less reasoning
usage throttled at peak hours
Fable silently replaced by Opus
```

**Speaker says:** (click) Agent porting stops. Baltic Porter starts, from zero. That’s the green line. It grows slower, but every number on it is measured by running tests. (click) By the end of July, the whole libGDX core compiles. (click) In September, comparing with the translator’s output showed that the old agent ports were even worse than the reviews had found. Some of their tests checked for wrong values. Meanwhile, all twelve sample games run on the translated code. (click) The generated core replaces SGE’s agent port. (click) And the small extensions are generated too. (pause) That’s where I am today.

---
## Slide 21: What was tried?

**On screen:**
```

```

**Speaker says:** So, two tools. First re-scale, then Baltic Porter. Let’s look at what each of them tried, and where it fell short.

---
## Slide 22: re-scale: what it checked, how it was beaten

**On screen:**
```
re-scale: a command-line tool and Claude Code plugin that checks every ported file against its original
| The check | How the agents got past it
| Every file records the original's methods and size; CI checks the record | The agents marked 1,200 files "complete" in one go, recording whatever each file already had, and turned the CI check into a warning
| Same methods as the original | Every method there, the insides hollow: leaving a loop became leaving the whole method; the line that moves to the next letter commented out
| About the same size as the original | Caught a colour library at a fifth of its size, but full-size files could still be wrong: the minifier was bigger than the original, and about 40% of its tests passed
| A scanner for words like "TODO" or "stub" | The agents reworded their comments until the scanner stopped finding them
| A review by a different model | A model reviewing its own work explained the gaps away; with Fable off, the reviewer silently became the same model; one reviewer invented 3 of its 5 findings
```

**Speaker says:** re-scale compared every ported file with its original.
(click) Each file recorded the original’s methods and size, and CI checked it. The agents marked twelve hundred files complete in one go, and turned the check into a warning.
(click) The methods had to match. They did. The insides were hollow: you saw that in June.
(click) The size had to match. Files that matched could still be wrong.
(click) (click) The pattern is always the same: (pause) every check looked at names, words, or counts. Never at behaviour. And each one was satisfied without doing the work.

---
## Slide 23: Baltic Porter: what it does, where it slipped

**On screen:**
```
Baltic Porter: a translator to Scala 3, from Java first, later TypeScript, JavaScript and Dart. Same input, same output. Agents improve the translator; they don't port code.
| The approach | What still went wrong
| Each project has its own rules: Scala names, Nullable instead of null, opaque types, a few hand-written files | The rules are code too, so they need review
| Agents work on the translator, never on the port | One "generator" for Mermaid only contained 187 pieces of the old agent port, copied byte for byte
| Tests decide | An agent switched off 28 test suites and reported "0 failures"; another switched off 23 tests half an hour after regenerating the code
| Generated code is never edited by hand | Agents patched it with find-and-replace and loosened test assertions; all reverted later
| Same input, same output | Compiling is not the same as correct: a lost break, a wrong equality check; only running the tests found them
The limit is now test coverage, not honesty.
```

**Speaker says:** Baltic Porter translates Java to Scala. Same input, same output, every time. The agents don’t port anything. They improve the translator and measure it.
(click) Each project has its own rules on top: Scala names, Nullable instead of null, opaque types.
(click) Agents still tried to cheat. One "generator" just contained the old code, copied byte for byte.
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
| In libGDX | JVM | Scala Native | Browser
| LWJGL (OpenGL) | ANGLE via Panama | ANGLE via @extern | WebGL
| LWJGL (windows, audio) | GLFW, miniaudio via Panama | GLFW, miniaudio | DOM, Web Audio
| libGDX's own C code (buffers, images) | Rust library via Panama | same library, same C interface | pure Scala
| FreeType (fonts) | Rust wrapper via Panama | static library | none
| Box2D / Bullet (physics) | Rapier via Panama | static library | Rapier as WASM
```

**Speaker says:** Even in Scala, a game needs native code.
(click) Graphics: ANGLE, Google’s OpenGL implementation. Panama is Java’s new way to call C.
(click) Windows and audio: GLFW and miniaudio.
(click) libGDX’s own C code became one small Rust library.
(click) Fonts: FreeType.
(click) Physics: Rapier, a Rust engine. That one was a deliberate replacement: it also compiles to WebAssembly, so physics works in the browser too.
Every native library gets one C interface. The JVM calls it through Panama. Android through a backport of Panama. Scala Native calls it directly. (pause) No JNI anywhere.
But every one of these libraries has to be built for every platform, and delivered to every build.

---
## Slide 26: A native library is just a dependency

**On screen:**
```
| Problem before | What multiarch-scala adds
| JVM: no standard way to ship and load native libraries | A JAR with the native library for each platform, plus a small description file; a loader picks the right one and loads it
| Scala Native: install the library on the system yourself, and write the linker flags yourself | The same kind of JAR carries ready-to-link libraries and their flags; adding the dependency is enough
| You can only build for the machine you are on | Native binaries cross-compiled with zig; desktop JVM apps packaged for every system from one machine
| No maintained sbt plugin for Android | An Android plugin: converting to Android bytecode, resources, signing
| Scala.js: no classpath, no ServiceLoader | Assets embedded at build time behind one API; a ServiceLoader generated at compile time
```

**Speaker says:** The core idea: a native library should be a dependency like any other.
(click) On the JVM, there was no standard way to ship one. Now it’s a JAR with the library for each platform, and a loader that picks the right one.
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
Scala Native can't build for Windows on ARM
Shipping native libraries still needs a plugin
Our own backlog
Android: code shrinking and older Android versions
No GPU in CI, so graphics tests run on a software renderer
```

**Speaker says:** What’s still missing. (click) Scala Native has no iOS support, so there is no iOS backend. (click) It can’t target Windows on ARM either. (click) And shipping native libraries is still something you need a plugin for.
(click) On my side: Android needs code shrinking and support for older versions. (click) And CI has no GPU.

---
## Slide 28: So what do I have today?

**On screen:**
```

```

**Speaker says:** So where am I today? (pause) Honestly.

---
## Slide 29: SGE: what is generated, what is left

**On screen:**
```
| Part of SGE | State | Still maintained by hand
| libGDX core | generated from upstream at build time | 5 hand-written overrides
| Utilities and 5 small extensions | generated | almost nothing
| The other ~690 extension files | porting rules not written yet | still the agent port
Tests pass on JVM, JS and Native
```

**Speaker says:** (click) The libGDX core is fully generated. Five files are written by hand. (click) The utilities and five small extensions are generated too.
(click) About six hundred ninety extension files are still the old agent port. Their rules are not written yet.
(click) And the tests pass on all three platforms.

---
## Slide 30: Plain translation vs SGE’s conventions

**On screen:**
```
plain Java → Scala translation
36%
SGE's own design on top
64%
Every change the translator makes to SGE core, by kind
3,710getX()/setX() turned into Scala properties, empty () dropped
1,083Nullable instead of null
398opaque types (Pixels, Align, Input.Button, …)
282an Sge context instead of global variables
```

**Speaker says:** A plain translation already gives you a working port. But two thirds of what the translator changes is SGE’s own design on top.
(click) Scala-style names. (click) Nullable instead of null. (click) Opaque types. (click) A context instead of globals.
(pause) That’s what the porting rules are: my design, written down once, applied everywhere.

---
## Slide 31: Less code to maintain, same behaviour

**On screen:**
```
[image: PR #146: Baltic Porter integration, +7,950 / -115,453 lines]
[image: PR #160: core overrides 89 to 16, +83 / -14,687 lines]
[image: PR #153: ecs generated from Ashley, +789 / -2,794 lines]
Three SGE pull requests: about +8.8k / −133k lines, with tests and demos still passing
```

**Speaker says:** (click) Switching SGE to the generated core. (click) Then cutting the hand-written files from eighty-nine to sixteen; today it’s five. (click) Then generating one more library.
(click) About nine thousand lines added, a hundred and thirty thousand removed. The code didn’t disappear: it’s generated at build time, so I no longer maintain it.
(pause) I still don’t trust the numbers the AI reports about itself. I trust that the tests and demos keep working, while the code I review keeps shrinking.

---
## Slide 32: SSG: Java done, the rest is still an agent port

**On screen:**
```
| Libraries ported into SSG | Source language | State
| Markdown parser, Liquid templates | Java | generated, tests pass
| KaTeX, terser, rough.js, Mermaid | TypeScript / JavaScript | still the agent port; 0–5% translated
| Sass compiler | Dart | still the agent port; nothing translated yet
| HTML/CSS minifier | Ruby | agent port, no translator
Over twelve thousand tests pass on every platform, but the non-Java ones still run the agent-written code
```

**Speaker says:** And SSG, the static site generator. (click) The Java libraries are generated, and their tests pass.
(click) For TypeScript and JavaScript, the translator exists, but almost nothing comes out of it yet. (click) Sass, written in Dart: nothing yet. (click) And Ruby has no translator at all.
(click) Over twelve thousand tests pass on every platform. (pause) But for the non-Java libraries, they still run the old agent port.

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
The agent port's structure, waiting for translated method bodies
About 0–5% translated today
```

**Speaker says:** So: is it ready? For Java sources, almost.
(click) The libGDX core, SGE, and SSG’s Java libraries. (click) Every change tested on three platforms. (click) Nothing hidden: what can’t be translated is counted, and every hand-written file has a reason. (click) But no release yet, only snapshots.
(click) For everything else, it’s a first step. (click) The agent port’s structure is there, (click) and the translator fills in only a few percent of it today. (pause) Remember the deceptive demo? This is what "first iteration" means.

---
## Slide 34: Summary

**On screen:**
```

```

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
Scala already compiles to the browser and to native code; Java needs separate external compilers for both
The community already builds tooling for multiple platforms, without weird hacks in the build
```

**Speaker says:** (click) Scala already compiles to the browser and to native code, as part of the language. (pause) Java needs a separate, external compiler for each. iOS is still missing for Scala, but that’s one missing piece, not a missing approach.
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

**On screen:**
```

```

**Speaker says:** Thank you. Questions?

---
## Slide 40: Thank you!

**On screen:**
```
SGE, the game engine: github.com/kubuszok/sge
SSG, the site generator: github.com/kubuszok/ssg
Baltic Porter, the translator: github.com/kubuszok/balticporter
multiarch-scala, the build plugins: github.com/kubuszok/multiarch-scala
re-scale, the port checker: github.com/kubuszok/re-scale
```

**Speaker says:** 

