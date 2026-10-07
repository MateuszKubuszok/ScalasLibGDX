# Timing and deliverability review: "Scala's LibGDX: A Report from the Trenches" (audience view v2)

Source: `audience-view-2.md` only.

## 1. Bottom line

| | Low | Likely | High |
|---|---|---|---|
| Total | **23.6 min** | **26.8 min** | **32.1 min** |
| vs 25-min target | −1.4 | **+1.8** | +7.1 |
| vs 30-min hard limit | −6.4 | −3.2 | **+2.1** |

- Spoken words (cues removed): **2,185**. That is ~19 minutes of pure speech at 115 wpm, before any clicks, pauses, the demo or reading time.
- Cues: **98 clicks** and **33 pauses**. Together they add 3–5 minutes.
- **Verdict: over.** The likely case misses the 25-minute target by about 2 minutes. If the demo hiccups or nerves slow you down, the high case runs past the 30-minute limit. Cut **about 3 minutes** (roughly 300 words plus a few silent clicks). Then the likely case is about 24 minutes and the high case about 29.
- Part I (slides 10–23) has **46% of the words** and 11 of the likely 27 minutes. Most of the cuts should come from there, mostly from parts that repeat each other. Slide 22 repeats slides 15 and 17. The Sass story is told twice, on slides 11–12 and again on slide 15.

## 2. Method

- **Speech**: words ÷ 120 wpm (low), 115 (likely), 110 (high). The high case adds 5% for restarts and ad-libs, which is realistic for a calm non-native speaker.
- **Clicks**: 1 / 1.5 / 2 s each. **Pauses**: 2 / 2.5 / 3 s each.
- **Transition** per slide: 1 / 1.5 / 2 s.
- **Audience reading**: extra time on dense slides. These are the tables (6, 22, 23, 25, 26, 32), the annotated timelines (15, 17, 20) and the 7-click reveals. Allowance: 0.25× / 0.5× / 1× of a 5–20 s budget per slide.
- **Demo (slide 7)**: 90 / 105 / 135 s. The high figure allows for one hiccup when switching windows. The 35 words of notes are inside this budget.

## 3. Per-slide timing

### Opening (1–9, incl. demo)

| # | Slide | Words | Speech @115 (s) | Clicks | Pauses | Low (s) | Likely (s) | High (s) |
|---|---|---|---|---|---|---|---|---|
| 1 | Scala’s LibGDX | 31 | 16 | 0 | 1 | 18 | 20 | 23 |
| 2 | About me | 64 | 33 | 0 | 1 | 35 | 37 | 42 |
| 3 | Why port libGDX to Scala? | 26 | 14 | 0 | 1 | 16 | 18 | 20 |
| 4 | What libGDX gives you | 49 | 26 | 0 | 1 | 29 | 32 | 38 |
| 5 | …and what you keep if you write it in Scala | 86 | 45 | 5 | 1 | 52 | 59 | 69 |
| 6 | The build tooling goes too | 52 | 27 | 0 | 2 | 36 | 44 | 58 |
| 7 | Demo | 35 | 18 | 0 | 1 | 90 | 105 | 135 |
| 8 | We’re done, thank you! | 11 | 6 | 0 | 1 | 8 | 10 | 11 |
| 9 | This demo is deceptive | 65 | 34 | 3 | 2 | 41 | 46 | 54 |
| | **Subtotal** | **419** | | | | **5.4 min** | **6.2 min** | **7.5 min** |

### Part I: Porting with agents (10–23)

| # | Slide | Words | Speech @115 (s) | Clicks | Pauses | Low (s) | Likely (s) | High (s) |
|---|---|---|---|---|---|---|---|---|
| 10 | Part I: Porting with agents | 19 | 10 | 0 | 0 | 10 | 11 | 13 |
| 11 | Claimed vs measured | 31 | 16 | 0 | 0 | 17 | 19 | 23 |
| 12 | Claimed vs measured | 15 | 8 | 0 | 1 | 11 | 13 | 16 |
| 13 | Claimed vs measured | 34 | 18 | 0 | 1 | 21 | 23 | 27 |
| 14 | Eight months | 126 | 66 | 4 | 1 | 71 | 78 | 90 |
| 15 | April: the files were "done" | 172 | 90 | 7 | 0 | 96 | 107 | 125 |
| 16 | Eight months | 47 | 25 | 3 | 1 | 30 | 33 | 38 |
| 17 | June: every method present, bodies hollow | 132 | 69 | 7 | 0 | 76 | 86 | 102 |
| 18 | Eight months | 53 | 28 | 2 | 1 | 32 | 35 | 39 |
| 19 | (untitled) | 42 | 22 | 0 | 1 | 24 | 26 | 29 |
| 20 | Eight months | 115 | 60 | 5 | 1 | 68 | 76 | 91 |
| 21 | What was tried? | 21 | 11 | 0 | 0 | 12 | 12 | 14 |
| 22 | re-scale: what it checked, how it was beaten | 85 | 44 | 5 | 2 | 56 | 66 | 82 |
| 23 | Baltic Porter: what it does, where it still slip | 109 | 57 | 6 | 1 | 67 | 77 | 94 |
| | **Subtotal** | **1001** | | | | **9.9 min** | **11.1 min** | **13.0 min** |

### Part II: Shipping cross-platform Scala (24–27)

| # | Slide | Words | Speech @115 (s) | Clicks | Pauses | Low (s) | Likely (s) | High (s) |
|---|---|---|---|---|---|---|---|---|
| 24 | Part II: Shipping cross-platform Scala | 22 | 11 | 0 | 1 | 14 | 15 | 18 |
| 25 | What still needs native code | 58 | 30 | 5 | 1 | 42 | 52 | 68 |
| 26 | A native library is just a dependency | 109 | 57 | 5 | 1 | 65 | 73 | 87 |
| 27 | What we still haven’t fixed | 51 | 27 | 5 | 0 | 32 | 36 | 41 |
| | **Subtotal** | **240** | | | | **2.5 min** | **2.9 min** | **3.6 min** |

### Where I am today (28–33)

| # | Slide | Words | Speech @115 (s) | Clicks | Pauses | Low (s) | Likely (s) | High (s) |
|---|---|---|---|---|---|---|---|---|
| 28 | So what do I have today? | 6 | 3 | 0 | 1 | 6 | 7 | 8 |
| 29 | SGE: what is generated, what is left | 39 | 20 | 3 | 0 | 25 | 29 | 35 |
| 30 | Plain translation vs SGE’s conventions | 47 | 25 | 4 | 1 | 32 | 37 | 45 |
| 31 | Less code to maintain, same behaviour | 102 | 53 | 4 | 1 | 60 | 68 | 81 |
| 32 | SSG: Java done, the rest is still an agent port | 59 | 31 | 4 | 1 | 39 | 46 | 57 |
| 33 | Ready, or a stepping stone? | 36 | 19 | 7 | 1 | 30 | 38 | 50 |
| | **Subtotal** | **289** | | | | **3.2 min** | **3.8 min** | **4.6 min** |

### Summary and close (34–40)

| # | Slide | Words | Speech @115 (s) | Clicks | Pauses | Low (s) | Likely (s) | High (s) |
|---|---|---|---|---|---|---|---|---|
| 34 | Summary | 4 | 2 | 0 | 0 | 3 | 4 | 4 |
| 35 | Porting with LLMs | 83 | 43 | 5 | 2 | 52 | 59 | 69 |
| 36 | Scala on every platform | 33 | 17 | 2 | 1 | 22 | 26 | 31 |
| 37 | What works today | 52 | 27 | 4 | 1 | 34 | 39 | 46 |
| 38 | An unexplored space | 61 | 32 | 3 | 0 | 35 | 39 | 46 |
| 39 | Questions? | 3 | 2 | 0 | 0 | 2 | 3 | 4 |
| 40 | Thank you! | 0 | 0 | 0 | 0 | 1 | 2 | 2 |
| | **Subtotal** | **236** | | | | **2.5 min** | **2.8 min** | **3.4 min** |

TOTAL 23.6 / 26.8 / 32.1

## 4. Cue / slide mismatches (they cost time on stage)

- **Slide 6**: a 5-row table, but the notes have **no click cues**. If the rows reveal one click at a time, you will either click through them in silence or end up talking over a blank table. Show the whole table at once (preferred: the notes don't read it anyway), or add cues.
- **Slide 13**: three percentages, no clicks. If they reveal one by one, add `(click)` before "About a third faithful", "A quarter…" and "A third…". That is a nice rhythm, and it costs about 3 s.
- **Slide 25**: **five silent clicks in a row** `(click) (click) (click) (click) (click)`. That is 10–20 s of dead air while the audience reads a 4-column table. Reveal it in one go, or say one short phrase per row ("Graphics." / "Windows and audio." / "Buffers and images." / "Fonts." / "Physics."). The phrase version is calmer and costs the same time.
- **Slide 29**: 3 clicks, but the screen also has the line "Tests pass on JVM, JS and Native". Add a 4th click and say "And all of it passes tests on all three platforms." Otherwise the line is never spoken.
- **Slide 32**: the footer line ("Over twelve thousand tests…") is the 5th reveal, but there are only 4 clicks. Put a `(click)` before "(pause) The tests pass everywhere."
- **Slide 33**: 4 + 3 silent clicks. Group each column into a single reveal (2 clicks total). That saves about 8 s and avoids awkward silence.
- **Slide 31**: three silent clicks for the PR images. Fine if you let people look, but don't hurry them.
- **Numbers that differ on screen**: slide 32 says "0–6% of method bodies translated", and slide 33 says "About 0–5% translated today". Pick one figure.

## 5. Notes that are still hard to speak, with rewrites

Main problems: long sentences with colons and semicolons, stacked numbers, and three ideas on one click.

**Slide 11**
> "Two hundred eighty-three of two hundred eighty-three files."

Number-heavy, and it is easy to trip on the second "two hundred eighty-three". The screen already shows 283/283.
→ "Migration complete. Every file. All two hundred eighty-three of them."

**Slide 14**
> "It is not to scale; only the dates are real. (click) In late February I picked SGE up again: SGE, the Scala Game Engine, is my Scala port of libGDX. This time I did it with AI agents. Anthropic's Opus model was the one doing the work."

The semicolon and colon make this written style. The audience already met SGE on the Demo slide.
→ "It is not to scale. Only the dates are real. (click) In February I went back to SGE, my game engine. This time with AI agents. Opus did the work."

**Slide 15: legend and purple**
> "In the zooms, red is what I found, blue is what I added in response, and purple is what was going wrong on Anthropic's side. (click) First, purple: Anthropic later admitted that in March Claude Code ran with lower default effort, and a bug kept wiping the model's earlier reasoning. (click) Usage was also throttled at peak hours."

→ "Three colours. Red: what I found. Blue: what I added. Purple: problems on Anthropic's side. (click) (click) Purple first. In March, Claude Code quietly used less effort, a bug wiped its earlier thinking, and usage was throttled at peak hours. Anthropic admitted this later."
(The two purple clicks are merged, and the three facts sit in one simple list.)

**Slide 15: the checks**
> "Compare each file's size with the original: one well-ported library told me a good port is about the same size."

"One library told me" is confusing when heard.
→ "Compare the size with the original. A good port is about the same size."

> "Then the Sass port: complete, said the agent. One test in five, said the test suite."

This repeats slides 11–12. → "Then the Sass port, which you already saw."

**Slide 17**
> "In the JavaScript minifier, more than half the tests were marked as expected to fail, so CI said: zero failures. Real conformance was about forty percent."

→ "In the JavaScript minifier, more than half the tests were marked 'expected to fail'. So CI said: zero failures. (pause) In reality, about forty percent worked."

> "(click) On Anthropic's side, a safety classifier could silently swap Fable for Opus. (click) And then Fable was switched off worldwide for almost three weeks. So Opus was auditing Opus."

→ "(click) (click) And in purple: Fable was sometimes silently swapped for Opus. Then it was switched off for three weeks. So Opus was auditing Opus."

**Slide 20 (three topics on one click)**
> "In September I compared the result with the old agent ports. They were even worse than the reviews had shown: their own tests checked for wrong values. That's the second red line. And in purple: Claude Code was quietly sending lower effort than I had selected, and Opus 5 was, in Anthropic's words, a really spiky model. Meanwhile, all twelve demos render."

→ "In September I compared the result with the old agent ports. They were worse than I thought. Their own tests expected wrong values. (pause) Meanwhile, all twelve demos render."
(Drop the purple sentence. You have made the purple point twice already. Saves about 15 s.)

**Slide 26**
> "Now native binaries are cross-compiled with zig, and desktop apps are packaged for every system from one laptop."
→ "Now zig cross-compiles the native code. And one laptop packages the app for every system."

> "And Scala.js, which has no classpath, gets its assets embedded at build time, and a ServiceLoader generated at compile time."
→ "Scala.js has no classpath. So assets are embedded at build time, and the ServiceLoader is generated by the compiler."

**Slide 29**
> "About six hundred ninety extension files are still the old agent port."
→ "Almost seven hundred extension files are still the old agent port."

**Slide 31**
> "About nine thousand lines added, a hundred and thirty thousand removed. … If that trend holds, a few maintained lines will support a lot of functionality. The risk of AI slop in those lines is still there. But the slop I have to review is much smaller."

→ "Nine thousand lines in. (pause) A hundred and thirty thousand out. That code is now generated at build time, so I don't maintain it. (pause) I still don't trust the numbers AI reports about itself. I trust the tests and the demos. And the code I have to review keeps getting smaller."
(About 100 → 55 words.)

**Slide 2**: fine to say, but long for an intro. → "A few words about me. (pause) I have written Scala for almost twelve years, and maintained Chimney for nine. That taught me a lot about macros, and about making Scala approachable." (64 → 32 words)

**Slide 22**: "every check looked at names, words, or counts. Never at behaviour." Good. Keep that line word for word: it is the thesis.

## 6. Cuts (target: −3 min)

| # | Change | Saves (likely) |
|---|---|---|
| A | **Slide 22**: drop the per-row narration (it repeats 15 and 17). Show the table in one reveal, give 5 s of silence, then say only: "Every check I added, they got past. (pause) Every check looked at names, words, or counts. Never at behaviour." | ~40 s |
| B | **Slide 15**: merge the purple clicks, drop "one well-ported library told me", shrink the Sass recap (rewrites above). 172 → ~115 words | ~30 s |
| C | **Slide 20**: drop the purple sentence (rewrite above). 115 → ~85 words | ~18 s |
| D | **Slide 14**: drop the repeated SGE definition and the semicolons. 126 → ~90 words | ~18 s |
| E | **Slide 17**: merge the two purple clicks. 132 → ~105 words | ~15 s |
| F | **Slide 31**: closing paragraph rewrite. 102 → ~55 words | ~25 s |
| G | **Slide 2**: shorter intro | ~15 s |
| H | **Slide 26**: shorter sentences. 109 → ~85 words | ~12 s |
| I | **Slides 25, 33**: no strings of silent clicks; group the reveals | ~15 s |
| | **Total** | **~3 min** |

That gives a new estimate of about **21 / 24 / 29 min**. That leaves the slow, calm pace and the pauses intact.

If you need more (for example, the demo overruns badly): drop **slide 16** and fold its single key sentence into slide 18 ("Certificates stamped on twelve hundred files at once; then Fable reviewed everything, and the line fell"). This saves about 25 s. Cut the timeline before you cut pauses.

**Do not cut**: the pauses on slides 8, 12, 19 and 35. They are where the talk's punchlines land, and they help a non-native speaker breathe.

## 7. Stage tips for a calm, non-native delivery

- Put a **time checkpoint** in your presenter view. Slide 10 (Part I) at about **7 min**, slide 24 (Part II) at about **17 min**, slide 34 (Summary) at about **22 min**. If you are more than 1 minute late at slide 24, use the slide-16 cut and say slide 27 in two sentences.
- The demo is the biggest variable. Open all three windows in advance, and use a fixed order and a fixed phrase per window. If one platform fails, say "and the same on Android" and move on. Don't debug on stage.
- Numbers on screen don't need to be read aloud. Where the slide shows a number, say a rounded word ("a fifth", "about forty percent"). You already do this well on slides 12–13.
