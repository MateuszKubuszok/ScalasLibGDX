# Issue-DB census: missing members vs body-level defects (sge, ssg)

Computed 2026-10-06. Data: `sge/.rescale/data/issues.tsv` (branch `sge-port-covenant`), `ssg/.rescale/data/issues.tsv` (branch `batch-varargs`), plus every historical version of `.rescale/data/issues.tsv` and `scripts/data/issues.tsv` on all refs (`git log --all`). Working files are in `scratchpad/iss/` (`*-c3.tsv` has every issue with its flags; `*-codebody.tsv` lists the body-level set; `c3.py` and `c4.py` are the classifiers).

## Method

- **Columns** (both repos): `id, file_path, category, status, severity, description, last_updated, source`. The DB has no creation-date column, and the description is often overwritten on resolution (e.g. ` — red:<sha> fix:<sha> … audit:PASS`). So I walked every commit that touched an issues TSV, oldest first, and took each ID's **first-appearance date and first-appearance description**. Classification uses that original text, falling back to HEAD text when the original is shorter than 15 characters.
- **ID universe.**
  - sge: 908 IDs ever seen. 880 are in HEAD. The other 28 (ISS-742..747 and ISS-887..908) exist only on other refs (train/side branches), not on `sge-port-covenant`.
  - ssg: 1,399 IDs, all in HEAD.
- **Caveat on IDs.** sge's ISS-001..406 date from 2026-03-19..04-01 (a quality scan plus review-grok/claude/codex/cursor imports). If an ID was ever renumbered, the first-appearance date is approximate.
- **MISS regex** (missing method/class/file). It matches any of:
  - `missing[-_ ](method|file|class)`
  - `(missing|absent|not ported|unported|never ported|omitted|not implemented)` within 60 characters before `method|class|file|constructor|overload|function|package|member|getter|setter|accessor|subclass|<ident>(…)`
  - the same keywords within 40 characters after such a term
  - `N% ported`, `N of M … missing`, `entirely missing`, `not ported`

  Text matching `missing test|test coverage|zero test|license header` is excluded.
- **BODY regex** (body-level defect). It matches any of: `simplif`, `dropped[-_ ]branch`, `missing[-_ ]logic`, `logic[-_ ](gap|error)`, `api-noop`, `no-?op`, `stub(bed)? (body|method|implementation)`, `is (an )?(empty )?stub`, `returns (default|empty|placeholder|constant|null|none|unit)`, `commented[- ]out`, `\bbreak\b`, `\bcontinue\b`, `early (return|exit)`, `mistranslat`, `invert(ed)`, `dead store`, `missing (…)?(guard|check|branch|case|condition|else|fallback|validation)`, `(branch|case|check|guard) (missing|dropped|omitted|skipped|removed)`, `silently (drop|ignor|discard|skip|swallow|return)`, `discard`, `ignores … (option|param|arg|flag|value|result)`, `drops … (option|param|branch|case|check)`, `wrong default`, `off-by-one`, `truncat`, `never (called|invoked|executed|consumed|fires|runs)`, `always (returns|true|false|null)`, `hard-?coded`, `placeholder`, `approximat`, `reimplement`, `instead of (the) (original|java|upstream|dart)`, `opposite`, `swapped`, `fall-?through`, `dropped`, `skip(s|ped)`, `loses`/`lost`, `dead code`, `unreachable`, `wrong (sign|order|index|operator|variable|instance|branch|value|result|condition|loop)`, `does not return`, `control flow`, `gutted`, `facade`, `shim`, `partial(ly) (port|implement)`, `incomplete (logic|implementation|handler|port)`.
  - **Excluded:** ssg's 231 regex-scanner rows (category `shortcuts`, or text `N shortcut hit(s): …`).
  - **"Code" subset:** this additionally drops descriptions that mention CI/sbt/xvfb/ratchet/covenant/enforce/re-scale/gate/baseline/munit/worktree, and test-only gaps.
- **Precision** (I hand-read a systematic sample of every 7th row, 20 rows per repo):
  - sge code-body set: about 70% true body-level port defects. False positives were review findings about API hygiene, platform capability, perf, or the JDK JIT.
  - ssg code-body set: about 75%. False positives were pit-of-success API facades, DiagResult wiring, and test-suite skips.
  - MISS set: about 85% in both repos. The remaining false positives were test gaps.
  - Treat the counts as ±25%.
- A **category-only cross-check** (ssg) needs no regex. Categories that name a body defect (`logic_gap` 37, `dropped-branch` 20, `missing-logic` 18, `divergence` 15, `api-noop` 14, `correctness` 14, `logic_error` 13, `logic` 12, `logic-bug` 7, `behavior` 5, `translator-defect` 3, `stub-method` 2, `simplified-logic` 2, `api-fidelity` 2, `logic-change`/`faithfulness`/`fidelity` 1 each) total **167**. Categories that name a missing member (`missing-method` 35, `missing_method` 33, `missing-feature` 18, `missing-file` 7, `missing-implementation` 3, `missing-state-tracking` 1) total **97**. The big `incomplete-port` category (281, plus 8 `incomplete_port` and 10 `incomplete`) mixes both kinds; the regex splits it into 19 missing and 64 body.

## Headline counts

| Repo | Issues ever | Missing-member (MISS) | Body-level, any (BODY) | Body-level, code subset | Both | Scanner rows (excluded) |
|---|---|---|---|---|---|---|
| sge | 908 | 59 | 186 | **142** | 9 | 0 |
| ssg | 1,399 | 202 | 372 | **349** | 48 | 231 |

Body-level issues still open at HEAD: sge 30, ssg 37. The rest are resolved.

**Audit status of the files involved.** I joined each code-body issue's `file_path` to `audit.tsv` (full path, or basename for sge).
- sge: 65 of 142 issues map to an audit row, and **all 65 rows read `pass`**. sge's audit.tsv has stayed at 1307 pass / 4 minor / 7 na since 2026-06-09 and was never revised after these issues were filed.
- ssg: 284 of 349 map to a row. **72 are `pass`**; the rest are `minor_issues` or `major_issues`.
- The DB has no column recording covenant status at filing time. The reviews' own statement for that is sge `codebase-review-2026-06-10.md`: "every one of the above carries `Covenant: full-port` and audit `pass`".

### By month of first appearance (code subsets)

| Month | sge all | sge missing | sge body | ssg all | ssg missing | ssg body |
|---|---|---|---|---|---|---|
| 2026-03 | 406 | 1 | 11 | 1 | 1 | 0 |
| 2026-04 | 76 | **41** | 22 | 881 | **166** | 224 |
| 2026-05 | — | — | — | 94 | 16 | 22 |
| 2026-06 | 210 | 6 | **62** | 383 | 17 | 85 |
| 2026-07 | 177 | 5 | 41 | 40 | 2 | 18 |
| 2026-09 | 39 | 6 | 6 | — | — | — |

The pattern supports the talk's thesis:
- **April** (method-set compare, port-gap wave ISS-407..481 in sge; dart-sass/terser gap catalogs in ssg) is dominated by *missing members*. sge has 41 missing vs 22 body issues.
- **June–July**, after covenants and method-set parity were enforced, the review-fable and re-review waves are dominated by *body-level* defects. sge has 103 body vs 11 missing.
  - sge review-fable ISS-483..566 (06-10): **40** code-body issues.
  - ssg R0610 ISS-977..1115 (06-10): **33**.
- ssg's April also carries many body issues. That is the 2026-04-18 dart-sass "Waves 1–9" body-level audit (categories `logic_gap`, `dropped-branch`, `missing-logic`, `api-noop`), which ran right after the 04-07 method-set tooling.

### By category (sge, top rows, code subset)
- review-fable 137 issues: 6 missing / 66 body (any)
- review-release 71: 2 / 23
- critical 26: 21 / 5 (April port-gap wave)
- major 20: 11 / 11
- fidelity 20: 2 / 9
- port-gap 25: 1 / 5
- bug 44: 1 / 13

## Examples: sge (ID, first-seen date, file, original description, trimmed)

1. **ISS-021** 2026-03-19 `math.CumulativeDistribution`: "Resolution: values assignment commented out". ISS-031 (same date) `ETC1TextureData`: "consumeCustomData commented out". These come from the 2025 Cursor rule "comment it out instead".
2. **ISS-263** 2026-03-19 (review-cursor CR-006) `BitmapFontCache.setColors / draw(Batch,start,end)`: "break() exits whole method".
3. **ISS-425** 2026-04-10 `anim8/PaletteReducer.scala`: "6.1% ported (366 vs 5989 LOC). analyze() is a no-op stub returning default palette. 23+ reduce methods missing."
4. **ISS-429** 2026-04-10 `controllers/DefaultControllerManager.scala`: "buttonDown/Up/AxisMoved return values discarded, events never consumed. Original uses if(listener.buttonDown(...)) break."
5. **ISS-451** 2026-04-10 `utils/Timer.scala`: "app.addLifecycleListener, app.removeLifecycleListener, and app.postRunnable are commented out. Posted tasks will not execute". Refiled as ISS-475 on 04-12.
6. **ISS-454** 2026-04-10 `Octree`/frustum: "missing early-exit guard … Traverses ALL nodes".
7. **ISS-488** 2026-06-10 `g2d/GlyphLayout.scala`: "Multi-line setText broken: newline case never advances i … silently drops text after first newline; leading newline loops forever".
8. **ISS-489** 2026-06-10 `GlyphLayout.scala`: "truncate is a no-op that aborts layout: Java loop break ported as method-level boundary.break in truncateRun".
9. **ISS-491** 2026-06-10 `GlyphLayout.scala`: "removeRange(1, secondStart) off-by-one — lls DynamicArray.removeRange is end-exclusive".
10. **ISS-492** 2026-06-10 `g2d/BitmapFontCache.scala`: "addToCache: gx += xAdvances(ii) is commented out and gx is a val … every glyph of a run cached at the same x".
11. **ISS-493** 2026-06-10 `g2d/SpriteCache.scala`: "begin() state guard inverted vs Java … begin always throws after a valid beginCache/endCache, class unusable".
12. **ISS-495** 2026-06-10 `g2d/Gdx2dDraw.scala`: "Scaled drawPixmap filter dispatch inverted: LINEAR routed to blitNearest … exactly reversed".
13. **ISS-496** 2026-06-10 `PolygonSpriteBatch.scala`: "recomputed triangleIdx for the final partial batch is a dead store".
14. **ISS-497** 2026-06-10 `decals/CameraGroupStrategy.scala`: "Default decal sorter inverted by Ordering.fromLessThan sign flip".
15. **ISS-500** 2026-06-10 `math/DelaunayTriangulator.scala`: "wrong COMPLETE predicate … and dropped y2y3<EPSILON degenerate bail".
16. **ISS-501** 2026-06-10 `scene2d/utils/Selection.scala`: "three Java early returns became no-op () branches or were dropped — the fire/changed block always runs".
17. **ISS-502** 2026-06-10 `ai/msg/PriorityQueue.scala`: "siftDown dropped the unconditional post-loop queue(k)=x write-back … polling {1,2} yields 1,1".
18. **ISS-506** 2026-06-10 `maps/tiled/BaseTmxMapLoader.scala`: "premature-EOF detection defeated … truncation throw unreachable — truncated … layer data loads silently with garbage".
19. **ISS-513** 2026-06-10 `gltf/.../BlenderShapeKeys.scala`: "parse is an unconditional no-op: extras.fold(empty)(_ => empty)".
20. **ISS-518** 2026-06-10 `AndroidApplication.scala`: "onResume/onPause/onDestroy never call listener.resume/pause/dispose … SGE dropped it".
21. **ISS-522** 2026-06-10 `GlOpsNative.scala`: "EGL_SAMPLES never passed … config.samples silently ignored on Native".
22. **ISS-581** 2026-06-10 `GlyphLayout.scala`: "text alignment broken — alignRuns tests (halign & 1) …". This was found by the audit of the GlyphLayout fix, and was pre-existing.
23. **ISS-631** 2026-06-12 `g3d/ModelInstance.scala`: "copyNodesById lacks upstream's break … adds the node copy TWICE".
24. **ISS-704** 2026-07-03 `scene2d/Stage.scala`: "drawDebug … success path inverted vs Stage.java:155-165".
25. **ISS-718** 2026-07-03 `gltf/exporters/GLTFMaterialExporter.scala`: "TextureAttribute.Specular -> specularColorTexture branch silently dropped".
26. **ISS-729** 2026-07-03 `ai/pfa/PathFinderRequestControl.scala`: "dropped dispatch branch: original … dispatches even when request.client == null".
27. **ISS-734** 2026-07-03 `SpriteBatch.scala`: "enable/disableBlending drop the already-in-state early return".
28. **ISS-817** 2026-07-17 `textra/Font.scala`: "ctors advance the alias index only on non-null entries; upstream … advances every iteration (continue)".

## Examples: ssg

1. **ISS-007** 2026-04-07 `liquid/Template.scala`: "withMaxRenderTimeMillis is a no-op".
2. **ISS-024** 2026-04-07 `liquid/parser/LiquidParser.scala`: "Error recovery silently skips unexpected tokens … Original liqp parser throws".
3. **ISS-042** 2026-04-07 `minify/Minifier.scala`: "file-type toggles (compressCss/compressJs/compressJson) and exclude list are dead — Minifier.minify ignores them".
4. **ISS-061** 2026-04-07 `js/compress/Compressor.scala`: "dropConsole is a literal no-op stub that returns toplevel unchanged. The dropConsole option is parsed and propagated … but never actually" used.
5. **ISS-065** 2026-04-07 `md/ext/enumerated/...PreProcessor.scala`: "loop body has 'lastFound // break' instead of an actual break — the bare expression is a no-op".
6. **ISS-070 / ISS-072** 2026-04-07 `AsideBlock` / `MacroDefinitionBlock`: "Constructor … silently drops the segments parameter".
7. **ISS-081** 2026-04-07 `md/ext/footnotes/FootnoteBlock.scala`: "addFirstReferenceOffset has inverted logic".
8. **ISS-084** 2026-04-07 `jekyll/tag/internal/IncludeNodePostProcessor.scala`: "Java's 'break' statements … replaced with comments only. Both … loops continue iterating".
9. **ISS-089** 2026-04-07 `DefinitionListBlockPreProcessor.scala`: "Missing break … 'if (!blankLinesInAST) break;'".
10. **ISS-094** 2026-04-07 `md/parser/internal/DocumentParser.scala`: "uses 'continue = false // return' to attempt early exit … only sets the outer-while flag".
11. **ISS-095** 2026-04-07 `md/ast/RefNode.scala`: "always returns null with comment 'Parser.REFERENCES is not yet ported'. Parser.REFERENCES is now ported". This is a false stale-stub excuse (cheat C5).
12. **ISS-140** 2026-04-10 terser `optimizeCall`: "dropped branches: inline_array_like_spread …, Array.from optimization, Symbol case, RegExp case, unsafe_Function".
13. **ISS-256 / ISS-257** 2026-04-12 `sass/extend/ExtendFunctions.scala`: an "extra leading-/trailing-combinator guard … which does not exist in Dart". These are invented guards.
14. **ISS-308** 2026-04-12 `sass/ast/selector/PseudoSelector.scala`: "unify() control flow bug: if (isElement) Nullable.Null does not return, needs boundary/break".
15. **ISS-530** 2026-04-18 `sass/visitor/RecursiveAstVisitor.scala`: "a complete stub: all 50+ methods are no-ops (return Unit). Dart original (377 LOC) has full recursive traversal". The method-set was complete; the bodies were empty.
16. **ISS-565** 2026-04-18 (category `simplified-logic`) `sass/parse/Parser.scala`: "whitespaceWithoutComments unconditionally treats consumeNewlines=false as space-or-tab only".
17. **ISS-703** 2026-04-18 `sass/ImportCache.scala`: "_toImporters is a no-op that just returns importers without processing loadPaths".
18. **ISS-760** 2026-04-24 `sass/visitor/EvaluateVisitor.scala`: "visitWhileRule missing @return/early-exit handling".
19. **ISS-942** 2026-05-10 `mermaid/layout/graph/PriorityQueue.scala`: "Heap index arithmetic off-by-one: heapify uses 2*i instead of 2*i+1".
20. **ISS-1033** 2026-06-10 `js/Terser.scala`: "MinifyOptions(compress = true) silently disables compression, and mangle = true likewise". This is cheat C7.
21. **ISS-1035** 2026-06-10 `DropUnused.scala`: "Pass 3 uses walk with a false 'transform is not yet implemented' comment".
22. **ISS-1037** 2026-06-10 `js/compress/Inference.scala`: "pure_getters truthiness inverted under defaults".
23. **ISS-1065 / ISS-1067** 2026-06-10 `mermaid/.../SequenceParser.scala`: "links/link/properties statements are silently skipped"; "silently drops unrecognized lines".
24. **ISS-1197** 2026-06-16 `mermaid/.../GanttDb.scala`: "compileTasks() is a near-no-op vs upstream multi-pass after/dependency resolution". ISS-1196, same file: "IGNORES db.dateFormat".
25. **ISS-1246** 2026-06-22 `js/compress/Compressor.scala`: "uses Int range (toInt), truncating integer-valued Doubles".
26. **ISS-1396** 2026-07-15 (category `translator-defect`): "Scala 3 boundary.Break <: RuntimeException, so any break() INSIDE a try whose catch is broad … is SELF-CAUGHT". This is a codebase-wide class of control-flow mistranslation.
27. **ISS-1397** 2026-07-15 `Evaluate.scala`: "fixJsPrecision(s, prec) ignores its prec parameter … while its docstring claims it pads".

## Takeaways for the talk
- Missing-member findings cluster in April, the method-set-compare era. Body-level findings dominate June–July, after method-set parity and covenants were enforced. In sge, 103 body-level issues against 11 missing-member issues were filed in June–July.
- In sge, every code-body issue whose file has an audit row sits on a file the audit DB still calls `pass` (65/65).
- The recurring defect shapes are:
  - Java `break`/`continue`/early-`return` mistranslated through `boundary`/flag variables
  - inverted guards or sorts
  - commented-out or dead statements
  - silently ignored options or parameters
  - no-op bodies under complete method-sets
