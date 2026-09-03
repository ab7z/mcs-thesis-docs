#!/usr/bin/env python3
"""Datenschicht fuer die FF1-Einzelbewertung der 67 Matrixzeilen.

Quelle: docs/requirements.md Abschnitt 3 des Implementierungsrepos am Auswertungsstand f847895
(Zeilen 162 bis 228; Spalten RFC area, Normative item, Level, Covered, Step, Notes). Die Spalten
level und covered geben diese Repository-Selbstauskunft inhaltlich wieder. Die Spalten normstufe,
anwendbar, kategorie und technisch tragen die am RFC-Primaertext und am Quelltext gepruefen Urteile
dieser Arbeit; Anwendbarkeit (A), Implementierungsstand (I) und technische Erfuellbarkeit (T) sind
seit der Zweitpruefung vom 2026-08-28 je Zeile getrennt gespeichert und werden unten nur noch auf
Konsistenz geprueft, nicht mehr voneinander abgeleitet.

Aenderungsstand 2026-08-28 (Zweitpruefung der Faktencheckrunde, verifiziert an RFC 9868 und am
Stand f847895):
  * Zeile 189: Anmerkung nennt Sec. 25.2 statt 25.3 als Fundstelle der Ressourcengrenze.
  * Zeile 199: bleibt I=P; der Beleg kennzeichnet die eigene Korrektur der Selbstauskunft
    "Covered yes" am Stand f847895.
  * Zeilen 216 und 221 (Sec. 14/15): vollstaendig -> teilweise. src/recv/pipeline.rs fuellt
    options nur in den Success-Zweigen; OptionReport traegt Kind, Status und Quelle. Bei Ignored
    und Failed sind die empfangenen Parameter ueber keinen oeffentlichen Pfad erreichbar, waehrend
    Sec. 15 "the per-packet options and their parameters as received" verlangt.
  * Zeile 226 (Sec. 25.2): teilweise -> nicht anwendbar. Das SHOULD zur empfangsseitigen
    Referenzordnung ist an das vorangehende, nicht gewaehlte MAY gebunden; der fruehere Beleg
    FR-14 betrifft nur die sendeseitige Ordnung (Zeile 186).

Fruehere Aenderungen (dritte Faktencheckrunde, 2026-08-26): Zeile 189 teilweise -> vollstaendig
(Sec. 11.2 verlangt nur Erkennung und Meldung); Zeile 222 nicht anwendbar -> teilweise (unmarkierte
normative Festlegung der Sec.-15-Einleitung). Zeile 224 buendelt eine Transit- und eine
Endpunktpflicht; nur die Endpunkthaelfte ist FF1-Gegenstand, die Zeile bleibt ungeteilt.

Das Skript schreibt thesis/daten/konformitaet-kategorien.csv und prueft die Summen (67 Zeilen;
Gruppen 8/17/22/9/7/4; Implementierungsstand 50/7/0/10; technische Erfuellbarkeit 57 vollstaendig,
0 teilweise, 0 nicht erfuellbar, 10 nicht anwendbar).
"""
import csv
from collections import Counter, OrderedDict
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
CSV = REPO / "thesis" / "daten" / "konformitaet-kategorien.csv"

V, T, N, A = "vollstaendig", "teilweise", "nicht erfuellbar", "nicht anwendbar"

# (quellzeile, gruppe, rfc_bereich, kurzinhalt, level, covered, normstufe,
#  anwendbar, kategorie, technisch, beleg, anmerkung)
# anwendbar, kategorie (= Implementierungsstand I) und technisch (= T) sind drei getrennt
# gespeicherte Einzelurteile; die Asserts unten pruefen ihre Konsistenz, leiten aber nichts ab.
ZEILEN = [
    (162, "Sec. 10", "10", "Ungueltige UDP-Laenge verwerfen und melden", "MUST", "yes", "MUST", "ja", V, V,
     "R; FR-49", ""),
    (163, "Sec. 7-9", "7", "Surplus Area hinter dem Ende gemaess UDP-Laenge", "MUST", "yes", "Festlegung", "ja", V,
     V, "W; FR-04", "Sec. 7 traegt keinen markierten Absatz"),
    (164, "Sec. 7-9", "8", "Ganze Surplus Area nutzen; OCS an erster Zweiergrenze", "MUST", "yes", "Festlegung",
     "ja", V, V, "W, O; FR-04/19", "beschreibender Eroeffnungssatz von Sec. 8"),
    (165, "Sec. 7-9", "8", "Pad vor OCS null, sonst Optionen verwerfen", "MUST", "yes", "MUST", "ja", V, V,
     "W, R; FR-05; S-04", "real belegt (S-04, G-Zelle)"),
    (166, "Sec. 7-9", "9", "OCS ueber Bereich und 16-Bit-Laengensummand", "MUST", "yes", "Festlegung", "ja", V, V,
     "O; FR-19; Wire-Pruefung", ""),
    (167, "Sec. 7-9", "9", "OCS nicht null, wenn UDP-Pruefsumme nicht null", "MUST", "yes", "MUST", "ja", V, V,
     "O; FR-21; S-06", ""),
    (168, "Sec. 7-9", "9", "Nichtnull-OCS als Voreinstellung", "MUST", "yes", "MUST", "ja", V, V, "O, A; FR-21", ""),
    (169, "Sec. 7-9", "9", "Bei OCS-Fehler Optionen und Surplus verwerfen", "MUST", "yes", "MUST", "ja", V, V,
     "R; FR-20; S-05", "real belegt (S-05)"),
    (170, "Sec. 7-9", "9/14", "Gueltige Nutzdaten trotz OCS-Fehler standardmaessig liefern", "MUST", "yes", "MUST",
     "ja", V, V, "R; FR-38; S-06", "S-06-Matrix real"),
    (171, "Sec. 10", "10", "TLV-Rahmung und erweitertes Laengenformat", "MUST", "yes", "Festlegung", "ja", V, V,
     "O; FR-07/09", ""),
    (172, "Sec. 10", "10", "NOP und EOL ohne Laengenfeld", "MUST", "yes", "Festlegung", "ja", V, V, "O; FR-08",
     "im markierten Absatz, aber ohne eigenes Schluesselwort"),
    (173, "Sec. 10", "10", "Laenge unter Formatminimum verwirft alle Optionen", "MUST", "yes", "MUST", "ja", V, V,
     "O, R; FR-10; S-11a", "S-11a real"),
    (174, "Sec. 10", "10", "Unterlauf oder Ueberlauf macht den Bereich ungueltig", "MUST", "yes", "MUST", "ja", V, V,
     "O, R; FR-10/50; S-11b", "S-11b real; Erratum 8834"),
    (175, "Sec. 10", "10", "Bekannte Option unter Mindestlaenge verwirft alle Optionen", "MUST", "yes", "MUST", "ja",
     V, V, "O, R; FR-11/12", ""),
    (176, "Sec. 10", "10", "Ab 255 erweitern; kleinste Kodierung bevorzugen", "MUST/SHOULD",
     "yes (send); local strict receive", "MUST/SHOULD", "ja", V, V, "O; FR-09/14",
     "dokumentierte lokale Empfangsstrenge"),
    (177, "Sec. 10", "10/14", "Optionen in Drahtreihenfolge verarbeiten", "MUST", "yes", "MUST", "ja", V, V,
     "O, R; FR-13", ""),
    (178, "Sec. 10", "10", "Acht Pflichtoptionen erkennen und bei Konfiguration erzeugen", "MUST", "yes", "MUST",
     "ja", V, V, "O; FR-06/14/22 bis 31", "real P0 (sopt)"),
    (179, "Sec. 10", "10", "Unbekannte SAFE-Optionen still uebergehen", "MUST", "yes", "MUST", "ja", V, V,
     "O, R; FR-11/12; S-10", "S-10 real"),
    (180, "Sec. 10", "10", "Defektes FRAG wie nicht unterstuetzte UNSAFE-Option", "MUST", "yes", "MUST", "ja", V, V,
     "R, F; FR-27", ""),
    (181, "Sec. 10", "10", "Bestimmte Optionen nur einmal; erste Instanz gilt", "SHOULD/MUST", "yes", "SHOULD/MUST",
     "ja", V, V, "O, R; FR-15", ""),
    (182, "Sec. 10", "10", "NOP darf sich zur Ausrichtung wiederholen", "MAY", "yes", "MAY", "ja", V, V, "O; FR-16",
     "gewaehlte MAY, Lauflimit 7"),
    (183, "Sec. 10", "10", "Mehrere FRAG machen den Optionsbereich ungueltig", "MUST", "yes", "MUST", "ja", V, V,
     "R, F; FR-29", ""),
    (184, "Sec. 10", "10", "Bei UNSAFE Nutzdaten leer und Inhalt im FRAG", "MUST", "yes (by construction)", "MUST",
     "ja", V, V, "R, F; FR-28/39", ""),
    (185, "Sec. 10", "10", "Erste unbekannte UNSAFE beendet die Verarbeitung", "MUST", "yes", "MUST", "ja", V, V,
     "R; FR-39; S-20", "S-20 real; Schritt-18-Fall"),
    (186, "Sec. 10", "10", "Pflichtoptionen ausser NOP/EOL vor anderen SAFE senden", "MUST/MAY", "yes", "MUST/MAY",
     "ja", V, V, "O, A; FR-14", ""),
    (187, "Sec. 11.x", "11.1", "Bei Restplatz EOL zuletzt; danach null senden", "MUST", "yes", "MUST", "ja", V, V,
     "O; FR-17; S-08", "S-08 real"),
    (188, "Sec. 11.x", "11.1", "Optionale Nullpruefung nach EOL samt Verwerfregel", "MUST (bedingt)/MAY",
     "not selected", "MAY/MUST", "nein", A, A, "FR-18; nicht gewaehlt", "nicht gewaehlte MAY-Pruefung (FR-18)"),
    (189, "Sec. 11.x", "11.2", "Hoechstens sieben aufeinanderfolgende NOP; dauerhafte Laeufe melden", "SHOULD",
     "partial", "SHOULD", "ja", V, V, "O, R; FR-16; NFR-05",
     "geprueft 2026-08-26: Sec. 11.2 verlangt Erkennung und Meldung, keinen Fruehabbruch; die Ressourcengrenze steht im bedingten SHOULD von Sec. 25.2 (Zeile 225)"),
    (190, "Sec. 11.x", "11.3", "APC als CRC32C; Fehlschlag angezeigt zustellen", "MUST/SHOULD", "yes",
     "Festlegung/SHOULD", "ja", V, V, "O, R; FR-22/23", "S-13 real"),
    (191, "Sec. 11.x", "11.3", "Unbekannte APC-Laenge wie fehlgeschlagene APC", "MUST", "yes", "MUST", "ja", V, V,
     "O, R; FR-12/23", ""),
    (192, "Sec. 11.x", "11.4", "FRAG-Laenge 10 oder 12 abhaengig von RDOS", "MUST", "yes", "Festlegung", "ja", V, V,
     "F; FR-26; S-19", "S-19 real"),
    (193, "Sec. 11.x", "11.4", "Bei FRAG sind UDP-Nutzdaten leer", "MUST", "yes", "MUST", "ja", V, V, "R, F; FR-28",
     ""),
    (194, "Sec. 11.x", "11.4", "Mindestens zwei Fragmente, jedes in 1500 Byte, reassemblieren", "MUST", "yes",
     "MUST", "ja", V, V, "F; FR-35; S-frag", "real (sfrag)"),
    (195, "Sec. 11.x", "11.4", "Kennung ueber den Timeout eindeutig; Erzeugung empfohlen", "MUST/SHOULD", "yes",
     "MUST/SHOULD", "ja", V, V, "F; FR-31; S-46", "S-46 real; Kollisionsfall als Normluecke"),
    (196, "Sec. 11.x", "11.4", "Ueberlappung abbrechen und ohne ICMP verwerfen", "MUST", "yes", "MUST", "ja", V, V,
     "F; FR-32/48; S-45", "S-45 real, auch byteidentisch"),
    (197, "Sec. 11.x", "11.4", "Exakte Duplikate duerfen verworfen werden", "MAY", "yes", "MAY", "ja", V, V,
     "F; FR-32; S-45 Z0", "gewaehlte MAY"),
    (198, "Sec. 11.x", "11.4", "Standardtimeout hoechstens zwei Minuten; kein ICMP", "SHOULD/MUST", "yes",
     "SHOULD/MUST", "ja", V, V, "F; FR-33; S-42", "S-42 real (nur Negativevidenz)"),
    (199, "Sec. 11.x", "11.4", "Speicher begrenzen und nicht socketuebergreifend teilen", "SHOULD", "yes", "SHOULD",
     "ja", T, V, "F, A; FR-34; NFR-06; eigene Korrektur von f847895",
     "Vertrag dokumentiert, Peer-Ebene loest ihn nur teilweise ein"),
    (200, "Sec. 11.x", "11.4", "Einzelne Fragmente nie an den Nutzer geben", "MUST", "yes", "MUST", "ja", V, V,
     "R, F; FR-31", ""),
    (201, "Sec. 11.x", "11.4", "Fehlgeschlagene Reassemblierung ohne Leerdatagramm", "SHOULD", "yes", "SHOULD", "ja",
     V, V, "R, F; FR-33; S-49", "S-49 real"),
    (202, "Sec. 11.x", "11.5", "MDS verarbeiten; MDS begrenzt das Senden nicht", "MUST", "yes", "MUST", "ja", V, V,
     "O, A; FR-24", "real (1400 nach MDS 1200)"),
    (203, "Sec. 11.x", "11.6", "MRDS-Mindestwerte und Voreinstellungen fuer IPv4", "MUST", "yes (IPv4)", "MUST",
     "ja", V, V, "O, F; FR-35", "IPv6-Anteil ausserhalb des Umfangs"),
    (204, "Sec. 11.x", "11.7", "REQ/RES ohne Autoantwort; RES-Token aus empfangenem REQ", "MUST", "delegated",
     "Festlegung/MUST", "ja", V, V, "O, A; FR-25; Vertrag",
     "RFC weist der Anwendung zu; Vertrag dokumentiert; s14 real still"),
    (205, "Sec. 11.x", "11.7", "Automatische REQ/RES-Schicht standardmaessig aus", "MUST", "yes (vacuous)", "MUST",
     "ja", V, V, "A; keine solche Schicht", "leer erfuellt, keine solche Schicht"),
    (206, "Sec. 11.x", "11.8", "TIME optional; verwendete Zeitwerte nie null", "MUST (wenn implementiert)", "out",
     "MAY/MUST", "nein", A, A, "nicht gewaehlt; S-23 Parser",
     "geprueft 2026-08-26: Sec. 11.8 fuehrt TIME als MAY; nur die Nullregel ist ein MUST NOT"),
    (207, "Sec. 11.x", "11.9", "AUTH ist reserviert", "reserviert", "out", "reserviert", "nein", A, A,
     "nicht definiert", ""),
    (208, "Sec. 11.x", "11.10", "EXP bei Wahl mit Mindestlaenge vier", "MUST (wenn implementiert)", "out", "MUST",
     "nein", A, A, "nicht gewaehlt", ""),
    (209, "Sec. 12-14", "12", "UCMP und UENC reserviert; UEXP als UNSAFE-Experimentoption", "reserviert", "out",
     "reserviert", "nein", A, A, "nicht definiert",
     "Kind 254 analog EXP (Kind 127); UCMP/UENC bleiben Reservierungen"),
    (210, "Sec. 12-14", "12", "UNSAFE nur in Fragmenten; unbekannte Art verwirft Daten", "MUST", "yes (drop side)",
     "MUST", "ja", V, V, "R, F; FR-39", ""),
    (211, "Sec. 12-14", "13", "Entwurfsregeln fuer neue Optionsarten", "MUST", "n/a", "MUST", "nein", A, A,
     "keine neue Optionsart", "keine neuen Optionen definiert"),
    (212, "Sec. 12-14", "14", "Empfangsfolge Pruefsumme, OCS, Optionen, Zustellung", "MUST", "yes", "Festlegung",
     "ja", V, V, "R; FR-36", ""),
    (213, "Sec. 12-14", "14", "Vorhandene Pflichtoptionen verarbeiten", "MUST", "yes", "MUST", "ja", V, V,
     "R; FR-06/36", ""),
    (214, "Sec. 12-14", "14", "Andere Optionsarten duerfen ignoriert werden", "MAY", "yes", "MAY", "ja", V, V,
     "R, A; gewaehlt", "gewaehlt, konfigurierbar"),
    (215, "Sec. 12-14", "14", "Nutzdaten bei SAFE unabhaengig vom Ergebnis liefern", "MUST", "yes", "MUST", "ja", V,
     V, "R; FR-38", ""),
    (216, "Sec. 12-14", "14", "FRAG/NOP/EOL intern; uebrige Status bereitstellen", "MUST", "yes", "MUST", "ja", T, V,
     "R, A; FR-37; Parameter nicht immer verfuegbar",
     "geprueft 2026-08-28: options nur in den Success-Zweigen gefuellt; OptionReport traegt Kind, Status und Quelle, nicht die Parameter"),
    (217, "Sec. 12-14", "14", "Optionsueberlauf nach Abschnitt 10 behandeln", "MUST", "yes", "MUST", "ja", V, V,
     "O, R; FR-50; Erratum 8834", "S-11b real"),
    (218, "Sec. 15-19", "15", "Empfangs-API: je Paket und Fragment gefordert oder aus", "MUST", "partial",
     "Normform", "ja", T, V, "A; FR-44", "nur gebuendelte, keine fragmentweise Steuerung"),
    (219, "Sec. 15-19", "15", "Fehlende Pflichtoption still verwerfen und melden", "MUST", "partial", "MUST/SHOULD",
     "ja", T, V, "A; FR-44", "quellagnostisch, nicht je Quellebene"),
    (220, "Sec. 15-19", "15", "Schalter fuer alle Optionsdatagramme; Standard verarbeiten", "MUST", "yes",
     "Normform/MUST", "ja", V, V, "A; FR-44", ""),
    (221, "Sec. 15-19", "15", "Optionen und Status fuer Nutzer verfuegbar", "MUST", "yes", "Normform/MUST", "ja", T,
     V, "R, A; FR-37; Parameter nicht immer verfuegbar",
     "geprueft 2026-08-28: options nur in den Success-Zweigen gefuellt; OptionReport traegt Kind, Status und Quelle, nicht die Parameter"),
    (222, "Sec. 15-19", "15", "Sende-API: Auswahl, Geltung, Mindestlaenge, Maximalfragment", "ohne BCP-14",
     "partial", "Normform", "ja", T, V, "A; SendConfig/Options",
     "geprueft 2026-08-26: unmarkierte Festlegung der Sec.-15-Einleitung, daher anwendbar; Optionsauswahl umgesetzt, Fragmentgeltung und Mindestlaenge nicht"),
    (223, "Sec. 15-19", "15/25", "Keine direkte Ordnungs- oder Fragmentgrenzensteuerung", "guidance", "yes",
     "Leitlinie", "nein", A, A, "A; kanonisiert", "Leitlinie ohne BCP-14; als Kanonisierung umgesetzt"),
    (224, "Sec. 15-19", "16/19", "Transit unveraendert (nicht FF1); SAFE-Fehler ignorieren und Nutzdaten liefern",
     "MUST", "yes (endpoint side)", "MUST", "ja", V, V,
     "R, A; FR-38 fuer Endpunkt; Transit: K, nicht als I bewertet",
     "geprueft 2026-08-26: Transitpflicht aus Sec. 16 ist FF2-Messgegenstand, Endpunktpflichten aus Sec. 19 sind FF1-Gegenstand"),
    (225, "Sec. 23-26", "25", "Bei DoS-Bedenken Grenzen fuer Optionen, NOP und Fragmente", "SHOULD",
     "partial / documented opt-out", "bed. SHOULD", "ja", T, V, "R, F; NFR-04/05/06/08",
     "NFR-04 begruendeter Verzicht; NFR-05 teilweise; NFR-06/08 umgesetzt"),
    (226, "Sec. 23-26", "25.2", "Bei Kanalbedenken Optionen in unabhaengiger Referenzordnung", "SHOULD", "partial",
     "bed. SHOULD", "nein", A, A, "nicht gewaehlt; kanonische Sendereihenfolge genuegt nicht",
     "geprueft 2026-08-28: das SHOULD aus Sec. 25.2 ist an das vorangehende, nicht gewaehlte MAY gebunden; FR-14 belegt nur die sendeseitige Ordnung (Zeile 186)"),
    (227, "Sec. 23-26", "23", "Multicast und Broadcast gesondert betrachten", "special", "out", "Leitlinie", "nein",
     A, A, "nur Unicast", "nur Unicast untersucht"),
    (228, "Sec. 23-26", "26", "Namensregeln fuer neue SAFE- und UNSAFE-Arten", "MUST", "n/a", "MUST", "nein", A, A,
     "keine neue Art", "keine neuen Kinds registriert"),
]

GRUPPEN_SOLL = OrderedDict([("Sec. 7-9", 8), ("Sec. 10", 17), ("Sec. 11.x", 22),
                            ("Sec. 12-14", 9), ("Sec. 15-19", 7), ("Sec. 23-26", 4)])

assert len(ZEILEN) == 67, f"Zeilenzahl {len(ZEILEN)} statt 67"
gruppen = Counter(z[1] for z in ZEILEN)
for g, soll in GRUPPEN_SOLL.items():
    assert gruppen[g] == soll, f"Gruppe {g}: {gruppen[g]} statt {soll}"
quellzeilen = [z[0] for z in ZEILEN]
assert sorted(quellzeilen) == list(range(162, 229)), "Quellzeilen nicht lueckenlos 162..228"

for z in ZEILEN:
    anw, kat, tec = z[7], z[8], z[9]
    assert anw in ("ja", "nein") and kat in (V, T, N, A) and tec in (V, T, N, A), f"Zeile {z[0]}"
    # Schemaregel: nicht anwendbare Zeilen tragen weder Implementierungs- noch Technikurteil.
    assert (anw == "nein") == (kat == A) == (tec == A), f"Zeile {z[0]}: A/I/T inkonsistent"

impl = Counter(z[8] for z in ZEILEN)
tech = Counter(z[9] for z in ZEILEN)
assert (impl[V], impl[T], impl[N], impl[A]) == (50, 7, 0, 10), f"Implementierungsstand {dict(impl)}"
assert (tech[V], tech[T], tech[N], tech[A]) == (57, 0, 0, 10), f"Technische Erfuellbarkeit {dict(tech)}"
assert [z[0] for z in ZEILEN if z[8] == T] == [199, 216, 218, 219, 221, 222, 225], "Teilmenge falsch"
assert [z[0] for z in ZEILEN if z[8] == A] == [188, 206, 207, 208, 209, 211, 223, 226, 227, 228], \
    "Menge der nicht anwendbaren Zeilen falsch"

with CSV.open("w", newline="") as fh:
    fh.write("# Vollstaendige FF1-Einzelbewertung der 67 Matrixzeilen.\n")
    fh.write("# Quelle: docs/requirements.md\n")
    fh.write("# Abschnitt 3 (Zeilen 162-228) am Auswertungsstand f847895. Die Spalten level und\n")
    fh.write("# covered geben die Repository-Selbstauskunft wieder; normstufe, anwendbar, kategorie\n")
    fh.write("# (Implementierungsstand) und technisch tragen die am RFC-Primaertext gepruefen\n")
    fh.write("# Urteile dieser Arbeit als drei getrennt gespeicherte Einzelurteile, Pruefstand\n")
    fh.write("# 2026-08-28. Erzeugt und geprueft von thesis/tikz/gen/ff1-kategorien.py (Asserts:\n")
    fh.write("# 67 Zeilen; Gruppen 8/17/22/9/7/4; Implementierung 50/7/0/10; technisch 57/0/0/10).\n")
    w = csv.writer(fh)
    w.writerow(["quellzeile", "gruppe", "rfc_bereich", "kurzinhalt", "level", "covered",
                "normstufe", "anwendbar", "kategorie", "technisch", "beleg", "anmerkung"])
    for z in ZEILEN:
        w.writerow(list(z))

print(f"geschrieben: {CSV} (67 Zeilen)")
print("Implementierungsstand:", {k: v for k, v in impl.items()})
print("Technische Erfuellbarkeit:", {k: v for k, v in tech.items()})
print(f"{'Gruppe':<11} {'n':>2} {'voll':>4} {'teil':>4} {'n.erf':>5} {'n.anw':>5}")
for g in GRUPPEN_SOLL:
    c = Counter(z[8] for z in ZEILEN if z[1] == g)
    print(f"{g:<11} {gruppen[g]:>2} {c[V]:>4} {c[T]:>4} {c[N]:>5} {c[A]:>5}")
