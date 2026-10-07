#!/usr/bin/env python3
"""Generates slides/platforms.adoc: "Why port libGDX to Scala?" diagrams and the build-tooling table.

Run: python3 scripts/platforms.py && yarn build
"""
from pathlib import Path

INK, MUTED, RED, AMBER, GREEN, BOX, CORE = "#262a2a", "#6b6f6b", "#c8322b", "#b7791f", "#2f8a57", "#e4e1d6", "#d6dce8"

# (id, name, line 2, line 3, verdict with Scala, verdict note)
BACKENDS = [
    ("desktop", "Desktop", "LWJGL3", "on a normal JVM", "ok", "works as is"),
    ("android", "Android", "Android SDK", "bytecode → dex", "warn", "works, but Scala/Android\nversion mismatches; natives"),
    ("browser", "Browser", "GWT", "Java source → JS", "no", "GWT compiles Java source,\nnot bytecode"),
    ("ios", "iOS", "RoboVM / MobiVM", "AOT bytecode → ARM", "no", "Scala on RoboVM:\nunsupported, unmaintained"),
]
W, H, GAP, TOP = 205, 92, 26, 230
X0 = (1000 - 4 * W - 3 * GAP) / 2


def text(x, y, s, size=18, color=INK, anchor="middle", weight="normal"):
    out = [f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}">']
    for i, ln in enumerate(s.split("\n")):
        out.append(f'<tspan x="{x:.1f}" dy="{0 if i == 0 else size * 1.2:.1f}">{ln}</tspan>')
    out.append("</text>")
    return "".join(out)


def diagram(language: str, with_scala: bool) -> str:
    p = ['<svg viewBox="0 0 1000 470" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;font-family:inherit">',
         '<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
         f'<path d="M0,0 L10,5 L0,10 z" fill="{MUTED}"/></marker></defs>']
    # core
    p.append(f'<rect x="280" y="30" width="440" height="96" rx="10" fill="{CORE}" stroke="{INK}" stroke-width="1.5"/>')
    p.append(text(500, 70, "Common game logic", 24, weight="bold"))
    p.append(text(500, 104, f"written in {language}, against the libGDX API", 17, MUTED))
    for i, (bid, name, l2, l3, verdict, note) in enumerate(BACKENDS):
        bx = X0 + i * (W + GAP)
        cx = bx + W / 2
        p.append(f'<line x1="{500 + (i - 1.5) * 90:.1f}" y1="126" x2="{cx:.1f}" y2="{TOP - 4}" stroke="{MUTED}" stroke-width="1.6" marker-end="url(#arr)"/>')
        p.append(f'<rect x="{bx:.1f}" y="{TOP}" width="{W}" height="{H}" rx="8" fill="{BOX}" stroke="{INK}" stroke-width="1.2"/>')
        p.append(text(cx, TOP + 30, name, 21, weight="bold"))
        p.append(text(cx, TOP + 56, l2, 16))
        p.append(text(cx, TOP + 78, l3, 14, MUTED))
        if with_scala:
            if verdict == "no":
                mark = (f'<line x1="{bx - 6:.1f}" y1="{TOP - 6}" x2="{bx + W + 6:.1f}" y2="{TOP + H + 6}" stroke="{RED}" stroke-width="5" stroke-linecap="round"/>'
                        f'<line x1="{bx + W + 6:.1f}" y1="{TOP - 6}" x2="{bx - 6:.1f}" y2="{TOP + H + 6}" stroke="{RED}" stroke-width="5" stroke-linecap="round"/>')
                col = RED
            elif verdict == "warn":
                mark = text(bx + W - 16, TOP + 24, "⚠", 22, AMBER)
                col = AMBER
            else:
                mark = text(bx + W - 16, TOP + 24, "✓", 22, GREEN, weight="bold")
                col = GREEN
            p.append(f'<g class="fragment">{mark}{text(cx, TOP + H + 32, note, 15, col)}</g>')
    if with_scala:
        p.append('<g class="fragment">'
                 f'<rect x="290" y="420" width="420" height="40" rx="8" fill="none" stroke="{MUTED}" stroke-width="1.2" stroke-dasharray="5 4"/>'
                 + text(500, 446, "Scala Native: not a libGDX target at all (Java + JNI)", 15, MUTED) + "</g>")
    p.append("</svg>")
    return "".join(p)


def tooling_table() -> str:
    rows = [
        ("Desktop apps for Windows / macOS / Linux, built on one host",
         "Construo (jlink + native launcher)",
         "sbt-native-packager: packages only for the platform you build on"),
        ("Android: dex, shrink, sign, package",
         "Android Gradle Plugin (D8, R8 / ProGuard, signing)",
         "sbt-android: unmaintained for years"),
        ("iOS: AOT-compile to ARM, package the app",
         "RoboVM / MobiVM Gradle plugin",
         "Nothing: RoboVM doesn't support Scala, Scala Native has no iOS"),
        ("Browser build, and knowing which assets exist at runtime",
         "GWT Gradle plugin; the build generates <code>assets.txt</code>, which GWT's preloader reads to fetch and list assets",
         "Scala.js has no classpath, so <code>getResourceAsStream</code> finds nothing; no build step to embed assets or generate a manifest"),
        ("Native libraries for every platform",
         "gdx-jnigen + per-platform natives JARs",
         "JVM: extract from the JAR by hand; Scala Native: install the library on the system and pass linker flags yourself"),
    ]
    trs = "".join(f'<tr class="fragment"><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in rows)
    return ('<table class="versus three"><thead><tr><th>What a game needs</th><th>libGDX + Gradle</th>'
            f'<th>Scala + sbt</th></tr></thead><tbody>{trs}</tbody></table>')


def main():
    out = ["// GENERATED by scripts/platforms.py; edit the script, not this file\n",
           "[.compact%auto-animate]\n=== What libGDX gives you\n\n++++\n"
           f'<div data-id="platforms">{diagram("Java", False)}</div>\n++++\n',
           "\n[NOTE.speaker]\n--\nlibGDX gives you one codebase and four targets. (pause) Desktop runs on a normal JVM. "
           "Android runs your bytecode after converting it. The browser goes through GWT, which compiles Java source to JavaScript. "
           "And iOS goes through RoboVM, a compiler that turns JVM bytecode into native code ahead of time.\n--\n",
           "\n[.compact%auto-animate]\n=== ...and what you keep if you write it in Scala\n\n++++\n"
           f'<div data-id="platforms">{diagram("Scala", True)}</div>\n++++\n',
           "\n[NOTE.speaker]\n--\nNow write the same game in Scala. (click) Desktop: fine. "
           "(click) Android: it works, but Scala and Android versions don't always agree, and native libraries make it harder. "
           "(click) The browser: GWT reads Java source, not bytecode, so Scala can't use it. "
           "(click) iOS: RoboVM could take Scala bytecode in theory, but nobody supports that path. "
           "(click) And Scala Native is not a libGDX target at all. libGDX is Java, calling C through JNI. "
           "(pause) So to have Scala everywhere, I had to own the engine. I had to port libGDX itself.\n--\n",
           "\n[.compact]\n=== The build tooling goes too\n\n++++\n" + tooling_table() + "\n++++\n",
           "\n[NOTE.speaker]\n--\nIt's not only the runtime. (pause) With Gradle, libGDX can package a desktop app for every system from one laptop. "
           "It can build and shrink Android apps. It can compile for iOS. "
           "(pause) For Scala and sbt, none of that existed. So I had to build it. That's the second part of this talk.\n--\n"]
    Path("slides").mkdir(exist_ok=True)
    Path("slides/platforms.adoc").write_text("".join(out))


if __name__ == "__main__":
    main()
