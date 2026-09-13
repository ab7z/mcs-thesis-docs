# Zweitmeinung zu Kapitel 4 "Analyse und Anforderungsmodell"

Unabhängige, ergebnisoffene Prüfung nach den 24 Kriterien aus `AGENTS.md` ("Kapitelprüfung und Freigabe").
Erstellt am 2026-09-13 (Prüfung 2026-09-12/13). Rein lesend; keine Projektdatei geändert.

## 1. Geprüfter Stand und tatsächlicher Prüfumfang

- Thesis-Repo HEAD `80022ba` (main). Vorhandene Änderungen: `AGENTS.md` uncommitted (ergänzt den Abschnitt
  "Kapitelprüfung und Freigabe" mit den 24 Kriterien); untracked `reviews/kapitel-4-vollpruefung-2026-09-12.md`
  (vorhandener Prüfbericht, auftragsgemäß NICHT gelesen).
- Kapitel: `thesis/chapters/04_analyse.tex`, 332 Zeilen, vollständig gelesen (alle Sätze, Überschriften, beide
  Fußnoten, vier Tabellen, eine Abbildung). PDF `thesis/main.pdf` (2026-09-10 18:44, 95 Seiten): Kapitel 4 auf
  den gedruckten Seiten 36 bis 43 (physisch 42 bis 49), als Text und als Seitenbilder geprüft; Übergänge S. 35/36
  und 43/44, Abbildungs- und Tabellenverzeichnis.
- Kriterium 24: Neubau einer Scratchpad-Kopie (`make pdf`, sauber): 95 Seiten, `pdftotext` aller Seiten identisch
  mit der ausgelieferten PDF; keine Overfull/Underfull-Boxen, keine undefinierten Verweise, biber ohne Warnung;
  einzige Meldung `makeglossaries: File 'main.glo' is empty` (Glossar leer, Abkürzungen laufen über acn/acr, nicht
  kapitelspezifisch). Keine Thesis-Quelle ist neuer als die PDF. `thesis/main.pdf` wurde nicht überschrieben.
- Primärquellen: `literature/rfc9868.txt` (Sec. 2, 3, 6, 7, 8, 9, 10, 11.2, 12, 15, 18, 25.2, Table 1),
  rfc2119/rfc8174; man7 raw(7) und packet(7), kernel.org v5.10 (tuntap, af_xdp), Chromium "Memory safety",
  Millers BlueHat-IL-2019-Folien (GitHub MSRC-Security-Research, PDF), MSRC-Blog 16.07.2019, Bun-Blog
  "Rewriting Bun in Rust" (08.07.2026), kernel.org dev-tools v5.10.
- Belege: `../udp-transport-options` bei HEAD `503c6c8` (Code, Tests, fuzz/, formal/, scripts/, docs/,
  journal.html, git-Historie, PR #12 und #25 per `gh`), `thesis/daten/konformitaet-kategorien.csv`,
  `thesis/evidence/README.md` und alle elf Archive (Inhaltslisten; gezielte Auszüge nur im Scratchpad),
  Kapitel 1, 2, 3, 5, 6, 7 für Begriffe, Ankündigungen und Rückverweise.
- Vorgehen: Workflow mit fünf parallelen Lanes (A Normtreue und Belege, B Sprache und Zusammenhang: Opus 5;
  C Implementierungsbelege, D Messbelege und FF2-Konsistenz, E PDF und externe Literatur: Sonnet 5). Jeden
  Befund der Lanes habe ich selbst an der genannten Quelle nachvollzogen; nicht Nachvollziehbares ist nicht
  aufgenommen oder unter "nicht prüfbar" geführt.
- Nicht gelesen: `reviews/`, `lernnotizen/`, Memory- und Chatverläufe. Das NSA-CSI-PDF antwortet direkt mit
  HTTP 403 und wurde über einen Lesedienst (r.jina.ai) abgerufen; Millers Videovortrag blieb ungeprüft (nur die
  Folien-PDF und der MSRC-Blog).

## 2. Status der 24 Kriterien

| Nr. | Kriterium | Status | Ergebnis |
|---|---|---|---|
| 1 | Fachliche Richtigkeit | geprüft | Zahlen (103, Verteilung, 65, 49/12, 67, 8 Pflichtoptionen) exakt; drei Überverallgemeinerungen: F1, F2, F3 |
| 2 | Quellen und Belege | geprüft | RFC-Abschnitte stimmen; externe Quellen tragen die Aussagen; Präzisierungen L1 bis L6 |
| 3 | Verbindlichkeit | geprüft | Normstufen in Tab. 4.1 im Wortlaut der Datei und RFC-konform; bedingtes SHOULD aus Sec. 25.2 optional (O1) |
| 4 | Persönlicher Schreibstil | geprüft | keine Gedankenstriche; wenige Anglizismen (Wire-Datagramme, must-support, Testsuite), Metapher "grüne Prüfkette" (O-Liste) |
| 5 | Einzelne Sätze | geprüft | Bezüge: V4 ("darüber hinaus"), V7 ("dazu"), V12; sonst klar |
| 6 | Zweck und Ursache | geprüft | Entscheidungen begründet; Lücken V7 (Bun), V9 (Pfadstufe 2), V13 (Gegenproben) |
| 7 | Zusammenhang | geprüft | Widersprüche zwischen einzeln richtigen Sätzen: F2, V1, V4 |
| 8 | Relevanz und Wiederholungen | geprüft | keine unnötigen Wiederholungen; Verankerungen (Z. 104 bis 128) sind angekündigte Festlegungen |
| 9 | Begriffe | geprüft | V1 (Konformitätsmatrix, Arbeitsindex, Einzelzuordnung), V5, V11; Altempfänger, Altsystem, Nutzlast kommen in K4 nicht vor |
| 10 | Fußnoten | geprüft | Fußnote 1: V1/L4; Fußnote 2 klar (Position optional, O-Liste) |
| 11 | Ziel und Umfang | geprüft | Ankündigungen aus K1 und K3 eingelöst; Grenzen erhalten; IPv6-Rolle nur als Tabellenzelle (V10) |
| 12 | Ergebniszuordnung | geprüft | fremde Ergebnisse, eigene Messungen, Schlüsse unterschieden; keine Gerätezuschreibung |
| 13 | IPv4, MTU, Fragmentierung | geprüft | Z. 307 bis 308 korrekt (raw(7)); optional Präzisierung Schnittstellen-MTU und FRAG (O2) |
| 14 | UDP und Prüfsummen | geprüft | Tab. 4.1 Sec. 9 korrekt (RFC Z. 524); keine weiteren relevanten Aussagen |
| 15 | Surplus Area und Optionen | geprüft | Tab. 4.1 Sec. 8/10/11.2 korrekt; must-support korrekt; F3 (UEXP) |
| 16 | Betriebssystem und Netzpfad | geprüft | Protocol 17, IP_HDRINCL, keine Fragmentierung, Prüflast bei Raw Sockets am Code belegt |
| 17 | Messbedingungen | geprüft | F1 (Werkzeugkette), F2 (Messpunkte); CGNAT-Aussage korrekt qualifiziert |
| 18 | Methodik | geprüft | Kategorien und Status mit K1/K3/K6 identisch; V2 (Leitlinien in "nicht anwendbar") |
| 19 | Aussagekraft der Nachweise | geprüft | Lean/Rust-Trennung und Fuzzing-Grenze korrekt; Hash-Fußnote L4 |
| 20 | Entwicklungs- und Prüfablauf | geprüft | PR #12 (Codex-Review), 23 Tests nachgezählt, Fuzz-Ziel je Schritt, Schritt 18/PR #25 belegt; F1 |
| 21 | Abbildungen, Tabellen, Verweise | geprüft | Abb. 4.1 exakt; Verzeichnisse vollständig; V3 (Verweis 3.4 ohne Einführung), V1 (67 Zeilen) |
| 22 | PDF-Lesbarkeit | geprüft | S2 bis S4 (kosmetisch) |
| 23 | Silbentrennung | geprüft | 29 Trennungen S. 36 bis 43 (25 Fließtext, 4 Tabellenzellen): eine falsch (S1) |
| 24 | Abschlusskontrolle | geprüft | Neubau textidentisch, Logs sauber, Quellstand und PDF passen zusammen |

## 3. Befunde

Fundstellen: Zeilen in `04_analyse.tex`, Seiten der gedruckten PDF. Konfidenz in Klammern.

### 3.1 Fachliche Fehler (Überverallgemeinerungen)

**F1 (hoch): Z. 314 bis 318, S. 43, Abschnitt 4.4.3.** Aussage: "Der eigene Prüfer aus Abschnitt 3.4 rechnet OCS
und Optionsstruktur aus den Bytes nach ...; tshark prüft unabhängig davon die IPv4- und UDP-Felder. Aufzeichnen,
Deuten und Gegenprüfen liegen damit bei drei verschiedenen Werkzeugen."
Beleglage: Die tshark-Gegenprobe und die unabhängige OCS/TLV-Nachrechnung gehören zur Wire-Prüfspur der Entwicklung
(`scripts/wire-check.sh` Z. 144 bis 152, `scripts/wire-check.py`, `scripts/pre-pr.sh`). In den FF2-Kampagnen ab
11.08. (bidir, hel, hotspots, p0p1p2 1blu/mcs, aws, gcp) gibt es keine tshark-Datei (elf Archive gelistet: nur
`external-campaign-20260810` enthält `hetzner-eval/artifacts/01-wire/tshark.*`, also die Wire-Spur auf dem Hetzner-
Endpunkt). Die Kampagnenauswerter `scripts/p0-eval.py`, `p1-eval.py`, `p2-eval.py` lesen beide PCAPs und vergleichen
die Surplus-Bytes, übernehmen den OCS-Status aber aus der Empfängerausgabe (`ocs_reports`, erzeugt von
`src/bin/udpopt-recv.rs`), rufen tshark nicht auf. `scripts/eval-check.py` (rechnet OCS selbst, Z. 237 bis 250)
lieferte `verdicts.jsonl` nur im Archiv vom 10.08. `docs/evaluation.md` Z. 28 bis 31 sagt selbst, der Evaluations-
prüfer validiere OCS nicht unabhängig. Derselbe Satz steht in K6 Z. 114 bis 115 (sec:testkonzept).
Bewertung: Als Beschreibung der Kampagnenauswertung zu breit (Kriterium 17, 20: geplante und nachweislich
ausgeführte Prüfungen unterscheiden). Der Satz ist für die Wire-Prüfspur richtig.
Ersatzvorschlag (Z. 314 bis 318):
"Die Kampagnenskripte zeichnen den Verkehr mit \texttt{tcpdump} in archivierbaren PCAP-Belegdateien auf. Weil
Wireshark in der verwendeten Version~4.6 die Surplus Area nicht dekodiert (\secref{sec:netzpfad}), deuten eigene
Python-Prüfer die Bytes: Der Kampagnenauswerter vergleicht die Surplus Area zwischen Sender- und
Empfängermitschnitt und übernimmt den OCS-Status aus der Empfängerausgabe; der Prüfer der Wire-Prüfung
(\secref{sec:pruefkette}) rechnet OCS und Optionsstruktur unabhängig nach, und \texttt{tshark} prüft dort die IPv4-
und UDP-Felder. Aufzeichnen und Deuten liegen damit bei getrennten Werkzeugen; die fremde Gegenprobe gibt es in der
Wire-Prüfung, nicht in den Kampagnen." Folgeänderung in K6 Z. 114 bis 115.

**F2 (mittel): Z. 147 bis 149, S. 39.** Aussage: "Jede Messung hat dabei genau zwei eigene Messpunkte: den
Mitschnitt beim Sender und den Mitschnitt beim Empfänger."
Beleglage: Die Kampagnen vom 10.08. und 11.08. (in K6 tab:eval-messlaeufe als "Kampagne" eingestuft) haben drei
Erfassungsstellen: Gast `enp2s0`, Mac `en0`, Hetzner `eth0` (`thesis/evidence/README.md` Z. 25; K6 Z. 495
"Mitschnitte: Gast, en0 (nur 10./11.08.), Ziel"); der en0-Mitschnitt wurde zur Eingrenzung genutzt (README Z. 47).
Tab. 4.3 nennt denselben Punkt "macOS-Messpunkt ... zusätzlicher Beobachtungspunkt". Für die P0/P1/P2-Kampagnen ab
14.08. stimmt "genau zwei" (je Richtung `egress.pcap` und `ingress.pcap`).
Bewertung: zu absolut; Leser sieht den Widerspruch zu Tab. 4.3 (Kriterien 7, 17).
Ersatzvorschlag: "Jede Messung hat dabei mindestens zwei eigene Messpunkte: den Mitschnitt beim Sender und den
Mitschnitt beim Empfänger. Alles dazwischen, auf realen Pfaden etwa Zugangs-, Transit- und Provider-Kanten, hat
keinen eigenen Messpunkt. Einzige Ausnahme ist der dritte Mitschnitt auf dem Entwicklungsrechner in den Kampagnen
vom 10. und 11.~August (\tabref{tab:scope-messung}); er teilt das Intervall auf diesem Zugangspfad, hebt die Regel
aber nicht auf." Tab. 4.3, Zeile macOS: "dritter Mitschnitt auf dem Entwicklungsrechner zwischen VMware-NAT und
Hotspot (nur 10./11.08.); keine Implementierungsplattform".

**F3 (gering): Tab. 4.1, Zeile Sec. 12 (Z. 94), S. 37.** Aussage: "UCMP, UENC und UEXP sind reservierte
UNSAFE-Optionen".
Beleglage: RFC Table 1: Kind 192 und 193 "Reserved for UNSAFE Compression/Encryption"; Kind 254 "RFC3692-style
UNSAFE experiments (UEXP)", Sec. 12.3 "reserved for experiments", mit ExIDs nutzbar wie EXP. Die eigene CSV (Zeile
209: "UCMP und UENC reserviert; UEXP als UNSAFE-Experimentoption") und K1 Z. 145 bis 147 ("AUTH, UCMP und UENC ...
lediglich reserviert") unterscheiden das. Die Spalte Normstufe ("reserved") ist Wortlaut der Datei und bleibt.
Ersatzvorschlag (nur Spalte Normative Aussage): "UCMP und UENC sind reserviert, UEXP ist die
UNSAFE-Experimentoption".

### 3.2 Beleglücken und Zuschreibungen

**L1 (gering): Z. 244 bis 246, S. 41.** "Miller berichtete 2019 auf Grundlage der seit 2004 gepflegten MSRC-Daten,
dass rund 70~Prozent der jährlich von Microsoft mit CVE versehenen Schwachstellen Speicherfehler sind."
Millers Folien (BlueHat IL, Februar 2019) sagen: "~70% of the vulnerabilities addressed through a security update
each year continue to be memory safety issues", Diagramm Patch-Jahre 2006 bis 2018; "2004" kommt nicht vor. "Since
2004, the MSRC has triaged every reported Microsoft security vulnerability" und "~70% of the vulnerabilities
Microsoft assigns a CVE each year" stehen im MSRC-Blog vom 16.07.2019 (der auf Millers Vortrag verweist, aber nicht
zitiert ist); das Video selbst blieb ungeprüft. Die Aussage ist damit inhaltlich gedeckt, die Zuschreibung an den
Vortrag allein nicht belegt. Ersatz: den MSRC-Blog als zweite Quelle aufnehmen (`\cite{microsoft-memory,<blog>}`)
oder ohne neue Quelle: "Miller berichtete 2019 auf Grundlage der MSRC-Daten der Patch-Jahre 2006 bis 2018, dass
rund 70~Prozent der jährlich per Sicherheitsupdate behobenen Microsoft-Schwachstellen Speicherfehler sind."

**L2 (gering): Z. 215, S. 40.** `\cite[Sec.~3 und 6]{rfc9868}` für die Entwurfsprinzipien: Sec. 3 ist
"Terminology" (definiert nur "User"); die Prinzipien 1 und 2 stehen in Sec. 6 (RFC Z. 274 bis 283). K2 Z. 725
zitiert dieselben Prinzipien mit Sec. 6. Ersatz: `\cite[Sec.~6]{rfc9868}`.

**L3 (gering): Z. 296 bis 297, S. 42.** `\cite[Sec.~18]{rfc9868}` trägt nur die Empfangsseite (getestete
Altsysteme "delivered only the user data indicated by the UDP Length field and silently discarded the surplus
area", RFC Z. 1894 bis 1897); die Sendeseite belegt K2 (Kernelverhalten) und RFC Sec. 15 (API-Erweiterung).
Ersatz: "Ein gewöhnlicher UDP-Socket kann die Surplus Area weder füllen noch auslesen (\secref{sec:netzpfad});
getestete Altsysteme liefern beim Empfang nur die Nutzdaten bis \texttt{UDP Length} \cite[Sec.~18]{rfc9868}."

**L4 (gering): Fußnote Z. 65 bis 68, S. 37.** Commit `6a5239a` existiert, liegt auf origin/main, enthält die CSV;
Datenzeilen identisch mit HEAD. Die verlinkte Fassung trägt aber die Kopfzeile "# Datenschicht fuer die
Anhangstabelle tab:eval-sollist"; diesen Anhang gibt es seit 2026-09-03 nicht mehr (Commit `b8a5277` ändert genau
diese Kommentarzeile). Ersatz: Link und Stand auf `b8a5277` (oder den Abgabe-Commit) setzen. Nebenbei: Kopfzeile 5
der CSV enthält den Tippfehler "gepruefen".

**L5 (gering): `literatur.bib` Eintrag `nsa-memory-safety` (zitiert Z. 248 und 275).** Der Eintrag nennt
`date = {2022-11-10}` ohne Fassung; die unter der Bib-URL ausgelieferte Datei trägt die Kopfzeile
"U/OO/219936-22 | PP-23-0782 | APR 2023 Ver. 1.1". Beide Kapitelaussagen stehen auch in Ver. 1.1 ("Examples of
memory safe language include Python, Java, C#, Go, Delphi/Object Pascal, Swift, Ruby, Rust, and Ada"; "Static
analysis examines the source code ..."; "DAST can only identify issues with code that is on the execution path").
Ersatz: `version = {1.1}` und `note = {überarbeitete Fassung, April 2023}` ergänzen.

**L6 (gering): Z. 273 bis 275, S. 42.** "Statische Werkzeuge können Quelltext ohne ausgeführten Programmpfad
prüfen; nur dynamische Prüfungen und Fuzzing bleiben auf erreichte Pfade beschränkt \cite{kernel-devtools,
nsa-memory-safety}": Die kernel.org-Indexseite (v5.10) listet nur Werkzeuge (Sparse, Coccinelle; kcov, KASAN, UBSAN,
KCSAN) ohne diese methodische Aussage; die NSA-Quelle trägt sie wörtlich. Ersatz: keiner nötig; optional nur
`\cite{nsa-memory-safety}` belegen und kernel-devtools als Beispiel für getrennte Werkzeugklassen nennen. Die
Umformulierung in V7 nimmt das auf.

**L7 (gering): Tab. 4.4, Z. 252 bis 267.** Die Tabelle enthält kein Zitat; "1.0 seit 2015" (Rust 1.0 am
15.05.2015), "vor 1.0" (Zig 0.16.0), "ISO-Norm" (C: ISO/IEC 9899, C++: ISO/IEC 14882) sind richtig, aber nur C ist
mit `iso-c` belegt; für C++ gibt es keinen Bib-Eintrag; "optional" (C++) und "teilweise" (Zig) sind Wertungen ohne
Quelle. Ersatz: keiner zwingend; optional `\cite{rust-lang}` am Datum und ein ISO-C++-Eintrag.

### 3.3 Verständlichkeit (echte Verständnisprobleme, Änderung empfohlen)

**V1 (hoch): Z. 57 bis 72 mit Fußnote 1, S. 37.** "Konformitätsmatrix" bezeichnet die Tabelle in
`docs/requirements.md` (Z. 59), die Fußnote nennt die CSV im Thesis-Repo "Vollständige Konformitätsmatrix", der
Haupttext nennt dieselbe CSV "geprüfte Einzelzuordnung"; K6 (Z. 849 bis 850, 894, 1083) nennt sie "die in 4.2
verlinkte Konformitätsmatrix". Im Druck fehlen Repositorium und Dateipfad. Die Zeilenzahl 67 fehlt in K4, obwohl
K6 Z. 833 und K7 Z. 44 sie als Inhalt von 4.2 anführen. Ersatz: Z. 59 "sowie eine Konformitätsmatrix mit 67
Zeilen;"; Z. 63 bis 65 "... stuft deshalb jede der 67 Zeilen am Primärtext ein (Normstufe, Anwendbarkeit,
FF1-Kategorie) und hält das Urteil je Zeile in einer eigenen Datei fest, der geprüften Einzelzuordnung."; Fußnote:
"Die geprüfte Einzelzuordnung liegt als \texttt{thesis/daten/konformitaet-kategorien.csv} im öffentlichen
Repositorium dieser Arbeit (\href{...}{github.com/ab7z/mcs-thesis-docs}, Stand: Commit \texttt{b8a5277}); sie
führt Selbstauskunft des Arbeitsindex und Urteil je Zeile nebeneinander."; Z. 72 "im Wortlaut des Arbeitsindex".
Folgeänderung K6 Z. 849 bis 850, 894, 1083: "verlinkte Einzelzuordnung".

**V2 (mittel): Z. 113 bis 115, S. 38.** "Nicht anwendbar ... hierhin gehören Aussagen außerhalb des Umfangs und
nicht gewählte MAY-Funktionen." K6 tab:eval-sollist-summe zählt in dieser Klasse auch "Leitlinie" (CSV Zeilen 223
und 227: Leitlinien ohne BCP-14-Schlüsselwort; Summe 10). Ersatz: "... Aussagen außerhalb des Umfangs, nicht
gewählte \texttt{MAY}-Funktionen und Leitlinien ohne BCP-14-Schlüsselwort." (Kriterium 18)

**V3 (mittel): Z. 315, S. 43.** "Der eigene Prüfer aus \secref{sec:pruefkette}": K3 3.4 nennt den
"Mitschnittprüfer" nur beiläufig ("wird dabei wiederverwendet", Z. 416); K2 Z. 953 verweist für den Prüfer auf
4.4.3; K5 nennt ihn nicht. Der Prüfer (`scripts/wire-check.py`: eigener PCAP-Leser, eigene RFC-1071-Faltung, CRC32C,
TLV-Lauf; Kampagnenauswerter `p0/p1/p2-eval.py`) wird nirgends eingeführt. Der Ersatz zu F1 löst das mit, wenn er
"eigene Python-Prüfer" benennt; sonst hier einen Halbsatz ergänzen: "ein eigenes Python-Skript, das PCAP-Dateien
ohne Rust-Code liest".

**V4 (mittel): Z. 142 bis 143 und 156 bis 159, S. 38 bis 39.** "Vorversuche ... werden nicht verallgemeinert" und
zwei Absätze später "Die Vorversuche dienten darüber hinaus dazu ... gehören die daraus abgeleiteten
Mechanismenklassen zu den Ergebnissen". "darüber hinaus" hat nach dem Auswertungsabsatz keinen Bezug; der Leser
muss den scheinbaren Widerspruch selbst auflösen. Ersatz Z. 156 bis 159: "Auch ohne Verallgemeinerung dienten die
Vorversuche dazu, mögliche Ursachen für beobachtete Veränderungen und Verluste als Hypothesen zu formulieren und
gezielte Folgemessungen zu planen. Weil die Mechanismenklassen erst aus diesen Messbeobachtungen entstanden, gehören
sie zu den Ergebnissen dieser Arbeit; \chapref{chap:evaluation} stellt sie mit ihren Belegen dar."

**V5 (gering): Z. 69 bis 70, S. 37.** "werden nur mit ihrem FF1-Anteil bewertet": "FF1-Anteil" wird nicht
erklärt; einen Nicht-FF1-Anteil hat nur die Zeile 16/19 (Transitpflicht = FF2), bei 11.2 und 25.2 bis 25.4 geht es
um die einmalige Zählung (CSV 189, 225; K6 Z. 943 bis 945). Ersatz: "bleiben eine Zeile. Bewertet wird nur ihr
Anteil an Endpunktpflichten im Sinne von FF1; die Transitpflicht aus Abschnitt~16 gehört zu FF2, und jede
Normaussage zählt nur einmal."

**V6 (mittel): Tab. 4.4, Z. 261 bis 264, S. 41.** Zeile "Schutzmechanismus: keiner / optional / Übersetzung,
modusabhängige Laufzeit / Compiler, Laufzeit": "optional" bei C++ bleibt unerklärt und ohne Quelle; "Übersetzung"
und "Compiler" meinen dasselbe; "RAII" und "Allokatoren" werden nicht aufgelöst; der Text nach der Tabelle erklärt
nur Rust und Zig. Ersatz: "Prüfung von Speicherzugriffen & keine & optional (Bibliotheken, Werkzeuge) & zur
Übersetzungszeit; zur Laufzeit je nach Build-Modus & zur Übersetzungszeit; Bereichsprüfungen zur Laufzeit";
"Speicherverwaltung & manuell & manuell, RAII (Freigabe im Destruktor) & explizite Allokatoren & Ownership". Was
"optional" bei C++ meint, muss der Autor festlegen.

**V7 (mittel): Z. 272 bis 278, S. 42.** (a) "Statische Werkzeuge können Quelltext ohne ausgeführten Programmpfad
prüfen; nur dynamische Prüfungen und Fuzzing bleiben auf erreichte Pfade beschränkt" steht ohne Anschluss an das
Argument, und "nur" ist falsch platziert. (b) "Die Migration von Bun von Zig nach Rust bildet dazu den Referenzfall
aus Abschnitt 3.1": "dazu" hat keinen klaren Bezug; direkt davor steht der Zig-1.0-Satz. Die Quelle (Bun-Blog,
08.07.2026, Jarred Sumner) nennt als Gründe Use-after-free, Double Free und vergessene Freigaben in Fehlerpfaden,
die in Safe Rust Übersetzungsfehler sind; Zigs Reifegrad oder 1.0 werden nicht genannt. K3 nutzt den Fall für die
Lehre "Prüfinstanz muss zum Artefakt passen" (undefiniertes Verhalten trotz Zweitprüfung, Miri). Ersatz: "Diese
Garantien setzen korrekte Verträge an jeder \texttt{unsafe}-Grenze voraus. Ihr Vorteil liegt in der statischen
Prüfung: Der Compiler prüft Quelltext ohne ausgeführten Programmpfad, dynamische Prüfungen und Fuzzing erfassen
dagegen nur erreichte Pfade \cite{kernel-devtools,nsa-memory-safety}. Zig prüft ebenfalls zur Übersetzungszeit;
seine Laufzeitprüfungen hängen aber vom Build-Modus ab, und die Sprache hat noch keine Fassung~1.0 erreicht
\cite{zig-lang}. Dass ein großes Zig-Projekt aus denselben Gründen nach Rust wechselte (Use-after-free, Double
Free und vergessene Freigaben in Fehlerpfaden werden in Safe Rust zu Übersetzungsfehlern), zeigt die Migration von
Bun, der Referenzfall aus \secref{sec:externe-faelle} \cite{bun-in-rust}. Für die Vertrauensgrenze dieser
Bibliothek fiel die Wahl deshalb auf Rust." Welche Lehre der Bun-Fall hier tragen soll, muss der Autor festlegen.

**V8 (gering): Z. 46 bis 51, S. 36.** "wohl aber eine Vorgabe des Projektumfangs: Abschnitt~7 verringert ..."
Der RFC enthält eine (unmarkierte, kleingeschriebene) Regel, aus der die Arbeit eine Umfangsvorgabe ableitet; der
Folgesatz sagt das richtig. Shim-Header sind nur in einer Fußnote von K2 (Z. 94 bis 96) erklärt, ohne Verweis aus
K4. Ersatz: "... enthält keinen einzigen markierten Absatz, wohl aber den Anlass für eine Umfangsvorgabe:
Abschnitt~7 verringert die Obergrenze der \texttt{UDP Length} um vorangehende Shim-Header, also zusätzliche Header
zwischen IPv4- und UDP-Header (\secref{sec:ipv4}). Die Implementierung ..."

**V9 (gering): Z. 132 bis 133, S. 38.** Pfadstufe 2 nennt nur Mittel, die vier anderen Stufen sagen, was sie
prüfen. Ersatz: "Linux-Netzwerk-Namensräume mit \texttt{veth} in einer Ubuntu-VM unter VMware Fusion; prüft
Weiterleitung, Adressumsetzung und Paketfilter unter eigener Kontrolle, ohne fremde Akteure." (K6 Z. 239 bis 252)

**V10 (gering): Tab. 4.3, Z. 200, S. 40.** K1 Z. 154 kündigt an, dass 4.3 die Rolle von IPv6 als Kontrollgröße
erklärt; die Zelle sagt nicht, was eine IPv6-Kontrolle ist. Ersatz: "IPv6-Datagramme als Vergleich zu
IPv4-Befunden auf demselben Pfad; nicht mit der Bibliothek erzeugt und nicht auf Konformität geprüft".

**V11 (gering): Z. 145 bis 146, S. 39.** "Sendeversuch, Sendemanifest": Sendemanifest wird erst in K5 (Z. 105 bis
106) beschrieben; Sendeversuch ist ein Vorgang, kein Artefakt. Ersatz: "das Ergebnis des Sendeaufrufs, das
Sendemanifest (je Sendevorgang eine Zeile mit Folgenummer, Adressen und Längen, die das Sendeprogramm schreibt),
Sender-PCAP, Empfänger-PCAP und Empfängerausgabe."

**V12 (gering): Z. 329 bis 332, S. 43.** "Dass daneben auch die Norm selbst Prüfgegenstand bleiben muss" kann als
Prüfung des RFC-Texts gelesen werden; gemeint ist der Abgleich der Implementierung mit dem Normtext. "grüner
Prüfkette" ist Werkzeugjargon (auch K6 Z. 1007, 1015, 1118). Ersatz: "Dass daneben der Abgleich mit dem Normtext
ein eigener Prüfschritt bleiben muss, zeigte die Schlussphase der Implementierung: Ein nachträglicher RFC-Abgleich
fand trotz bestandener Prüfkette noch Konformitätslücken ..."

**V13 (gering): Z. 323 bis 324, S. 43.** "Die vierte Entscheidung" zwingt zum Zurückzählen auf Z. 216 bis 217;
"Testsuite" kommt sonst nicht vor; warum die Gegenproben auf das Gefahrenmodell antworten, steht nur in K3. Ersatz:
"Als vierte Entscheidung treten neben die Unit-, Integrations- und Property-Tests (\secref{subsec:pruefmittel})
zwei Gegenproben, deren Ergebnis nicht von einer Modellaussage abhängt (\secref{sec:gefahrenmodell})."

### 3.4 Silbentrennung und PDF

**S1 (Fehler, Kriterium 23): S. 43, Z. 315.** "Optionss- / truktur" ist falsch getrennt (Wortbestandteil
"struktur" zerrissen). Fix: `Options\-struktur`, danach Neubau und Kontrolle des Umbruchs auf S. 43. Vollständige
Zählung S. 36 bis 43: 30 Zeilenend-Striche, davon 26 korrekte Trennungen (Ab-schnitt, Abschnit-ten,
Im-plementierung, Fund-stelle, dokumentier-tes, Messzeit-punkt, Tabel-le, Finn-land, Sende-manifest, Verwerfun-gen,
abge-leiteten, Spra-che, Drit-tens, Betriebssystemschnitt-stellen, über-setzt, Spei-chersicherheit,
Speicher-bereichs, Speichersicher-heit, Schutzmechanis-mus, Speicherverwal-tung, über-dauern, Kapi-tel,
dokumen-tiert, Parser-codes, Voraus-setzungen, Prüfgegen-stand), 3 reguläre Bindestriche (Provider-Kanten,
IPv4-Header, PCAP-Beweisdateien) und die eine falsche Trennung.
**S2 (kosmetisch): S. 37, Tab. 4.1.** "MUST/ SHOULD" mit sichtbarem Leerzeichen nach dem Schrägstrich (Quelle
`\texttt{MUST/} \texttt{SHOULD}`, Z. 91). Alternative: `\texttt{MUST/}\allowbreak\texttt{SHOULD}`.
**S3 (kosmetisch): S. 42.** Fußnotenziffer 2 steht im Wortinneren ("unsafe²-Blöcke", Z. 283); Fußnote an die
erste Nennung in Z. 273 verschieben.
**S4 (akzeptabel): S. 39.** Leerraum unten (etwa ein Fünftel der Seite), weil Tab. 4.3 mit `[H]` auf S. 40 rutscht.
Übergänge S. 35/36 und 43/44, Fußnotenplatzierung, Abb. 4.1 (Balken, Zahlen, Klammer), Verzeichnisse (Abb. 4.1,
Tab. 4.1 bis 4.4) und Verweisnummern sind in Ordnung; kein "??"; kein Text im Rand.

### 3.5 Sprachlich optional (Geschmack, keine Abgaberelevanz)

- O1 Z. 101 bis 102: "die bedingte Ressourcengrenze aus Abschnitt~25.2" (Sec. 25.2 ist ein bedingtes SHOULD).
- O2 Z. 307 bis 308: "in die MTU der ausgehenden Schnittstelle passen; größere logische Datagramme teilt die
  Bibliothek mit FRAG".
- O3 Z. 100: "zeigt zugleich eine Grenze des Arbeitsindex:" (Plural "Grenzen" mit nur einem Beispiel).
- O4 Z. 120 bis 121: FF2-Wortlaut wie K1: "auf den untersuchten realen Netzpfaden ... unverändert erhalten bleibt".
- O5 Z. 123 bis 124: "Surplus Area erhalten, verändert oder entfernt oder Datagramm verworfen" (Objekte trennen,
  wie tab:operationalisierung).
- O6 Z. 123: "Wire-Datagramme" durch "IP-Datagramme" ersetzen (K2 Z. 776).
- O7 Z. 178: "acht Pflichtoptionen (im RFC \textit{must-support})" (K5 Z. 108 sagt Pflichtoptionen).
- O8 Z. 171: Spaltenkopf "Außerhalb des Umfangs" groß schreiben.
- O9 Z. 264: "Stand der Sprachdefinition" statt "Sprachfassung".
- O10 Z. 269 bis 271: "Speichersicherheitsgarantien (in Safe Rust)" statt "Safe-Rust-Garantien"; "Buffer
  Overflow" wie Z. 242 statt "Pufferüberläufen".
- O11 Z. 213: "die den nötigen Zustand und jede Antwort ... verorten".
- O12 Z. 244 bis 247: "Matt Miller vom Microsoft Security Response Center (MSRC)", "in der stabilen Auslieferung
  (Stable Channel)".
- O13 Z. 289: "fiel erst der Zweitprüfung im Pull-Request auf" (wie K6 Z. 1004; Fund kam laut PR #12 von der
  Codex-Prüfung).
- O14 Z. 314: "PCAP-Belegdateien" statt "PCAP-Beweisdateien" (K3 spricht von Belegen).
- O15 Z. 21: "Anforderungskatalog" statt "Anforderungsbestand" (Z. 9 und 53 sagen Katalog).
- O16 Z. 331: "grüner Prüfkette" (Metapher) durch "bestandener Prüfkette" ersetzen, auch in K6.

## 4. Bestätigte Aussagen (Auswahl mit Beleg)

- 103 mit `>>` markierte Absätze; 104. grep-Treffer ist der Erläuterungssatz in Sec. 2 (RFC Z. 126). Verteilung je
  Hauptabschnitt exakt wie Abb. 4.1 (8/2, 9/5, 10/21, 11/44, 12/3, 13/9, 14/6, 15/5, 16/1, 19/2, 25/4, 26/1); 65
  von 103 in Sec. 10 und 11; Abschnitte 1 bis 7 ohne Marker.
- Sec. 7 (RFC Z. 365 bis 366): Obergrenze um vorangehende Shim-Header verringert; Protocol 17 (`src/wire/ip.rs:70`).
- `docs/requirements.md`: 49 FR (FR-01 bis FR-50 ohne FR-47), 12 NFR, Matrix 67 Zeilen (162 bis 228); erster
  Commit 2026-05-30 vor Step 1 (2026-06-10), 15 Commits bis 2026-09-03.
- Tab. 4.1: alle fünf Zeilen stimmen mit dem Wortlaut der Matrix (Level, Covered, FR/NFR) und mit dem RFC überein
  (Sec. 8 Z. 465 bis 467; Sec. 9 Z. 524; Sec. 10 Z. 622 bis 626; Sec. 11.2 Z. 863 bis 871; Sec. 12 Table 1);
  Bündelung der Ressourcengrenze aus Sec. 25.2 (RFC Z. 2125 bis 2131) korrekt.
- FF1-Wortlaut "vollständig, teilweise oder nicht" in K1 Z. 111 bis 112; Kategorien und FF2-Status identisch mit
  K3 tab:operationalisierung und K6.
- Acht must-support-Optionen: EOL, NOP, APC, FRAG, MDS, MRDS, REQ, RES (RFC Z. 700 bis 703); TIME, AUTH, EXP, UCMP,
  UENC, UEXP nicht darunter; keine typisierte Verarbeitung dieser Arten im Code; REQ/RES nur Parsen/Serialisieren.
- Sec. 6 Prinzipien 1 und 2 tragen "Zustand und Antwort in Anwendung oder Bibliothek"; man7 raw(7): "When the
  IP_HDRINCL option is set, datagrams will not be fragmented and are limited to the interface MTU."
- PR #12 (2026-06-11): Codex-Review fand die SurplusLayout-Inkonsistenz bei ungeradem Start; 23 Tests im Commit
  2c7d62a nachgezählt (9+6+8+0); Fix f0fb445 vor dem Merge. Fuzz-Ziel und Property-Tests je Parsefläche (neun
  Fuzz-Ziele mit Erst-Commits Step 2 bis 12; `tests/properties_*.rs`); Fuzz- und Property-Läufe nachweislich
  ausgeführt (proptest-Regressionsdateien, geschrumpfte Seeds); Pflichtgate `scripts/pre-pr.sh`.
- Zwei `unsafe`-Blöcke in der Bibliothek (`src/socket/send.rs:131`, `src/socket/recv.rs:169`); geborgte
  `&'a [u8]`-Ausschnitte (`src/options/parse.rs`); Enums für Optionsarten und acht Fehler-Enums; keine
  Parser-Crates (Cargo.toml: thiserror, socket2, libc, crc32c, log, clap).
- cargo-fuzz/libFuzzer (`fuzz/Cargo.toml`); elf handgeschriebene Lean-Module; `LEAN_RFC9868_VALIDATION.md` grenzt
  Modell und Rust-Code ab; Schritt 18 und PR #25 (2026-08-02) als nachträglicher RFC-Abgleich.
- Pfadstufen, Ubuntu-VM unter VMware Fusion (vmware.log im Archiv vom 10.08.), WireGuard-Stufe 3, Endpunkte,
  Hotspot mit Hotspot-NAT und offener CGNAT-Frage, tcpdump beidseitig, fünf Artefakttypen je Richtung, Attributions-
  intervall in K6 gleich verwendet, keine Gerätezuschreibung, Wireshark/tshark 4.6 (Repo-Doku, K2, K3).
- Chromium-Seite wörtlich: "Around 70% of our serious security bugs are memory safety problems"; "912 high or
  critical severity security bugs since 2015, affecting the Stable channel". Bun-Blog: "Bun v1.3.14 was the last
  version of Bun written in Zig. Bun v1.4.0 will be the first version of Bun written in Rust." NSA-CSI (Ver. 1.1)
  nennt Rust unter den speichersicheren Sprachen und trägt die SAST/DAST-Aussage. Zig-Dokumentation 0.16.0:
  Laufzeitprüfungen je Build-Modus (Debug/ReleaseSafe an, ReleaseFast/ReleaseSmall weitgehend aus), keine 1.0.
  Rust Book Kap. 9.1 (panic bei `v[99]`) und 10.3 (Lifetimes gegen hängende Referenzen); N2310 Annex J.2
  (Array-Index außerhalb des Bereichs ist undefiniert).
- Alle Ankündigungen aus K1 (Z. 141, 154, 166) und K3 (Z. 168, 415, 544) sowie alle Rückverweise aus K2, K5, K6, K7
  auf Kapitel 4 treffen vorhandenen Inhalt (Ausnahme: Zahl 67, siehe V1).

## 5. Nicht prüfbare Aussagen und fehlende Belege

- Millers Vortrag (Video) selbst: nur Folien und MSRC-Blog geprüft (L1).
- NSA-CSI: nur über einen Lesedienst abrufbar (L5); Inhalt geprüft, die Erstfassung vom 10.11.2022 selbst nicht.
- kernel-devtools: nur die Indexseite geprüft, nicht die verlinkten Einzelseiten (L6).
- Tab. 4.4: "optional" (C++) und "teilweise" (Zig) sind Wertungen ohne zitierte Quelle (L7, V6); "1.0 seit 2015"
  und "vor 1.0" (Bib: Zig 0.16.0) korrekt.
- `iso-c` zitiert N2310 als "Arbeitsentwurf zu ISO/IEC 9899:2018 (C17)"; N2310 ist formal der erste C2x-Entwurf
  nach C17 und gilt als frei verfügbarer Näherungstext zu C17. Die belegte Aussage (Annex J.2, Zugriff außerhalb
  eines Arrays ist undefiniert) steht darin; kein Befund.
- Kopfzeile der CSV nennt "Auswertungsstand f847895"; das Implementierungsrepo hat seitdem Zeile 199 der Matrix
  (Covered yes zu partial) angepasst; K6 Z. 892 bis 894 führt Zeile 199 bereits als Abweichung. Kein K4-Befund.
- Land des Endpunkts 1blue (AS42730) nennt keine zugelassene Quelle; "Deutschland und Finnland" für das
  Cloud-Dreieck (mcs Nürnberg, HEL1, 1blue) ist damit nicht vollständig belegt.
- Ob "Jede Messung ... genau zwei Messpunkte" als Regelfall gemeint war, ist Autorenabsicht (F2 gibt die Faktenlage).

## 6. Urteil zur Abgabereife (im geprüften Umfang)

Kapitel 4 ist fachlich in seinen Kernaussagen richtig und gut belegt: Alle Zahlen (Marker, Verteilung, Anforderungen,
Matrixzeilen, Pflichtoptionen, Testzahl), alle RFC-Zuordnungen der Tabelle 4.1, die FF1-Kategorien, das
FF2-Statusvokabular, die Raw-Socket-Begründung und die Implementierungsaussagen halten der Prüfung am Primärtext,
am Code und an den Archiven stand. Der Stil ist kurz und konkret, ohne Gedankenstriche, mit wenigen Anglizismen.

Nicht abgabereif ohne Korrektur sind nach meiner Einschätzung vier Punkte: F1 (Werkzeugkette tshark/OCS-Nachrechnung
gilt für die Wire-Prüfung, nicht für die FF2-Kampagnen; mit Folgeänderung in K6), F2 ("genau zwei Messpunkte"
gegen die Kampagnen vom 10./11.08. und Tab. 4.3), S1 (Trennung "Optionss-/truktur") und V1 (drei Namen für zwei
Dateien, fehlende Zahl 67, Fußnote ohne Repositorium). Dazu empfehle ich V2, V3, V4 und V7 als kleine, eng
begrenzte Änderungen; F3, L1 bis L7 und V5 bis V13 sind Präzisierungen mit geringem Aufwand. Die Punkte in 3.5 sind
Geschmack und können entfallen.

Nach Umsetzung von F1, F2, S1 und V1 (plus Neubau und Kontrolle der neuen Trennungen) halte ich Kapitel 4 im
geprüften Umfang für abgabereif. Grenzen dieses Urteils: keine Wiederholung von Tests oder Messungen; nicht alle 67
Einzelurteile der CSV am RFC geprüft (nur die fünf Tabellenzeilen, die Bündelzeilen 189, 224, 225 und die Summen);
Miller-Video nicht abgerufen, NSA-Dokument nur über einen Lesedienst; Kapitel 5 und 6 nur für Verweise und
Konsistenz gelesen.
