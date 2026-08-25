#!/usr/bin/env python3
"""TikZ-Generator fuer fig:eval-opfermatrix: Hinwege EU/US nach Asien-Pazifik.

Liest thesis/daten/ap-opfermatrix.csv, schreibt thesis/tikz/ap-opfermatrix.tex. Farbcodierung:
Klasse zugestellt = akzenthell/akzent, Klasse verworfen = warnhell/warnton, nicht gemessen =
sqhell gestrichelt; Pilotbelege (ohne Captures) zusaetzlich mit duennem Rahmen und Vermerk.
Nicht von Hand aendern; Aenderungen in Skript oder Datenschicht.
"""
import csv
from collections import OrderedDict
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
DATEN = REPO / "thesis" / "daten" / "ap-opfermatrix.csv"
FRAGMENT = REPO / "thesis" / "tikz" / "ap-opfermatrix.tex"

matrix = OrderedDict()
ziele = []
with DATEN.open() as fh:
    for r in csv.DictReader(l for l in fh if not l.startswith("#")):
        matrix.setdefault(r["quelle"], OrderedDict())[r["ziel"]] = (r["status"], r["beleg"])
        if r["ziel"] not in ziele:
            ziele.append(r["ziel"])

bw, bh, gap = 1.72, 0.56, 0.14
x0 = 3.1

tex = []
tex.append("% Generiert von thesis/tikz/gen/ap-opfermatrix.py aus thesis/daten/ap-opfermatrix.csv.")
tex.append("% Nicht von Hand aendern; Aenderungen im Skript oder in der Datenschicht vornehmen.")
tex.append("\\begin{tikzpicture}[")
tex.append("  ok/.style={draw=akzent, fill=akzenthell, rounded corners=2pt, semithick},")
tex.append("  okpilot/.style={draw=akzent, fill=akzenthell, rounded corners=2pt, thin},")
tex.append("  kill/.style={draw=warnton, fill=warnhell, rounded corners=2pt, semithick},")
tex.append("  killpilot/.style={draw=warnton, fill=warnhell, rounded corners=2pt, thin},")
tex.append("  leer/.style={draw=sqgrau, fill=sqhell, rounded corners=2pt, thin, dashed},")
tex.append("  zelle/.style={font=\\scriptsize, minimum height=%.2fcm, minimum width=%.2fcm}," % (bh - 0.1, bw))
tex.append("  reihe/.style={font=\\scriptsize\\ttfamily},")
tex.append("  kopf/.style={font=\\scriptsize\\bfseries}]")
for j, ziel in enumerate(ziele):
    tex.append(f"  \\node[kopf] at ({x0 + j*(bw+gap) + bw/2:.2f},0.62) {{{ziel}}};")
tex.append("  \\node[kopf, anchor=west] at (0,0.62) {Quelle};")
for i, (quelle, zl) in enumerate(matrix.items()):
    y = -i * (bh + gap)
    beleg = next(iter(zl.values()))[1]
    zusatz = " (Pilot)" if beleg == "pilot" else ""
    tex.append(f"  \\node[reihe, anchor=west] at (0,{y:.2f}) {{{quelle}{zusatz}}};")
    for j, ziel in enumerate(ziele):
        status, bel = zl[ziel]
        if status == "ok":
            stil = "ok" if bel == "zellen" else "okpilot"
            inhalt = "\\checkmark"
        elif status == "kill":
            stil = "kill" if bel == "zellen" else "killpilot"
            inhalt = "$\\times$"
        else:
            stil, inhalt = "leer", "$\\cdot$"
        tex.append(f"  \\node[{stil}, zelle, anchor=west] at ({x0 + j*(bw+gap):.2f},{y:.2f}) {{{inhalt}}};")
y_fuss = -len(matrix) * (bh + gap) - 0.05
tex.append(f"  \\node[font=\\scriptsize, text=feldlinie, anchor=north west, text width=13.6cm] "
           f"at (0,{y_fuss:.2f}) {{\\checkmark~Surplus-Klasse zugestellt; $\\times$~Surplus-Klasse "
           f"verworfen (Baselines kamen in allen Lanes vollzählig an); $\\cdot$~nicht gemessen; "
           f"dünner Rahmen: Pilotbeleg ohne Mitschnitt ($n=6$ je Lane), sonst Zellenbeleg mit "
           f"Mitschnitten ($n=20$ je Zelle und Richtung)}};")
tex.append("\\end{tikzpicture}")
FRAGMENT.write_text("\n".join(tex) + "\n")
print(f"geschrieben: {FRAGMENT} ({len(matrix)} Quellen x {len(ziele)} Ziele)")
