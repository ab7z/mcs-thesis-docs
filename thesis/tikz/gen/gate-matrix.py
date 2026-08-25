#!/usr/bin/env python3
"""TikZ-Generator fuer fig:eval-gate: Pruefsummen-Gate-Kreuzzellen je Richtung.

Liest thesis/daten/gate-zellen.csv, schreibt thesis/tikz/gate-matrix.tex. Farbcodierung:
zugestellt = akzenthell/akzent, verworfen = warnhell/warnton; Glyphen fuer den Graustufendruck
(\\checkmark bzw. $\\times$). Nicht von Hand aendern; Aenderungen in Skript oder Datenschicht.
"""
import csv
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
DATEN = REPO / "thesis" / "daten" / "gate-zellen.csv"
FRAGMENT = REPO / "thesis" / "tikz" / "gate-matrix.tex"

rows = []
with DATEN.open() as fh:
    for r in csv.DictReader(l for l in fh if not l.startswith("#")):
        rows.append(r)

zeilenhoehe = 0.62
spalten = [("g", "G: Pad ff,\\\\OCS gültig"), ("c", "C: OCS 5b53\\\\kompensiert"),
           ("k", "Kontrolle")]
x0, bw, gap = 4.55, 2.35, 0.3

tex = []
tex.append("% Generiert von thesis/tikz/gen/gate-matrix.py aus thesis/daten/gate-zellen.csv.")
tex.append("% Nicht von Hand aendern; Aenderungen im Skript oder in der Datenschicht vornehmen.")
tex.append("\\begin{tikzpicture}[")
tex.append("  zu/.style={draw=akzent, fill=akzenthell, rounded corners=2pt, semithick},")
tex.append("  weg/.style={draw=warnton, fill=warnhell, rounded corners=2pt, semithick},")
tex.append("  zelle/.style={font=\\scriptsize, minimum height=4.6mm, minimum width=%.2fcm}," % bw)
tex.append("  reihe/.style={font=\\scriptsize\\ttfamily},")
tex.append("  gruppe/.style={font=\\scriptsize\\bfseries, text=feldlinie},")
tex.append("  kopf/.style={font=\\scriptsize\\bfseries, align=center}]")
for i, (key, titel) in enumerate(spalten):
    tex.append(f"  \\node[kopf] at ({x0 + i*(bw+gap) + bw/2:.2f},1.05) {{{titel}}};")
tex.append("  \\node[kopf, anchor=west] at (0,1.05) {Richtung};")
y = 0.0
letzte_gruppe = None
for r in rows:
    if r["gruppe"] != letzte_gruppe:
        letzte_gruppe = r["gruppe"]
        tex.append(f"  \\node[gruppe, anchor=west] at (0,{y:.2f}) {{{letzte_gruppe}}};")
        y -= zeilenhoehe * 0.85
    anzeige = r["richtung"].replace("->", "$\\rightarrow$")
    tex.append(f"  \\node[reihe, anchor=west] at (0.25,{y:.2f}) {{{anzeige}}};")
    for i, (key, _) in enumerate(spalten):
        zu, n = int(r[f"{key}_zu"]), int(r[f"{key}_n"])
        stil = "zu" if zu > 0 else "weg"
        glyph = "\\checkmark" if zu > 0 else "$\\times$"
        tex.append(f"  \\node[{stil}, zelle, anchor=west] at ({x0 + i*(bw+gap):.2f},{y:.2f}) "
                   f"{{{glyph}~{zu}/{n}}};")
    y -= zeilenhoehe
tex.append(f"  \\node[font=\\scriptsize, text=feldlinie, anchor=north west, text width=12.4cm] "
           f"at (0,{y - 0.05:.2f}) {{Zugestellt (\\checkmark) heißt: am fernen Ende aufgezeichnet "
           f"beziehungsweise ausgeliefert; die zugestellten G-Datagramme verwirft der Empfänger "
           f"anschließend regelkonform (Pad ungleich null), die Nutzdaten stellt er zu}};")
tex.append("\\end{tikzpicture}")
FRAGMENT.write_text("\n".join(tex) + "\n")
print(f"geschrieben: {FRAGMENT} ({len(rows)} Zeilen)")
