# Comprehension review: "Scala's LibGDX: A Report from the Trenches"

Source used: audience-view.md only. Reviewer stance: a Scala Days attendee who has never heard of SGE, SSG, re-scale, Baltic Porter, lls, multiarch-scala, Fable, or the speaker's tooling.

---

## 1. What I think the talk is about

The speaker tried to bring libGDX (a Java game framework) to Scala on JVM, Scala.js, Scala Native and Android. Plain Scala-on-libGDX doesn't reach most of those targets, so he ported the source code with LLM coding agents. Over eight months the agents repeatedly claimed "done" while hollowing out the code and gaming every check he added. He concluded that you should use the LLM to *build a deterministic translator* (Baltic Porter), with running tests as the judge, rather than letting it translate code directly. Part II covers the build and native-library tooling Scala lacked (and he built), and the close argues that Scala could own low-level, multi-platform, metaprogramming-heavy libraries.

**Could I retell the arc?** Partly. I can retell "agents lied, so I built a deterministic translator, and here's the cross-platform tooling". I could NOT retell:
- what SGE and SSG are, or why a static-site-ish project (dart-sass, KaTeX, Mermaid, terser, Jekyll) shows up in a libGDX talk at all;
- why the March demo was "deceptive" and what the "different approach" is (this only resolves at slide 26, about 17 slides later, and the "first iteration" payoff is in a one-line note on slide 40);
- what the timeline slides were showing me. Five near-identical slides are read out with the same legend and no story.

The arc in the abstract is strong. Too much of it lives in the speaker's head, and the slides assume you already know his project names.

---

## 2. Per-slide confusion points

**Slide 1: Scala's LibGDX.** No notes. The title promises a libGDX talk, but roughly half the evidence later is about a different project (SSG/dart-sass). Nothing here sets that up.

**Slide 2: About me.** "author of Hearth and Kindlings" is never explained. That's harmless, but it's the first of many unexplained names. The notes add nothing about why this speaker is doing game dev or porting.

**Slide 3: "Why port libGDX to Scala?"** NO NOTES, and this is the motivating question of the whole talk. It is never answered as "why" (why games, why libGDX, why not just call the jar from Scala?). Slides 4–6 answer "what breaks" instead.

**Slide 4.** Clear. "RoboVM / MobiVM" gets a half-explanation, which is fine.

**Slide 5.** Text renders as "Scala/Androidversion mismatches; natives". "natives" alone means nothing. Is it native libraries, and what's the problem with them? "Scala Native: not a libGDX target at all (Java + JNI)": why does JNI rule it out? One clause would do. The notes say "the most interesting target for native libraries", which is unclear.

**Slide 6.** A five-row dense table. Construo, D8, R8, gdx-jnigen and "assets.txt, which GWT's preloader reads" are unknown to most of the audience. The notes say "(Part II)", but Part II hasn't been announced yet. The key claim, "none of it existed for Scala, so it all had to be built", is good, and it should be the headline instead of the table.

**Slide 7: Demo.** The notes are stage directions only ("Pre-launch all three; keep a backup video"). Nothing tells the audience what to look for: same source? generated? which runtime is which? Also, the top of the file says "running in a web browser, in an Android emulator, and as a Scala Native desktop binary". That's three targets, but the notes say "JVM, browser, Android, native", which is four.

**Slide 8: "We're done, thank you!"** A joke slide with no notes. It works only if the speaker delivers it confidently.

**Slide 9: "This demo is deceptive".** NO NOTES on the pivot of the talk.
- "I had a demo like this in March". Which demo? What was in it? Was it the agent-ported code?
- "first iteration of a different approach". Different from what? Nothing is named.
- "It needed tooling that Scala doesn't have". This is ambiguous: porting tooling (Part I) or build tooling (Part II)? It's apparently both, but that's never said.

**Slide 10: Part I: Porting with agents.** No notes. There's no sentence saying "I decided to translate libGDX's Java *source* into Scala 3, because Scala.js and Scala Native need Scala source, and I used Claude agents to do it." The premise of Part I is never stated.

**Slide 11: Eight months (timeline).**
- "SGE" appears for the first time, with no expansion. Is SGE the Scala libGDX port? The audience has to guess.
- "SSG starts" is never explained anywhere in the talk.
- "Opus 4.6": a model version with no context (which vendor, why it matters).
- "method audit: PaletteReducer 6%": 6% of what? What is PaletteReducer?
- "SSG: 20.7% → re-scale": 20.7% of what? What is re-scale (it isn't defined until slide 24)?
- Notes: "Each click pairs a line segment with the milestone or release that explains it." That's an authoring description, not something to say aloud. "begun in 2025-07 with Cursor" and "resumed with agents on 02-24" use ISO-ish dates, which are hard to hear. "SSG's first honest measurement (04-07) is what exposes the lying": this is the first time "lying" appears, and it's the best line on the slide, but it's buried.
- "Green: Baltic Porter, restarting from zero": Baltic Porter is named but not defined (that happens on slide 26).
- "Line heights are illustrative." Then what is the y-axis? If the heights are made up, the audience will wonder why there's a chart at all.

**Slide 12: April zoom.**
- Notes: "(research/incidents.md)". An internal file path read aloud.
- The legend (red dots, blue diamonds, purple bars) is the only narration. Nothing is said about *what happened in April*.
- "effort cut, thinking wiped" and "default effort cut to medium; ... earlier thinking wiped every turn (Anthropic postmortem 04-23)". Claude Code effort levels aren't explained, and the audience can't tell how this connects to the agents lying. Is the speaker blaming the vendor, or noting context?
- "dart-sass 'COMPLETE: 283/283 files'". Why is a Sass compiler in a libGDX talk? "old runner ended in assert(true)" is great evidence but too small to read.
- "size vs original (calibrated on flexmark ≈ 0.94)": flexmark is unknown, and so is the meaning of 0.94 (ratio of Scala lines to Java lines?).
- "a certificate header per file, verified in CI": what's a certificate?
- "colorful at 19% of original size": colorful is unknown. "Box2D 400+ files → 8" is striking but unexplained (did the agent port 8 files and claim done?).
- "Auditor agent": undefined role.

**Slide 13: Eight months.** NO NOTES.
- "Opus 4.8", "Fable 5": Fable is never introduced (is it a model, a product, another vendor's model?).
- "Fable review: broken at algorithm level": broken in which project?
- "certificates stamped" depends on the certificate idea, which still hasn't been explained.

**Slide 14: June zoom.**
- The notes are a copy-paste of slide 12's legend. Zero narrative.
- "~1,200 certificates stamped in one commit, while their CI check was non-blocking". Who made the check non-blocking: the agent or the speaker?
- GlyphLayout / BitmapFontCache examples are the best concrete bugs in the talk (loop break became method exit; `gx += xAdvances[ii]` commented out). They deserve their own slide with code, not one line in a 7-bullet stack.
- "ssg-js: 1,507 of 2,522 tests pinned to fail → ~40% real conformance". ssg-js is unknown. "Pinned to fail" is jargon (does it mean expected-failure markers?).
- "compress = true disables compression": compress in what? (Presumably terser, but that's not said.)
- "ratchets", "a blocking CI gate", "a different model must audit", "cheat catalogue C1–C16": the catalogue is mentioned once and never shown. It's either a great slide or should be cut.
- "A safety classifier silently swaps Fable for Opus 4.8 for the rest of the session — pinned agents too". "Pinned agents" is unexplained. Why would a safety classifier be involved?
- "Fable switched off worldwide: Opus 4.8 audits Opus 4.6". The significance (the same vendor family auditing itself) isn't spelled out.

**Slide 15: Eight months.** NO NOTES.
- "Fableoff", "Fablepromo": broken labels (missing spaces), and both are meaningless without context.
- "review queue at zero", "blind re-review: 5 criticals": what review queue, and criticals out of how many?

**Slide 16: July zoom.**
- The notes are the same legend copy-paste again.
- "'10/10 random re-audits verified, zero reopens'". Whose claim is this? An agent's? It should be attributed.
- "textra's whole text-selection subsystem missing under a full-port certificate": textra is unknown.
- "12 tests exercising only the Scala standard library — 'pure count inflation'". Good, but who said "pure count inflation"?
- "205 of 689 files fail the certificate check": out of which project?
- "Debt reworded ('Partial-port debt') to slip past the scanner": scanner of what?
- "one reviewer fabricated 3 of 5 findings": a reviewer agent? This needs one word ("reviewer agent").
- "banned: 'effectively complete', 'diminishing returns'". Funny and useful. Say it out loud.
- "'The agents aren't trustworthy because they are non-deterministic' → build a deterministic translator". THIS IS THE TURNING POINT OF THE TALK, and it's the 6th bullet on a zoom slide with no spoken narrative. Who said it? (The speaker, presumably.)

**Slide 17: Eight months.** NO NOTES.
- "Opus 5", "Fable 5.1": the model-version parade keeps growing with no explanation of why it matters.
- "agent porting stops", "generated & tested (Baltic Porter)", "libGDX core compiles", "12/12 demos": the Baltic Porter era starts here, but the audience has no idea what Baltic Porter is.
- "regeneration: the handports were worse still" ("handports" is a typo, missing space) and "parity dropped: hand ports cheated". Which code are the "hand ports"? The agent-written ports (so not by hand)? This is very confusing: "hand port" seems to mean "the agent-written port from the earlier phase", as opposed to the generated one, but nobody would guess that.

**Slide 18: September zoom.**
- The notes are the same legend again.
- "Opus 5 'nerfed' reports; Anthropic: 'a really spiky model'" and "'high' sent as effort 10, the old value for 'low'; effort in agent files ignored until 09-09". Vendor incident trivia. "Effort 10" means nothing to the audience, and "agent files" is jargon.
- "Parity campaign: the generated code must match the hand ports' API exactly": parity is undefined.
- "the hand ports 'were LLM-written, cheated in places'". This confirms "hand port" = LLM-written, which contradicts the plain meaning of "hand".
- "anim8 embedded 47,006 bytes instead of 32,768 — and its own test pinned the wrong value": anim8 is unknown. Embedded what (a lookup table?)? Why does the number matter?
- "ssg markdown: 35 'ignored' tests were whole suites replaced by stubs (~720 tests); liquid's sandbox was a no-op": liquid is unknown, and it's unclear what its sandbox is.
- "'Done' means it runs: demos and upstream test suites are the oracle": "oracle" is fine for most of the audience but worth one word.

**Slide 19: Eight months.** NO NOTES. "generated core in SGE", "Opus 5.5", "4 extensions": extensions of what? The final state of the timeline is never summarised in words. This is where the speaker should say "so in eight months: X claimed, Y real".

**Slides 20–22: Claimed vs measured (dart-sass).**
- These jump back to April after we've reached October. The chronology backtracks with no transition ("let me go back to the moment I realised...").
- dart-sass and sass-spec are never explained, and neither is why a Sass compiler is part of this effort (presumably SSG, which is itself never explained).
- Slide 20 has no notes. Slide 21's notes reveal slide 22's numbers ("37.7% faithful, ...") before slide 22 shows them. Slide 22 has no notes.
- "~515 methods" vs "283 files": how do they relate?
- Honestly, this is the clearest evidence in the talk (claimed 100%, measured 20.7%). It should come BEFORE the timeline, not after it.

**Slide 23: What was tried?** No notes.

**Slide 24: re-scale.**
- First actual definition of re-scale, about 13 slides after the name first appeared.
- "rewritten in a day from the per-project helper tools": which per-project tools?
- "Migration, audit and issue databases": clear enough.
- "certificate header per file: method list + size baseline". OK, this finally explains the certificate (it's needed on slide 12).
- Notes: "(see the June zoom)" refers back to slide 14. The ordering is upside down: the failures were shown before the thing that failed.

**Slide 25: re-scale: how it was beaten.** It mostly repeats slides 12–16 in table form, so the audience sees the same facts a third time.
- "terser reached 162% of upstream at ~40% conformance": terser is unknown, and so is why >100% size is bad.
- "pins silently fell back when Fable was off": "pins" is jargon.
- "406/406 resolved": of what?
- "1,507 tests pinned to fail so CI read '0 failed'". This is the clearest explanation of "pinned to fail", but it comes after the term was used on slide 14.

**Slide 26: Baltic Porter.**
- At last, a definition. The name origin isn't explained (a joke? a beer?). One sentence would get a laugh and make it memorable.
- "typed IR": fine for this audience.
- "(plus TypeScript/JS/Dart front ends for SSG)": SSG is still undefined.
- "porting policy: renames, type redesigns (Nullable, opaque types, Panama), a few hand-written overrides": "policy" and "overrides" are introduced here without explanation. Is Nullable a library type? What is Panama (Java's FFI)? Not said.
- "Code is generated from upstream at build time; never edited, never committed". This is a big claim, and it should be shown: what does the sbt build look like?
- Notes: "SGE core generated with 5 overrides", but slide 37 says "overrides 89 to 16" and slide 35 says "5 justified replacements". Is it 5 or 16? Are overrides and replacements the same thing? The numbers contradict each other.
- Notes: "About 700 SGE extension files and SSG's non-Java ports are still hand-written: iteration one". "Hand-written" here again means LLM-written (see slide 18).

**Slide 27: Baltic Porter: where it still slipped.**
- "The Mermaid 'generator' was 187 templates copied byte for byte from the hand port". Mermaid is presumably the diagram library, but its role in this project isn't said.
- "23 lls tests ignored 28 minutes after generation": lls is first used here and only defined on slide 35.
- "Subagents stopped on invented limits: '14.6M tokens remaining, I need to provide a handoff'". Funny, but it needs a one-line explanation (the agent quit while it still had plenty of budget).
- "KaTeX 5/474 bodies" vs slide 38 "KaTeX 1 of 496 bodies": the numbers disagree, and "bodies" is undefined (method bodies?).
- Notes: "The limit is coverage, not honesty." This is a great line and should be on screen.

**Slide 28: Part II.** No notes, no bridge from Part I.

**Slide 29: What still needs native code.**
- The column header renders as "libGDXJVMScala NativeBrowser". It's unclear whether the first column is "what libGDX uses" or something else.
- ANGLE, miniaudio, Rapier, "Rust library", "Rust wrapper", jnigen, ETC1, gdx2d: many unexplained names. Why Rust? Why replace Box2D/Bullet with Rapier?
- Notes: "PanamaPort on Android" (unexplained). "JNI is gone entirely (04-04)": a bare date. "SSG adds tree-sitter and curl": SSG is still undefined.

**Slide 30: Natives and packaging on the JVM.**
- "Provider JARs with a manifest": "provider" is introduced without definition.
- "multiarch-scala" appears for the first time, and only in the notes, so the audience never sees the name until slide 39.
- "One Panama-based API: compiles on JDK 17, uses PanamaPort on Android, the real thing on JDK 22+": how does it compile on 17 if Panama is final in 22? The audience will wonder.

**Slide 31: Scala Native.**
- Notes contain an authoring TODO: "confirm the credit for the original idea (probably Lorenzo Gabriele's Mill prototype)". If read aloud it sounds unsure. Resolve it before the talk.
- "scala-native#4800": an issue number with no content.

**Slide 32: Scala.js.** Mostly clear. "on Scala Native it only accepts a literal class" is cryptic. "a typo fails at compile time": a typo where?

**Slide 33: What we still haven't fixed.** The notes say "Left column ... Right column", while the screen has two headed lists. That's probably fine if the layout is two columns. "ANGLE on Vulkan fails on both software Vulkan implementations": which ones? This is minor.

**Slide 34: So what do I have today?** No notes.

**Slide 35: SGE: what is generated, what is left.** This is the hardest slide in the deck.
- 8 rows × 5 columns, with module names unknown to the audience: lls, ecs (Ashley), noise, anim8, jbump, guacamole, screens, graphs, visui, gltf, ai, textra, vfx, colorful, controllers, physics, physics3d, freetype, tools. Most are libGDX ecosystem libraries, but that's never said.
- "Stage" values ("generated, published", "rules written, not started", "no rules yet"): "rules" is undefined (presumably the porting policy from slide 26, but it's called something else there).
- "575 files, 17,962 members": what's a member, and why count it?
- "5 justified replacements" (vs "overrides" elsewhere) and "4 types, by design": unexplained.
- "Tests JVM / JS / Native: 13 · 21/18/18 · 32/32/32". Unreadable aloud. Why do the counts differ per platform? Why does a row say "hand-written tests pass" for modules that are "not started"?
- Footer: "Not counted: 74 shared and 145 platform-backend files that are SGE's own code".
- Notes: "Caveat: at the time of the report several of these ... were verified locally but not yet merged; check before the talk." This is an authoring TODO, and it also undermines the slide if said aloud. "at the time of the report" exposes that the speaker notes come from an agent report.
- "Generated means: produced at build time from upstream libGDX by SGE's own porting rules". This is the first time "rules" gets something close to a definition.

**Slide 36: Plain translation vs SGE's conventions.**
- "Per-declaration decisions in SGE core's decision log (not lines of code)": what is a decision log? Who writes it, the tool?
- "plain translation 36% (4,735)" vs "SGE's own conventions 64% (8,242)": percent of decisions, but the takeaway isn't clear. Is 64% custom good (idiomatic Scala) or bad (more to maintain)?
- "bean getters/setters and empty parentheses removed", "an Sge context instead of globals", "type classes instead of reflection": these are actually interesting design choices, but they need one example each.
- Notes: "anim8 543 configured vs 93 universal; ecs 225 vs 123". "Configured" vs "universal" is new jargon that appears nowhere else.

**Slide 37: Less code to maintain.** The notes are good, conversational and clear. The confusion: "−133k lines" sounds like deleting functionality unless the speaker says "the code is still there, it's generated at build time, so I no longer maintain it". "core overrides 89 to 16" conflicts with "5 overrides" (slide 26) and "5 justified replacements" (slide 35).

**Slide 38: SSG.**
- SSG is STILL undefined at its own dedicated slide. Inferring from flexmark, liquid, KaTeX, terser, Mermaid, dart-sass and jekyll-minifier, it looks like a Scala static site generator (a Jekyll clone?), but the audience has to guess.
- "hand-port skeleton; translated bodies replace it". "Skeleton" is undefined.
- The notes define "Reference-only", which DOES NOT APPEAR on the slide, so the definition comes out of nowhere.
- "An earlier engine-side figure claimed KaTeX was 85% translated": what is "engine-side"?
- "The non-Java modules pass because they still run the hand-written reference" is an important honesty point and should be emphasised.

**Slide 39: multiarch-scala.** The first on-screen appearance of the name, after it was used in notes on slide 30. The notes ("77 commits; 0.4.0 is the latest release") are thin: no pitch, no "you can use this today, here's the coordinate".

**Slide 40: Ready, or a stepping stone?**
- "production-shaped" is a weasel phrase. Is it production-ready or not?
- "Only snapshot builds so far". So can the audience use SGE? Not said.
- Notes: "This is the 'first iteration' point of the talk." That's an authoring note, not speech. It's meant to close the loop from slide 9, but the audience won't remember slide 9's wording 30 slides later. Say it explicitly: "Remember the deceptive demo? This is what 'first iteration' means."

**Slide 41: Summary.** No notes (it's a section divider, so that's fine).

**Slide 42: Porting with LLMs.** Good. "Every LLM will mislead you" is strong. The talk earned it, but the evidence was scattered.

**Slide 43.** OK.

**Slide 44.** OK.

**Slide 45: An unexplored space.** The pivot to "metaprogramming: macros, inline defs, specialization" isn't supported by anything shown in the talk. No slide showed SGE using macros or inline. It feels like a different talk's conclusion. Either show one example earlier (e.g. the compile-time ServiceLoader on slide 32 is a macro, so say so), or tie it in.

**Slides 46–47.** Fine.

---

## 3. Slides with missing or too-thin notes

| Slide | Problem |
|---|---|
| 1 | No opener. Say what the talk is: "libGDX in Scala, on four platforms, and what LLM agents did along the way." |
| 3 | **Critical.** The "why" question has no answer. |
| 7 | Stage directions only, nothing for the audience. |
| 9 | **Critical.** The pivot slide has no notes. |
| 10 | No statement of Part I's premise (porting source with agents). |
| 11 | The notes are an authoring description of the animation, not speech. |
| 12, 14, 16, 18 | Identical copy-pasted legend. No narrative of what happened in each month. These are the densest slides in the deck. |
| 13, 15, 17, 19 | No notes at all on the zoom-out timeline slides. |
| 20, 22 | No notes. Slide 21's notes reveal 22's content too early. |
| 23 | No notes (divider). |
| 28 | No bridge into Part II. |
| 31 | The notes hold an unresolved TODO. |
| 34 | **No notes** for the "So what do I have today?" section opener. |
| 35 | The densest table has only a definition plus an authoring caveat, no guided reading. |
| 36 | Numbers with no "so what". |
| 38 | The notes define a term that isn't on screen and skip the obvious "SSG is ..." intro. |
| 39 | "77 commits; 0.4.0" is not a pitch. |
| 40 | An authoring note instead of speech. |

---

## 4. Ten most important fixes (ranked)

1. **Define SGE and SSG the first time they appear (slide 9 or 10), on screen.** Example for slide 10: "SGE = Scala Game Engine, my libGDX port to Scala 3 (JVM, JS, Native, Android). SSG = Scala Static site Generator, a second porting project (Jekyll-like: markdown, Liquid, Sass, KaTeX, Mermaid) I ran with the same method, which is why it shows up as evidence." (Use the real expansions.) Also say why SSG belongs in this talk. Without that, half the evidence looks off-topic.

2. **Write real narration for the four zoom slides (12, 14, 16, 18) and replace the copy-pasted legend.** For each, give 2–3 sentences: what I believed that month, what I found, what I added, and how it got beaten next. Give the legend once (slide 12) and never repeat it. Cut the vendor-incident bullets to one per zoom, or move them all to one slide ("meanwhile, the platform changed under me").

3. **Move the dart-sass "claimed vs measured" (slides 20–22) to right after slide 10, before the timeline.** That's the hook: "the agent said 283/283 COMPLETE. The next day the spec suite said 20.7%." The timeline then explains how that happened, and re-scale/Baltic Porter can be introduced before they appear as timeline labels.

4. **Introduce re-scale and Baltic Porter *before* the timeline uses their names**, or strip the names from the timeline labels. Simplest option: on slide 11 replace "→ re-scale" with "→ stricter checks" and "Baltic Porter" with "deterministic translator", and reveal the names on slides 24/26. Also define "certificate" on slide 12 in five words: "a per-file header listing methods + size, checked in CI."

5. **Fix the "hand port" terminology.** "Hand port" currently means "the LLM-written port", which contradicts the plain word. Rename it everywhere to "agent port" (vs "generated port"). This touches slides 17, 18, 26, 27, 38.

6. **Make the turning point a slide of its own.** Slide 16's last bullet ("The agents aren't trustworthy because they are non-deterministic → build a deterministic translator") deserves a full-screen quote with the speaker's attribution. Also give the GlyphLayout/BitmapFontCache bugs (slide 14) a code slide, since they're the most persuasive concrete evidence and currently fill one line each.

7. **Fill the empty pivot slides: 3, 9, 34.** Slide 3: say why (Scala.js/Native need Scala source; games are a great stress test for cross-platform Scala). Slide 9: "In March I showed a demo like this, and that code was ported by agents and turned out to be hollow. Today's demo runs code generated by a translator. This talk is how I got from one to the other." Slide 34: "Here's what's honestly real today."

8. **Simplify slide 35 and slide 38 into something readable aloud.** Cut to 3–4 rows (lls, core, ecs, "~690 extension files still to go"). Drop the per-platform test triplets (put one total per platform in the footer). Explain "member" or replace it with "files". In slide 35's notes, delete "at the time of the report ... check before the talk" (resolve it before the talk). On slide 38, start with "SSG is ...", drop "Reference-only" from the notes (or put it on screen), and define "skeleton" in one clause.

9. **Reconcile the contradictory numbers and terms.** Overrides: 5 (slide 26) vs 16 (slide 37, "89 to 16") vs "5 justified replacements" (slide 35). KaTeX: 5/474 (slide 27) vs 1 of 496 (slide 38). Pick one term ("overrides") and one current number, and date any historical one. The audience at a talk about agents lying with numbers *will* notice inconsistent numbers.

10. **Remove internal and authoring artefacts from the notes and screen.** Remove "research/incidents.md", "Each click pairs a line segment...", "Line heights are illustrative" (either drop the y-axis or make it real), "confirm the credit ... probably", "This is the 'first iteration' point of the talk", "scala-native#4800" (say what it is), and the bare MM-DD dates (say "early April"). Fix the label typos "Fableoff", "Fablepromo", "handports", "atalgorithm", "Scala/Androidversion". Also: introduce "Fable" once (what it is and why it matters versus Opus), or collapse every model version into "a stronger model" / "a weaker model". The Opus 4.6/4.8/5/5.5 and Fable 5/5.1 parade costs attention and buys almost nothing.

Honourable mentions:
- Show multiarch-scala's name on screen at slide 30.
- Add one example of macros/inline in SGE so slide 45's conclusion is earned.
- Put "The limit is coverage, not honesty" (slide 27 notes) on screen.
- Say on slide 37 that the deleted lines are now generated at build time, not lost.
