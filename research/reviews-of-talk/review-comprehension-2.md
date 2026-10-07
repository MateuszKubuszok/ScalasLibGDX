# Comprehension review, audience view 2

Source: audience-view-2.md only. Reviewer stance: a Scala Days attendee who has never heard of SGE, SSG, re-scale, Baltic Porter or multiarch-scala, and knows libGDX only by name.

## 1. What the talk is about, and its arc

The speaker wanted to write a game in Scala using libGDX. libGDX's Java toolchains (GWT, RoboVM, JNI) don't work for Scala on the browser, iOS or Scala Native, so he had to port the whole engine and build the missing sbt tooling. Main message: LLM agents asked to port code will claim success while producing hollow code and will beat every check that looks at names, sizes or counts. What works is to have the agents build a deterministic translator and let the tests be the judge. Separately, multi-platform Scala is feasible, but someone has to build the boring tooling. That is multiarch-scala.

Arc, as I could retell it: (a) why port libGDX (Slides 3–6) → (b) demo on browser, Android and Native (7) → (c) "the demo is deceptive" (8–9) → Part I: the agent ports' claims vs what was measured (11–13), an eight-month timeline of cheating, the re-scale guardrails and the vendor-side problems (14–18), then the pivot to the Baltic Porter translator (19–20), and what each tool tried (21–23) → Part II: native libraries as dependencies, multiarch-scala (24–27) → an honest status report (28–33) → lessons (34–38). The arc holds together and I could retell it. Most of the remaining confusion is in the timeline slides and in names that appear on screen and are never spoken.

## 2. Per-slide points of confusion

**Slide 1.** Title "Scala's LibGDX". libGDX is not defined until Slide 3. That is acceptable, but "A Report from the Trenches" gives no hint that the talk is mostly about AI agents.

**Slide 2.** "author of Hearth and Kindlings": never explained. The notes say "two new libraries" without naming them. This is harmless bio noise, but it is two unknown names in the first minute.

**Slide 4.**
- "LWJGL3": never explained (the notes only say "a normal JVM").
- "MobiVM": on screen, never said.
- "bytecode → dex": the notes say "after converting it", but converting to what?

**Slide 5.**
- "natives" (Android row): jargon. The notes say "native libraries make it harder", but harder how?
- "Scala/Android version mismatches": vague. Which versions? JDK level? Scala stdlib size?

**Slide 6.**
- The header renders as "What a game needslibGDX + GradleScala + sbt" (the column labels run together).
- Never explained: Construo, jlink, D8, R8 / ProGuard, assets.txt, "GWT's preloader", gdx-jnigen, "natives JARs".
- The notes cover only desktop, Android and iOS. The browser-assets row and the native-libraries row (the two most text-heavy rows) are never spoken.
- The notes say "For Scala and sbt, none of that existed", but the table lists sbt-native-packager and sbt-android, so something did exist. Say "nothing usable".

**Slide 7 (Demo).**
- Four targets were promised on Slide 4. The demo shows three, and desktop JVM is not among them. The missing iOS is not mentioned until Slide 27.
- The notes don't say what the audience should look at (the same model, the same input handling).

**Slide 9.**
- "a different approach": the notes say "made in a completely different way" but don't name it (the translator). That is fine as a teaser, but "hollow" is used before anyone has defined it.
- "It needed tooling that Scala doesn't have": fine.

**Slide 11.**
- "The Sass compiler … dart-sass": in a game-engine talk, the audience wonders why Sass is here. The link (SSG, a static site generator that needs Sass) only arrives three slides later, on Slide 14.
- "283/283 files": files of what? The Dart sources?

**Slide 13.**
- "every method checked against the original": checked by whom or what? By hand, by a tool, by another model? When? This is the key evidence, and its provenance is missing.
- The three percentages add up to 99.6%. That is fine, but say "of N methods".

**Slide 14 (timeline overview).**
- "method audit: PaletteReducer 6%": PaletteReducer is never explained anywhere in the talk (here or on Slide 15).
- "SSG: 20.7% → re-scale": re-scale has not been introduced yet. 20.7% was the Sass test pass rate, and the label attributes it to SSG as a whole.
- "Opus 4.6": the notes say only "Anthropic's Opus model".
- The "blue line" is "not to scale; only the dates are real". So what is the y-axis? Without one, "the line fell" (Slide 16) and "the green line … grows slower" (Slide 20) are hard to interpret.

**Slide 15.**
- The legend is given only by colour ("red is what I found…"). The shapes on screen (▲●◆) are never mapped. If the slide encodes by shape as well as colour, say so; colour-blind viewers depend on it.
- "effort cut, thinking wiped" / "default effort cut to medium": "effort" is a Claude Code setting that not everyone in the audience knows.
- "colorful at 19% of original size": colorful is undefined (the notes say "one library"). Is it a game library or an SSG library?
- "PaletteReducer 6%": unexplained, again.
- "Box2D 400+ files → 8": Box2D is not identified as a physics engine until Slide 25.
- "one well-ported library told me a good port is about the same size": which library?
- Project attribution is unclear: are colorful, PaletteReducer and Box2D part of SGE or SSG? The timeline mixes both.

**Slide 16.**
- "Fable review: broken at algorithm level": on screen, not spoken.
- "And the line fell": the blue line was defined as "what the agents told me". If a reviewer finds bugs, does the agents' claim fall, or does measured reality? The meaning of the line shifts here.
- "Opus 4.8", "Fable 5": a new model name per slide. Model versions are noise to the audience unless the story depends on them.

**Slide 17.**
- Which project had the text-layout and font-rendering bugs? Presumably SGE, while the timeline's red markers so far were mostly SSG. Say it.
- "JavaScript minifier": the SSG table on Slide 32 lists terser (JS) and an "HTML/CSS minifier" (Ruby). Which one is this?
- "counters that only go down": counters of what? (Expected failures? TODOs?)
- "A safety classifier silently swaps Fable for Opus 4.8": why would a safety classifier do that? This is unexplained and sounds like a grievance, not a lesson.
- "Fable switched off worldwide" (screen: 06-12) vs. "almost three weeks" (notes): why it was switched off is not explained. That is acceptable, but it is a side plot.

**Slide 18.**
- "Fable promo": undefined (the notes say "came back for a short time").
- "blind re-review": what is blind about it?
- "A whole subsystem missing": which subsystem?
- "Tests that only tested the standard library": needs one concrete example.
- "one reviewer agent invented three of its five findings": so were there five criticals or two? This undercuts the slide's own number.

**Slide 19.**
- The quote says the agents are untrustworthy "because they are non-deterministic". Everything shown so far is about dishonesty or gaming the checks, not non-determinism. Logical gap: why does determinism fix cheating? (The answer, that a translator's output can be re-run, inspected and diffed, is never stated.)
- "Baltic Porter": the name is not explained. Fine, but nobody will know it's a translator until Slide 23 unless the notes say "a Java-to-Scala translator" here. Right now they only say "a translator … deterministic".

**Slide 20.**
- On screen but never spoken: "Opus 5", "Fable 5.1", "Opus 5.5", "parity dropped: agent ports cheated", "generated & tested (Baltic Porter)".
- "12/12 demos": which twelve demos? The libGDX demos? Never introduced.
- "4 extensions": which ones? And Slide 29 says "6 small extensions". Inconsistent.
- "regeneration": never defined. What is regenerated?
- "the green line … every number on it is measured": measured as what (the percentage of what passing)?
- "Opus 5 'spiky'": an Anthropic quote with no source shown and no explanation of what it means for the story.

**Slide 22.**
- Rows 4–5 are not read ("I won't read the rest" plus two silent clicks), yet they contain "Partial-port debt", "pinned models silently fell back" and the invented findings.
- "the minifier grew to 162% of the original at ~40% conformance": the size check was presented as a heuristic, and this row actually shows that bigger isn't better either. That's a good point, but it is unspoken.
- "Claude Code plugin": fine for this audience.

**Slide 23.**
- "Nullable": a type the speaker uses, not standard Scala. Is it an opaque type? Explicit nulls? Undefined.
- "a few hand-written overrides": overrides of what?
- "The Mermaid 'generator'": Mermaid is a JavaScript library, but Baltic Porter is introduced as "Java → Scala 3". A Mermaid generator inside a Java translator is contradictory unless the translator handles more languages, which Slide 32 later implies ("For TypeScript and JavaScript, the translator exists"). Fix the definition on this slide.
- "28 test suites stubbed out → '0 failures, 18,011 tests'": versus "Over twelve thousand tests" on Slide 32. Different projects? This needs clarification.
- "this time we caught all of it": an overclaim that contradicts the next line ("The limit now is test coverage"). Who is "we"?

**Slide 25.**
- Never explained: ANGLE, Panama, `@extern`, GLFW, miniaudio, Rapier, WASM.
- The table has no Android column, but the notes mention "a backport of Panama" for Android. Which backport? This is the only mention.
- Five silent "(click)"s: the table builds row by row with no narration.
- "jnigen natives (buffers, images) → Rust library": why Rust? Who wrote it?
- "Box2D / Bullet → Rapier": this is a big contradiction with Part I. Part I said a faithful port is the goal and that replacing Box2D with a wrapper was cheating (Slide 15), yet here physics is replaced by a different engine. The audience will ask about it. Address it in one sentence.
- "FreeType … Browser: none": so how are fonts rendered in the browser?

**Slide 26.**
- "Provider JARs": jargon. Explain it as "a JAR that only carries native binaries".
- "zig": most people know the language, but "zig as a C cross-compiler" deserves a few words.

**Slide 27.**
- "No Windows on ARM; those builds ship untested" vs notes "It can't target Windows on ARM either". If it can't target it, what builds ship? Inconsistent.

**Slide 29.**
- "5 hand-written overrides" vs Slide 31's "core overrides 89 to 16". Is it 5 or 16? Inconsistent.
- "6 small extensions" vs Slide 20's "4 extensions".
- "~690 extension files": extensions of libGDX (like Box2D or FreeType)? Not named.
- "generated from upstream at build time": an important point (you don't keep the generated code in the repo), but it is only mentioned in passing here and on Slide 31.

**Slide 30.**
- "Share of the translator's recorded decisions": what is a "recorded decision"? What does 36% vs 64% tell the audience? The notes say "A plain translation already gives you a working port", but a 36% share doesn't show that.
- "an Sge context instead of global variables": the context is undefined (what were the globals? `Gdx.graphics`?).
- "Pixels, Align, Input.Button": fine as examples.

**Slide 31.**
- The PR images mention "ecs generated from Ashley": ecs and Ashley are undefined.
- "core overrides 89 to 16": conflicts with Slide 29's "5".
- "I still have little trust in the numbers the AI reports about itself": good line. But the slide's numbers are line counts from git, so make clear these are not AI-reported.

**Slide 32.**
- KaTeX, terser, rough.js, Mermaid, Liquid: most people know these, but rough.js and Liquid may need a few words each.
- "0–6% of method bodies translated" vs Slide 33's "About 0–5% translated today": inconsistent.
- "HTML/CSS minifier | Ruby": Slide 17 talked about a "JavaScript minifier". Which minifier was the ~40% one?

**Slide 33.**
- "Only snapshot builds so far, no release": snapshots of what, and published where? No repo or link is given anywhere in the talk.
- Seven silent clicks.

**Slide 36.**
- "Scala targets natively what Java reaches with hacks: a separate AOT compiler for iOS": Slide 27 said Scala Native has no iOS support at all. As stated, this is false for iOS. Rephrase.

**Slide 38.**
- "Not immutable FP, but metaprogramming": this lands abruptly. Only one thin link back ("ServiceLoader generated at compile time"). It reads as a separate talk's conclusion.

**Slides 39–40.**
- No links, QR codes or repo names (SGE, multiarch-scala, re-scale, Baltic Porter) for the audience to follow up.

## 3. Missing or too-thin notes

- **Slide 4:** LWJGL3 and MobiVM are not spoken.
- **Slide 6:** 2 of 5 rows are not spoken, and the terms are dense.
- **Slide 7:** no guidance on what to watch. The missing iOS and desktop JVM are not acknowledged.
- **Slide 14:** PaletteReducer, and the y-axis meaning.
- **Slide 15:** colorful and PaletteReducer are not identified; the shape legend is not given.
- **Slide 16:** "Fable review: broken at algorithm level" is not spoken.
- **Slide 20:** the densest slide; at least 6 on-screen labels are not spoken (Opus 5, Fable 5.1, Opus 5.5, 12/12 demos meaning, regeneration, parity).
- **Slide 22:** two rows are skipped on purpose; the 162% insight is lost.
- **Slide 25:** five silent clicks, seven unexplained technology names, and no Android column.
- **Slide 30:** "recorded decisions" is undefined.
- **Slide 33:** seven silent clicks; the notes summarise but don't cover "what can't be translated is counted".
- **Slide 40:** no notes, and no links.

## 4. Top fixes, ranked

1. **Fix the contradictory numbers.** Overrides: 5 (Slide 29) vs 16 (Slide 31). Extensions: 4 (Slide 20) vs 6 (Slide 29). Translated: 0–6% (Slide 32) vs 0–5% (Slide 33). Tests: 18,011 vs "over twelve thousand". Windows on ARM: "can't target" vs "builds ship untested". An audience that has just been told not to trust numbers will notice.
2. **Define Baltic Porter's scope correctly.** Slide 23 says "Java → Scala 3", but the slides also talk about a Mermaid generator and a TypeScript translator. Say "Java (and, experimentally, TS/JS) → Scala 3", and say on Slide 19 that it is a source-to-source translator.
3. **Bridge Slide 19's logic.** Explain why determinism beats dishonesty: the translator's output can be re-run, diffed and measured, and a bug in it is fixed once for all files. Without this, "non-deterministic" doesn't follow from "they cheat".
4. **Simplify the timeline slides (14–20).**
   - Drop the model version labels that aren't in the story (Opus 4.8/5/5.5, Fable 5.1), or speak them.
   - Explain or remove PaletteReducer and colorful.
   - Define what the y-axis means, or say once that it is only a qualitative trend.
   - Tag each red finding with SGE or SSG.
5. **Address the Rapier and Box2D tension on Slide 25.** One sentence on why replacing the physics engine is a deliberate design choice and not the same as the agent's "400 files → 8" cheat.
6. **Fix Slide 36's iOS claim.** Say something like "Scala can target these platforms without a separate compiler bolted on (JS today; iOS once Scala Native supports it)."
7. **Narrate Slide 25 or cut it down.** Give each silent click a short phrase (ANGLE = OpenGL on top of each OS's graphics API; Panama = the JVM's FFI replacing JNI; Rapier = a Rust physics engine). Add an Android column, or say "Android = JVM column, via a Panama backport".
8. **Move the SSG introduction before the Sass numbers.** On Slide 11, add a line like "my second project, a static site generator, needed a Sass compiler", so the Sass detour makes sense right away.
9. **Say who did the Slide 13 audit and how.** One sentence, because it is the foundation of the "claimed vs measured" story.
10. **Add follow-up links.** Put repo URLs or a QR code for SGE, multiarch-scala, re-scale and Baltic Porter on Slide 39 or 40, and say whether the snapshots are public.

Honourable mentions:
- Slide 6: the header text runs together. Speak or cut the browser and native rows.
- Slide 18: "5 criticals" while one reviewer invented 3. Say how many were real.
- Slide 30: define "recorded decisions", or replace the 36/64 donut with just the four counts.
- Slide 38: tie the closing more firmly to the talk, or cut it.
