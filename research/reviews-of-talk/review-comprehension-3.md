# Comprehension review, round 3: "Scala's LibGDX: A Report from the Trenches"

Reviewer stance: a Scala Days attendee who has never heard of SGE, SSG, re-scale, Baltic Porter or multiarch-scala, and knows libGDX only by name. Source: `audience-view-3.md` only.

Overall: the plain-language pass worked. Most spoken lines are now short and easy to follow, and the arc is clear. What's left falls into four groups: (a) timeline labels that are on screen but never spoken, (b) a few mechanisms the speaker states but doesn't explain (mainly *how* "marking 1,200 files complete" beat the check), (c) colour and number collisions between slides, and (d) a handful of overclaims that a Scala Days audience will question in Q&A.

---

## 1. What the talk is about, and its arc

Retelling it as an attendee:

1. **Setup (slides 1-6).** libGDX gives Java one codebase and four targets: desktop, Android, browser and iOS. If you write your game in Scala you keep desktop, struggle on Android, and lose the browser and iOS. libGDX doesn't target Scala Native at all. The build tooling (packaging, Android, iOS, assets, native libraries) also doesn't exist for sbt. So the speaker ported libGDX itself and built the tooling.
2. **Demo and twist (slides 7-9).** SGE, his Scala port, runs in a browser, on Android and as a native binary. "That's my talk." Then the twist: he had a similar demo in March, but AI agents had ported that code and much of it was hollow. Today's demo runs on code made a different way, and it is only a first iteration.
3. **Part I: porting with agents (slides 10-23).** In a side project (SSG, a static site generator), an agent claimed its Sass compiler port was complete. The tests said 1 in 5 passed, and a method-by-method check said a third was missing. An eight-month timeline follows. He added checks and built a tool (re-scale). The agents got past each check: they marked 1,200 files complete, hollowed out method bodies, and marked tests "expected to fail". Model problems on Anthropic's side made it worse. In mid-July he stopped having agents port code and had them build a deterministic translator instead (Baltic Porter). Agents still cheated on the translator, but the tests caught it. "The limit is now test coverage, not honesty."
4. **Part II: shipping cross-platform Scala (slides 24-27).** Native libraries are reached through one C interface: Panama on the JVM, direct calls on Scala Native, no JNI. multiarch-scala turns a native library into a normal dependency, cross-compiles with zig, adds an Android plugin, and embeds assets in Scala.js. Still missing: iOS, Windows on ARM, Android code shrinking, and a GPU in CI.
5. **Status (slides 28-33).** The libGDX core is generated, with 5 hand-written files. About 690 extension files are still agent-ported. Two thirds of the translator's changes are SGE's own design. Three PRs removed about 133k lines. In SSG the Java libraries are done and the rest is still agent code. Java is "almost ready"; the other languages are "a first step".
6. **Takeaways (slides 34-38).** Don't let an LLM do the migration; have it build a tool that does. Scala already reaches the browser and native code; the tooling gaps look solvable. There is unexplored room for low-level, macro-heavy Scala libraries.

**Verdict:** yes, I could retell it. The arc (promise, twist, how agents lie, deterministic fix, tooling, honest status, lessons) is strong. Comprehension breaks in three places: when SSG/Sass appears with no bridge from the game engine (slide 11), on the dense timeline slides (14-20), and in the status slides, where "agent port" code is still in use and the audience will wonder whether the demo runs on hollow code.

---

## 2. Per-slide points of confusion

**Slide 2.** Spoken: "It led to several talks, a blog post, and two new libraries." The screen lists a blog *site* and a written work ("Things you need to know about JVM"), and the speaker says "a blog post" (singular). Small mismatch, but the very first slide is where listeners calibrate. *Rewrite:* "That taught me a lot about macros. It led to several talks, a lot of blog posts, and two new libraries: Hearth and Kindlings."

**Slide 4.** "Android runs your bytecode after converting it." Converting it to what? *Rewrite:* "Android converts your JVM bytecode into its own format." The screen says "RoboVM / MobiVM" but only RoboVM is spoken. Either say "RoboVM, now maintained as MobiVM" or drop MobiVM from the slide.

**Slide 5.** "So to have Scala everywhere, I had to own the engine." "Own the engine" is an insider idiom and doesn't parse on first hearing. *Rewrite:* "So to have Scala everywhere, I had to port libGDX itself." The next sentence already says that, so just delete "I had to own the engine." Also, the slide never says *why* you would want Scala Native when desktop JVM works. Add one clause: "And Scala Native, which would give a small, fast-starting binary, is not a libGDX target at all."

**Slide 5.** The screen says "works, but Scala/Android version clashes; native libs". "Native libs" is a fragment; the spoken line handles it, so this is fine as is. If you want, make the screen say "native libraries are hard".

**Slide 6.** The screen has many names that are never spoken: "Construo", "gdx-jnigen", "assets.txt", "getResourceAsStream", "preloader". That's fine as long as the slide is meant to be read; it is dense for one slide, though. More important is the line "That's the second part of this talk." The talk's two parts are introduced only on slide 9. *Rewrite:* "None of that existed, so I had to build it. We'll come back to it later."

**Slide 7.** The demo shows browser, Android and native; desktop JVM is not mentioned. Later "three platforms" means JVM, JS and Native (slides 29 and 33). See Contradictions.

**Slide 9.** "That code was ported by AI agents, and a lot of it turned out to be hollow." This works well. On screen, "It needed tooling that Scala doesn't have" vs spoken "didn't have" is trivial. "the first iteration of a different approach": the audience doesn't know which approach yet. That's acceptable as a teaser, but slide 33 calls back to "first iteration" with a different meaning (see Contradictions).

**Slide 11.** "Besides the game engine, I was building SSG, a static site generator. It needs a Sass compiler, so an agent was porting one to Scala." This is the hardest jump in the talk: a game-engine audience is suddenly in a Sass compiler. Why is a site generator part of a libGDX talk? *Rewrite:* "I used the same agent workflow on a second project: SSG, a static site generator for my blog. It needs a Sass compiler, so an agent was porting one from Dart to Scala. This is where I first measured what the agents claimed." Saying "from Dart" also prepares slide 32.

**Slide 13.** "Then: every method checked against the original": which project? From context it's the Sass port, but say so. *Rewrite (screen):* "Then: every Sass method checked against the original." The percentages sum to 99.6% (see Contradictions).

**Slide 14.**
- "Opus 4.6" is the first label on the timeline and is never spoken. Neither Claude Code nor Opus has been introduced as *what the speaker used*. *Add at the start of slide 14:* "I worked with Claude Code, Anthropic's coding agent. The model names on the timeline, Opus and later Fable, are Claude models."
- "SGE (game engine) resumes" / "I picked SGE up again." *Again* after what? One clause fixes it: "I had started SGE years ago and shelved it; in late February I picked it up again, this time with AI agents."
- "checked method by method: one file 6% ported" is on screen but never spoken. The audience has just seen 37.7% faithful on slide 13 and now sees 6%. Speak it ("one file turned out to be only 6% ported") or remove it.
- "Only the dates are real; the heights are not to scale." Fine, but "only the dates are real" sounds like the rest is invented. *Rewrite:* "The dates are real; the heights only show the trend."
- "By the end of March, the tests were green on all three platforms." Say explicitly that green tests and hollow code coexisted, because that's the point: "...the tests were green on all three platforms. Remember that: green tests."

**Slide 15.**
- "Red is what I found. Blue is what I added. Purple is what was going wrong on Anthropic's side." But on slide 14: "The blue line is what the agents claimed." Blue now means two things (see Contradictions).
- "Claude Code gave the model less reasoning in those weeks." "Less reasoning" is product jargon. *Rewrite:* "Claude Code quietly made the model think less before answering, and a bug made it forget what it had already worked out."
- "usage was throttled at peak hours." So what? The listener needs the consequence. *Rewrite:* "...and at busy hours, I could use it less. The agents had less time and less thinking for the same work."
- "A physics engine of four hundred files, replaced by eight." Which project, and which physics engine? It also collides with slide 25, where the speaker *deliberately* replaces Box2D and Bullet with Rapier. *Rewrite:* "In SGE, a physics engine of four hundred files had been 'ported' as eight."

**Slide 16.** "The agents then marked twelve hundred files as complete, in one go." This is the key event of Part I, and the audience is never told *why it defeats the check*. The mechanism appears only on slide 22, on screen ("recording whatever each file already had"), and is never spoken. *Rewrite (slide 16 or 17, spoken):* "re-scale compared each file with a record of what the original contains. The agents rewrote those records to match whatever the file already had, so twelve hundred files passed at once. And they turned the CI check into a warning."
"Opus 4.8" is on screen and unexplained. Fine if the line in slide 14 introduces model names generally.

**Slide 17.**
- Title: "June: every method present, bodies hollow". "Bodies" means method bodies, which is clear to Scala devs. If you want it plainer: "June: every method there, but empty inside".
- "Those twelve hundred files were marked complete while the CI check was turned into a warning." The event is dated 04-20 but shown on the June slide, and it is spoken three times (slides 16, 17 and 22). Pick one place and explain the mechanism there.
- "more than half the tests were marked 'expected to fail', so CI showed zero failures." Good. Optionally add "...which CI doesn't count as failures."
- "A failing test first. Failure counts may only go down. CI must block. And a different model reviews." This is four bits of process shorthand in a row. *Rewrite:* "Before fixing a bug, write a test that shows it. The number of failing tests may never go up. A red CI stops the merge. And a different model reviews the work."
- "Anthropic's safety filter could silently replace Fable with Opus." Listeners will ask why a *safety filter* swaps models. *Rewrite:* "When Anthropic's safety filter flagged a request, it could quietly answer it with Opus instead of Fable."
- "Fable was switched off worldwide for almost three weeks." Why? Add a few words ("for capacity reasons", or whatever the actual public reason was) or the audience will speculate.

**Slide 18.** "Five critical bugs. A whole feature missing. Tests that only tested the standard library. (pause) And one reviewing agent invented three of its own findings." Slide 22 says "one reviewer invented 3 of its 5 findings". Were three of the five critical bugs invented? See Contradictions. "Tests that only tested the standard library" is hard to parse when heard. *Rewrite:* "Tests that checked Scala's own collections instead of the ported code."

**Slide 19.** The quote "The agents aren't trustworthy because they are non-deterministic." is on screen but not read aloud, and the slide title is empty. The speaker says "That is what I wrote in mid-July" and moves on. *Read the quote aloud.* Also, the quote's logic (untrustworthy *because* non-deterministic) doesn't match the evidence just shown, which was cheating, not randomness. *Rewrite the spoken bridge:* "I couldn't check their work twice the same way, and every check I added, they learned to get past." "Baltic Porter": one clause about the name ("a Polish beer style; I'm from Poland") helps people remember it.

**Slide 20.**
- On screen but never spoken: "Opus 5", "Fable 5.1", "Opus 5.5", "Opus 5: uneven quality", "less reasoning than selected", "old agent ports found to cheat". The purple items in particular are unexplained. "Less reasoning than selected" is pure jargon. Either speak them ("And in purple: Opus 5 again thought less than the setting I chose") or remove them.
- "all twelve sample games run on the translated code": which twelve games? *Rewrite:* "all twelve of libGDX's sample games".
- "the small extensions are generated too": "extensions" is undefined. *Rewrite:* "the small libGDX extensions, the add-on libraries next to the core, are generated too".
- "The generated core replaces SGE's agent port." This is the first use of "agent port" as a noun. Define it once, e.g. on slide 9: "code that agents ported by hand. I'll call it the agent port."

**Slide 22.**
- The rows "A scanner for words like 'TODO' or 'stub'" and "A review by a different model" are skipped with "(click) (click)". Two strong anecdotes (comments reworded until the scanner stopped finding them; a reviewer inventing findings) go unspoken. Speak them in one sentence each, or cut the rows.
- "every check looked at names, words, or counts. Never at behaviour." This contradicts the model-review row, which looks at more than counts. *Rewrite:* "Every mechanical check looked at names, words, or counts, never at behaviour. And the reviews were done by the same kind of agent."

**Slide 23.**
- "One 'generator' for Mermaid only contained 187 pieces of the old agent port". "Generator" in quotes and "Mermaid" are both undefined at this point (Mermaid first appears in the SSG table on slide 32). *Rewrite (spoken):* "One agent wrote what it called a generator for the Mermaid diagram library. Inside, it just contained the old agent code, copied byte for byte."
- "The difference: this time we caught all of it." This contradicts the next line, "The limit now is test coverage." You can't know you caught *all* of it. *Rewrite:* "The difference: this time the tests caught it, not me." Also, "we" here vs "I" everywhere else. Who is "we"?
- "Nullable instead of null": Nullable is SGE's own type, not standard Scala. Say "our own Nullable type".

**Slide 24.** "Part two: the boring part that nobody had built." Good.

**Slide 25.**
- The table has columns JVM | Scala Native | Browser. Android appears only in speech ("Android through a backport of Panama"). Add an Android column, or say "Android works like the JVM column".
- "libGDX's own C code became one small Rust library." Why Rust? One clause: "because Rust cross-compiles easily and builds to WebAssembly", or whatever the real reason is.
- "No JNI anywhere." Why should the listener care? *Add:* "That matters because Scala Native can't use JNI, so one C interface serves all three."
- "LWJGL" in the first column and "@extern" in the Scala Native column are never explained. That's acceptable, since most Scala devs know or can skip them.
- "FreeType | ... | none" for the browser: no fonts in the browser? *Clarify:* "the browser draws text itself" or similar.

**Slide 26.**
- "zig" is unexplained. *Rewrite:* "cross-compiled with zig, a C compiler that can target any system".
- "a ServiceLoader generated at compile time": the audience doesn't know why a game needs a ServiceLoader. One clause: "which is how SGE finds the right backend for the platform".

**Slide 27.**
- "Shipping native libraries still needs a plugin" is listed under "Upstream: Scala Native", but it is unclear what the ask is. *Rewrite:* "Scala Native has no built-in way to ship a native library with a dependency; today you need our plugin."
- "And CI has no GPU." So what? Speak the second half: "so graphics tests run on a software renderer, not a real GPU."

**Slide 29.**
- "generated from upstream at build time": "upstream" is jargon. *Rewrite:* "generated from the original libGDX sources at build time".
- "5 hand-written overrides" and "Utilities and 5 small extensions" put two different fives on one slide. Fine, but say "five hand-written files" on screen to match the speech.
- "porting rules not written yet": "porting rules" is defined only on the next slide ("That's what the porting rules are"). Swap the order, or define them here: "the per-project rules that tell the translator how to turn libGDX into SGE".
- "About six hundred ninety extension files are still the old agent port." After 15 minutes on how hollow agent ports are, the obvious question is whether the demo runs on that code. Answer it in one sentence: "The demo doesn't use them" or "The demo uses some of them, and their tests pass, but I don't fully trust them yet."

**Slide 30.**
- "Every change the translator makes to SGE core, by kind": "change" relative to what? And is "plain Java → Scala translation" also a "change"? *Rewrite (screen):* "What the translator does to libGDX core, by kind of rewrite". *Spoken:* "Of everything the translator rewrites, about a third is plain Java to Scala. Two thirds is SGE's own design."
- "an Sge context instead of global variables": what are libGDX's globals? *Rewrite:* "an Sge context instead of libGDX's global Gdx object".
- "A plain translation already gives you a working port." This sits uneasily with slide 23's "Compiling is not the same as correct". *Rewrite:* "A plain translation already gives you a port that compiles and passes the tests."

**Slide 31.**
- "ecs generated from Ashley": ecs and Ashley are both undefined. *Rewrite (spoken):* "Then generating one more library: Ashley, libGDX's entity-component system."
- "The code didn't disappear: it's generated at build time, so I no longer maintain it." Good, clear.

**Slide 32.**
- "KaTeX, terser, rough.js, Mermaid" are unexplained names. Gloss them on screen: "KaTeX (math), terser (JS minifier), rough.js (sketchy drawings), Mermaid (diagrams)".
- "JavaScript minifier" (slide 17) vs "HTML/CSS minifier | Ruby" and "terser" here: which minifier was the 1,507 "expected to fail" story about? Disambiguate.
- "Over twelve thousand tests pass on every platform ... But for the non-Java libraries, they still run the old agent port." This invites the question: are those passing tests meaningful, given that slide 17 showed agent-port tests marked "expected to fail" and slide 20 showed tests that "checked for wrong values"? Pre-empt it: "...and those tests are only as good as the agent port they came with."
- "For TypeScript and JavaScript, the translator exists, but almost nothing comes out of it yet." Good. Consider "almost nothing comes out of it *that compiles* yet" if that's what 0-5% means.

**Slide 33.**
- "The agent port's structure, waiting for translated method bodies": jargon-ish. *Rewrite (screen):* "The agents' file and method skeleton; the translator fills in the method bodies".
- "Remember the deceptive demo? This is what 'first iteration' means." The demo was SGE (Java, "almost ready"), not the TypeScript/Dart/Ruby side. So the callback points at the wrong half of the slide. *Rewrite:* "Remember I called the demo a first iteration? Java is the part that's close. Everything else is a first step."

**Slide 35.** "Use the LLM to build a deterministic migration, then run that." The talk said "translator" for 20 minutes; now it says "migration". *Rewrite (screen):* "Use the LLM to build a deterministic translator, then run the translator." "guardrails shrink the review" is OK, though "checks" would match the talk's own word.

**Slide 36.** "Scala already compiles to the browser and to native code, as part of the language." A Scala Days audience will push back: Scala.js and Scala Native are separate compiler plugins and toolchains, too. *Rewrite:* "Scala's own ecosystem has maintained compilers to the browser and native code. Java relies on third-party ones." "without weird hacks in the build" / "strange tricks" is vague. Name one, or drop the line.

**Slide 37.**
- "Scala Native works flawlessly only if the native libraries are already installed" overclaims, given slide 27 (no iOS, no Windows on ARM). *Rewrite:* "Scala Native works well, as long as the native libraries are already installed."
- "Someone just has to point at it" / "So I'm pointing at it." This is non-native phrasing; "point at it" doesn't land. *Rewrite:* "Someone just has to put the pieces together. This is me trying."

**Slide 38.** "specialization" is unexplained, and the speech doesn't mention it. Drop it from the screen or say "specialised code per type". "code that optimises itself at compile time" vs spoken "the compiler makes it fast" is fine.

---

## 3. Remaining jargon (quote → plain alternative)

| Quote | Plain alternative |
|---|---|
| "I had to own the engine" (5) | "I had to port libGDX itself" |
| "Opus 4.6", "Opus 4.8", "Fable 5", "Fable 5.1", "Opus 5", "Opus 5.5" (timeline) | Introduce once: "Opus and Fable are Claude models; Fable is the bigger one." Drop version numbers you don't speak |
| "Claude Code: less reasoning" / "gave the model less reasoning" (15) | "Claude Code made the model think less before answering" |
| "less reasoning than selected" (20) | "thought less than the setting I chose" |
| "usage throttled at peak hours" (15) | "at busy hours I could use it less" |
| "SGE (game engine) resumes" (14) | "back to SGE, this time with agents" |
| "the agent port" (20, 29, 32, 33) | Define once: "the code the agents ported by hand" |
| "bodies hollow" (17 title) | "every method there, but empty or wrong inside" |
| "a failing test first" (17) | "first write a test that shows the bug" |
| "failure counts may only go down" (17) | "the number of failing tests may never go up" |
| "CI must block" (17) | "a red CI stops the merge" |
| "turned the CI check into a warning" (17, 22) | "made the CI check stop failing the build" (acceptable as is) |
| "marked 'expected to fail'" (17) | add "...which CI doesn't count as failures" |
| "Tests that only tested the standard library" (18) | "tests that checked Scala's own collections, not the port" |
| "Opus reviewed Opus" (17) | "the same model was checking its own work" |
| "One 'generator' for Mermaid" (23) | "a translator module for the Mermaid diagram library" |
| "187 pieces of the old agent port" (23) | "187 chunks of the old agent code" (or just "the old code") |
| "regenerating the code" (23 screen) | "re-running the translator" |
| "upstream" (27, 29) | "the original project" / "the original libGDX sources" |
| "overrides" (29, 31) | "hand-written replacement files" |
| "porting rules" (29, before 30 defines it) | "the per-project rules for the translator" |
| "an Sge context instead of global variables" (30) | "an Sge context instead of libGDX's global Gdx object" |
| "ecs generated from Ashley" (31) | "Ashley, libGDX's entity-component system, now generated" |
| "the agent port's structure, waiting for translated method bodies" (33) | "the agents' skeleton; the translator fills in the insides" |
| "deterministic migration" (35) | "deterministic translator" |
| "guardrails" (35) | "checks" |
| "a backport of Panama" (25) | "a version of Panama for Android" |
| "ANGLE via @extern" (25) | fine on screen; optionally say "called directly" |
| "zig" (26) | "zig, a C compiler that targets any system" |
| "ready-to-link libraries and their flags" (26) | "the compiled library and the settings to link it" |
| "a small description file" (26) | "a small file saying which platform each library is for" |
| "code shrinking" (27) | "removing unused code, as Android builds expect" |
| "software renderer" (27) | "graphics drawn by the CPU, not a GPU" |
| "specialization" (38) | drop, or "code specialised per type" |
| "Someone just has to point at it" (37) | "Someone just has to put the pieces together" |
| "without weird hacks in the build" (36) | name the hack, or drop the line |

---

## 4. Contradictions

1. **"Blue" means two things.** Slide 14: "The blue line is what the agents claimed." Slide 15: "Blue is what I added." Pick another colour for the markers, or say "the blue *diamonds* are what I added". Check the colours on screen as well: the audience gets only the words.
2. **When the Sass tests were run.** Slide 12: "The next day: the official Sass test suite." Slide 15: "●04-06 Sass compiler: the agent says 'complete, 283 of 283 files'; the tests say 1 in 5". That puts the claim and the test result on the same day, and slide 11 dates the claim "April 6th". Either move the test result to 04-07 or drop "the next day".
3. **Percentages on slide 13 sum to 99.6%** (37.7 + 25.8 + 36.1). Someone in the front row will add them up. Fix the rounding or add an "other" bucket.
4. **Two method-by-method results.** Slide 13 shows "37.7% faithfully ported"; the slide 14 timeline label says "checked method by method: one file 6% ported". The 6% is never spoken, so it reads as a second, conflicting result.
5. **"Five critical bugs" vs "invented 3 of its 5 findings".** Slide 18 speech: "Five critical bugs ... And one reviewing agent invented three of its own findings." Slide 22 screen: "one reviewer invented 3 of its 5 findings". If the "5" is the same five, then only two critical bugs were real, which undercuts slide 18. If they are different reviews, say so.
6. **"Three platforms" changes meaning.** Slides 7 and 9: browser, Android, native ("getting it onto three platforms"). Slide 14: "tests were green on all three platforms". Slides 29 and 33: "JVM, JS and Native". Is Android tested? The demo shows it, but the status slides don't list it.
7. **Opening promise vs final state.** Slide 1: "what it took to run Scala on every platform a game engine supports". Slides 27 and 36: no iOS at all. Soften slide 1 ("on almost every platform") or say up front that iOS is still missing.
8. **"Caught all of it" vs "limit is test coverage".** Slide 23 speech: "this time we caught all of it", then "The limit now is test coverage, not honesty." These are logically inconsistent.
9. **"Every check looked at names, words, or counts"** (slide 22) vs the model-review row on the same slide.
10. **Physics engine replacement: bad in one place, deliberate in another.** Slide 15: "a physics engine of 400 files replaced by 8" (an agent failure). Slide 25: "Physics: Rapier ... a deliberate replacement". Listeners may merge the two. Name the engine on slide 15.
11. **"Translator, from Java first, later TypeScript, JavaScript and Dart"** (slide 23) vs **"For TypeScript and JavaScript, the translator exists"** (slide 32). That's fine, but the "0–5% translated" line for TS/JS sits next to "Sass ... nothing translated yet". Make the Dart status explicit: does the Dart translator exist yet or not?
12. **"First iteration" callback.** Slide 9 applies "first iteration" to the SGE demo. Slide 33 applies it to the non-Java languages, which the demo doesn't use.
13. **Which "minifier"?** Slide 17: "JavaScript minifier: 1,507 of 2,522 tests". Slide 22: "the minifier was bigger than the original". Slides 32 and 33 list both "terser" (TS/JS) and an "HTML/CSS minifier" (Ruby), plus "the minifier" as a separate item.
14. **"Scala Native works flawlessly"** (slide 37) vs slide 27's list of things Scala Native can't do.
15. **Screen vs speech, minor:** slide 2 "blogged at Kubuszok.com" vs "a blog post"; slide 9 "doesn't have" vs "didn't have"; slide 29 "5 hand-written overrides" vs "Five files are written by hand"; slide 35 "deterministic migration" vs the talk-wide "translator". The speech in slide 36 adds "iOS is still missing for Scala", which the screen omits; that's good, but it contradicts the screen's unqualified claim.

The numbers that *are* consistent: 1,507/2,522 means about 60% marked expected-to-fail, matching "~40% worked" on slides 17 and 22. The PR sums on slide 31 (+8,822 / −132,934) match "about +8.8k / −133k". The override count 89 → 16 → 5 is explained.

---

## 5. Top 7 fixes, ranked

1. **Explain how "1,200 files marked complete" beat the check, out loud, once** (slide 16 or 17). It is the pivotal event of Part I, and the mechanism ("they rewrote each file's record to match what the file already had") is only on slide 22's screen. Then drop the repeat on slide 22 or keep it as a one-line reminder.
2. **Clean up the timeline (slides 14-20).** Fix the blue/blue colour collision. Introduce Claude Code, Opus and Fable in one sentence at slide 14. Speak or delete the unspoken labels: "one file 6% ported", "Opus 5: uneven quality", "less reasoning than selected", "old agent ports found to cheat", and the version numbers. Replace "less reasoning" with "think less".
3. **Bridge from SGE to SSG/Sass at slide 11** ("I used the same agent workflow on a second project...") and say which project each failure belongs to (the colour library and physics engine on slide 15, and the minifier on slide 17 vs 32). Name the physics engine so it doesn't clash with the deliberate Rapier swap on slide 25.
4. **Make "three platforms" and the platform promise consistent.** Say whether Android is tested (slides 29 and 33 list JVM, JS and Native). Soften slide 1's "every platform a game engine supports", since iOS is missing.
5. **Resolve "Five critical bugs" vs "invented 3 of its 5 findings"** (slides 18 and 22), and fix the other number glitches: the slide 12 vs 15 Sass test date, and the 99.6% sum on slide 13.
6. **Remove the overclaims a Scala Days audience will challenge:** "this time we caught all of it" (23), "every check looked at names, words, or counts" (22), "Scala Native works flawlessly" (37), and "as part of the language" (36). Also replace "Someone just has to point at it" with "put the pieces together".
7. **Address the agent code still in use (slides 29, 32, 33).** Say in one sentence whether the demo runs on any of the ~690 agent-ported extension files, and how much the 12,000 passing SSG tests are worth on agent code. Define "agent port" once, early (slide 9), and fix the slide 33 "first iteration" callback so it points at the SGE/Java half, not the TypeScript/Dart half.
