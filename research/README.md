# Research for the talk

Evidence collected on 2026-10-06 from the git history of sge, ssg, balticporter, re-scale, lls, multiarch-scala and the native-provider repos, Claude Code prompt history, session transcripts and memory. Every claim in the reports cites a commit hash, a file path or a dated prompt.

Rendered overview (timeline, models, reviews, coverage, size-ratio heuristic, cheating episodes, talk plan): `talk-timeline.html`, also published at https://claude.ai/artifact/9oVrnkEbcwKUJ3cwrAyGRa

| File | Contents |
|---|---|
| `sge.md` | SGE timeline, progress claims, cheat discoveries, re-scale, native/CI pain points |
| `ssg.md` | SSG timeline, progress claims, C1–C16 cheat catalogue, Baltic Porter adoption |
| `rescale-balticporter.md` | Why each re-scale feature exists, why it failed, Baltic Porter phases, current coverage buckets |
| `models.md` | Which model when, why it stopped, the Fable 5 availability story, public release dates (with URLs) |
| `lls.md` | Low Level Scala: extraction, releases, Baltic Porter regeneration, tooling gaps |
| `natives-multiarch.md` | LibGDX native code → SGE replacements, multiarch-scala, what is still missing |
| `coverage.md` | How much was really ported (claimed vs measured), missing APIs, hollow method bodies |
| `coverage-issues.md` | Issue-database census of missing-member vs body-level defects |
| `coverage-scrapped.md` | Claims and findings that were later deleted or rewritten |
| `cheating-pressure.md` | "Wrap up" pressure (or the lack of it), worst cheating episodes, correlations |
| `reviews/` | Copies of every review/audit document, including deleted ones |
| `deleted/` | Deleted status/progress/audit docs, read at their last version; `removed-lines.txt` |
| `sge-log.txt`, `ssg-log.txt`, `prs.json`, `stats-daily.txt` | Raw logs and per-day model token usage |
| `scripts/`, `upstream-lists/` | Line-count script and the upstream file lists used for size ratios |
| `raw/` | **Private, git-ignored:** the full prompt log, transcript phrase hits, recorded system prompts |

Caveats: local Claude Code history before 2026-06-18 was wiped; transcripts survive from 2026-07-28; commits never name a model. Size ratios are raw line counts; issue counts are keyword-classified (±25%).
