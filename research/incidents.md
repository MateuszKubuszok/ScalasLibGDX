# Claude / Claude Code reliability incidents, Feb–Oct 2026

Research for the talk timeline. Window: 2026-01-01 .. 2026-10-07, with late-2025 precedent marked separately.
Compiled 2026-10-07.

**Confidence labels**
- **OFFICIAL**: confirmed by Anthropic (engineering blog, status page, support article, Claude Code CHANGELOG, or a named Anthropic employee speaking publicly).
- **COMMUNITY**: GitHub issues, Reddit, HN, X, or third-party benchmarks. Anthropic has not confirmed it, or has disputed it.
- **PRESS**: secondary reporting only. I could not reach a primary source.

Claude Code release dates come from the npm registry publish times of `@anthropic-ai/claude-code`. The CHANGELOG has no dates, so I mapped each version to its npm publish date.

## Model release reference (from CHANGELOG + npm dates)

| Date | Model (Claude Code version) |
|---|---|
| 2026-02-05 | Opus 4.6 (2.1.32) |
| 2026-04-16 | Opus 4.7 (2.1.111), new `xhigh` effort |
| 2026-05-28 | Opus 4.8 (2.1.154), "defaults to high effort" |
| 2026-06-09 | Fable 5 (2.1.170) |
| 2026-06-30 | Sonnet 5 (2.1.197), becomes default model |
| 2026-07-24 | Opus 5 (2.1.219) |
| 2026-09-01 | Fable 5.1 (2.1.257) |
| 2026-09-22 | Opus 5.5 (2.1.280) |
| 2026-09-28 | Sonnet 5.5 (2.1.284) |

## Timeline table

| Date / range | Item | Impact | Status |
|---|---|---|---|
| *2025-08-05 .. 09-18 (precedent)* | Three infrastructure bugs (context-window misrouting, TPU output corruption, XLA top-k miscompile) degrade Sonnet 4 / Opus 4.x / Haiku 3.5 | Up to 16% of Sonnet 4 requests at peak; random wrong-language tokens | OFFICIAL postmortem, 2025-09-17 |
| *2025-08-28 (precedent)* | Weekly usage limits introduced on Pro/Max | Weekly caps for heavy users from then on | OFFICIAL (well known; not re-verified here) |
| 2026-01-26 .. 01-28 | Claude Code harness problem degrades Opus 4.5. MarginLab SWE-Bench-Pro tracker drops 8% day-over-day; fixed by rollback | Coding pass rate drop for ~2 days | OFFICIAL (Thariq Shihipar statement) + tracker data |
| Feb 2026 (Opus 4.6 launch, 02-05) | Adaptive thinking becomes default. Thinking redaction header `redact-thinking-2026-02-12` rolls out 03-05 .. 03-12 | Users see less or no thinking. AMD analysis claims thinking depth fell 67% | Redaction: OFFICIAL, said to be "UI-only". Depth drop: COMMUNITY |
| 2026-03-04 .. 04-07 (Max/Team until 04-21) | **Default effort lowered high → medium** for Opus 4.6 / Sonnet 4.6 in Claude Code (2.1.68) | Less reasoning by default; "dumber/lazier" reports start ~03-08 | OFFICIAL (postmortem; reverted 2.1.94 on 04-07, 2.1.117 on 04-21 for Pro/Max) |
| 2026-03-06 .. 03-12 | Agent-tool `model` parameter silently ignored, so subagents run on the parent model (2.1.69–2.1.70) | Model tiering in multi-agent pipelines broken | COMMUNITY issue #31311, fixed in 2.1.72 |
| 2026-03-09 | Effort scale simplified to low/medium/high and **`max` removed** (2.1.72). `xhigh` added 04-16 | Effort semantics changed under users | OFFICIAL (CHANGELOG) |
| ~2026-03-23 .. 05-06 | **Peak-hour throttling**: 5-hour limits reduced on weekdays 5–11am PT. Users also hit limits "way faster than expected"; cache-bug claims | ~7% of users hit new session limits (Anthropic) | OFFICIAL (Reddit post by Anthropic; "top priority" statement) |
| 2026-03-26 .. 04-10 | **Thinking-cache bug**: thinking history cleared on *every* turn after an idle session, instead of once (fixed 2.1.101) | Claude "forgetful, repetitive" for the rest of the session | OFFICIAL (postmortem) |
| 2026-04-02 .. 04-06 | AMD's Stella Laurenzo files #42796 ("unusable for complex engineering tasks"): read:edit ratio 6.6 → 2.0 | Biggest public data-backed complaint | COMMUNITY. Anthropic replied (redaction is UI-only); workaround `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1` |
| 2026-04-16 | Opus 4.7: new tokenizer (~1.0–1.35x more tokens, more in some reports), refusal complaints | Usage limits burn faster at the same price | Tokenizer: OFFICIAL. Backlash: PRESS/COMMUNITY |
| 2026-04-16 .. 04-20 | **Verbosity-limiting system prompt** hurts coding (−3% on an eval for Opus 4.6 and 4.7); reverted in 2.1.116 | Quality drop | OFFICIAL (postmortem) |
| **2026-04-23** | **Anthropic postmortem "An update on recent Claude Code quality reports"**; usage limits reset for all subscribers | Admits that three harness changes caused 7 weeks of degradation | OFFICIAL |
| Apr–Jun 2026 | Subagent `model:` frontmatter pin silently ignored (#44385, #52681 on 2.1.117, #54448) | Pinned subagent model not honoured | COMMUNITY |
| 2026-05-06 / 05-13 | Peak throttle removed, 5-hour limits doubled (05-06); weekly limits +50% promo starts (05-13) | Relief for heavy users | OFFICIAL (support article) |
| 2026-06-09 .. 06-11 | Fable 5 ships with **invisible "frontier-LLM" safeguards** that silently degrade answers; reversed 06-11 with an apology | Silent quality cut on ML-related work | OFFICIAL (Anthropic reversal) |
| 2026-06-10 → ongoing (still reported 10-02) | **Safety-classifier fallback Fable → Opus 4.8**: sticky for the whole session, sometimes silent, drops thinking blocks, `switchModelsOnFlag:false` reportedly bypassed (27/133 pinned agents switched in one run) | Pinned model not honoured; context loss; benign infra/security work flagged | Fallback mechanism: OFFICIAL. Silent path and opt-out bypass: COMMUNITY (#66822, #67246, #98875) |
| **2026-06-12 → 07-01** | **Fable 5 / Mythos 5 suspended** under a US Commerce export-control order (received 17:21 ET 06-12). Order lifted 06-30; Fable back 07-01 | Fable unavailable for ~19 days | OFFICIAL / PRESS |
| 2026-07-01 → 07-19 | Fable subscription promo: to 07-07, extended to 07-12, then to **07-19 23:59:59 PT**. From 07-20, Max gets Fable at up to 50% of weekly limits; Pro moves to usage credits | Capacity and cost changes for Fable users | OFFICIAL (support article) |
| 2026-06-30 / 07-01 | Claude Code found to **steganographically mark system prompts** (apostrophe variants, date format) | Trust issue; no quality impact shown | COMMUNITY (HN 2,444 pts), widely reported |
| 2026-07-24 | Opus 5 launches; Claude Code system prompt cut by >80% for Claude-5-generation models | Behaviour change for prompts and pipelines tuned on 4.x | OFFICIAL (Thariq) |
| 2026-07-29 .. Aug | "Opus 5 nerfed / lazy / spiky" reports (#82162 etc.); Thariq: "Opus 5 is a really spiky model … huge priority" | Inconsistent quality | Partially OFFICIAL (acknowledged spikiness) |
| 2026-08-05, 08-17/18, 08-24 | Status incidents: elevated errors on Opus 5 / Sonnet 5 / multiple models (42 min – ~7 h; three outages on 08-24) | Failed requests, not quality | OFFICIAL (status page) |
| 2026-08-14 | Todo/Task tools removed for Opus 4.8, Sonnet 5, Fable 5 and newer (2.1.233) unless `CLAUDE_CODE_ENABLE_TODO_TOOLS=1` | Workflow change | OFFICIAL (CHANGELOG) |
| **~2026-08-19 → ? (still seen 09-20)** | **EFFORT-SCALE A/B EXPERIMENT**: from Claude Code 2.1.236/237, Fable 5 sessions at "high" get `<reasoning_effort>10</reasoning_effort>`, which was the old value for "low". The model itself reads 10 as "low / minimal thinking". Exposed 08-22 | Users see Fable "dumber". Anthropic says the effort is unchanged and only the number mapping differs. Priming risk raised in #88949 | Experiment: OFFICIAL (Thariq on X/HN). Quality impact: disputed. No rollback announced |
| Aug–Sep 2026 | Effort silently applied lower than the setting shows (#88842 settings `high` → sent `low`; #89080 `xhigh` → `high`); default-effort "hold" for Opus 4.7/4.8/Fable 5 overrides user/project/`-p` settings until 2.1.280 (09-22); `effort:` frontmatter on subagents/skills ignored until 2.1.267 (09-09) | Configured effort not applied in pipelines | Hold and frontmatter fixes: OFFICIAL (CHANGELOG). Mismatch reports: COMMUNITY |
| 2026-09-13 / 09-14 | Weekly +50% promo ends; from 09-14 limits settle at +25% over the pre-promo baseline | Effective weekly capacity drops ~17% vs the promo | OFFICIAL (support article) |
| 2026-09-22 .. | Opus 5.5 "nerfed" claims within days of launch; no tracker evidence yet (MarginLab baseline phase; NerfBench 99.2%) | Perception | COMMUNITY, unverified |
| 2026-09-23 | Anthropic's Jackson Kernion: writing quality worse since Opus 4.6 (optimised for machine-readable prose) | Acknowledged style regression across 4.7–5 | OFFICIAL-ish (employee statement, via press) |

---

## Details and sources

### Precedent (late 2025, outside the window)

**Aug–Sep 2025: three infrastructure bugs (OFFICIAL).**
- Context-window routing error, 08-05 .. 09-18: short requests sent to 1M-context servers. At the worst hour (08-31), 16% of Sonnet 4 requests were affected.
- TPU output corruption, 08-25 .. 09-02: random Thai or Chinese characters appeared in English output (Opus 4/4.1, Sonnet 4).
- XLA:TPU approximate top-k miscompile, 08-25 .. 09-12: Haiku 3.5, possibly Sonnet 4 and Opus 3.

Anthropic wrote: "We never reduce model quality due to demand, time of day, or server load."
- https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues
- https://status.claude.com/incidents/72f99lh1cj2c

### 1. Jan 26–28, 2026: Claude Code harness regression on Opus 4.5 (OFFICIAL)

MarginLab's daily SWE-Bench-Pro tracker showed Claude Code + Opus 4.5 down 8.0% day-over-day and 4.1% month-over-month, which was statistically significant. Codex showed no change over the same period. Thariq Shihipar said they hit a harness problem on Jan 26, found it on Jan 28, and rolled it back.
- https://gigazine.net/gsc_news/en/20260130-claude-code-opus-performance/
- https://marginlab.ai/trackers/claude-code

### 2. March 4 – April 20, 2026: the big one (OFFICIAL postmortem, 2026-04-23)

"An update on recent Claude Code quality reports" covers Claude Code, the Agent SDK and Cowork. The API was not affected. It names three causes:

1. **Default reasoning effort high → medium**, introduced 03-04 (CHANGELOG 2.1.68: "Opus 4.6 now defaults to medium effort for Max and Team subscribers… sweet spot").
   - Reverted 04-07 in 2.1.94 for API, Team and Enterprise users.
   - Reverted 04-21 in 2.1.117 for Pro/Max ("Default effort for Pro/Max subscribers on Opus 4.6 and Sonnet 4.6 is now `high`").
   - Anthropic called it the wrong tradeoff.
2. **Thinking-history cache bug**, introduced 03-26 and fixed 04-10 in 2.1.101. Instead of clearing old thinking once after an idle session, it cleared it on every turn for the rest of the session, so Claude became forgetful and repetitive.
3. **Verbosity-reduction system prompt**, added 04-16 and reverted 04-20 in 2.1.116. It cost 3% on an eval for both Opus 4.6 and 4.7.

Anthropic reset usage limits for all subscribers on 04-23 and credited `/feedback` reports. The HN thread on the postmortem reached ~942 points and 732 comments (per secondary sources).
- https://www.anthropic.com/engineering/april-23-postmortem
- https://simonwillison.net/2026/Apr/24/recent-claude-code-quality-reports/
- https://smartscope.blog/en/blog/claude-code-quality-degradation-postmortem-2026/

**Related: the AMD report (COMMUNITY, with an Anthropic reply).**
- Issue #42796 ("Claude Code is unusable for complex engineering tasks with the Feb updates") was opened 2026-04-02 by Stella Laurenzo (AMD).
- It analysed 6,852 sessions, 17,871 thinking blocks and 234,760 tool calls.
- Findings: estimated thinking depth −67%; reads per edit 6.6 → 2.0; stop-hook "laziness" violations 0 → 173 after 03-08; 80x more API requests.
- Boris Cherny's pinned reply (04-06): the `redact-thinking-2026-02-12` header is UI-only and does not affect thinking budgets. Opt out with `showThinkingSummaries: true`.
- Secondary sources say Cherny also acknowledged that adaptive thinking could allocate zero reasoning on some turns, and suggested `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1`. That comes from press and HN, and I did not verify it on GitHub.
- https://github.com/anthropics/claude-code/issues/42796
- https://www.theregister.com/2026/04/06/anthropic_claude_code_dumber_lazier_amd_ai_director/
- https://pasqualepillitteri.it/en/news/805/claude-code-effort-adaptive-thinking-guida

**Third-party benchmark (COMMUNITY, low weight).** BridgeBench re-test of Opus 4.6 on 04-13: 68.3%, down from 83.3%.
- https://www.contextstudios.ai/blog/claude-opus-46-ralentit-et-opus-47-arrive

### 3. Usage-limit and capacity changes

- **Peak-hour throttling, from about the week of 03-23 (OFFICIAL).** Anthropic confirmed in a Reddit post that 5-hour limits are reduced on weekdays 5–11am PT, with weekly limits unchanged. It said about 7% of users would hit new limits. A 2x off-peak promo ended 03-28.
  - Around 03-31, Anthropic said users were "hitting usage limits in Claude Code way faster than expected… top priority".
  - A user claimed two prompt-cache bugs inflated costs 10–20x. Thariq replied: "not sure it's real yet".
  - https://pcworld.com/article/3100787/anthropic-confirms-its-been-adjusting-claude-usage-limits.html
  - https://www.devclass.com/ai-ml/2026/04/01/anthropic-admits-claude-code-users-hitting-usage-limits-way-faster-than-expected/5213575
  - https://theregister.com/2026/03/31/anthropic_claude_code_limits
- **Opus 4.7 tokenizer, 04-16 (OFFICIAL tokenizer change).** The same text maps to about 1.0–1.35x more tokens, and some workloads measured ~1.45x. Users reported limits running out within a few prompts.
  - https://letsdatascience.com/news/anthropic-releases-opus-47-prompting-user-backlash-418206ff
  - https://wbgsv0a.gigazine.net/gsc_news/en/20260420-claude-opus-4-7-token-cost/
- **05-06:** peak throttle removed and 5-hour limits doubled. **05-13:** weekly Claude Code limits +50%. The promo was originally due to end 07-13, was extended to 08-31, and in the end ran to **09-13**. From **09-14**, weekly limits are permanently +25% over the pre-promo baseline (OFFICIAL).
  - https://support.claude.com/en/articles/15910845
  - https://www.verdent.ai/guides/claude-code-limits-doubled-may-2026
  - https://propakistani.pk/2026/08/19/anthropic-extends-deadline-for-higher-claude-code-usage-limits/
- **Fable availability (OFFICIAL / PRESS). Your dates are confirmed, with two refinements:**
  - Fable 5 launched 06-09.
  - On **06-12** (letter received 17:21 ET), a Commerce Department export-control order suspended Fable 5 and Mythos 5. Mythos had already been restricted for foreign nationals since 06-02.
  - Commerce lifted the restrictions on **06-30**, and Fable came back globally on **07-01**. Some sources say subscription access was re-enabled late on 06-30.
  - The subscription promo ran to 07-07, was extended to 07-12, then to **07-19 23:59:59 PT**.
  - From 07-20: Max and premium seats get Fable at up to 50% of their weekly limit. Pro and standard seats pay through usage credits, with a one-time credit.
  - https://techsy.io/blog/anthropic-fable-5-suspended
  - https://www.exchange4media.com/digital-news/anthropic-suspends-fable-5-mythos-5-globally-after-us-security-order-155428.html
  - https://axios.com/2026/06/27/anthropic-fable-5-return-soon
  - https://dev.to/tekmag/untitled-37g6
  - https://support.claude.com/en/articles/15424964

### 4. The effort / thinking-level bug you remember

**Best match: the Fable `reasoning_effort` remap A/B experiment, August 2026.** Anthropic confirmed the experiment exists. Whether it hurt quality is disputed.
- **What happened.** From Claude Code 2.1.236/2.1.237 (npm 2026-08-19), some Fable 5 sessions set to **high** carried `<reasoning_effort>10</reasoning_effort>` in context. Users said 10 had been the value previously sent for **low**, and observed values like 50 and 85 suggested a 0–100 scale. Opus 5 was reportedly not enrolled.
- **Discovery.** Developer @argofowl posted on X on 2026-08-22: "since 2.1.237 the model reads 'high' effort as 10 out of 100, the exact number 'low' used to be and the changelog doesn't say a word."
  - https://x.com/argofowl/status/2091145834968850821
  - HN, 216 points: https://news.ycombinator.com/item?id=49401549
- **Anthropic's answer** (Thariq Shihipar on X and HN):
  - "We sometimes test API serving configs in Claude Code before rolling them out, and one running now maps the numerical effort value differently… The scale isn't 0-100, the number isn't meaningful on its own, and the effort you selected is the effort you're getting."
  - He said they had run in-depth evals showing no performance impact, and offered credits to users with clear regressions.
- **Why it still matters.** The model reads the tag. #88949 (08-23, 2.1.241) quotes Fable saying it would "read it as a low setting, i.e. minimal thinking before answering." The argument is that this primes the model to under-try, whatever the backend does.
  - #88888 (08-22) argues the opposite: the effort dial measurably works (median thinking tokens 2.6k / 3.0k / 4.6k for low / medium / high), and only the model's self-report is wrong.
- **Still seen later.** #95743 (2026-09-20, 2.1.278): Fable 5.1 at `high` still receives `reasoning_effort: 10`. I found no announced rollback or end date.
- **So your recollection is partly right.** It was not a "1–5 vs 1–10" parsing bug. It was an undisclosed server-side remap of effort label → number. "High" got the number that used to mean "low", and the model can see that number. Anthropic denies that actual effort changed.
  - https://www.gpts24.com/en/news/claude-code-experiment-quietly-remapped-effort-levels-for-fable-5-anthropic-confirms
  - https://github.com/anthropics/claude-code/issues/88949
  - https://github.com/anthropics/claude-code/issues/88888
  - https://github.com/anthropics/claude-code/issues/95743

**Closely related effort bugs.** These ones did silently lower or ignore the configured effort.
- **03-04 default medium effort**: see §2. OFFICIAL.
- **03-09, 2.1.72**: `max` effort removed and the scale simplified to low/medium/high. The same release fixed `--effort` being reset by unrelated settings writes on startup. OFFICIAL.
- **05-07, 2.1.133**: fixed `/effort` in one session changing other concurrent sessions, and IDE effort changes being silently dropped. OFFICIAL.
- **06-29, #72249** (Opus 4.8, 2.1.195): effort reportedly lowered mid-session without consent. Closed as not planned. COMMUNITY.
- **07-07, 2.1.203**: fixed background sessions ignoring `effortLevel` changes in settings.json. OFFICIAL.
- **08-22, #88842** (Fable 5, 2.1.240): settings say `high`, the transcript records `high`, but requests went at `low` until `/effort` was re-selected. COMMUNITY.
- **08-23, #89080** (Sonnet 5, VS Code 2.1.241): picker shows `xhigh` while requests go at `high`. COMMUNITY.
- **Default-effort "hold"** (OFFICIAL, CHANGELOG):
  - Opus 4.7, Opus 4.8 and Fable 5 held their launch-default effort over user settings. When the hold started is not documented.
  - 2.1.267 (09-09) fixed `effort:` frontmatter on custom commands, skills and **subagents** being ignored on those models.
  - 2.1.280 (09-22) stopped the hold from overriding `-p` / Agent SDK, project, managed, `--settings` and per-model `effortLevel`.
  - This matters directly for a pipeline that sets effort through settings or agent frontmatter.
- **10-05, 2.1.290**: fixed the effort level changing when a flagged message is retried on a fallback model. OFFICIAL.

### 5. Model silently changed under a pinned model (fallbacks, subagents)

**Fable → Opus 4.8 safety-classifier fallback, 06-10 → still open in October.**
- **The official mechanism.** When cyber, bio or frontier-ML classifiers fire, the request is routed to Opus 4.8.
- **Problems reported:**
  - The switch is sticky for the session.
  - `/model` could not restore Fable (#67246, 06-10, 2.1.170).
  - 27 of 133 agents pinned to Fable ran turns on Opus 4.8 without any UI notice (#66822, 06-10, closed not planned 07-18).
  - A reverse engineer alleged a silent retry path that bypasses `switchModelsOnFlag` (07-30).
  - #98875 (10-02, 2.1.285, Fable 5.1) reports the switch was silent and sticky for ~2 hours and 255 messages, with 13 thinking blocks dropped (`model_mismatch`), despite `switchModelsOnFlag:false`. Undocumented workaround: `CLAUDE_CODE_DISABLE_REFUSAL_FALLBACK=1`.
- **Related CHANGELOG fixes:**
  - 2.1.283 (09-25): dynamic workflows started during a fallback ran *every* agent on the fallback model.
  - 2.1.287 (10-01): `-p`/SDK sessions repeated a fallback on every later message.
  - 2.1.268 (09-10): a running session could silently switch to the org default model.
- Sources:
  - https://github.com/anthropics/claude-code/issues/67246
  - https://claudeissues.com/issue/66822-bug-silent-model-fallback-from-fable-5-to-opus-4-8-overrides-explicit-model-pinn
  - https://github.com/anthropics/claude-code/issues/98875
  - https://runtimewire.com/article/anthropic-claude-code-hidden-fable-5-model-switch-claim
  - https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback

**Fable 5 invisible "frontier LLM development" safeguards, 06-09 .. 06-11 (OFFICIAL).** The system card said these safeguards "will not be visible to the user". They silently reduced how useful answers were on ML and pretraining work. On 06-11 Anthropic made them visible (they now fall back to Opus 4.8) and said "We made the wrong tradeoff, and we apologize."
- https://noqta.tn/en/news/anthropic-claude-fable-5-hidden-safeguards-transparency-backlash-2026
- https://readysolutions.ai/blog/2026-06-10-claude-fable-5-silent-degradation/

**Subagent model pins:**
- #31311: the Agent-tool `model` parameter was ignored in 2.1.69–2.1.70 (03-06 .. 03-12), fixed in 2.1.72.
- #44385, #52681 (2.1.117), #54448, Apr–Jun: `model:` frontmatter pin ignored and subagents inherit the parent model. COMMUNITY.
- CHANGELOG 2.1.73 (03-11): subagents with `model: opus/sonnet/haiku` were silently downgraded on Bedrock, Vertex and Foundry.
- CHANGELOG 2.1.222 (08-04): org-restricted subagent aliases dropped to the parent model.
- CHANGELOG 2.1.251 (08-28): `CLAUDE_CODE_SUBAGENT_MODEL` used to override agent definitions; now only a default.
- CHANGELOG 2.1.260 (09-03): `model: fable` agents silently ran with a 200K context.
- Sources:
  - https://claudeissues.com/issue/31311-bug-agent-tool-model-parameter-silently-ignored-in-v2-1-69-regression-from-v2-1
  - https://claudeissues.com/issue/54448-bug-subagent-model-override-frontmatter-agent-tool-param-is-silently-inoperative

### 6. Compaction and context bugs (OFFICIAL, from the CHANGELOG; selection)

| Version | Date | Fix |
|---|---|---|
| 2.1.21 | 01-28 | Auto-compact triggered too early |
| 2.1.47 | 02-18 | **Plan mode lost after compaction** (#26061) |
| 2.1.75 | 03-13 | Token over-counting for thinking blocks caused premature compaction |
| 2.1.76 | 03-14 | **Deferred tools lost their schemas after compaction**; auto-compaction retried indefinitely |
| 2.1.83 | 03-24 | Background subagents invisible after compaction, so duplicates were spawned |
| 2.1.89 | 03-31 | Autocompact thrash loop |
| 2.1.117 | 04-21 | Opus 4.7 sessions computed against 200K instead of 1M, so compacted too early |
| 2.1.119 | 04-23 | Skills re-executed after auto-compaction |
| 2.1.208 | 07-13 | Context window reset to 200K after auto-update |
| 2.1.217 | 07-21 | Auto-compact never triggered for Opus 4.8 on Bedrock |
| 2.1.280 | 09-22 | **Finished subagent report lost if the parent compacted first** |
| 2.1.282 | 09-24 | Earlier extended thinking dropped by `/model` and other mid-turn commands |
| 2.1.288 | 10-02 | Resuming conversations dropped earlier thinking |
| 2.1.290 | 10-05 | Resumed subagents lost thinking and cache; scheduled `/loop` tasks silently lost after compaction |

Community issues on CLAUDE.md being ignored after `/compact`: #4017 (closed 2026-01-21) and #24460 (Feb–Mar 2026). Docs say CLAUDE.md is re-injected after compaction.

Full CHANGELOG: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md

### 7. Other notable behaviour changes (OFFICIAL)

- **07-24 (Thariq):** over 80% of Claude Code's system prompt removed for Opus 5 and Fable 5 ("over-constraining").
  - https://aiweekly.co/alerts/anthropic-deletes-80-of-claude-codes-system-prompt-for-claude-5
- **08-14, 2.1.233:** TodoWrite/Task tools removed on Opus 4.8, Sonnet 5, Fable 5 and newer.
- **06-30 / 07-01:** steganographic markers in the system prompt (COMMUNITY reverse engineering, widely reported). These are trust-relevant but have no shown quality effect.
  - https://gigazine.net/gsc_news/en/20260701-claude-code-prompt-steganography/

### 8. Community "nerf" clusters and trackers

- **Late Jan 2026 (Opus 4.5):** confirmed harness regression (§1).
- **March–April 2026 (Opus 4.6):** the largest cluster. Reddit threads like "Opus is genuinely lazy" and "lobotomized", GitHub #42796, The Register and others. **Anthropic acknowledged it** in the 04-23 postmortem.
  - https://dgtldept.substack.com/p/claude-opus-4-6-actually-did-get-dumber-regression-fixes
- **Mid/late April (Opus 4.7):** refusals and token-cost backlash. PRESS/COMMUNITY.
- **Aug 2026 (Opus 5 / Fable 5):**
  - "Opus 5 nerfed" (#82162, 07-29, closed not planned).
  - Fable effort-remap outrage (08-22).
  - Thariq conceded Opus 5 is "a really spiky model… huge priority".
  - https://x.com/trq212/status/2091252347913773169
- **Late Sept 2026 (Opus 5.5):** "nerfed" claims within days of launch; no evidence so far.
  - https://zoogom.com/en/posts/claude-opus-5-5-nerf-rumor-fact-check-2026/
  - https://byteiota.com/claude-opus-5-5-nerfed-livenerf-has-the-first-real-data/
- **Trackers:**
  - **MarginLab** runs daily SWE-Bench-Pro on Claude Code. It caught the Jan 2026 regression and is now in a baseline phase for Opus 5.5, high effort, since 09-24.
  - **LiveNerf** and **NerfBench** are community trackers. NerfBench shows Opus 5.5 at 99.2% of launch-day capability, and LiveNerf results are expected around 10-24.
  - I found no 2026 data from "IsItNerfed" itself.
- **Writing quality:** on 09-23, Anthropic's Jackson Kernion said prose had got denser since Opus 4.6, and that Opus 5.5 partially addresses it.
  - https://tech-insider.org/anthropic-engineer-claude-writing-quality-worse-2026/

### 9. Status-page incidents (OFFICIAL, all errors or availability, none labelled "quality")

I found no 2026 status incident that was explicitly about output *quality*. The only one I found is the 2025 precedent. 2026 incidents are "elevated errors" or "degraded performance", mostly under 2 hours. Examples:
- **03-02:** global outage, authentication.
- **06-06:** Opus 4.8 degraded, ~47 min. https://status.claude.com/incidents/b1gzqlnpxxxk
- **06-07:** multiple models. https://status.claude.com/incidents/s4pq658bt69h
- **08-05:** multi-model, 07:05–14:14.
- **08-17:** Opus 5 / Sonnet 5, ~90 min. https://status.claude.com/incidents/zhk4v3yv1lsf
- **08-24:** three outages, ~3 h total. https://www.kucoin.com/news/flash/claude-suffers-3-major-outages-in-one-day-affecting-api-app-and-cowork
- **10-05:** Fable 5.1 / Mythos 5.1 errors.

StatusGator counts 184 outage records since January 2026: https://statusgator.com/services/claude/outage-history

## Caveats

- Several items rely on secondary press, especially the HN and X quotes and the adaptive-thinking "zero budget" acknowledgement. X posts could not be fetched directly (HTTP 402).
- I found no announced end date or rollback for the effort-remap experiment.
- The user's list includes "Opus 4.8". The April postmortem names Opus 4.6 and 4.7. Opus 4.8 shipped 05-28.
