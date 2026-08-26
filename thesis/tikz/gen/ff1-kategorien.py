#!/usr/bin/env python3
"""Datenschicht fuer Tabelle 6.2: FF1-Einzelbewertung der 67 Konformitaetsmatrix-Zeilen.

Quelle: docs/requirements.md Abschnitt 3 des Implementierungsrepos am Auswertungsstand f847895
(Zeilen 162 bis 228; Spalten RFC area, Normative item, Level, Covered, Step, Notes). Die Spalten
level und covered geben diese Repository-Selbstauskunft unveraendert wieder. Die Spalten normstufe,
anwendbar, kategorie und technisch tragen dagegen die am RFC-Primaertext geprueften Urteile dieser
Arbeit (Pruefstand 2026-08-26, dritte Faktencheckrunde); sie sind damit nicht mehr die Zuordnung
"vor der Korrektur", sondern der entschiedene Stand.

Geprueft und gegenueber dem Stand vor der Korrektur veraendert wurden zwei Zeilen:
  * Zeile 189 (Sec. 11.2): teilweise -> vollstaendig. Sec. 11.2 verlangt vom Empfaenger nur das
    gelegentliche Melden dauerhafter NOP-Laeufe ueber sieben, keinen Fruehabbruch; die geforderte
    Ressourcenbegrenzung steht im bedingten SHOULD von Sec. 25.3 und wird bereits in Zeile 225
    als teilweise gefuehrt.
  * Zeile 222 (Sec. 15): nicht anwendbar -> teilweise. Die Sende-API-Form gehoert zur Einleitung
    "This API is extended to support options as follows" und ist damit eine unmarkierte normative
    Festlegung, keine blosse Leitlinie wie Zeile 223. Optionsauswahl und kanonische EOL-Nullfuellung
    sind umgesetzt, getrennte Optionslisten je Fragment und eine aufrufergesteuerte Mindestlaenge
    nicht.
Zeile 224 buendelt eine Transit- und eine Endpunktpflicht; nur die Endpunkthaelfte ist FF1-Gegenstand,
die Transitpflicht ist FF2-Messgegenstand. Die Gesamteinstufung der Zeile aendert sich dadurch nicht.

Das Skript schreibt thesis/daten/konformitaet-kategorien.csv und thesis/tikz/ff1-sollist.tex
(Tabelle 6.2) und prueft die Summen (67 Zeilen; Gruppen 8/17/22/9/7/4; Implementierungsstand
52/6/0/9; technische Erfuellbarkeit 58 vollstaendig, 0 teilweise, 0 nicht erfuellbar, 9 nicht
anwendbar).
"""
import csv
from collections import Counter, OrderedDict
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
CSV = REPO / "thesis" / "daten" / "konformitaet-kategorien.csv"
FRAGMENT = REPO / "thesis" / "tikz" / "ff1-sollist.tex"

V, T, N, A = "vollstaendig", "teilweise", "nicht erfuellbar", "nicht anwendbar"

# (quellzeile, gruppe, rfc_bereich, kurzinhalt, level, covered, normstufe, kategorie, beleg, anmerkung)
# kategorie = Implementierungsstand; die technische Erfuellbarkeit leitet sich daraus ab (siehe unten).
ZEILEN = [
    (162, "Sec. 10", "10", "Ungueltige UDP-Laenge verwerfen und melden", "MUST", "yes", "MUST", V,
     "R; FR-49", ""),
    (163, "Sec. 7-9", "7", "Surplus Area hinter dem Ende gemaess UDP-Laenge", "MUST", "yes",
     "Festlegung", V, "W; FR-04", "Sec. 7 traegt keinen markierten Absatz"),
    (164, "Sec. 7-9", "8", "Ganze Surplus Area nutzen; OCS an erster Zweiergrenze", "MUST", "yes",
     "Festlegung", V, "W, O; FR-04/19", "beschreibender Eroeffnungssatz von Sec. 8"),
    (165, "Sec. 7-9", "8", "Pad vor OCS null, sonst Optionen verwerfen", "MUST", "yes", "MUST", V,
     "W, R; FR-05; S-04", "real belegt (S-04, G-Zelle)"),
    (166, "Sec. 7-9", "9", "OCS ueber Bereich und 16-Bit-Laengensummand", "MUST", "yes",
     "Festlegung", V, "O; FR-19; Wire-Pruefung", ""),
    (167, "Sec. 7-9", "9", "OCS nicht null, wenn UDP-Pruefsumme nicht null", "MUST", "yes", "MUST",
     V, "O; FR-21; S-06", ""),
    (168, "Sec. 7-9", "9", "Nichtnull-OCS als Voreinstellung", "MUST", "yes", "MUST", V,
     "O, A; FR-21", ""),
    (169, "Sec. 7-9", "9", "Bei OCS-Fehler Optionen und Surplus verwerfen", "MUST", "yes", "MUST",
     V, "R; FR-20; S-05", "real belegt (S-05)"),
    (170, "Sec. 7-9", "9/14", "Gueltige Nutzdaten trotz OCS-Fehler standardmaessig liefern", "MUST",
     "yes", "MUST", V, "R; FR-38; S-06", "S-06-Matrix real"),
    (171, "Sec. 10", "10", "TLV-Rahmung und erweitertes Laengenformat", "MUST", "yes",
     "Festlegung", V, "O; FR-07/09", ""),
    (172, "Sec. 10", "10", "NOP und EOL ohne Laengenfeld", "MUST", "yes", "Festlegung", V,
     "O; FR-08", "im markierten Absatz, aber ohne eigenes Schluesselwort"),
    (173, "Sec. 10", "10", "Laenge unter Formatminimum verwirft alle Optionen", "MUST", "yes",
     "MUST", V, "O, R; FR-10; S-11a", "S-11a real"),
    (174, "Sec. 10", "10", "Unterlauf oder Ueberlauf macht den Bereich ungueltig", "MUST", "yes",
     "MUST", V, "O, R; FR-10/50; S-11b", "S-11b real; Erratum 8834"),
    (175, "Sec. 10", "10", "Bekannte Option unter Mindestlaenge verwirft alle Optionen", "MUST",
     "yes", "MUST", V, "O, R; FR-11/12", ""),
    (176, "Sec. 10", "10", "Ab 255 erweitern; kleinste Kodierung bevorzugen", "MUST/SHOULD",
     "yes (send); local strict receive", "MUST/SHOULD", V, "O; FR-09/14",
     "dokumentierte lokale Empfangsstrenge"),
    (177, "Sec. 10", "10/14", "Optionen in Drahtreihenfolge verarbeiten", "MUST", "yes", "MUST", V,
     "O, R; FR-13", ""),
    (178, "Sec. 10", "10", "Acht Pflichtoptionen erkennen und bei Konfiguration erzeugen", "MUST",
     "yes", "MUST", V, "O; FR-06/14/22 bis 31", "real P0 (sopt)"),
    (179, "Sec. 10", "10", "Unbekannte SAFE-Optionen still uebergehen", "MUST", "yes", "MUST", V,
     "O, R; FR-11/12; S-10", "S-10 real"),
    (180, "Sec. 10", "10", "Defektes FRAG wie nicht unterstuetzte UNSAFE-Option", "MUST", "yes",
     "MUST", V, "R, F; FR-27", ""),
    (181, "Sec. 10", "10", "Bestimmte Optionen nur einmal; erste Instanz gilt", "SHOULD/MUST",
     "yes", "SHOULD/MUST", V, "O, R; FR-15", ""),
    (182, "Sec. 10", "10", "NOP darf sich zur Ausrichtung wiederholen", "MAY", "yes", "MAY", V,
     "O; FR-16", "gewaehlte MAY, Lauflimit 7"),
    (183, "Sec. 10", "10", "Mehrere FRAG machen den Optionsbereich ungueltig", "MUST", "yes",
     "MUST", V, "R, F; FR-29", ""),
    (184, "Sec. 10", "10", "Bei UNSAFE Nutzdaten leer und Inhalt im FRAG", "MUST",
     "yes (by construction)", "MUST", V, "R, F; FR-28/39", ""),
    (185, "Sec. 10", "10", "Erste unbekannte UNSAFE beendet die Verarbeitung", "MUST", "yes",
     "MUST", V, "R; FR-39; S-20", "S-20 real; Schritt-18-Fall"),
    (186, "Sec. 10", "10", "Pflichtoptionen ausser NOP/EOL vor anderen SAFE senden", "MUST/MAY",
     "yes", "MUST/MAY", V, "O, A; FR-14", ""),
    (187, "Sec. 11.x", "11.1", "Bei Restplatz EOL zuletzt; danach null senden", "MUST", "yes",
     "MUST", V, "O; FR-17; S-08", "S-08 real"),
    (188, "Sec. 11.x", "11.1", "Optionale Nullpruefung nach EOL samt Verwerfregel",
     "MUST (bedingt)/MAY", "not selected", "MAY/MUST", A, "FR-18; nicht gewaehlt",
     "nicht gewaehlte MAY-Pruefung (FR-18)"),
    (189, "Sec. 11.x", "11.2", "Sender hoechstens sieben NOP; dauerhafte Faelle melden", "SHOULD",
     "partial", "SHOULD", V, "O, R; FR-16; NFR-05",
     "geprueft 2026-08-26: Sec. 11.2 verlangt Erkennung und Meldung, keinen Fruehabbruch; "
     "die Ressourcengrenze steht im bedingten SHOULD von Sec. 25.3 (Zeile 225)"),
    (190, "Sec. 11.x", "11.3", "APC als CRC32C; Fehlschlag angezeigt zustellen",
     "MUST/SHOULD", "yes", "Festlegung/SHOULD", V, "O, R; FR-22/23", "S-13 real"),
    (191, "Sec. 11.x", "11.3", "Unbekannte APC-Laenge wie fehlgeschlagene APC", "MUST", "yes",
     "MUST", V, "O, R; FR-12/23", ""),
    (192, "Sec. 11.x", "11.4", "FRAG-Laenge 10 oder 12 abhaengig von RDOS", "MUST", "yes",
     "Festlegung", V, "F; FR-26; S-19", "S-19 real"),
    (193, "Sec. 11.x", "11.4", "Bei FRAG sind UDP-Nutzdaten leer", "MUST", "yes", "MUST", V,
     "R, F; FR-28", ""),
    (194, "Sec. 11.x", "11.4", "Mindestens zwei Fragmente in 1500 Byte reassemblieren", "MUST",
     "yes", "MUST", V, "F; FR-35; S-frag", "real (sfrag)"),
    (195, "Sec. 11.x", "11.4", "Kennung ueber den Timeout eindeutig; Erzeugung empfohlen",
     "MUST/SHOULD", "yes", "MUST/SHOULD", V, "F; FR-31; S-46",
     "S-46 real; Kollisionsfall als Normluecke"),
    (196, "Sec. 11.x", "11.4", "Ueberlappung abbrechen und ohne ICMP verwerfen", "MUST", "yes",
     "MUST", V, "F; FR-32/48; S-45", "S-45 real, auch byteidentisch"),
    (197, "Sec. 11.x", "11.4", "Exakte Duplikate duerfen verworfen werden", "MAY", "yes", "MAY", V,
     "F; FR-32; S-45 Z0", "gewaehlte MAY"),
    (198, "Sec. 11.x", "11.4", "Standardtimeout hoechstens zwei Minuten; kein ICMP", "SHOULD/MUST",
     "yes", "SHOULD/MUST", V, "F; FR-33; S-42", "S-42 real (nur Negativevidenz)"),
    (199, "Sec. 11.x", "11.4", "Speicher begrenzen und nicht socketuebergreifend teilen", "SHOULD",
     "yes", "SHOULD", T, "F, A; FR-34; NFR-06",
     "Vertrag dokumentiert, Peer-Ebene loest ihn nur teilweise ein"),
    (200, "Sec. 11.x", "11.4", "Einzelne Fragmente nie an den Nutzer geben", "MUST", "yes", "MUST",
     V, "R, F; FR-31", ""),
    (201, "Sec. 11.x", "11.4", "Fehlgeschlagene Reassemblierung ohne Leerdatagramm", "SHOULD",
     "yes", "SHOULD", V, "R, F; FR-33; S-49", "S-49 real"),
    (202, "Sec. 11.x", "11.5", "MDS verarbeiten; MDS begrenzt das Senden nicht", "MUST", "yes",
     "MUST", V, "O, A; FR-24", "real (1400 nach MDS 1200)"),
    (203, "Sec. 11.x", "11.6", "MRDS-Mindestwerte und Voreinstellungen fuer IPv4", "MUST",
     "yes (IPv4)", "MUST", V, "O, F; FR-35", "IPv6-Anteil ausserhalb des Umfangs"),
    (204, "Sec. 11.x", "11.7", "REQ/RES ohne Autoantwort; RES-Token aus empfangenem REQ",
     "MUST", "delegated", "Festlegung/MUST", V, "O, A; FR-25; Vertrag",
     "RFC weist der Anwendung zu; Vertrag dokumentiert; s14 real still"),
    (205, "Sec. 11.x", "11.7", "Automatische REQ/RES-Schicht standardmaessig aus", "MUST",
     "yes (vacuous)", "MUST", V, "A; keine solche Schicht", "leer erfuellt, keine solche Schicht"),
    (206, "Sec. 11.x", "11.8", "TIME optional; verwendete Zeitwerte nie null",
     "MUST (wenn implementiert)", "out", "MAY/MUST", A, "nicht gewaehlt; S-23 Parser",
     "geprueft 2026-08-26: Sec. 11.8 fuehrt TIME als MAY; nur die Nullregel ist ein MUST NOT"),
    (207, "Sec. 11.x", "11.9", "AUTH ist reserviert", "reserviert", "out", "reserviert", A,
     "nicht definiert", ""),
    (208, "Sec. 11.x", "11.10", "EXP bei Wahl mit Mindestlaenge vier", "MUST (wenn implementiert)",
     "out", "MUST", A, "nicht gewaehlt", ""),
    (209, "Sec. 12-14", "12", "Reservierte UNSAFE-Arten UCMP, UENC und UEXP", "reserviert", "out",
     "reserviert", A, "nicht definiert", ""),
    (210, "Sec. 12-14", "12", "UNSAFE nur in Fragmenten; unbekannte Art verwirft Daten", "MUST",
     "yes (drop side)", "MUST", V, "R, F; FR-39", ""),
    (211, "Sec. 12-14", "13", "Entwurfsregeln fuer neue Optionsarten", "MUST", "n/a", "MUST", A,
     "keine neue Optionsart", "keine neuen Optionen definiert"),
    (212, "Sec. 12-14", "14", "Empfangsfolge Pruefsumme, OCS, Optionen, Zustellung", "MUST", "yes",
     "Festlegung", V, "R; FR-36", ""),
    (213, "Sec. 12-14", "14", "Vorhandene Pflichtoptionen verarbeiten", "MUST", "yes", "MUST", V,
     "R; FR-06/36", ""),
    (214, "Sec. 12-14", "14", "Andere Optionsarten duerfen ignoriert werden", "MAY", "yes", "MAY",
     V, "R, A; gewaehlt", "gewaehlt, konfigurierbar"),
    (215, "Sec. 12-14", "14", "Nutzdaten bei SAFE unabhaengig vom Ergebnis liefern", "MUST", "yes",
     "MUST", V, "R; FR-38", ""),
    (216, "Sec. 12-14", "14", "FRAG/NOP/EOL intern; uebrige Status bereitstellen", "MUST", "yes",
     "MUST", V, "R, A; FR-37", ""),
    (217, "Sec. 12-14", "14", "Optionsueberlauf nach Abschnitt 10 behandeln", "MUST",
     "yes", "MUST", V, "O, R; FR-50; Erratum 8834", "S-11b real"),
    (218, "Sec. 15-19", "15", "Empfangs-API: je Paket und Fragment gefordert oder aus", "MUST",
     "partial", "Normform", T, "A; FR-44", "nur gebuendelte, keine fragmentweise Steuerung"),
    (219, "Sec. 15-19", "15", "Fehlende Pflichtoption still verwerfen und melden", "MUST",
     "partial", "MUST/SHOULD", T, "A; FR-44", "quellagnostisch, nicht je Quellebene"),
    (220, "Sec. 15-19", "15", "Schalter fuer alle Optionsdatagramme; Standard verarbeiten", "MUST",
     "yes", "Normform/MUST", V, "A; FR-44", ""),
    (221, "Sec. 15-19", "15", "Optionen und Status fuer Nutzer verfuegbar", "MUST", "yes",
     "Normform/MUST", V, "A; FR-37", ""),
    (222, "Sec. 15-19", "15", "Sende-API: Auswahl, Geltung, Mindestlaenge, Maximalfragment",
     "ohne BCP-14", "partial", "Normform", T, "A; SendConfig/Options",
     "geprueft 2026-08-26: unmarkierte Festlegung der Sec.-15-Einleitung, daher anwendbar; "
     "Optionsauswahl umgesetzt, Fragmentgeltung und Mindestlaenge nicht"),
    (223, "Sec. 15-19", "15/25", "Keine direkte Ordnungs- oder Fragmentgrenzensteuerung",
     "guidance", "yes", "Leitlinie", A, "A; kanonisiert",
     "Leitlinie ohne BCP-14; als Kanonisierung umgesetzt"),
    (224, "Sec. 15-19", "16/19",
     "Transit unveraendert (nicht FF1); SAFE-Fehler ignorieren und Nutzdaten liefern", "MUST",
     "yes (endpoint side)", "MUST", V,
     "R, A; FR-38 fuer Endpunkt; Transit: K, nicht als I bewertet",
     "geprueft 2026-08-26: Transitpflicht aus Sec. 16 ist FF2-Messgegenstand, "
     "Endpunktpflichten aus Sec. 19 sind FF1-Gegenstand"),
    (225, "Sec. 23-26", "25", "Bei DoS-Bedenken Grenzen fuer Optionen, NOP und Fragmente", "SHOULD",
     "partial / documented opt-out", "bed. SHOULD", T, "R, F; NFR-04/05/06/08",
     "NFR-04 begruendeter Verzicht; NFR-05 teilweise; NFR-06/08 umgesetzt"),
    (226, "Sec. 23-26", "25", "Bei Kanalbedenken Optionen in unabhaengiger Referenzordnung",
     "SHOULD", "partial", "bed. SHOULD", T, "A; FR-14",
     "Sendeordnung kanonisch; Empfangs-Neuordnung nicht Standard"),
    (227, "Sec. 23-26", "23", "Multicast und Broadcast gesondert betrachten", "special", "out",
     "Leitlinie", A, "nur Unicast", "nur Unicast untersucht"),
    (228, "Sec. 23-26", "26", "Namensregeln fuer neue SAFE- und UNSAFE-Arten", "MUST", "n/a",
     "MUST", A, "keine neue Art", "keine neuen Kinds registriert"),
]

GRUPPEN_SOLL = OrderedDict([("Sec. 7-9", 8), ("Sec. 10", 17), ("Sec. 11.x", 22),
                            ("Sec. 12-14", 9), ("Sec. 15-19", 7), ("Sec. 23-26", 4)])

# Anwendbarkeit und technische Erfuellbarkeit leiten sich aus der Kategorie ab: Nicht anwendbare
# Zeilen werden nicht auf technische Erfuellbarkeit geprueft; fuer alle uebrigen ergab die Pruefung
# keinen belegten Hinderungsgrund unter Linux, IPv4 und Benutzerraum mit Raw Sockets.
KUERZEL = {V: "V", T: "P", N: "X", A: "N"}


def anwendbar(kategorie):
    return "nein" if kategorie == A else "ja"


def technisch(kategorie):
    return A if kategorie == A else V


assert len(ZEILEN) == 67, f"Zeilenzahl {len(ZEILEN)} statt 67"
gruppen = Counter(z[1] for z in ZEILEN)
for g, soll in GRUPPEN_SOLL.items():
    assert gruppen[g] == soll, f"Gruppe {g}: {gruppen[g]} statt {soll}"
quellzeilen = [z[0] for z in ZEILEN]
assert sorted(quellzeilen) == list(range(162, 229)), "Quellzeilen nicht lueckenlos 162..228"

impl = Counter(z[7] for z in ZEILEN)
tech = Counter(technisch(z[7]) for z in ZEILEN)
assert (impl[V], impl[T], impl[N], impl[A]) == (52, 6, 0, 9), f"Implementierungsstand {dict(impl)}"
assert (tech[V], tech[T], tech[N], tech[A]) == (58, 0, 0, 9), f"Technische Erfuellbarkeit {dict(tech)}"
assert [z[0] for z in ZEILEN if z[7] == T] == [199, 218, 219, 222, 225, 226], "Teilmenge falsch"
assert [z[0] for z in ZEILEN if z[7] == A] == [188, 206, 207, 208, 209, 211, 223, 227, 228], \
    "Menge der nicht anwendbaren Zeilen falsch"

with CSV.open("w", newline="") as fh:
    fh.write("# Datenschicht fuer Tabelle 6.2 (FF1-Einzelbewertung). Quelle: docs/requirements.md\n")
    fh.write("# Abschnitt 3 (Zeilen 162-228) am Auswertungsstand f847895. Die Spalten level und\n")
    fh.write("# covered geben die Repository-Selbstauskunft wieder; normstufe, anwendbar, kategorie\n")
    fh.write("# (Implementierungsstand) und technisch tragen die am RFC-Primaertext geprueften\n")
    fh.write("# Urteile dieser Arbeit, Pruefstand 2026-08-26. Erzeugt und geprueft von\n")
    fh.write("# thesis/tikz/gen/ff1-kategorien.py (Asserts: 67 Zeilen; Gruppen 8/17/22/9/7/4;\n")
    fh.write("# Implementierung 52/6/0/9; technisch 58/0/0/9).\n")
    w = csv.writer(fh)
    w.writerow(["quellzeile", "gruppe", "rfc_bereich", "kurzinhalt", "level", "covered",
                "normstufe", "anwendbar", "kategorie", "technisch", "beleg", "anmerkung"])
    for z in ZEILEN:
        w.writerow([z[0], z[1], z[2], z[3], z[4], z[5], z[6], anwendbar(z[7]), z[7],
                    technisch(z[7]), z[8], z[9]])

UML = {"ae": "ä", "oe": "ö", "ue": "ü", "Ae": "Ä", "Oe": "Ö", "Ue": "Ü", "ss": "ß"}


def tex(s, slash=False):
    """Setzt den ASCII-Datenbestand fuer LaTeX; nur Umlaute der Kurztexte werden ausgeschrieben."""
    for quelle, ziel in (
        ("Ungueltige", "Ungültige"), ("gemaess", "gemäß"), ("Laenge", "Länge"),
        ("laenge", "länge"), ("Laengen", "Längen"), ("ueber", "über"), ("uebergehen", "übergehen"),
        ("unterstuetzte", "unterstützte"), ("Ueberlauf", "Überlauf"), ("Ueberlappung", "Überlappung"),
        ("Ungueltig", "Ungültig"), ("gueltig", "gültig"), ("Gueltige", "Gültige"),
        ("standardmaessig", "standardmäßig"), ("hoechstens", "höchstens"), ("Faelle", "Fälle"),
        ("abhaengig", "abhängig"), ("unabhaengig", "unabhängig"), ("duerfen", "dürfen"),
        ("ausser", "außer"), ("Nullpruefung", "Nullprüfung"), ("Pruefsumme", "Prüfsumme"),
        ("uebrige", "übrige"), ("verfuegbar", "verfügbar"), ("Mindestlaenge", "Mindestlänge"),
        ("Optionsueberlauf", "Optionsüberlauf"), ("unveraendert", "unverändert"),
        ("socketuebergreifend", "socketübergreifend"), ("fuer", "für"), ("Namensregeln", "Namensregeln"),
        ("Entwurfsregeln", "Entwurfsregeln"), ("Kuerzel", "Kürzel"), ("Pruefung", "Prüfung"),
        ("gewaehlt", "gewählt"),
    ):
        s = s.replace(quelle, ziel)
    if slash:
        s = s.replace("/", r"\slash ")
    return s


zeilen_tex = []
zeilen_tex.append("% Generiert von thesis/tikz/gen/ff1-kategorien.py aus dem dortigen Datenbestand.")
zeilen_tex.append("% Nicht von Hand aendern; Aenderungen im Skript oder in der Datenschicht vornehmen.")
zeilen_tex.append(r"\begingroup")
zeilen_tex.append(r"\footnotesize")
zeilen_tex.append(r"\setlength{\tabcolsep}{2pt}")
zeilen_tex.append(r"\renewcommand{\arraystretch}{1.00}")
zeilen_tex.append(r"\begin{longtable}{@{}r l L{4.45cm} L{2.00cm} c c c L{4.20cm}@{}}")
zeilen_tex.append(r"\caption{Prüfung der 67 Matrixzeilen gegen RFC 9868 und den Implementierungsstand}")
zeilen_tex.append(r"\label{tab:eval-sollist}\\")
kopf = (r"\textbf{Z.} & \textbf{Sec.} & \textbf{Normtext, gekürzt} & \textbf{Stufe} & \textbf{A} &"
        "\n" r"\textbf{I} & \textbf{T} & \textbf{Beleg} \\")
zeilen_tex.append(r"\toprule")
zeilen_tex.append(kopf)
zeilen_tex.append(r"\midrule")
zeilen_tex.append(r"\endfirsthead")
zeilen_tex.append(r"\toprule")
zeilen_tex.append(kopf)
zeilen_tex.append(r"\midrule")
zeilen_tex.append(r"\endhead")
zeilen_tex.append(r"\bottomrule")
zeilen_tex.append(r"\endfoot")
for z in ZEILEN:
    kat = z[7]
    spalten = [
        str(z[0]),
        z[2],
        tex(z[3]),
        tex(z[6], slash=True),
        "J" if kat != A else "N",
        KUERZEL[kat],
        "V" if kat != A else "n.a.",
        tex(z[8]),
    ]
    zeile = " & ".join(spalten) + r" \\"
    if len(zeile) > 120:
        teile, akt = [], spalten[0]
        for sp in spalten[1:]:
            if len(akt) + 3 + len(sp) > 116:
                teile.append(akt + " &")
                akt = "  " + sp
            else:
                akt = akt + " & " + sp
        teile.append(akt + r" \\")
        zeilen_tex.extend(teile)
    else:
        zeilen_tex.append(zeile)
zeilen_tex.append(r"\midrule")
zeilen_tex.append(r"\multicolumn{8}{@{}l@{}}{Implementierung: %d V, %d P, %d N. "
                  r"Technisch: %d V, %d P, %d nicht erfüllbar.} \\"
                  % (impl[V], impl[T], impl[A], tech[V], tech[T], tech[N]))
zeilen_tex.append(r"\end{longtable}")
zeilen_tex.append(r"\endgroup")

FRAGMENT.write_text("\n".join(zeilen_tex) + "\n", encoding="utf-8")

print(f"geschrieben: {CSV} (67 Zeilen)")
print(f"geschrieben: {FRAGMENT}")
print("Implementierungsstand:", {k: v for k, v in impl.items()})
print("Technische Erfuellbarkeit:", {k: v for k, v in tech.items()})
print(f"{'Gruppe':<11} {'n':>2} {'voll':>4} {'teil':>4} {'n.erf':>5} {'n.anw':>5}")
for g in GRUPPEN_SOLL:
    c = Counter(z[7] for z in ZEILEN if z[1] == g)
    print(f"{g:<11} {gruppen[g]:>2} {c[V]:>4} {c[T]:>4} {c[N]:>5} {c[A]:>5}")
