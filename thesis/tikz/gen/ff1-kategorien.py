#!/usr/bin/env python3
"""Datenschicht fuer Tabelle 6.2: FF1-Einzelbewertung der 67 Konformitaetsmatrix-Zeilen.

Quelle: docs/requirements.md Abschnitt 3 des Implementierungsrepos am Auswertungsstand f847895
(Zeilen 162 bis 228; Spalten RFC area, Normative item, Level, Covered, Step, Notes). Die Kategorie
je Zeile folgt der repository-internen Zuordnung, die Tabelle 6.2 als Stand vor der Korrektur
ausweist (06_evaluation.tex, sec:soll-ist): Anwendbarkeit zuerst (nicht gewaehlte MAY-Funktionen
und Aussagen ausserhalb des Umfangs zaehlen als nicht anwendbar; zwei unmarkierte API-Saetze aus
Sec. 15 sind allein wegen fehlender BCP-14-Schluesselwoerter so eingeordnet, was das Kapitel als
offene Einstufungsfrage kennzeichnet); Partial-in-userspace = teilweise;
Not-feasible-in-userspace = nicht erfuellbar; Delegated nur mit dokumentiertem Vertrag vollstaendig;
Partially implemented bestimmt die Erfuellbarkeit noch nicht und wird je Zeile entschieden.
Sonderfaelle sind in der Spalte anmerkung begruendet. Das Skript schreibt
thesis/daten/konformitaet-kategorien.csv und prueft die Summen (67; Gruppen 8/17/22/9/7/4).
"""
import csv
from collections import Counter, OrderedDict
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
CSV = REPO / "thesis" / "daten" / "konformitaet-kategorien.csv"

V, T, N, A = "vollstaendig", "teilweise", "nicht erfuellbar", "nicht anwendbar"

# (Quellzeile in requirements.md, Gruppe, RFC-Bereich, Kurzinhalt, Level, Covered, Kategorie, Anmerkung)
ZEILEN = [
    (162, "Sec. 10", "Sec. 10", "UDP Length in [8, IP-Nutzlast], sonst verwerfen und melden", "MUST", "yes", V, ""),
    (163, "Sec. 7-9", "Sec. 7", "Surplus Area als IP-Nutzlast-Rest hinter UDP Length geortet", "MUST", "yes", V, ""),
    (164, "Sec. 7-9", "Sec. 8", "Optionen nutzen die ganze Surplus Area; OCS auf 2-Byte-Grenze", "MUST", "yes", V, ""),
    (165, "Sec. 7-9", "Sec. 8", "Pad vor dem OCS muss null sein, sonst Surplus verwerfen", "MUST", "yes", V, "real belegt (S-04, G-Zelle)"),
    (166, "Sec. 7-9", "Sec. 9", "OCS-Berechnung mit Laengensummand", "MUST", "yes", V, ""),
    (167, "Sec. 7-9", "Sec. 9", "OCS ungleich null, wenn UDP-Pruefsumme ungleich null", "MUST", "yes", V, ""),
    (168, "Sec. 7-9", "Sec. 9", "Voreinstellung: OCS ungleich null senden", "MUST", "yes", V, ""),
    (169, "Sec. 7-9", "Sec. 9", "OCS-Fehler: alle Optionen ignorieren, Surplus verwerfen", "MUST", "yes", V, "real belegt (S-05)"),
    (170, "Sec. 7-9", "Sec. 9/14", "Daten mit gueltiger UDP-Pruefsumme trotz OCS-Fehler zustellen", "MUST", "yes", V, "S-06-Matrix real"),
    (171, "Sec. 10", "Sec. 10", "TLV-Rahmung; Length gesamt; 255 leitet erweitertes Format ein", "MUST", "yes", V, ""),
    (172, "Sec. 10", "Sec. 10", "NOP und EOL ohne Laengenform", "MUST", "yes", V, ""),
    (173, "Sec. 10", "Sec. 10", "Laenge unter Formatminimum: Fehler, alle Optionen verwerfen", "MUST", "yes", V, "S-11a real"),
    (174, "Sec. 10", "Sec. 10", "Unter-/Ueberlauf: malformed Surplus, alles verwerfen", "MUST", "yes", V, "S-11b real; Erratum 8834"),
    (175, "Sec. 10", "Sec. 10", "Bekannte Option unter Kind-Minimum: alles verwerfen", "MUST", "yes", V, ""),
    (176, "Sec. 10", "Sec. 10", "Erweitertes Format ab 255; kleinste Form als SHOULD", "MUST/SHOULD", "yes (send); local strict receive", V, "dokumentierte lokale Empfangsstrenge"),
    (177, "Sec. 10", "Sec. 10/14", "Optionen in Surplus-Reihenfolge verarbeiten", "MUST", "yes", V, ""),
    (178, "Sec. 10", "Sec. 10", "Alle must-support-Optionen erkennen und erzeugen", "MUST", "yes", V, "real P0 (sopt)"),
    (179, "Sec. 10", "Sec. 10", "Unbekannte SAFE-Optionen still uebergehen", "MUST", "yes", V, "S-10 real"),
    (180, "Sec. 10", "Sec. 10", "Malformed FRAG wie unsupported UNSAFE behandeln", "MUST", "yes", V, ""),
    (181, "Sec. 10", "Sec. 10", "Nicht-FRAG/NOP/EXP/UEXP hoechstens einmal; first wins", "SHOULD/MUST", "yes", V, ""),
    (182, "Sec. 10", "Sec. 10", "NOP darf wiederholen (Ausrichtung)", "MAY", "yes", V, "gewaehlte MAY, Lauflimit 7"),
    (183, "Sec. 10", "Sec. 10", "FRAG mehr als einmal: Optionsbereich malformed", "MUST", "yes", V, ""),
    (184, "Sec. 10", "Sec. 10", "Bei UNSAFE: user data leer, Nutzlast im FRAG", "MUST", "yes (by construction)", V, ""),
    (185, "Sec. 10", "Sec. 10", "Unsupported UNSAFE: sofort abbrechen, Optionen verwerfen", "MUST", "yes", V, "S-20 real; Schritt-18-Fall"),
    (186, "Sec. 10", "Sec. 10", "must-support vor anderen SAFE; Empfaenger-MAY bei Verstoss", "MUST/MAY", "yes", V, ""),
    (187, "Sec. 11.x", "Sec. 11.1", "EOL als letzte Nicht-NOP-Option; Nullfuellung beim Senden", "MUST", "yes", V, "S-08 real"),
    (188, "Sec. 11.x", "Sec. 11.1", "Pruefung der Bytes nach EOL (MAY) mit bedingtem MUST", "MUST (bedingt)/MAY", "not selected", A, "nicht gewaehlte MAY-Pruefung (FR-18)"),
    (189, "Sec. 11.x", "Sec. 11.2", "Hoechstens 7 NOPs; lange Laeufe melden und begrenzen", "SHOULD", "partial", T, "Erkennung ja, Fruehabbruch nein (NFR-05)"),
    (190, "Sec. 11.x", "Sec. 11.3", "APC als CRC32C; Fehlschlag mit Anzeige zustellen", "MUST/SHOULD", "yes", V, "S-13 real"),
    (191, "Sec. 11.x", "Sec. 11.3", "Unbekannte APC-Laenge wie fehlgeschlagene APC", "MUST", "yes", V, ""),
    (192, "Sec. 11.x", "Sec. 11.4", "FRAG-Laengen 10/12 (RDOS)", "MUST", "yes", V, "S-19 real"),
    (193, "Sec. 11.x", "Sec. 11.4", "Bei FRAG: user data leer", "MUST", "yes", V, ""),
    (194, "Sec. 11.x", "Sec. 11.4", "Reassemblierung von mindestens 2 Fragmenten je 1500", "MUST", "yes", V, "real (sfrag)"),
    (195, "Sec. 11.x", "Sec. 11.4", "Identification eindeutig ueber den Timeout", "MUST/SHOULD", "yes", V, "S-46 real; Kollisionsfall als Normluecke"),
    (196, "Sec. 11.x", "Sec. 11.4", "Keine Ueberlappung; Abbruch ohne ICMP", "MUST", "yes", V, "S-45 real, auch byteidentisch"),
    (197, "Sec. 11.x", "Sec. 11.4", "Exakte Duplikate duerfen verworfen werden", "MAY", "yes", V, "gewaehlte MAY"),
    (198, "Sec. 11.x", "Sec. 11.4", "Reassembly-Timeout hoechstens 2 min; kein ICMP", "SHOULD/MUST", "yes", V, "S-42 real (nur Negativevidenz)"),
    (199, "Sec. 11.x", "Sec. 11.4", "Reassembly-Speicher begrenzt, nicht paaruebergreifend", "SHOULD", "yes", T, "Vertrag dokumentiert, Peer-Ebene loest ihn nur teilweise ein"),
    (200, "Sec. 11.x", "Sec. 11.4", "Einzelfragmente nie an den Nutzer", "MUST", "yes", V, ""),
    (201, "Sec. 11.x", "Sec. 11.4", "Reassembly-Fehlschlag ohne Leerdatagramm", "SHOULD", "yes", V, "S-49 real"),
    (202, "Sec. 11.x", "Sec. 11.5", "MDS kodieren/dekodieren; MDS begrenzt das Senden nicht", "MUST", "yes", V, "real (1400 nach MDS 1200)"),
    (203, "Sec. 11.x", "Sec. 11.6", "MRDS-Minima und Voreinstellungen", "MUST", "yes (IPv4)", V, "IPv6-Anteil ausserhalb des Umfangs"),
    (204, "Sec. 11.x", "Sec. 11.7", "REQ/RES ohne Auto-Antwort; Token-Herkunft aus REQ", "MUST", "delegated", V, "RFC weist der Anwendung zu; Vertrag dokumentiert; s14 real still"),
    (205, "Sec. 11.x", "Sec. 11.7", "Auto-REQ/RES-Schicht standardmaessig aus", "MUST", "yes (vacuous)", V, "leer erfuellt, keine solche Schicht"),
    (206, "Sec. 11.x", "Sec. 11.8", "TIME-Option", "MUST (wenn implementiert)", "out", A, "nicht gewaehlt; real als 0x08:ignored belegt"),
    (207, "Sec. 11.x", "Sec. 11.9", "AUTH (reserviert)", "reserviert", "out", A, ""),
    (208, "Sec. 11.x", "Sec. 11.10", "EXP-Option", "MUST (wenn implementiert)", "out", A, "nicht gewaehlt"),
    (209, "Sec. 12-14", "Sec. 12", "UNSAFE-Optionen UCMP/UENC/UEXP", "reserviert", "out", A, ""),
    (210, "Sec. 12-14", "Sec. 12", "UNSAFE nur in Fragmenten; unsupported: Daten verwerfen", "MUST", "yes (drop side)", V, ""),
    (211, "Sec. 12-14", "Sec. 13", "Entwurfsregeln fuer neue Optionen", "MUST", "n/a", A, "keine neuen Optionen definiert"),
    (212, "Sec. 12-14", "Sec. 14", "Empfangsreihenfolge Pruefsumme, OCS, Optionen, Zustellung", "MUST", "yes", V, ""),
    (213, "Sec. 12-14", "Sec. 14", "Alle vorhandenen must-support-Optionen verarbeiten", "MUST", "yes", V, ""),
    (214, "Sec. 12-14", "Sec. 14", "Andere Optionen duerfen ignoriert werden", "MAY", "yes", V, "gewaehlt, konfigurierbar"),
    (215, "Sec. 12-14", "Sec. 14", "Daten bei SAFE-Optionen unabhaengig vom Ausgang zustellen", "MUST", "yes", V, ""),
    (216, "Sec. 12-14", "Sec. 14", "FRAG/NOP/EOL nicht an den Nutzer; uebrige Status verfuegbar", "MUST", "yes", V, ""),
    (217, "Sec. 12-14", "Sec. 14+Err. 8834", "Options-Ueberlauf nach Sec.-10-Verfahren", "MUST", "yes", V, "S-11b real"),
    (218, "Sec. 15-19", "Sec. 15", "Empfangs-API: required/omitted je Paket und Fragment", "MUST", "partial", T, "nur gebuendelte, keine fragmentweise Steuerung"),
    (219, "Sec. 15-19", "Sec. 15", "Fehlende Pflichtoption: still verwerfen und melden", "MUST", "partial", T, "quellagnostisch, nicht je Quellebene"),
    (220, "Sec. 15-19", "Sec. 15", "Schalter: alle optionstragenden Datagramme verwerfen", "MUST", "yes", V, ""),
    (221, "Sec. 15-19", "Sec. 15", "Optionen und Status fuer den Nutzer verfuegbar", "MUST", "yes", V, ""),
    (222, "Sec. 15-19", "Sec. 15", "Beschreibende Sende-API-Form", "ohne BCP-14", "partial", A, "beschreibend, keine markierte Pflicht"),
    (223, "Sec. 15-19", "Sec. 15/25", "Keine Nutzerkontrolle ueber Optionsreihenfolge", "guidance", "yes", A, "Leitlinie ohne BCP-14; als Kanonisierung umgesetzt"),
    (224, "Sec. 15-19", "Sec. 16/19", "Endpunkt veraendert Optionen unterwegs nicht", "MUST", "yes (endpoint side)", V, "Transit-Integritaet ist FF2-Messgegenstand"),
    (225, "Sec. 23-26", "Sec. 25.2-.4", "DoS-Grenzen fuer Optionen, NOP-Laeufe, Reassemblierung", "SHOULD", "partial / documented opt-out", T, "NFR-04 begruendeter Verzicht; NFR-05 teilweise; NFR-06/08 umgesetzt"),
    (226, "Sec. 23-26", "Sec. 25", "Optionen in Referenzreihenfolge zurueckgeben", "SHOULD", "partial", T, "Sendeordnung kanonisch; Empfangs-Neuordnung nicht Standard"),
    (227, "Sec. 23-26", "Sec. 23", "Multicast/Broadcast-Betrachtungen", "special", "out", A, "nur Unicast untersucht"),
    (228, "Sec. 23-26", "Sec. 26", "Namensregeln fuer neue Kinds", "MUST", "n/a", A, "keine neuen Kinds registriert"),
]

GRUPPEN_SOLL = OrderedDict([("Sec. 7-9", 8), ("Sec. 10", 17), ("Sec. 11.x", 22),
                            ("Sec. 12-14", 9), ("Sec. 15-19", 7), ("Sec. 23-26", 4)])

assert len(ZEILEN) == 67, f"Zeilenzahl {len(ZEILEN)} statt 67"
gruppen = Counter(z[1] for z in ZEILEN)
for g, soll in GRUPPEN_SOLL.items():
    assert gruppen[g] == soll, f"Gruppe {g}: {gruppen[g]} statt {soll}"
quellzeilen = [z[0] for z in ZEILEN]
assert sorted(quellzeilen) == list(range(162, 229)), "Quellzeilen nicht lueckenlos 162..228"

with CSV.open("w", newline="") as fh:
    fh.write("# Datenschicht fuer Tabelle 6.2 (FF1-Einzelbewertung). Quelle: docs/requirements.md\n")
    fh.write("# Abschnitt 3 (Zeilen 162-228) am Auswertungsstand f847895; Kategorien nach der\n")
    fh.write("# repository-internen Zuordnung vor der Korrektur (Tabelle 6.2, 06_evaluation.tex;\n")
    fh.write("# offene Normstufenpruefung dort ausgewiesen). Erzeugt und geprueft von\n")
    fh.write("# thesis/tikz/gen/ff1-kategorien.py (Summen-Asserts: 67 Zeilen; Gruppen 8/17/22/9/7/4).\n")
    w = csv.writer(fh)
    w.writerow(["quellzeile", "gruppe", "rfc_bereich", "kurzinhalt", "level", "covered", "kategorie", "anmerkung"])
    for z in ZEILEN:
        w.writerow(z)

print(f"geschrieben: {CSV} (67 Zeilen)")
gesamt = Counter(z[6] for z in ZEILEN)
print("Gesamt:", dict(gesamt))
print(f"{'Gruppe':<11} {'n':>2} {'voll':>4} {'teil':>4} {'n.erf':>5} {'n.anw':>5}")
for g in GRUPPEN_SOLL:
    c = Counter(z[6] for z in ZEILEN if z[1] == g)
    print(f"{g:<11} {gruppen[g]:>2} {c[V]:>4} {c[T]:>4} {c[N]:>5} {c[A]:>5}")
