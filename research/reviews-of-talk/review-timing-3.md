# Timing & deliverability review (round 3)

Source: `audience-view-3.md` only. Talk: Scala Days 2026, "Scala's LibGDX: A Report from the Trenches", 30-min slot, target ~25 min of content.

## 1. Bottom line

| Scenario | Total | vs 25:00 target | vs 30:00 slot |
|---|---|---|---|
| Low (120 wpm, short cues, demo 90 s) | **25:12** | +0:12 | −4:48 |
| Likely (115 wpm, demo 105 s) | **28:55** | **+3:55** | −1:05 |
| High (110 wpm +5%, long cues, demo 135 s) | **35:09** | +10:09 | **+5:09** |

Spoken words: 2,288 across 40 slides, with 150 clicks and 35 pauses.

**Verdict: over. Cut about 4 minutes.** Even the best case only just reaches 25 minutes. The likely case leaves about 1 minute for questions and no buffer for the demo. In the high case (a slow speaker, a demo hiccup, the audience reading the timeline and tables) the talk runs 5 minutes past the slot. Part I (slides 10–23) takes about 11 minutes and is where the time goes. The five annotated timeline slides and the two "check vs. how it was beaten" tables tell much of the same story twice.

Section subtotals (low / likely / high):

| Section | Slides | Words | Low | Likely | High |
|---|---|---|---|---|---|
| Opening + demo | 1–9 | 472 | 6:18 | 7:09 | 8:39 |
| Part I: Porting with agents | 10–23 | 945 | 9:36 | 10:58 | 13:17 |
| Part II: Shipping cross-platform | 24–27 | 296 | 3:04 | 3:32 | 4:20 |
| Where I am today | 28–33 | 319 | 3:32 | 4:09 | 5:08 |
| Summary + close | 34–40 | 256 | 2:43 | 3:08 | 3:46 |

## 2. Method

- Spoken words were counted per slide from the speaker notes, after removing `(click)` and `(pause)`. Any token containing a letter or digit counts as one word.
- Speech rate is 120 / 115 / 110 wpm (low / likely / high). In the high case speech time gets +5% for restarts and self-corrections.
- Each click adds 1 / 1.5 / 2 s and each pause 2 / 2.5 / 3 s. Each slide transition adds 1 / 1.5 / 2 s.
- Dense slides get extra audience reading time. Each slide has a reading budget of 3–20 s: 20 s for the big tables and the fully annotated timelines (6, 15, 17, 22, 23, 26), 15 s for the medium tables and the final timeline (20, 25, 32), 10 s for 5, 29, 30, 33, and about 5 s for bullet slides. 0.25× / 0.5× / 1× of that budget is added.
- The demo adds 90 / 105 / 135 s on top of its spoken lines.
- Slides 39–40 (Questions / links) are counted at about 6–11 s. Q&A itself is not counted.

## 3. Per-slide timing (seconds)

W = words, C = clicks, P = pauses, R = reading budget (s).

### Opening + demo
| # | Slide | W | C | P | R | Low | Likely | High |
|---|---|---|---|---|---|---|---|---|
| 1 | Scala's LibGDX | 31 | 0 | 1 | 0 | 18 | 20 | 23 |
| 2 | About me | 64 | 0 | 1 | 5 | 36 | 40 | 47 |
| 3 | Why port libGDX to Scala? | 26 | 0 | 1 | 0 | 16 | 18 | 20 |
| 4 | What libGDX gives you | 49 | 0 | 1 | 5 | 29 | 32 | 38 |
| 5 | …and what you keep in Scala | 86 | 5 | 1 | 10 | 54 | 61 | 74 |
| 6 | The build tooling goes too | 105 | 5 | 1 | 20 | 66 | 76 | 95 |
| 7 | Demo (incl. 90/105/135 s demo) | 35 | 0 | 1 | 0 | 110 | 127 | 160 |
| 8 | We're done, thank you! | 11 | 0 | 1 | 0 | 8 | 10 | 11 |
| 9 | This demo is deceptive | 65 | 3 | 2 | 0 | 40 | 45 | 51 |

### Part I: Porting with agents
| # | Slide | W | C | P | R | Low | Likely | High |
|---|---|---|---|---|---|---|---|---|
| 10 | Part I title | 19 | 0 | 0 | 0 | 10 | 11 | 13 |
| 11 | Claimed vs measured (283/283) | 39 | 0 | 0 | 5 | 22 | 24 | 29 |
| 12 | Claimed vs measured (20.7%) | 15 | 0 | 1 | 0 | 10 | 12 | 14 |
| 13 | Claimed vs measured (method split) | 34 | 0 | 1 | 5 | 21 | 24 | 29 |
| 14 | Eight months (Feb–Apr) | 81 | 4 | 1 | 5 | 49 | 55 | 64 |
| 15 | April: the files were "done" | 141 | 7 | 0 | 20 | 84 | 96 | 117 |
| 16 | Eight months (May–Jun) | 39 | 3 | 1 | 5 | 27 | 31 | 38 |
| 17 | June: bodies hollow | 132 | 7 | 0 | 20 | 79 | 91 | 112 |
| 18 | Eight months (late Jun) | 56 | 2 | 1 | 5 | 34 | 39 | 46 |
| 19 | Quote: non-deterministic | 69 | 0 | 2 | 0 | 40 | 42 | 48 |
| 20 | Eight months (Jul–Oct) | 93 | 5 | 1 | 15 | 58 | 68 | 83 |
| 21 | What was tried? | 21 | 0 | 0 | 0 | 12 | 12 | 14 |
| 22 | re-scale: checked / beaten | 91 | 5 | 1 | 20 | 58 | 69 | 87 |
| 23 | Baltic Porter: does / slipped | 115 | 6 | 1 | 20 | 72 | 83 | 103 |

### Part II: Shipping cross-platform Scala
| # | Slide | W | C | P | R | Low | Likely | High |
|---|---|---|---|---|---|---|---|---|
| 24 | Part II title | 22 | 0 | 1 | 3 | 15 | 17 | 21 |
| 25 | What still needs native code | 106 | 5 | 1 | 15 | 65 | 74 | 91 |
| 26 | A native library is just a dependency | 117 | 5 | 1 | 20 | 72 | 83 | 102 |
| 27 | What we still haven't fixed | 51 | 5 | 0 | 5 | 33 | 38 | 46 |

### Where I am today
| # | Slide | W | C | P | R | Low | Likely | High |
|---|---|---|---|---|---|---|---|---|
| 28 | So what do I have today? | 6 | 0 | 1 | 0 | 6 | 7 | 8 |
| 29 | SGE: generated / left | 47 | 4 | 0 | 10 | 31 | 37 | 47 |
| 30 | Plain translation vs conventions | 49 | 4 | 1 | 10 | 34 | 41 | 51 |
| 31 | Less code to maintain | 76 | 4 | 1 | 5 | 46 | 52 | 62 |
| 32 | SSG: Java done | 63 | 5 | 1 | 15 | 43 | 52 | 66 |
| 33 | Ready, or a stepping stone? | 78 | 7 | 1 | 10 | 52 | 60 | 74 |

### Summary + close
| # | Slide | W | C | P | R | Low | Likely | High |
|---|---|---|---|---|---|---|---|---|
| 34 | Summary | 4 | 0 | 0 | 0 | 3 | 4 | 4 |
| 35 | Porting with LLMs | 83 | 5 | 2 | 5 | 53 | 60 | 71 |
| 36 | Scala on every platform | 53 | 2 | 1 | 5 | 33 | 37 | 44 |
| 37 | What works today | 52 | 4 | 1 | 5 | 34 | 40 | 48 |
| 38 | An unexplored space | 61 | 3 | 0 | 5 | 36 | 40 | 48 |
| 39 | Questions? | 3 | 0 | 0 | 0 | 2 | 3 | 4 |
| 40 | Thank you! (links) | 0 | 0 | 0 | 5 | 2 | 4 | 7 |
| | **Total** | **2,288** | **150** | **35** | | **1,512 (25:12)** | **1,735 (28:55)** | **2,109 (35:09)** |

## 4. Speakability issues

| Slide | Quote / issue | Fix |
|---|---|---|
| 11 | "Every file, two hundred eighty-three of them." A long number that is hard to say, and the audience reads "283/283" faster than you can say it. | "Every single file." The screen already shows 283. |
| 13 | The screen shows 37.7 / 25.8 / 36.1 while you say "about a third / a quarter / a third". That is good. But a "third" and a "third" for 37.7 and 36.1 sounds like a slip. | "About a third faithful, a quarter cut short, and a third, *more than* a third, missing", or just "over a third missing". |
| 14 | "checked method by method: one file 6% ported" and "Opus 4.6" are on screen but never mentioned. The audience will wonder what the 6% file is. | One clause: "…one file turned out to be six percent ported." Or remove the label. |
| 15 | "(click) (click) In purple: Anthropic later admitted that Claude Code gave the model less reasoning in those weeks, and that usage was throttled at peak hours." This is a 27-word sentence with "admitted that … and that …". It is hard to say in one breath, and the on-screen annotation is longer still (it adds the "forget its earlier reasoning" bug). | Split it: "In purple: the model got less reasoning by default. Anthropic admitted it later. And usage was throttled at peak hours." |
| 15 | The notes read the on-screen annotations almost word for word: "Is each file about as long as the original? Does it have the same methods? Any TODOs or stubs?" and "A colour library at a fifth of its original size, with no TODO anywhere." | Let the screen carry the detail. Say "So I added checks: length, methods, TODOs. And put them in CI with a tool, re-scale." |
| 16 | "Opus 4.8" label is never mentioned. "Through May the claims stayed high" has a click but nothing new appears on screen. | Drop the Opus 4.8 label, or drop that click. |
| 17 | "the line that moves to the next letter was commented out" while the screen shows `// gx += xAdvances[ii]`. That is fine, but "Every letter drawn in the same place" is a sentence with no verb, so say it with emphasis. Two clicks fire together for the purple items, then two facts follow in one 30-word run. | Same as on slide 15: shorten the purple part to "And Fable could be silently swapped for Opus, then was switched off for three weeks. Opus reviewed Opus." |
| 18 | "Tests that only tested the standard library." The tested/tested repetition is a mini tongue-twister. | "Tests that only checked the standard library." |
| 19 | The on-screen quote shows "non-deterministic.me, mid-July". The attribution is glued onto the quote, so it reads as a domain name. "non-deterministic" and "deterministic" are hard words for a non-native speaker at a slow pace. The talk uses them three times in a row here. | Fix the slide layout (a line break or em dash before "me, mid-July"). Practise the word, or say "A translator gives the same output every time" instead of "is deterministic". |
| 19 | "Every check I added, the agents learned to get past." The fronted object is awkward to say. | "The agents learned to get past every check I added." |
| 20 | The screen shows Opus 5, Fable 5.1, Opus 5.5, "Opus 5: uneven quality" and "less reasoning than selected". None of these labels is mentioned. This is the densest slide of the deck with 15 s of reading. | Either say one purple sentence or remove the unmentioned labels. Fewer labels also shortens the reading time. |
| 20 | "In September, comparing with the translator's output showed that the old agent ports were even worse than the reviews had found." A gerund subject followed by a nested clause is hard to say. | "In September, the translator's output showed the old ports were even worse than we thought." |
| 22 | Clicks don't match the notes: there are 5 clicks for 5 rows, but rows 4 (the TODO scanner, "reworded their comments") and 5 (the review by a different model, "invented 3 of its 5 findings") are revealed by a silent "(click) (click)". The TODO-rewording row has the best anecdote and is never said aloud. Rows 1–3 repeat slides 15/17 almost word for word ("twelve hundred files complete in one go, and turned the check into a warning" is said for the 3rd time). | Say rows 1–3 in one sentence ("You've seen these: bulk marking, hollow bodies, size that lies."), then say the scanner row: "They even reworded comments until the TODO scanner stopped finding them." |
| 23 | The "rules are code too, so they need review" cell is never mentioned. "Another switched off twenty-eight test suites": the screen also says "another switched off 23 tests". Two similar numbers (28 and 23) sit next to each other on screen. | Fine to leave unsaid, but consider dropping the 23 from the slide. |
| 25 | Acronym-heavy run: "ANGLE, Google's OpenGL implementation. Panama is Java's new way to call C. … GLFW and miniaudio." "GLFW" is four letters to spell out. The table's "@extern", "WebGL", "WASM" and FreeType's browser "none" are never mentioned. Five clicks, one per row, for a table the audience reads faster than you speak. | Summarise: "Graphics, windows, audio, fonts, physics: each became one native library with one C interface." Keep the Rapier/WASM point and "No JNI anywhere." |
| 26 | Mostly reads out the right-hand column of the table. | Fine to keep, but at a slow pace this is the second-longest slide in Part II. Trimming the JVM and Native rows into one sentence saves about 15 s. |
| 29 | "About six hundred ninety extension files": a number that is awkward to say aloud. | "About seven hundred extension files" (the screen already says ~690). |
| 30 | On screen: "3,710 / 1,083 / 398 / 282" (plus the screen glues each number to its label, "3,710getX()"). The speaker says none of the numbers, which is good. But four clicks, each a 2–3 word fragment ("(click) Scala-style names. (click) Nullable instead of null."), give a click-click-click rhythm. | Reveal all four rows in one click, or say one sentence over the reveals. Fix the missing space after each number on the slide. |
| 31 | "About nine thousand lines added, a hundred and thirty thousand removed." The screen says −133k, and the PR images add up to 132,936. The speaker rounds down in one place but up in another (8.8k → nine thousand). That is acceptable, but "a hundred and thirty thousand" is a mouthful. | "Nine thousand lines in, a hundred thirty thousand out." |
| 33 | Clicks don't match the fragments: the screen has 8 fragments after the first heading (4 Java sub-items, the TS/Dart/Ruby heading, and 3 sub-items), but the notes have 7 clicks. The "KaTeX, terser, rough.js, Sass, Mermaid, the minifier" line has no matching beat. Also, the whole slide repeats slides 29 and 32. | Either add a click with "The same libraries as on SSG's slide", or reveal the heading and the list together. Better still, see cut C6. |
| 36 | "Java needs a separate, external compiler for each. iOS is still missing for Scala, but that's one missing piece, not a missing approach." "missing piece, not a missing approach" is a nice line but tongue-twisty when said slowly. | Rehearse it, or say "one missing piece, not a missing idea". |
| 38 | "specialization" on screen is never mentioned. "optimises" (on screen) vs. "makes it fast" (spoken) is fine. | Drop "specialization" from the slide or name it. |
| 2 | Slide lists Hearth, Kindlings, Kubuszok.com and the JVM article. The notes say "two new libraries" and "a blog post" without names. That is fine, but the notes are a paraphrase of a list the audience is already reading. | Shorten (see cuts). |

## 5. Suggested cuts (target: about −240 s from the likely case)

| # | Cut | Saves (likely) |
|---|---|---|
| C1 | **Slide 22 (re-scale table):** don't retell rows 1–3, which the audience saw on the timeline 3 minutes earlier. Keep one sentence for those rows, the TODO-rewording anecdote, and the "names, words, counts — never behaviour" pattern. Alternatively, delete the slide and say the pattern line on slide 21. | 30 s (55 s if deleted) |
| C2 | **Slides 15 + 17 (annotated timelines):** cut the purple Anthropic narration down to one short sentence each, and stop reading the check list and anecdotes verbatim. Also remove the 03-23 throttling annotation. | 40 s |
| C3 | **Slide 20:** remove the unmentioned model/purple labels (fewer to read). Shorten the September sentence. | 20 s |
| C4 | **Slide 25:** replace the five row-by-row clicks with one summary sentence plus Rapier/WASM and "No JNI anywhere". | 30 s |
| C5 | **Slide 2 (About me):** two sentences ("Scala for 12 years, Chimney for 9; that got me into macros and talks."). | 15 s |
| C6 | **Slide 33 (Ready or stepping stone?):** it repeats slides 29 and 32. Keep only the two headings ("Java: almost ready, no release yet" and "TS/Dart/Ruby: a first step") plus the "deceptive demo" callback, and drop the 7-click reveal. | 35 s |
| C7 | **Slide 30:** one click and one sentence ("names, Nullable, opaque types, a context: two thirds of the changes are my design"). | 15 s |
| C8 | **Slide 26:** merge the JVM and Scala Native rows into one sentence. | 15 s |
| C9 | **Slide 23:** drop the "rules" click (slide 30 covers the rules) and merge "another patched by hand" into the previous line. | 10 s |
| C10 | **Slide 27:** read the two headings and only the iOS item; let the audience read the rest. | 15 s |
| C11 | **Demo:** script it to a fixed 90 s (pre-launch all three targets, pre-arrange the windows, no live builds). The high case assumes 135 s. | 15 s likely / 45 s high |

C1–C10 save about 225 s in the likely case, which brings it to about 25:10. Adding C11 brings it to about 24:55. In the high case the same cuts bring the talk to about 30:30. To be safe even in the high case, also delete slide 22 entirely (+25 s) and merge slides 11–13 into a single slide with three reveals (about 10 s from fewer transitions and less re-reading).

Do not cut the fake ending (slide 8, 10 s) or the quote slide (19). They are cheap, and they turn the talk from the demo to the story.
