#!/usr/bin/env python3
"""Datenschicht und TikZ-Generator fuer die TTL-Auswertung (Abbildung fig:eval-ttl, Kapitel 6.1).

Zwei Betriebsarten:
  --ableiten [TABELLE ...]
               parst ttl-report.py-Ausgabetabellen und schreibt die versionierte Datenschicht
               thesis/daten/ttl-verteilung.csv (aggregierte Paketsummen je Richtung, Erfassungsseite,
               Verkehrsklasse und TTL; keine Adressen, keine Rohpfade). Ohne Tabellenargumente werden
               die lokalen Arbeitskopien unter lernnotizen/ (nicht versioniert) gelesen.
  (ohne Flag)  liest thesis/daten/ttl-verteilung.csv und schreibt das TikZ-Fragment
               thesis/tikz/ttl-uniformitaet.tex.

Reproduzierbarkeit aus den versiegelten Archiven (am 2026-09-02 nachvollzogen, CSV identisch):
  1. Paar 1blue/mcs: die archivierte Tabellenkopie ttl-report-alle-captures.md aus
     ff2-ttl-pfadanalyse-20260815.tar.zst (enthaelt die Kampagnen-Stamps und die lokale
     p1-checksumgate-Reihe).
  2. Helsinki-Paare: scripts/ttl-report.py des Implementierungsrepos (Stand f847895) ueber alle PCAPs der
     p0-, p1- und p2-Stamps aus hel-kampagne-20260815.tar.zst (ohne die checksumgate-Stamps; die
     AppleDouble-Eintraege ._*.pcap des Archivs sind keine Mitschnitte und auszuschliessen).
  Aufruf: ttl-uniformitaet.py --ableiten <ttl-report-alle-captures.md> <hel-tabelle.md>
Die Kopfzeilen der CSV nennen die Archive samt SHA-256 und die Einschlussregel je Paar.
"""
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
DATEN = REPO / "thesis" / "daten" / "ttl-verteilung.csv"
FRAGMENT = REPO / "thesis" / "tikz" / "ttl-uniformitaet.tex"

QUELLEN = [
    REPO / "lernnotizen" / "ff2-ttl-pfad" / "ttl-report-alle-captures.md",
    REPO / "lernnotizen" / "hel-kampagne" / "ttl" / "ttl-paar-a.md",
    REPO / "lernnotizen" / "hel-kampagne" / "ttl" / "ttl-paar-b.md",
]

HOST = {"46.225.188.39": "mcs", "178.254.35.195": "1blue", "62.238.103.75": "hel"}

ARCHIVE_KOPF = [
    "# Datenschicht fuer fig:eval-ttl. Aggregiert aus den ttl-report.py-Tabellen der Messkampagnen.",
    "# Rohdaten (PCAPs) in thesis/evidence/: p0p1p2-kampagnen-1blu-mcs-20260814-15.tar.zst",
    "#   (SHA-256 644955e5bf51d03dd353273a5606e7e2bc9150c723393ddc9a2e889e85566dad),",
    "#   hel-kampagne-20260815.tar.zst (SHA-256 1545f30a5f2d1c97d0a55d657c7615f035fecb0fd6c7841a0944ce9ecf5bb063);",
    "#   Tabellenkopien in ff2-ttl-pfadanalyse-20260815.tar.zst",
    "#   (SHA-256 0e9cbbcd1391756e6e3f64a24058b571177b1ec5d0dd6b84710657b57e7aedca).",
    "# Werkzeug: scripts/ttl-report.py (Implementierungsrepo, Auswertungsstand f847895).",
    "# Einschlussregel: Die Richtungen des Paars 1blue/mcs enthalten neben den Kampagnen-Stamps die lokale,",
    "#   nicht versiegelte p1-checksumgate-Reihe (je Richtung 124 Egress- und 72 Ingress-Pakete, Differenz 52);",
    "#   die vier Helsinki-Richtungen enthalten nur die Kampagnen-Stamps, nicht die checksumgate-Stamps des",
    "#   hel-Archivs (je Richtung 51 Egress- und 31 Ingress-Pakete, Differenz 20). Nur mit Kampagnen-Stamps",
    "#   stimmen Egress und Ingress auf allen sechs Richtungen ueberein.",
]


def ableiten(quellen=None) -> None:
    agg = defaultdict(int)
    zeilen = 0
    for quelle in (quellen or QUELLEN):
        for line in quelle.read_text().splitlines():
            if not line.startswith("|") or line.startswith("|---") or "| Klasse |" in line or "| Datei |" in line:
                continue
            teile = [t.strip() for t in line.strip("|").split("|")]
            if len(teile) != 5:
                continue
            datei, klasse, pakete, ttlliste, fluss = teile
            if klasse == "-" or ttlliste == "-" or pakete == "0":
                continue
            m = re.match(r"([0-9.]+)->([0-9.]+)", fluss)
            if not m:
                continue
            src, dst = HOST.get(m.group(1)), HOST.get(m.group(2))
            if src is None or dst is None:
                continue
            seite = "egress" if "egress" in datei or "-eg" in datei else "ingress"
            for eintrag in ttlliste.split(","):
                ttl, anzahl = eintrag.split(":")
                agg[(f"{src}->{dst}", seite, klasse, int(ttl))] += int(anzahl)
            zeilen += 1
    with DATEN.open("w", newline="") as fh:
        for kopf in ARCHIVE_KOPF:
            fh.write(kopf + "\n")
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["richtung", "seite", "klasse", "ttl", "pakete"])
        for (richtung, seite, klasse, ttl), n in sorted(agg.items()):
            w.writerow([richtung, seite, klasse, ttl, n])
    print(f"{zeilen} Quellzeilen verarbeitet -> {DATEN}")
    # Kontrollwerte gegen die dokumentierten Berichte
    def summe(richtung, seite, klasse=None, ttl=None):
        return sum(n for (r, s, k, t), n in agg.items()
                   if r == richtung and s == seite and (klasse is None or k == klasse) and (ttl is None or t == ttl))
    kontrollen = [
        ("1blue->mcs ingress normal TTL 54 (S-53-Fenster)", summe("1blue->mcs", "ingress", "normal", 54), 137),
        ("1blue->mcs ingress canary TTL 54", summe("1blue->mcs", "ingress", "canary", 54), 10),
        ("1blue->hel ingress TTL 54", summe("1blue->hel", "ingress", ttl=54), 7136),
        ("1blue->hel ingress TTL 53", summe("1blue->hel", "ingress", ttl=53), 70),
        ("1blue->hel ingress canary TTL 53", summe("1blue->hel", "ingress", "canary", 53), 40),
        ("mcs->hel ingress TTL 51 gesamt", summe("mcs->hel", "ingress", ttl=51), 5236 + 1920 + 50),
        ("hel->mcs ingress TTL 51 gesamt", summe("hel->mcs", "ingress", ttl=51), 5236 + 1920 + 50),
        ("hel->1blue ingress TTL 52 gesamt", summe("hel->1blue", "ingress", ttl=52), 5236 + 1920 + 50),
    ]
    ok = True
    for name, ist, soll in kontrollen:
        status = "OK" if ist == soll else "ABWEICHUNG"
        if ist != soll:
            ok = False
        print(f"  Kontrolle {status}: {name}: ist {ist}, dokumentiert {soll}")
    for richtung in ["mcs->1blue", "1blue->mcs", "mcs->hel", "hel->mcs", "hel->1blue", "1blue->hel"]:
        eg = summe(richtung, "egress")
        eg64 = summe(richtung, "egress", ttl=64)
        print(f"  Egress {richtung}: {eg} Pakete, davon TTL 64: {eg64}")
        if eg != eg64:
            ok = False
            print("    ABWEICHUNG: Egress nicht einheitlich TTL 64")
    if not ok:
        sys.exit("Kontrollwerte abweichend; CSV nicht verwenden, Quellen pruefen.")


def generieren() -> None:
    agg = defaultdict(int)
    with DATEN.open() as fh:
        rows = [r for r in csv.reader(l for l in fh if not l.startswith("#"))]
    for richtung, seite, klasse, ttl, n in rows[1:]:
        agg[(richtung, seite, int(ttl))] += int(n)
    reihen = []  # (Anzeige, [(ttl, pakete, dominant)], Routerzahl-Text)
    for richtung, router in [("mcs->1blue", "11"), ("1blue->mcs", "11 / 10"), ("mcs->hel", "13"),
                             ("hel->mcs", "13"), ("hel->1blue", "12"), ("1blue->hel", "10 / 11")]:
        ttls = sorted(((t, n) for (r, s, t), n in agg.items() if r == richtung and s == "ingress"),
                      key=lambda x: -x[1])
        gesamt = sum(n for _, n in ttls)
        reihen.append((richtung, [(t, n, n == ttls[0][1]) for t, n in ttls], router, gesamt))
    eg_gesamt = sum(n for (r, s, t), n in agg.items() if s == "egress")
    zeilenhoehe = 0.82
    tex = []
    tex.append("% Generiert von thesis/tikz/gen/ttl-uniformitaet.py aus thesis/daten/ttl-verteilung.csv.")
    tex.append("% Nicht von Hand aendern; Aenderungen im Skript oder in der Datenschicht vornehmen.")
    tex.append("\\begin{tikzpicture}[")
    tex.append("  dominant/.style={draw=akzent, fill=akzenthell, rounded corners=2pt, semithick},")
    tex.append("  nebenzweig/.style={draw=sqgoldrand, fill=sqgold, rounded corners=2pt, semithick},")
    tex.append("  reihe/.style={font=\\footnotesize\\ttfamily},")
    tex.append("  wert/.style={font=\\footnotesize},")
    tex.append("  kopf/.style={font=\\footnotesize\\bfseries}]")
    tex.append("  \\node[kopf, anchor=west] at (0,0.9) {Richtung};")
    tex.append("  \\node[kopf, anchor=west] at (3.35,0.9) {Ankunfts-TTL (Pakete)};")
    tex.append("  \\node[kopf, anchor=east] at (12.9,0.9) {Router\\textsuperscript{*}};")
    for i, (richtung, ttls, router, gesamt) in enumerate(reihen):
        y = -i * zeilenhoehe
        anzeige = richtung.replace("->", " $\\rightarrow$ ")
        tex.append(f"  \\node[reihe, anchor=west] at (0,{y:.2f}) {{{anzeige}}};")
        x = 3.35
        for ttl, n, dom in ttls:
            stil = "dominant" if dom else "nebenzweig"
            breite = 3.0 if dom else 2.6
            tex.append(f"  \\node[{stil}, wert, anchor=west, minimum height=5.4mm, minimum width={breite}cm] "
                       f"at ({x:.2f},{y:.2f}) {{TTL {ttl}: {n}}};")
            x += breite + 0.25
        tex.append(f"  \\node[wert, anchor=east] at (12.9,{y:.2f}) {{{router}}};")
    y_fuss = -len(reihen) * zeilenhoehe - 0.15
    tex.append(f"  \\node[wert, anchor=north west, text=feldlinie, text width=12.6cm, align=left] "
               f"at (0,{y_fuss:.2f}) "
               f"{{Gesendet: alle {eg_gesamt} erfassten Egress-Pakete einheitlich TTL 64; "
               f"\\textsuperscript{{*}}abgeleitet unter der Annahme von genau einem Dekrement je "
               f"Weiterleitung}};")
    tex.append("\\end{tikzpicture}")
    FRAGMENT.write_text("\n".join(tex) + "\n")
    print(f"geschrieben: {FRAGMENT}")
    for richtung, ttls, router, gesamt in reihen:
        print(f"  {richtung}: " + ", ".join(f"TTL {t}={n}" for t, n, _ in ttls) + f" (gesamt {gesamt})")


if __name__ == "__main__":
    if "--ableiten" in sys.argv:
        tabellen = [Path(a) for a in sys.argv[1:] if a != "--ableiten"]
        ableiten(tabellen or None)
    else:
        generieren()
