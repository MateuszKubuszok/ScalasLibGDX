# Timing and deliverability review: "Scala's LibGDX: A Report from the Trenches"

Source: `audience-view.md` only. Pace assumed: calm, 110–120 words/min (115 used). Target 25:00, hard limit 30:00, Q&A outside the slot.

## Headline

| | Low | Likely | High |
|---|---|---|---|
| Total as the deck stands | **~28 min** | **~38–39 min** | **~50 min** |
| vs 25-min target | +3 | **+13 to +14** | +26 |
| vs 30-min hard limit | −2 (barely fits) | **+8 to +9** | +21 |

Even the low estimate, where every click gets one short sentence, misses the 25-minute target. The likely case overruns the hard limit by about 9 minutes. The notes add up to only ~1,450 words (~12.5 min of speech), and that number is misleading for two reasons:

1. **About 20 slides have no notes, or notes that are stage directions rather than speech**, but they still need something said: dividers, timeline returns, the "Eight months" overviews, and tables whose notes only say "Zoom on the drop".
2. **The time goes on the clicks, not on the notes.** The four timeline zooms reveal 6–8 annotated events each, and those annotations are not in the notes. The deck also has ~12 dense tables (100–210 words of on-screen text each). Narrating one click calmly takes 10–15 s. Letting an audience read a table takes 20–40 s.

Part I (timeline and zooms) alone is likely ~12 minutes, half the target, and is the main place to cut.

---

## 1. Per-slide estimate

Columns: notes words → speaking time at 115 wpm; extra time = clicks, reading time for the audience, transitions and pauses; likely total, with low–high range in brackets. Times in seconds.

### Intro

| # | Slide | Notes words | Notes time | Extra beyond notes | Likely (low–high) |
|---|---|---|---|---|---|
| 1 | Title | 0 | 0 | Greeting, title, a breath | 20 (15–30) |
| 2 | About me | 98 | 51 | 6 bullets click in; pause | 60 (50–75) |
| | **Subtotal** | | | | **1:20 (1:05–1:45)** |

### Why libGDX

| # | Slide | Notes words | Notes time | Extra | Likely (low–high) |
|---|---|---|---|---|---|
| 3 | Why port libGDX to Scala? | 0 | 0 | Divider; needs one line | 10 (5–15) |
| 4 | What libGDX gives you | 24 | 13 | 4 backends revealed; LWJGL3/GWT/RoboVM need saying slowly | 40 (30–55) |
| 5 | …what you keep in Scala | 42 | 22 | Click per backend, 4 verdicts + Scala Native | 60 (45–80) |
| 6 | Build tooling goes too | 52 | 27 | 5-row table, 161 words on screen | 75 (50–100) |
| | **Subtotal** | | | | **3:05 (2:10–4:10)** |

### Demo

| # | Slide | Notes words | Notes time | Extra | Likely (low–high) |
|---|---|---|---|---|---|
| 7 | Demo | 14 (stage directions) | — | 3 targets, window switching | 105 (90–150) |
| 8 | We're done, thank you! | 0 | 0 | Joke; wait for the laugh | 10 (5–15) |
| 9 | This demo is deceptive | 0 | 0 | 3 bullets; the key pivot of the talk, with no notes | 30 (20–40) |
| | **Subtotal** | | | | **2:25 (1:55–3:25)** |

### Part I: timeline and zooms

| # | Slide | Notes words | Notes time | Extra | Likely (low–high) |
|---|---|---|---|---|---|
| 10 | Part I divider | 0 | 0 | Transition | 10 (5–15) |
| 11 | Eight months (overview) | 69 | 36 | ~7 clicks, legend, SGE/SSG never introduced | 80 (60–100) |
| 12 | April zoom | 36 (legend only) | 19 | 7 annotated events, none in notes | 120 (90–150) |
| 13 | Eight months (return) | 0 | 0 | 4 new labels | 30 (20–45) |
| 14 | June zoom | 36 (same legend) | 19 | 7 events | 120 (90–150) |
| 15 | Eight months (return) | 0 | 0 | 4 new labels | 30 (20–45) |
| 16 | July zoom | 36 (same legend) | 19 | 6 events | 105 (80–135) |
| 17 | Eight months (return) | 0 | 0 | 9 new labels | 40 (25–55) |
| 18 | September zoom | 36 (same legend) | 19 | 7 events, most numeric | 120 (90–150) |
| 19 | Eight months (final) | 0 | 0 | 3 new labels, closing line | 25 (15–35) |
| 20 | Claimed vs measured (claim) | 0 | 0 | One bar | 15 (10–20) |
| 21 | Claimed vs measured (20.7%) | 16 | 8 | Pause for effect | 20 (15–30) |
| 22 | Claimed vs measured (audit) | 0 | 0 | 3 numbers (already spoken on 21) | 20 (15–25) |
| | **Subtotal** | | | | **12:15 (8:55–15:55)** |

### re-scale / Baltic Porter

| # | Slide | Notes words | Notes time | Extra | Likely (low–high) |
|---|---|---|---|---|---|
| 23 | What was tried? | 0 | 0 | Divider | 10 (5–15) |
| 24 | re-scale | 43 | 22 | 5 bullets to reveal before the "why not" | 60 (45–75) |
| 25 | re-scale: how it was beaten | 19 | 10 | 6-row table, 153 words on screen | 90 (60–120) |
| 26 | Baltic Porter | 60 | 31 | 6 bullets | 80 (60–100) |
| 27 | Baltic Porter: where it slipped | 32 | 17 | 6-row table, 136 words | 85 (60–110) |
| | **Subtotal** | | | | **5:25 (3:50–7:00)** |

### Part II

| # | Slide | Notes words | Notes time | Extra | Likely (low–high) |
|---|---|---|---|---|---|
| 28 | Part II divider | 0 | 0 | Transition | 10 (5–15) |
| 29 | What still needs native code | 45 | 23 | 5×4 table | 70 (50–90) |
| 30 | Natives and packaging on JVM | 20 | 10 | 4-row table, 107 words | 60 (45–80) |
| 31 | Scala Native | 41 (half is a to-do) | 21 | 3 dense rows | 55 (40–75) |
| 32 | Scala.js | 26 | 14 | 2 rows | 40 (30–55) |
| 33 | What we still haven't fixed | 16 | 8 | 9 bullets | 55 (40–75) |
| | **Subtotal** | | | | **4:50 (3:30–6:30)** |

### "So what do I have today?"

| # | Slide | Notes words | Notes time | Extra | Likely (low–high) |
|---|---|---|---|---|---|
| 34 | Divider | 0 | 0 | Transition | 10 (5–15) |
| 35 | SGE: generated vs left | 49 (half is a to-do) | 26 | 8-row number table, 211 words, the densest slide | 75 (50–100) |
| 36 | Plain translation vs conventions | 36 | 19 | Bar + 7 rows of numbers | 55 (40–75) |
| 37 | Less code to maintain | 123 | 64 | 3 PR images | 80 (65–100) |
| 38 | SSG: Java done | 27 | 14 | 9-row table | 55 (40–75) |
| 39 | multiarch-scala | 7 | 4 | 9 bullets | 40 (25–55) |
| 40 | Ready, or a stepping stone? | 9 (a stage note) | — | 2 columns, 9 lines | 40 (30–55) |
| | **Subtotal** | | | | **5:55 (4:15–7:55)** |

### Summary

| # | Slide | Notes words | Notes time | Extra | Likely (low–high) |
|---|---|---|---|---|---|
| 41 | Summary divider | 0 | 0 | — | 5 (5–10) |
| 42 | Porting with LLMs | 104 | 54 | 5 bullets; final pause | 65 (55–80) |
| 43 | Scala on every platform | 53 | 28 | — | 35 (30–45) |
| 44 | What works today | 73 | 38 | — | 45 (40–55) |
| 45 | An unexplored space | 73 | 38 | — | 45 (40–55) |
| 46–47 | Questions / Thank you | 0 | 0 | Outside the slot | 5 (5–10) |
| | **Subtotal** | | | | **3:20 (2:55–4:10)** |

### Section totals

| Section | Low | Likely | High | Share of likely |
|---|---|---|---|---|
| Intro | 1:05 | 1:20 | 1:45 | 3% |
| Why libGDX | 2:10 | 3:05 | 4:10 | 8% |
| Demo | 1:55 | 2:25 | 3:25 | 6% |
| Part I timeline + zooms | 8:55 | **12:15** | 15:55 | **32%** |
| re-scale / Baltic Porter | 3:50 | 5:25 | 7:00 | 14% |
| Part II | 3:30 | 4:50 | 6:30 | 13% |
| So what do I have today? | 4:15 | 5:55 | 7:55 | 15% |
| Summary | 2:55 | 3:20 | 4:10 | 9% |
| **Total** | **~28:00** | **~38:35** | **~50:50** | |

---

## 2. Structural problems that affect timing

- **The deck makes some points twice.** The dart-sass 20.7% and the method audit appear in the April zoom (12), in the slide 21 notes, and in slides 20–22. The certificate stamping, hollow bodies and reworded debt appear in the June/July zooms (14, 16), again in the slide 24 notes, and again in table 25. Whichever slide you say it on second costs time and adds nothing.
- **The four zoom slides share one note**, a legend ("Red dots… Blue diamonds… Purple bars…"). That legend needs saying once. The 6–8 events on each zoom have no prepared speech at all, which on stage leads to either reading the slide aloud or improvising, and improvising in a second language is slower.
- **Key terms are never introduced in the notes:** SGE, SSG, Fable, Opus, re-scale (until slide 24), Baltic Porter (named on slide 11 before it is explained), LWJGL3, GWT, AOT, IR, ABI, ETC1, R8/D8, aapt2, AAR, PanamaPort. Each one costs either a pause to explain it or the audience's attention.
- **Slide 9 ("This demo is deceptive") has no notes**, but it is the hinge of the whole talk. It needs 2–3 prepared sentences.
- **Several "notes" are author memos, not speech** (see section 3c). Read aloud by mistake, they cost time and confuse the audience.

---

## 3. Notes that are not speakable as written

### 3a. Too long or dense to say calmly

| Slide | As written | Speakable rewrite |
|---|---|---|
| 2 | "This gave me some insight into how macros are working and about metaprogramming in Scala in general, which resulted in several presentations, a blog post, and recently a new library." | "That taught me a lot about macros. *(pause)* It led to several talks, a blog post, and recently a new library." |
| 2 | "During all that time I have also been learning about functional programming and sharing what I learned, how JVM works, how to make it performant, how to make Scala approachable to other programmers." | "I also like sharing what I learn: about functional programming, about the JVM, and about making Scala approachable." |
| 6 | "libGDX's Gradle setup packages desktop apps for every OS from one machine, builds and shrinks Android apps, and AOT-compiles for iOS. Moving to sbt and Scala-first backends means porting those plugins too: none of it existed for Scala, so it all had to be built (Part II)." | "It's not only the runtime. With Gradle, libGDX can package a desktop app for every system from one laptop. It can build and shrink Android apps. It can compile for iOS. *(pause)* For Scala and sbt, none of that existed. So I had to build it. More on that in Part Two." |
| 11 | "SGE was begun in 2025-07 with Cursor and resumed with agents on 02-24; on 03-30 the same approach starts SSG, and SSG's first honest measurement (04-07) is what exposes the lying." | "I started SGE, my Scala port of libGDX, last July. In late February I picked it up again, this time with agents. At the end of March I started a second project, SSG, the same way. *(pause)* A week later I measured SSG honestly for the first time. That is where the lying showed." |
| 26 | "Its own first output had the same bug classes as the agents' (dropped breaks, == as identity, discarded anonymous classes), but running the tests caught them." | "Its first output had the same bugs the agents made: a dropped break, a wrong equality. *(pause)* The difference: the tests caught them." |
| 27 | "The difference from re-scale: these were caught, because the oracle is running tests and every count is computed by the tool, not reported by an agent. The limit is coverage, not honesty." | "Agents still tried to cheat. But this time we caught it. The tests decide, and the tool does the counting, not the agent. *(pause)* The limit now is test coverage, not honesty." |
| 29 | "One C ABI shared by every runtime: Panama on the JVM (and PanamaPort on Android), @extern on Scala Native. JNI is gone entirely (04-04)." | "Every native library has one C interface. The JVM calls it through Panama, Android through a backport of Panama, Scala Native directly. *(pause)* No JNI anywhere." |
| 36 | "The plain translation alone already makes a valid port; two-thirds of the recorded decisions are SGE's design layered on top. Extensions show the same split (e.g. anim8 543 configured vs 93 universal; ecs 225 vs 123)." | "A plain translation already gives you a working port. But two thirds of the decisions are SGE's own design on top: Scala names, Nullable instead of null, opaque types. The extensions look the same." (Drop the anim8/ecs numbers.) |
| 42 | "It may look harder, but in practice it is much more reliable not to let the LLM do the whole migration: use it to develop a deterministic migration, and then run the deterministic system." | "Don't let the LLM do the migration. *(pause)* Let it build a tool that does the migration. Then run the tool. It sounds harder. In practice it is much more reliable." |
| 43 | "Scala as a language has the potential to natively support things that Java achieves through hacks, like RoboVM, an iOS-dedicated ahead-of-time compiler, or GWT, a Java-to-JavaScript compiler developed outside of the language." | "Java reaches iOS and the browser with hacks: a separate compiler for iOS, another for JavaScript. *(pause)* Scala can target these platforms natively." |
| 44 | "Perhaps it's only a matter of nobody pointing out that they could and should be solved, maybe even in a very easy way by leveraging existing solutions." | "Maybe nobody has pointed at them yet. *(pause)* Often the fix already exists somewhere. We just need to reuse it." |
| 45 | "They would use metaprogramming, macros, inline defs and specialization to write code that is perhaps less idiomatic for Scala, maybe closer to Java without runtime reflection, but which macro-optimises itself while keeping the code the programmer writes quite readable." (50 words, one sentence) | "These libraries would not be immutable FP. They would use macros and inline defs. *(pause)* Closer to Java, but without reflection. The code you write stays readable, and the compiler makes it fast." |

### 3b. Numbers and dates that are hard to say aloud

| Slide | As written | Say instead |
|---|---|---|
| 11, 12, 14, 16, 18 | "02-24", "03-30", "04-07", "06-10", "07-03"… | Month names only: "end of February", "early April", "mid-June". Leave the exact dates on screen. |
| 21 | "37.7% faithful, 25.8% simplified, 36.1% missing" | Move to slide 22 and say "about a third faithful, a quarter cut short, a third simply missing." |
| 21 | "20.7% (2,439 / 11,797)" (on screen) | "One test in five." |
| 37 | "#146 Baltic Porter integration (+7,950 / -115,453), #160 overrides 89 → 16 (+83 / -14,687), #153 … (+789 / -2,794)" | Cut the whole PR list. Say: "Three pull requests: about nine thousand lines added, a hundred and thirty thousand removed. Tests and demos still pass." |
| 35 | "575 files, 17,962 members", "2,102 / 1,595 / 1,604" | Say one number: "The libGDX core is fully generated. Five hand-written replacements." Leave the rest on screen. |
| 38 | "JVM 13,611 · JS 12,701 · Native 12,561" | "Over twelve thousand tests on every platform." |
| 30, 39 | "0.1.0 in April, 0.4.0 in July", "77 commits; 0.4.0 is the latest release" | "Released as multiarch-scala; four releases since April." |
| 18 | "47,006 bytes instead of 32,768", "~720 tests" | "anim8 wrote the wrong number of bytes, and its own test checked for the wrong number." |

### 3c. Author memos and stage directions, not speech (do not say these)

- Slide 5: "Click through the backends."
- Slide 7: "Pre-launch all three; keep a backup video." (A good checklist item. Move it off the speech line.)
- Slide 11: "Line heights are illustrative." Either drop it or say "The heights are not to scale."
- Slides 12/14/16/18: "(research/incidents.md)". Remove. "they stay after zooming out" is also a stage note.
- Slide 24: "(see the June zoom)" → "as we saw".
- Slide 31: "(scala-native#4800)" and "zig cross-compilation: confirm the credit for the original idea (probably Lorenzo Gabriele's Mill prototype)." This is a to-do. Resolve it before the talk, then say "The idea of cross-compiling with zig comes from <name>."
- Slide 35: "Caveat: at the time of the report several of these … were verified locally but not yet merged; check before the talk." A to-do, and the phrase "at the time of the report" sounds like an agent's report. Remove.
- Slide 38: "'Reference-only' means members with no counterpart…". The term is not on the slide, so this note explains nothing the audience can see. Delete. "An earlier engine-side figure claimed KaTeX was 85% translated" → "At one point the tool claimed KaTeX was 85% done. Really, almost nothing is."
- Slide 40: "This is the 'first iteration' point of the talk." A note to self. Replace it with real speech: "So: is it ready? For Java sources, almost. For everything else, it is a first step."

### 3d. Parentheses and abbreviations to expand or drop

- "(LWJGL3)", "RoboVM/MobiVM", "AOT": say "a native JVM library", "an iOS compiler for Java bytecode".
- "(Part II)", "(04-04)", "(07-29)", "(09-07)": drop all of them.
- "== as identity": unclear aloud. Say "comparing objects by reference instead of by value".
- "SGE", "SSG": introduce once, early (slide 9 or 11): "SGE, my Scala port of libGDX, and SSG, a static site generator."
- "Fable", "Opus 4.6/4.8/5/5.5": say once what these are ("Anthropic's models") and after that say "the model", not version numbers.

---

## 4. Where to cut (to land near 25:00)

Savings are against the likely estimate.

| # | Change | Saves |
|---|---|---|
| A | **Part I: keep the overview (11) and two zooms, not four.** Keep April (claims vs reality) and June (hollow bodies). Fold July's single best line ("10 out of 10 audits verified" → a whole subsystem missing) into one sentence on the return slide. Drop the September zoom or reduce it to one line on 19 ("even the old hand ports had cheated"). On each kept zoom, narrate at most 3 events; leave the others visible but unspoken. Say the purple Anthropic-incident bars once, in one sentence. | **4:00–5:00** |
| B | **Slides 20–22 vs April zoom: keep one.** Either keep 20–22 (strong visual) and remove dart-sass from the April narration, or cut 20–22. | 0:45 |
| C | **Merge 24 + 25.** Show the re-scale idea in one sentence, then table 25 with only 3 rows narrated (certificates, method list, scanner). Same for **26 + 27**: 3 bullets from 26, 2 rows from 27. | 2:00 |
| D | **Part II: merge 30, 31, 32 into one slide**, "A native library is just a dependency": provider JARs, a loader, cross-compiling with zig, assets embedded for Scala.js. Cut 33 to 3 items (no iOS, no Windows-on-ARM testing, no GPU in CI). | 1:45 |
| E | **"Today" section: replace table 35 with one headline** ("libGDX core: fully generated, 5 hand-written replacements; extensions: about 65 of 760 so far"). Keep 36 but read only the bar and the top 2 rows. Cut 39 (multiarch-scala). Its content has already been said in Part II. Shorten 38 to its last line. | 2:30 |
| F | Slide 6: reveal the table but speak only 2 rows (desktop from one host, Android). | 0:30 |
| G | Slide 37: drop the PR list from the speech (see 3b). | 0:20 |

**After A–G: likely ≈ 25:30–26:30, low ≈ 20, high ≈ 33.** That leaves the 30-minute hard limit as a real safety margin. If rehearsal still runs long, the next cut is slide 45 (merge with 44): about 40 s.

### Keep and protect (do not compress)

- Demo + slides 8–9: the hook of the talk.
- Slide 25's final line: "Every check was satisfied without doing the work."
- Slide 37's spoken part about trust: it is the most human, memorable part.
- Slide 42: the main takeaway.

---

## 5. Deliberate pauses (2–3 s, silent, look at the audience)

- After slide 8 "We're done, thank you!": let the laugh happen, then click.
- After the first bullet of slide 9: "I had a demo like this in March." Pause before "This is a different approach."
- Slide 21, after the bar drops to 20.7%: say nothing for 2 seconds. The slide does the work.
- Slide 25, after "satisfied without doing the work".
- Slide 37, after "I still have little trust in the numbers the AI reports about itself."
- Slide 42, after "Every LLM will mislead you", and again before the last bullet.
- Before each section divider (10, 23, 28, 34, 41): breathe, then click.

## 6. One-line transitions for slides with no notes

- **1 (Title):** "Hello. I'm Mateusz, and this is a report from the trenches: what it took to run Scala on every platform libGDX supports."
- **3 (Why port libGDX):** "First: why would anyone want libGDX in Scala?"
- **8 (We're done):** "…That's it. Thank you." *(pause)* "Well, not quite."
- **9 (Deceptive):** "I had a demo like this in March. What you just saw is not that demo. It's the first result of a completely different approach. And that approach needed tooling Scala doesn't have."
- **10 (Part I):** "Part one: how I tried to port a large library with AI agents, and how they lied to me."
- **13/15/17/19 (timeline returns):** one sentence each, naming the new label: "In May, a new model, and the certificates were stamped…" Then click. No more than that.
- **20 (Claimed):** "Here is what one agent told me in April."
- **23 (What was tried):** "So what did I do about it? Two things."
- **28 (Part II):** "Part two: the boring part that nobody had built: shipping Scala to every platform."
- **34 (Today):** "So where am I today?"
- **41 (Summary):** "Let me sum up."
- **46 (Questions):** "Thank you. Questions?"
