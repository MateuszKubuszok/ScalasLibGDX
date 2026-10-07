#!/usr/bin/env python3
"""Generates slides/timeline.adoc: the timeline sequence with inline SVG.

The sequence alternates overview slides and zoom slides:
  overview (reveal steps up to a red drop) -> zoom on that drop (findings + new checks)
  -> overview (continue) -> zoom -> ... -> overview (to the end)
All slides share one frame (data-id), so reveal.js auto-animate zooms in and out between them.

Run: python3 scripts/timeline.py && yarn build
Evidence for every label: research/ (sge.md, ssg.md, coverage.md, models.md, rescale-balticporter.md).
Line heights are illustrative; dates and labels are evidence.
"""
from datetime import date
from pathlib import Path

START, END = date(2026, 2, 1), date(2026, 10, 10)
X0, X1 = 40, 960  # usable x range inside the 1000-wide viewBox
AXIS_Y = 250

OPUS, FABLE, SONNET, RED, AMBER, INK, MUTED, ANTHROPIC = (
    "#2f62c9", "#b7791f", "#2f8a57", "#c8322b", "#d9a441", "#262a2a", "#6b6f6b", "#7a4fa8")


def x(d: str) -> float:
    m, dd = map(int, d.split("-"))
    return X0 + (date(2026, m, dd) - START).days / (END - START).days * (X1 - X0)


def py(v: float) -> float:
    return AXIS_Y - 20 - v * 130


# ---------------------------------------------------------------- overview data
# Every element names the step (click) it belongs to, so a line segment appears
# together with the milestone or release that explains it.

# Public model releases: (date, name, colour, step)
RELEASES = [
    ("02-05", "Opus 4.6", OPUS, 0), ("05-28", "Opus 4.8", OPUS, 5), ("06-09", "Fable 5", FABLE, 6),
    ("07-24", "Opus 5", OPUS, 9), ("09-01", "Fable 5.1", FABLE, 11), ("09-22", "Opus 5.5", OPUS, 13),
]

# Agent ports, "claimed progress": points and the step of each segment (segment i ends at point i)
CLAIMED = [("02-24", .10), ("03-30", .80), ("04-01", .95), ("04-10", .45), ("04-28", .95), ("06-09", .95),
           ("06-10", .30), ("07-01", .95), ("07-03", .55), ("07-19", .60)]
CLAIMED_STEPS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
DROP_LABELS = {"04-10": ("method audit:\nPaletteReducer 6%", "end"),
               "06-10": ("Fable review:\nbroken at\nalgorithm level", "end"),
               "07-03": ("blind re-review:\n5 criticals", "start")}
# Found later, by regenerating the same libraries: the hand ports were worse still
LATE_DROP = (("07-19", .60), ("09-05", .20), 11, "regeneration: the agent\nports were worse still")

# Baltic Porter: starts again from zero, slower but measured by tests
GENERATED = [("07-18", .0), ("07-29", .18), ("08-25", .30), ("09-07", .40), ("09-11", .50), ("09-27", .58)]
GENERATED_STEPS = [9, 10, 11, 12, 13]

# Milestones below the axis: (date, label, row, step[, text anchor])
EVENTS = [
    ("02-24", "SGE (game engine) resumes", 0, 0),
    ("03-26", "SGE: CI green", 1, 1),
    ("03-30", "SSG (site generator) starts", 2, 2, "end"),
    ("04-07", "SSG: 20.7% → re-scale", 0, 3),
    ("04-20", "certificates stamped", 2, 4),
    ("07-01", "review queue at zero", 2, 7),
    ("07-18", "Baltic Porter", 1, 9),
    ("07-29", "libGDX core compiles", 0, 10),
    ("09-05", "parity dropped: agent ports cheated", 2, 11),
    ("09-07", "12/12 demos", 0, 11),
    ("09-11", "generated core in SGE", 1, 12),
    ("09-27", "4 extensions", 0, 13),
]

# Fable availability: (from, to, label, colour, opacity, step)
BANDS = [("06-12", "07-01", "Fable\noff", RED, .12, 7), ("07-01", "07-19", "Fable\npromo", AMBER, .18, 8)]

# Incident bars shown directly on the overview (no zoom for that period): (step, (from, to, label, row))
OVERVIEW_BARS = [
    (11, ("07-29", "08-31", "Opus 5 \"spiky\"", 1)),
    (11, ("08-19", "09-22", "effort lower than selected", 2)),
]

# ---------------------------------------------------------------- zoom data
# Phases: the overview reveals steps [lo, hi]; then (optionally) a zoom on the drop that ends the phase.
# Zoom notes: (date or None, kind, html). kind: "found" (red dot), "check" (a check we added, blue diamond),
# "context" (grey dot). Date None = no axis marker.
PHASES = [
    dict(lo=0, hi=3,
         note="This is the last eight months. (pause) The blue line is what the agents told me: how much was ported. "
              "It is not to scale; only the dates are real. "
              "(click) In late February I picked SGE up again: SGE, the Scala Game Engine, is my Scala port of libGDX. "
              "This time I did it with AI agents. Anthropic's Opus model was the one doing the work. "
              "(click) By the end of March, all three platforms were green in CI. "
              "(click) Then I started a second project the same way: SSG, a static site generator. "
              "It needs a Markdown parser, a template engine, a Sass compiler, so it is also mostly ported libraries. "
              "(click) And the second project is where it broke: the Sass port you just saw. Let's zoom in.",
         zoom=dict(
        title="April: the files were \"done\"", center="04-06",
        note="In the zooms, red is what I found, blue is what I added in response, and purple is what was going wrong on Anthropic's side. "
             "(click) First, purple: Anthropic later admitted that in March Claude Code ran with lower default effort, "
             "and a bug kept wiping the model's earlier reasoning. (click) Usage was also throttled at peak hours. "
             "(click) Then the Sass port: complete, said the agent. One test in five, said the test suite. "
             "(click) So I added checks. Compare each file's size with the original: one well-ported library told me a good port is about the same size. "
             "Compare the list of methods. Scan for TODOs and stubs. "
             "(click) I put those checks into a tool, re-scale. Every file gets a certificate: a header with its methods and size, checked in CI. "
             "(click) The checks found more right away: one library at a fifth of its original size, with no TODO anywhere. "
             "Box2D, four hundred files, replaced by an eight-file wrapper. "
             "(click) And a rule for the agents: porting is binary. A hundred percent, or not done.",
        notes=[
            ("03-04", "anthropic", "Claude Code: default effort cut to medium; from 03-26 earlier thinking wiped every turn (Anthropic postmortem 04-23)",
             ("03-04", "04-20", "effort cut, thinking wiped", 0)),
            ("03-23", "anthropic", "Peak-hour throttling of session limits, until 05-06",
             ("03-23", "05-06", "peak-hour throttling", 1)),
            ("04-06", "found", "Sass compiler: <b>\"COMPLETE: 283/283 files\"</b>; next day the spec suite passes <b>20.7%</b>"),
            ("04-07", "check", "New checks: size vs the original (a good port is about the same size), method list vs the original, TODO/stub scanner"),
            ("04-08", "check", "re-scale: a <b>certificate</b> per file (its methods and size), checked in CI"),
            ("04-10", "found", "colorful at <b>19%</b> of original size, no TODO in sight; PaletteReducer <b>6%</b>; Box2D 400+ files → 8"),
            ("04-11", "check", "Rule for agents: \"porting is binary — 100% or not done\""),
        ])),
    dict(lo=4, hi=6,
         note="(click) The agents then stamped those certificates on about twelve hundred files at once. "
              "(click) Through May the claims stayed high. A new model came out, Opus 4.8. "
              "(click) In June, Anthropic released Fable, a stronger and more expensive model. I asked it to review everything. "
              "(pause) And the line fell.",
         zoom=dict(
        title="June: every method present, bodies hollow", center="06-10",
        note="(click) The certificates had been stamped while the CI check was switched off. "
             "(click) Every method was there, but the bodies were hollow. In text layout, a loop's break became an exit from the whole method. "
             "(click) In font rendering, the line that moves to the next letter was commented out. Every letter drawn in the same place. "
             "(click) In the JavaScript minifier, more than half the tests were marked as expected to fail, so CI said: zero failures. "
             "Real conformance was about forty percent. "
             "(click) So, new rules: a failing test first, counters that may only go down, a blocking CI gate, and a different model must audit. "
             "(click) On Anthropic's side, a safety classifier could silently swap Fable for Opus. "
             "(click) And then Fable was switched off worldwide for almost three weeks. So Opus was auditing Opus.",
        notes=[
            ("04-20", "context", "~1,200 certificates stamped in one commit, while their CI check was non-blocking"),
            ("06-10", "found", "Text layout: Java's loop <code>break</code> became a method exit, so truncation is a no-op"),
            ("06-10", "found", "Font rendering: <code>// gx += xAdvances[ii]</code> commented out, so every glyph is drawn at the same x"),
            ("06-10", "found", "JavaScript minifier: 1,507 of 2,522 tests marked as expected failures → <b>~40%</b> real conformance"),
            ("06-10", "check", "New rules: failing test first, counters that only go down, a blocking CI gate, a different model must audit"),
            ("06-10", "anthropic", "A safety classifier silently swaps Fable for Opus 4.8 for the rest of the session",
             ("06-10", "10-06", "classifier silently swaps Fable → Opus 4.8", 0)),
            ("06-12", "context", "Fable switched off worldwide: Opus 4.8 audits Opus 4.6"),
        ])),
    dict(lo=7, hi=8,
         note="(click) Fixing all of that took until the end of June. The review queue reached zero. "
              "(click) Then Fable came back for a short time, and I ran a blind re-review. "
              "Five critical findings. A whole subsystem missing. Tests that only tested the standard library. "
              "(pause) And one reviewer agent invented three of its five findings.",
         zoom=None,
         quote=("The agents aren't trustworthy because they are non-deterministic.",
                "That is what I wrote in mid-July. (pause) Every check I added, the agents learned to get past. "
                "So I stopped asking them to port the code. I asked them to build a translator instead: a deterministic one. "
                "I called it Baltic Porter.")),
    dict(lo=9, hi=13,
         note="(click) Agent porting stops. Baltic Porter starts, from zero. That's the green line. "
              "It grows slower, but every number on it is measured by running tests. "
              "(click) By the end of July, the whole libGDX core compiles. "
              "(click) In September I compared the result with the old agent ports. They were even worse than the reviews had shown: "
              "their own tests checked for wrong values. That's the second red line. "
              "And in purple: Claude Code was quietly sending lower effort than I had selected, and Opus 5 was, in Anthropic's words, "
              "a really spiky model. Meanwhile, all twelve demos render. "
              "(click) The generated core replaces SGE's agent port. "
              "(click) And four extensions are generated too. (pause) That's where I am today.",
         zoom=None),
]
ZOOM_SCALE = 2.0
ZOOM_FOCUS_Y = 200


def text(tx, ty, s, size=11, color=INK, anchor="middle", weight="normal"):
    out = [f'<text x="{tx:.1f}" y="{ty:.1f}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}">']
    for i, ln in enumerate(s.split("\n")):
        out.append(f'<tspan x="{tx:.1f}" dy="{0 if i == 0 else size * 1.15:.1f}">{ln}</tspan>')
    out.append("</text>")
    return "".join(out)


def seg(d0, v0, d1, v1, col):
    return (f'<line x1="{x(d0):.1f}" y1="{py(v0):.1f}" x2="{x(d1):.1f}" y2="{py(v1):.1f}" '
            f'stroke="{col}" stroke-width="3" stroke-linecap="round"/>')


def drop_label(d, v, label, anchor):
    dx = -5 if anchor == "end" else 5
    return text(x(d) + dx, py(v) + (4 if anchor == "end" else 14), label, 10, RED, anchor=anchor)


def elements():
    """All overview elements as (step, svg)."""
    items = []
    for d0, d1, label, col, op, step in BANDS:
        items.append((step, f'<rect x="{x(d0):.1f}" y="40" width="{x(d1) - x(d0):.1f}" height="{AXIS_Y - 40}" fill="{col}" opacity="{op}"/>'
                            + text((x(d0) + x(d1)) / 2, 52, label, 9, RED if col == RED else FABLE)))
    for i, (d, name, c, step) in enumerate(RELEASES):
        items.append((step, f'<path d="M{x(d):.1f},{AXIS_Y + 30} l-5,-9 h10 z" fill="{c}"/>'
                            + text(x(d), AXIS_Y + 46 + (i % 2) * 14, name, 10, c, weight="bold")))
    for i in range(1, len(CLAIMED)):
        (d0, v0), (d1, v1) = CLAIMED[i - 1], CLAIMED[i]
        g = seg(d0, v0, d1, v1, RED if v1 < v0 else OPUS)
        if d1 in DROP_LABELS:
            g += drop_label(d1, v1, *DROP_LABELS[d1])
        if i == 1:
            g += text(X0, 24, "claimed progress (agent ports)", 10, OPUS, anchor="start", weight="bold")
        items.append((CLAIMED_STEPS[i - 1], g))
    items.append((9, text(x("07-19") - 3, py(.60) - 8, "agent porting stops", 9, MUTED, anchor="end")))
    (ld0, lv0), (ld1, lv1), lstep, llabel = LATE_DROP
    mid = (x(ld0) + x(ld1)) / 2
    items.append((lstep, seg(ld0, lv0, ld1, lv1, RED)
                  + text(x(ld0) + 20, py(lv0) - 22, llabel, 10, RED, anchor="start")))
    for i in range(1, len(GENERATED)):
        (d0, v0), (d1, v1) = GENERATED[i - 1], GENERATED[i]
        g = seg(d0, v0, d1, v1, SONNET)
        if i == 1:
            g += text(X0, 38, "generated & tested (Baltic Porter)", 10, SONNET, anchor="start", weight="bold")
        items.append((GENERATED_STEPS[i - 1], g))
    for step, bar in OVERVIEW_BARS:
        items.append((step, incident_bar(*bar)))
    for d, label, row, step, *anchor in EVENTS:
        anchor = anchor[0] if anchor else "middle"
        tx = x(d) + (3 if anchor == "end" else 0)
        items.append((step, f'<circle cx="{x(d):.1f}" cy="{AXIS_Y}" r="4" fill="{INK}"/>'
                            f'<line x1="{x(d):.1f}" y1="{AXIS_Y + 4}" x2="{x(d):.1f}" y2="{AXIS_Y + 70 + row * 24:.1f}" '
                            f'stroke="{MUTED}" stroke-width=".5" stroke-dasharray="2 2"/>'
                            + text(tx, AXIS_Y + 82 + row * 24, label, 11, INK, anchor=anchor)))
    return sorted(items, key=lambda it: it[0])


def marker(d, kind, level=0):
    """Axis marker; markers on (nearly) the same date are spread sideways along the axis."""
    cx, cy = x(d) + level * 9, AXIS_Y
    if kind == "check":
        return f'<path d="M{cx:.1f},{cy - 5:.1f} l5,5 -5,5 -5,-5 z" fill="{OPUS}" stroke="#fff" stroke-width=".8"/>'
    col = RED if kind == "found" else MUTED
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="5" fill="{col}" stroke="#fff" stroke-width=".8"/>'


def incident_bar(d0, d1, label, row):
    """Purple lane right above the axis: Anthropic-side incidents (research/incidents.md)."""
    y = AXIS_Y - 14 - row * 13
    return (f'<rect x="{x(d0):.1f}" y="{y}" width="{x(d1) - x(d0):.1f}" height="10" rx="2" fill="{ANTHROPIC}" opacity=".9"/>'
            + text(x(d0) + 3, y + 7.6, label, 7.5, "#fff", anchor="start"))


def svg(static_max, frag_lo=None, frag_hi=None, notes=(), bars=()):
    """Elements with step <= static_max are always shown; steps in [frag_lo, frag_hi] are fragments;
    later steps are omitted. Dated notes add axis markers revealed with their bullet; notes that carry
    an incident bar reveal the bar instead. `bars` are incident bars from earlier zooms (always shown)."""
    p = ['<svg viewBox="0 0 1000 400" xmlns="http://www.w3.org/2000/svg" '
         'style="width:100%;height:auto;font-family:inherit">',
         f'<line x1="{X0}" y1="{AXIS_Y}" x2="{X1}" y2="{AXIS_Y}" stroke="{INK}" stroke-width="1.5"/>']
    for m, name in enumerate(["Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"], start=2):
        mx = x(f"{m:02d}-01")
        p.append(f'<line x1="{mx:.1f}" y1="{AXIS_Y}" x2="{mx:.1f}" y2="{AXIS_Y + 6}" stroke="{INK}"/>')
        p.append(text(mx, AXIS_Y + 20, name, 12, MUTED))
    for step, g in elements():
        if step <= static_max:
            p.append(g)
        elif frag_lo is not None and frag_lo <= step <= frag_hi:
            p.append(f'<g class="fragment" data-fragment-index="{step - frag_lo}">{g}</g>')
    for b in bars:
        p.append(incident_bar(*b))
    placed = []
    for i, (d, kind, _, *bar) in enumerate(notes):
        if bar:
            p.append(f'<g class="fragment" data-fragment-index="{i}">{incident_bar(*bar[0])}</g>')
        elif d:
            level = 0
            while any(abs(px - (x(d) + level * 9)) < 9 for px in placed):
                level += 1
            placed.append(x(d) + level * 9)
            p.append(f'<g class="fragment" data-fragment-index="{i}">{marker(d, kind, level)}</g>')
    p.append("</svg>")
    return "".join(p)


def frame(svg_html, x0, x1, focus_y=200):
    """Scale the SVG so that viewBox x-range [x0, x1] fills a fixed 2.5:1 frame centred on focus_y.
    Only width/margins change between slides, which auto-animate interpolates."""
    scale = 1000 / (x1 - x0)
    left = -x0 / 1000 * 100 * scale
    top = 100 * (0.2 - 0.4 * scale * focus_y / 400)
    return (f'<div data-id="tl-frame" class="tl-frame">'
            f'<div data-id="tl-svg" style="width:{scale * 100:.2f}%;margin-left:{left:.2f}%;'
            f'margin-top:{top:.2f}%">{svg_html}</div></div>')


ICON = {"found": f'<span class="tl-ico" style="color:{RED}">●</span>',
        "check": f'<span class="tl-ico" style="color:{OPUS}">◆</span>',
        "context": f'<span class="tl-ico" style="color:{MUTED}">●</span>',
        "anthropic": f'<span class="tl-ico" style="color:{ANTHROPIC}">▲</span>'}


def notes_html(notes):
    li = []
    for i, (d, kind, body, *_) in enumerate(notes):
        when = f'<span class="tl-date">{d}</span> ' if d else ""
        li.append(f'<li class="fragment" data-fragment-index="{i}">{ICON[kind]}{when}{body}</li>')
    return '<ul class="tl-notes">' + "".join(li) + "</ul>"


def slide(title, body, note=None):
    out = f"[.timeline%auto-animate]\n=== {title}\n\n++++\n{body}\n++++\n"
    if note:
        out += f"\n[NOTE.speaker]\n--\n{note}\n--\n"
    return out


def bar_slide(title, rows, note=None):
    body = ["<div style='text-align:left;font-size:.6em'>"]
    for rid, label, pct, color, sub in rows:
        body.append(f"<div data-id='{rid}-label' style='margin-top:.8em'>{label}</div>"
                    f"<div data-id='{rid}-track' style='background:#ddd9cc;height:1.1em;border-radius:3px'>"
                    f"<div data-id='{rid}-bar' style='width:{pct}%;height:100%;background:{color};border-radius:3px'></div></div>"
                    f"<div data-id='{rid}-sub' style='font-size:.75em;color:{MUTED}'>{sub}</div>")
    body.append("</div>")
    return slide(title, "".join(body), note)


def main():
    out = ["// GENERATED by scripts/timeline.py; edit the script, not this file\n"]
    # Hook first: claimed vs measured
    out.append(bar_slide("Claimed vs measured", [
        ("sass", "The Sass compiler, ported by an agent, April 6th: <b>\"migration COMPLETE: 283/283 files\"</b>", 100, OPUS, "the agent's claim")],
        note="Here is what an agent told me in April. I was porting dart-sass, the Sass compiler, to Scala. "
             "The agent said: migration complete. Two hundred eighty-three of two hundred eighty-three files."))
    out.append(bar_slide("Claimed vs measured", [
        ("sass", "The next day: the official Sass test suite", 20.7, RED, "<b>20.7%</b> of the tests pass")],
        note="The next day I ran the official Sass test suite. (pause) One test in five passed."))
    out.append(bar_slide("Claimed vs measured", [
        ("sass", "Then: every method checked against the original", 37.7, SONNET, "37.7% faithfully ported"),
        ("simp", "", 25.8, AMBER, "25.8% simplified: it exists, but cuts corners"),
        ("miss", "", 36.1, RED, "36.1% missing")],
        note="Then I checked method by method. About a third faithful. A quarter cut short. A third simply missing. "
             "(pause) This part of the talk is about how that happens, and what I did about it."))
    bars = []  # incident bars revealed by earlier zooms stay on the timeline
    for n, ph in enumerate(PHASES):
        out.append(slide("Eight months",
                         frame(svg(ph["lo"] - 1, ph["lo"], ph["hi"], bars=bars), 0, 1000), ph["note"]))
        z = ph["zoom"]
        if z:
            half = 500 / ZOOM_SCALE
            x0 = min(max(x(z["center"]) - half, 0), 1000 - 2 * half)
            out.append(slide(z["title"],
                             frame(svg(ph["hi"], notes=z["notes"], bars=bars), x0, x0 + 2 * half, ZOOM_FOCUS_Y)
                             + notes_html(z["notes"]), z["note"]))
            bars = bars + [note[3] for note in z["notes"] if len(note) > 3]
        if ph.get("quote"):
            q, qn = ph["quote"]
            out.append(f"[.quote-slide]\n=== !\n\n++++\n<blockquote class=\"big-quote\">{q}<footer>me, mid-July</footer></blockquote>\n++++\n"
                       f"\n[NOTE.speaker]\n--\n{qn}\n--\n")
    Path("slides").mkdir(exist_ok=True)
    Path("slides/timeline.adoc").write_text("\n".join(out))


if __name__ == "__main__":
    main()
