# SGE natives, multiarch-scala, and the Scala tooling gaps: research notes

Sources: git history and docs of `sge`, `multiarch-scala`, `sge-native-providers`, `ssg-native-providers`,
`sge-angle-natives`, `curl-natives`, `tree-sitter-natives`, `sbt-kubuszok`, `lls`, `ssg`, plus the workspace
roadmap `/Users/dev/Workspaces/kubuszok/FABLE5_PLANNING_ROADMAP.md`. All repos are under
`/Users/dev/Workspaces/kubuszok/`. Dates are commit dates (YYYY-MM-DD).

---

## 0. What does "Colorless" mean?

No file, module, commit message or branch in any repo under `/Users/dev/Workspaces/kubuszok` contains
"colorless" or "colourless", so it is a speech-to-text error. Candidates, ranked:

1. **"Claude"**, i.e. "all the things we did *with Claude* as part of extraction from LibGDX". This is the best fit.
   The rest of the sentence (extraction from LibGDX, improvements along the way, Scala tooling gaps that led to
   multiarch-scala) describes the native/multiarch story, not a single component. Almost all of that work was
   agent-driven: CLAUDE.md files in every repo, the "Fable 5" and Opus planning windows
   (`FABLE5_PLANNING_ROADMAP.md`, `OPUS_PLAYBOOK-2026-07-11.md`), the re-scale skills, and multiarch-scala
   commit `43f0517` (2026-05-09), "Extract PanamaProvider from SGE, add Claude plugin with 6 skills".
2. **"colorful"**, the `sge-extension/colorful` port of tommyettinger's `colorful-gdx`
   (`original-src/colorful-gdx`; port commit `49481311`, 2026-04-11). It fits the sound ("color-ful/less") and it
   is a LibGDX-ecosystem extraction. But it is pure Scala with no natives, so it cannot explain the
   "multiarch / Scala tooling" half of the question.
3. Less likely: "headless" (HeadlessApplication, the GLFW null platform) or "collections" (lls).

**Best guess: "with Claude".** If the speaker meant the colorful extension, only its single port commit is relevant.

---

## 1. Native code in LibGDX and what replaced it in SGE

### 1.1 What LibGDX had (JNI via jnigen)
Found in `sge/original-src/libgdx`:

| LibGDX native piece | Location | Mechanism |
|---|---|---|
| `BufferUtils` (copy, vertex transforms, find, unsafe alloc) | `gdx/src/.../utils/BufferUtils.java` | jnigen `static native` |
| `Matrix4` batch `mulVec`, `prj`, `rot` | `gdx/src/.../math/Matrix4.java` | jnigen |
| `ETC1` codec | `gdx/jni/etc1`, `ETC1.java` | jnigen + C |
| `Gdx2DPixmap` (stb_image decode + C drawing) | `gdx/jni/gdx2d`, `Gdx2DPixmap.java` | jnigen + C |
| iOS GL | `gdx/jni/iosgl` | RoboVM |
| FreeType | `extensions/gdx-freetype/jni` | jnigen |
| Box2D | `extensions/gdx-box2d/.../jni` | jnigen + C++ |
| Bullet | `extensions/gdx-bullet/jni` | SWIG/JNI |
| Native loading | `SharedLibraryLoader` (moved to the `gdx-jnigen-loader` artifact) | |
| Desktop backend | `backends/gdx-backend-lwjgl3` (LWJGL: GLFW, OpenGL, OpenAL, stb) plus the optional `extensions/gdx-lwjgl3-angle` | |

In total libGDX core has 59 Java `native` members (`sge/sge-port/src/main/scala/sge/port/LibgdxNativeBodies.scala`).

### 1.2 Timeline of the SGE replacement

| Date | Commit (repo) | Event |
|---|---|---|
| 2025-07-01 | `e1aff235` (sge) | SGE starts: LibGDX Java converted to Scala 3. |
| 2026-03-01 | `c4de2218` (sge) | Rust "native-ops" crate integrated as a sibling sbt module. Native operations restructured into the `sge.platform` package as traits (`BufferOps`, `ETC1Ops`, `Gdx2dOps`, `GlOps`, `WindowingOps`, `AudioOps`) with JVM/JS/Native implementations. |
| 2026-03-05 | `fe890bc5` | Desktop and browser backends; Panama FFM foundation on the JVM; WebGL20/30 and Web Audio on JS. |
| 2026-03-05 | `docs/architecture/wasm-strategy.md` | Decision: stay on Scala.js; the Wasm backend is opt-in. |
| 2026-03-06 | `0a1e6491` | **ANGLE adopted**: `AngleGL20`..`AngleGL32` call ANGLE via Panama downcalls. GLFW windowing and miniaudio audio via Panama. LWJGL removed. |
| 2026-03-06 | `fabd8044` | Scala Native `@extern` FFI for GLFW, miniaudio, ANGLE GL ES 2.0-3.2 and EGL. New `scaladesktop/` source set shared by JVM and Native. |
| 2026-03-07 | `cb84d506` | Rust cross-compilation for 6 desktop targets. |
| 2026-03-08 | `319fd370` | Android via PanamaPort (`com.v7878.foreign`, Panama on ART, no JNI). FreeType extension; physics via **Rapier2D (Rust) instead of Box2D**. jlink plus Roast launcher packaging. |
| 2026-03-10 | `a6c89321` | **Gdx2DPixmap re-implemented**: drawing in pure Scala (`Gdx2dDraw`); decoding via the Rust `image` crate on Native, ImageIO/BitmapFactory on JVM, pure-Scala decoders on JS. |
| 2026-03-14 | `c8b49c4a` | First `NativeLibLoader`: natives bundled in the JVM JAR. Native EGL fixes (ANGLE platform display, CALayer). FFI wiring validation (76 endpoints, 6 libraries). |
| 2026-03-20 | `810061e` (sge-angle-natives) | **ANGLE build CI repo created**: 10 targets (macOS Metal, Linux Vulkan, Windows D3D11/Vulkan, Android ×3, iOS static). |
| 2026-03-24 | `9c900f18` | CI rewrite: one macOS runner builds all 9 targets (cargo-zigbuild for Linux, cargo-xwin for Windows, NDK for Android). JDK switched to Zulu 25. |
| 2026-03-31 | `096bdf68` | `NativeLibBundle` sbt plugin (`native-bundle.json` manifests, merged per-platform linker flags). Scala Native GLFW joystick FFI. |
| 2026-04-01 | `7edfba2` (multiarch-scala, then named sbt-multi-arch-release) | **Plugins extracted from SGE**: NativeLibBundlePlugin, ZigCrossPlugin, MultiArchJvmReleasePlugin, scala-native-curl-provider. |
| 2026-04-01 | `a21ee8a` (sge-native-providers, then named sge-native-components) | Provider JAR repo created. |
| 2026-04-03 | `4fa5b88` (curl-natives) | MSVC-built static libcurl for 6 platforms. It replaces MinGW static-curl, which the Scala Native MSVC link cannot use. |
| 2026-04-03 | `ea220355` (sge) | **SGE drops its in-house plugins.** Natives now come from published provider JARs; the CI build-native job is deleted. |
| 2026-04-04 | `c0e68a03` (sge) | Granular providers (freetype and physics split from core), stubs eliminated, **all JNI references removed**. The miniaudio and GLFW submodules move to the external repo. |
| 2026-04-04 | `c9853fca` (sge) | Rust toolchain is no longer a prerequisite for SGE contributors. |
| 2026-04-05 | `88cf783` (tree-sitter-natives) | Monolithic tree-sitter library: 6 platforms plus WASM. It later grew to 85 grammars (`fa27353`, 2026-05-04). |
| 2026-04-11 | `a3c03846` (sge) | JVM controllers backend via Panama (GLFW joystick). |
| 2026-04-14 | `8678029`, `0349d55` (multiarch) | Renamed to **multiarch-scala**. New sbt-free `multiarch-core`. **`sn-provider.json` / `jni-provider.json` / `pnm-provider.json`** replace `native-bundle.json`. ZigCrossPlugin renamed **MultiArchNativeReleasePlugin**. |
| 2026-04-14 | `d84c3f5` (providers), `f2e00884` (sge) | Providers renamed to `sn-provider-sge*` / `pnm-provider-sge*`. sge-build becomes AutoPlugins (`SgeDesktopJvmPlatform`, `SgeBrowserPlatform`, `SgeDesktopNativePlatform`, `SgeAndroidPlatform`). demos/build.sbt shrinks from about 440 to about 120 lines. |
| 2026-04-17 | `8800cf3` (multiarch) | `NativeCrossAxis`, `withCrossNative`, and the Android build plugin extracted from sge-build. |
| 2026-04-17 | `3a7f6b8`, `4aa5932` (providers); `7a8acbdd` (sge) | Rapier2D 0.32 and **Rapier3D replacing Bullet** (physics3d). |
| 2026-04-18 | multiarch tag 0.1.0 | First release. 0.1.1 followed on 04-19, 0.1.2 on 04-24 (Windows DLLs copied next to the SN exe, `4bc8f44`). |
| 2026-05-04/05 | `f4be844` (ssg-native-providers), `a40ed056` (ssg) | **Second consumer**: SSG tree-sitter highlighting on JVM (Panama), Native (static) and JS (WASM). |
| 2026-05-09 | `43f0517` (multiarch), `6e64433b` (sge) | **Panama abstraction extracted**: `multiarch-panama-api` (JDK 17, PanamaPort on Android) and `multiarch-panama-jdk` (JDK 22+). multiarch 0.2.0. |
| 2026-05-16 | `a59e2d0` (sbt-kubuszok) | **sbt-kubuszok** created; adopted the same day in multiarch, providers and lls. |
| 2026-05-28 | `2e30b2db` (sge) | Provider JARs become transitive POM dependencies; `sgeExtensions` setting added. |
| 2026-06-16 | `49c82d00` (sge) | Real fail-closed release gate on the resolved provider JARs. It immediately found 8 missing or undersized Windows/macOS binaries (ISS-673). |
| 2026-06-17 | `9256968a`, `fc404b0b` | Physics on Scala.js over the Rapier2D/3D WASM builds. FreeType's JS axis dropped (`ecabff65`). |
| 2026-06-20 | `f69a749`, `27e3646`, `2b68c53` (multiarch) | Plugin cross-built for sbt 1.x and sbt 2.0. **multiarch-resources** added (classpath resources on Scala.js). multiarch 0.3.0. |
| 2026-06-21/22 | sge `53a4e573`, `51d2d319` | sbt 2.0 migration. Browser assets moved to multiarch-resources. |
| 2026-06-23/24 | sge-native-providers `82ff3b6`..`afd81fe` | Windows cross-link fixes: lld-link vs clang-cl, arm64 vs arm64x/arm64ec, real `glfw3.lib` / `sge_audio.lib` import libs, runtime DLLs. |
| 2026-06-24 | sge `68f76494`..`4a6a1954` | ANGLE on headless CI: Vulkan over lavapipe and over SwiftShader both fail, so ANGLE-GL-over-llvmpipe is used under xvfb (ISS-691). |
| 2026-07-02/03 | multiarch `e6a737f`..`f3cafb6` (MA-1..MA-5) | **Manifest v2**: provider artifact/version, `bundles`, collision detection at 4 sites, version-namespaced `native/<artifact>/<version>/<platform>/`. 0.4.0 released 2026-07-07 with a MiMa baseline. |
| 2026-07-16 | sge `platform-targets.md` | macos-x86_64 and windows-aarch64 withdrawn from CI. Scala Native cannot target windows-aarch64. |
| 2026-07-18 | sge `b7acad15` | ISS-857: the `sge_native_ops` load is memoized. |
| 2026-08-14 | multiarch `03f6b70`, `863d8ee` | **multiarch-serviceloader**: a ServiceLoader that works on JVM, JS and Native. |
| 2026-09-11 onward | sge `4be61f3c`, `8bcfc9da` | Baltic Porter regenerates the core. JVM bodies for the 59 `native` members come from `LibgdxNativeBodies.scala` (they delegate to `Gdx2DNative`, `BufferUtilsNative`, `ETC1Native`; Matrix4's strided loops are written out in Scala). |

### 1.3 Replacement summary per piece

| LibGDX | JVM | Scala Native | Scala.js | Android |
|---|---|---|---|---|
| LWJGL GL | ANGLE (libEGL + libGLESv2) via Panama | ANGLE via `@extern` | WebGL / WebGL2 | system GLES (no ANGLE) |
| LWJGL GLFW | GLFW via Panama (`WindowingOpsJvm`) | GLFW `@extern` | DOM | GLSurfaceView |
| OpenAL | miniaudio (`sge_audio`) via Panama | miniaudio `@extern` | Web Audio | miniaudio (OpenSL ES) |
| BufferUtils / ETC1 (jnigen) | Rust `sge_native_ops` via Panama | Rust via C ABI | pure Scala | Rust via PanamaPort |
| gdx2d | ImageIO decode; pure-Scala draw | Rust `image` crate | pure-Scala PNG/BMP/GIF/JPEG decoders | BitmapFactory |
| Matrix4 natives | pure Scala | pure Scala | pure Scala | pure Scala |
| FreeType | Rust `sge_freetype` via Panama | static | dropped (ISS-553) | Panama |
| Box2D | Rapier2D (Rust) via Panama | static | Rapier2D WASM | Panama |
| Bullet | Rapier3D (Rust) | static | Rapier3D WASM | Panama |
| SharedLibraryLoader | `multiarch.core.NativeLibLoader` | linker (NativeProviderPlugin) | n/a | APK `lib/` and `findLibrary` |

No bindings are generated: there is no jextract or jnigen use in the SGE code. The FFI is hand-written and
checked by the 76-endpoint wiring validation (`c8b49c4a`) and the native FFI integration tests.

---

## 2. Improvements made along the way

- **One C ABI for every runtime.** Rust and C exports are shared by Panama, Scala Native and PanamaPort, so JNI
  was removed completely (`c0e68a03`). Rationale: `sge/docs/architecture/platform-targets.md`, "Why Panama FFM",
  "Why ANGLE".
- **ANGLE everywhere on desktop.** It gives one GL ES API, and Metal on macOS despite Apple's OpenGL deprecation.
- **No native toolchain for consumers.** Provider JARs replaced roughly 15 minutes of Rust/zig/xwin/NDK builds
  (`sge-native-providers/README.md`).
- **Granular providers.** Five providers became 11, then 14 directories (core, angle, freetype, physics, physics3d
  × pnm-desktop / pnm-android / sn). A JAR bundles only its own libraries. Stubs were removed (`9165c31`, `c0e68a03`).
- **MSVC curl** (curl-natives) replaced MinGW stubs, so sttp works on Scala Native with no system libcurl.
- **Windows correctness:** `.lib` aliases (`2c3b437`), DLLs copied next to the exe because Windows has no rpath
  (`4bc8f44`), real import libs (sge-native-providers, June 23-24). **macOS:** rpath (`8a0d17d`) and a
  `fullPath` mode that works around ld64 flag deduplication (`7edfba2`).
- **Manifest v2 and collision safety** (multiarch MA-1..MA-5, 0.4.0, 2026-07-07). Corrupt-manifest hardening and
  a MiMa baseline were added at the same time (`1468385`, `acde47c`).
- **Fail-closed native release gate** (`49c82d00`). Guards against false-green CI: `SGE_CI_REQUIRE_DISPLAY`
  (ISS-485), a sentinel for crashed forked JVMs (ISS-690), and native GL FFI tests under xvfb (`25c06fff`).
- **Smaller build files:** SgePackaging went from 1035 to about 280 lines, and demos from about 440 to about
  120 (`f2e00884`).
- **Physics gained a JS backend** via Rapier WASM, which LibGDX's GWT Box2D never had in this form.
- **Cross-platform resources and ServiceLoader** were factored out of SSG and SGE into multiarch.
- **Data structures extracted into lls** (2026-05-14 onward): allocation-free `Nullable` and `MkArray`, plus
  lls-io.

---

## 3. Tooling gaps that forced multiarch-scala and sbt-kubuszok

| Gap in Scala/sbt tooling | Evidence | multiarch answer |
|---|---|---|
| Scala Native has no way to ship native libraries through Maven. The linker needs system libs (for example libcurl for sttp). | `7edfba2` cites **scala-native/scala-native#4800** | `NativeProviderPlugin` plus `sn-provider.json`: discover the manifest on the classpath, extract `.a`/`.lib` for the target, merge and deduplicate `flags-groups`, wire `nativeConfig.linkingOptions` |
| Scala Native cannot cross-compile for another OS or arch out of the box. | `MultiArchNativeReleasePlugin` (formerly ZigCross) | zig cc/c++ wrappers; `zigCrossTarget`; `NativeCrossAxis` / `withCrossNative` for projectmatrix |
| JVM natives have no standard loader or packaging convention (LibGDX used jnigen's SharedLibraryLoader). | `NativeLibLoader` (`c8b49c4a`, then multiarch-core) | `pnm-provider.json` / `jni-provider.json`; resolution order is java.library.path, then v2 index, then legacy path, then Android |
| sbt-native-packager's JDKPackager builds only for the host JDK and platform. | multiarch README | `MultiArchJvmReleasePlugin`: jlink plus the Roast launcher for 6 platforms, built offline on one machine (a Scala answer to *construo*) |
| Panama differs between JDK 22+ and Android, and libraries targeting JDK 17 cannot call `java.lang.foreign`. | `43f0517` | `multiarch-panama-api` (JDK 17, picks PanamaPort on Android) and `multiarch-panama-jdk` (JDK 22+) |
| No maintained sbt Android plugin. | `8800cf3` and the AndroidBuild code | `AndroidPlugin` (D8, aapt2, apksigner, AAR extraction) |
| Scala.js has no classpath resources. | `27e3646`, `2b68c53` | `multiarch-resources` plus a build-time base64 embed generator |
| `java.util.ServiceLoader` is missing on Scala.js; on Native it accepts only a literal `classOf`. | `863d8ee` | `multiarch-serviceloader` plus a META-INF/services code generator (a typo fails at compile time) |
| Two JARs bundling the same `.so` collide silently (classpath order wins). | roadmap ground truth §4 | manifest v2 `bundles` plus 4 collision checks |
| Plugins must support both sbt 1 and sbt 2 (sbt 2 is built on Scala 3.8.4 and caching requires `Def.uncached`). | `f69a749` (multiarch), `5229a2f` (sbt-kubuszok) | `Compat` shims per axis |
| Every cross-built library (JVM/JS/Native × Scala 2.13/3) repeats the same projectmatrix, commandmatrix, publishing, MiMa and IDE boilerplate. | `a59e2d0` | **sbt-kubuszok**: one plugin bundle, `ci-release`, `DevProperties`, generated CI aliases |

**multiarch-scala releases:** 0.1.0 (2026-04-18), 0.1.1 (04-19), 0.1.2 (04-24), 0.2.0 (05-09), 0.3.0 (06-20),
0.4.0 (07-07). It was renamed from sbt-multi-arch-release on 2026-04-14.

**sbt-kubuszok releases:** 0.1.0 (2026-05-16), 0.2.0 (05-21), 0.2.1 (06-03), 0.2.2 and 0.2.3 (06-20).

---

## 4. Still missing (open as of 2026-10-06)

**Upstream Scala Native and Scala.js**
- No iOS support in Scala Native: GC segfaults (scala-native#4334) and C-runtime guards (#2875). The SGE iOS
  backend is deferred (`sge/docs/architecture/ios-backend-feasibility.md`).
- Scala Native cannot target windows-aarch64 (`platform-targets.md`, 2026-07-16).
- Native-library distribution is not part of Scala Native itself (#4800); multiarch is a third-party workaround.
- Scala.js Wasm: JSPI is not in Safari and module splitting is unsupported (`wasm-strategy.md`). The no-go
  decision is in `sge/docs/plans/2026-07-async-and-wasm.md`.
- Scala.js still has no resources or ServiceLoader of its own; multiarch fills the gap.

**multiarch-scala and the providers**
- The provider repos never migrated to manifest v2: every `sn-provider.json` / `pnm-provider.json` is still
  schema `0.1.0`, and physics3d providers have no manifest at all.
- The flag-necessity audit (Workstream A, `scripts/flag-audit.sh`) was never done.
- `--enable-native-access=ALL-UNNAMED` is still used everywhere (`sge/build.sbt:175`, `JvmPackaging.scala:127`).
- ssg still has the TODO at `ssg/build.sbt:220` ("check if NativeProviderPlugin.projectSettings is necessary").
- **Android R8 and merged proguard.txt (minSdk 26 instead of 36)** were planned (`sge/docs/plans/2026-07-android-r8.md`,
  multiarch 0.5.0) but there is no R8 commit in multiarch-scala. The standalone sbt-android plugin
  (`multiarch-scala/docs/plans/2026-07-sbt-android-plugin.md`, AP-1..7) has not started.
  `android-native-constraints.md` still claims API 36 is an upstream constraint, which kubuszok/sge#5 disputes.
- **Release blocker ISS-751:** SGE pins the SNAPSHOT `nativeComponents = 0.1.2-33-gcf10406-SNAPSHOT`
  (`sge/project/Versions.scala:45`). sge-native-providers has had no release since 0.1.2 (2026-05-02), so the
  Windows fixes exist only as snapshots.
- ISS-754: the JVM JAR's contents vary with whether the release runner has an Android SDK.
- ISS-828: the freetype provider's ABI gap (glyph metrics marshals only 5 of 8 fields). ISS-811: the Native
  audio recorder needs miniaudio capture symbols that the provider does not export.
- Android uses system GLES, not ANGLE. No hot reload.
- macos-x86_64 and windows-aarch64 binaries ship untested (ISS-793).

**Capability gaps**
- Physics: Rapier lacks gear, pulley, friction and wheel joints, and pre/post-solve callbacks
  (`physics-limitations.md`).
- FreeType has no JS backend.
- JS has no sockets or local/absolute files. Native has no text-input dialog or recorder (`capability-matrix.md`).

**CI**
- No GPU tier on CI. ANGLE-Vulkan fails on both software Vulkans, and cross-context EGL sharing works only on a
  real GPU (ISS-691). The plan is a local or self-hosted T3 tier.
