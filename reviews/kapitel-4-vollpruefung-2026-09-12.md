# Kapitel 4: vollständige Prüfung nach 24 Kriterien

Prüfdatum: 12. September 2026. Autor der Thesis: GreenCodeDoesntSmell.
Geprüft wurde das Kapitel „Analyse und Anforderungsmodell“ im bestehenden Wortlaut.
Der Bericht enthält Befunde und Ersatzvorschläge; kein Vorschlag wurde in den Thesis-Text übernommen.

## Aktueller Abschlussstand

Die Befunde wurden inzwischen umgesetzt und erneut geprüft. Maßgeblich ist jetzt der
[Abschlussbericht vom 13. September](kapitel-4-abschluss-2026-09-13.md).
Die nachfolgenden Befunde und der erste Nachtrag dokumentieren den damaligen Zwischenstand.
Insbesondere die dortige Verwendung von `docs/evaluation.md` wurde durch den direkten Codeabgleich korrigiert.

## Nachtrag vom 13. September 2026: Abgleich mit der unabhängigen Zweitmeinung

Der unveränderte Zweitbericht liegt unter
[kapitel-4-zweitmeinung-2026-09-13.md](kapitel-4-zweitmeinung-2026-09-13.md).
Dieser Nachtrag dokumentiert einen gezielten Quellenabgleich der zentralen Unterschiede,
keine erneute vollständige Kapitel- oder PDF-Prüfung. Der ursprüngliche Bericht folgt darunter.
Seine Zahl von vier Korrekturpunkten ist durch die zusätzlichen Befunde überholt.

- **Werkzeugkette: zusätzlicher bestätigter Sachbefund (Claude F1).**
  Die ursprüngliche Bestätigung in E05 und der Ersatzvorschlag L11 sind zu weit gefasst und müssen
  ersetzt werden. `scripts/wire-check.sh:144-157` verbindet tshark mit der unabhängigen Wire-Prüfung.
  Dagegen übernehmen `scripts/p0-eval.py:271`, `p1-eval.py:122` und `p2-eval.py:259-260` den
  OCS-Status aus `ocs_reports` der Empfängerausgabe. Auch `docs/evaluation.md:28-33` unterscheidet
  die Prüfrollen ausdrücklich. Die unterschiedlichen Verfahren dürfen nicht als einheitliche
  Kampagnenprüfung beschrieben werden. Die Verallgemeinerung steht ebenfalls in
  `06_evaluation.tex:114-115`; diese Stelle muss bei einer Umsetzung mit korrigiert werden.
  Die elf Archivlisten wurden in diesem Nachtrag nicht erneut vollständig geprüft; die Aussage
  über das Fehlen von tshark-Dateien in allen späteren Archiven bleibt hier Claudes Nachweis.
- **Dateibezeichnungen und Nenner: zusätzlicher bestätigter Verständlichkeitsbefund (Claude V1).**
  Kapitel 4 nennt die Repository-Matrix, die eigene Einzelzuordnung und in der Fußnote erneut eine
  Konformitätsmatrix. Kapitel 6 verweist unter diesem Namen auf die CSV. Die Zahl 67 steht in
  Kapitel 6, fehlt aber bei der Einführung in Kapitel 4. Zwei Dateien eindeutig benennen, die
  67 Zeilen bei der Einführung nennen und Folgebezeichnungen in Kapitel 6 angleichen.
- **Messpunkte, Worttrennung und NSA-Ausgabe:** Übereinstimmung der beiden Berichte
  (ursprünglich F01/F03/F04; Claude F2/S1/L5). Der erneute Textabgleich bestätigt den zusätzlichen
  macOS-Mitschnitt in `thesis/evidence/README.md:25-26`. Keine erneute PDF-Prüfung für diesen Nachtrag.
- **UEXP:** Die Formulierung sollte präzisiert werden; die Einordnung als klarer Sachfehler ist
  nicht zwingend. RFC 9868, Abschnitt 12.3, nennt die Kennung selbst „reserved for experiments“.
  Die Unterscheidung zwischen UCMP/UENC und der nutzbaren Experimentoption UEXP bleibt sinnvoll.
- **Testvorgabe (ursprünglich F02):** Claude nennt zusätzliche historische Nachweise für die
  tatsächliche Umsetzung. Diese müssen vor einer endgültigen Entscheidung gegen die konkrete
  universale Aussage geprüft werden. F02 belegt weiterhin keinen Verstoß gegen die Testvorgabe.
  Es wäre falsch, daraus einen feststehenden historischen Ausführungsfehler zu machen.

Nicht alle Ersatzvorschläge des Zweitberichts sollten wörtlich übernommen werden:

- „Jede Messung hat mindestens zwei … Mitschnitte“ bleibt angesichts der in Kapitel 6 ausdrücklich
  beschriebenen Piloten ohne Mitschnitt zu weit. Die vorhandenen Belege je Messstufe benennen.
- „Leitlinien ohne BCP-14-Schlüsselwort“ darf kein allgemeines Ausschlusskriterium werden.
  Die CSV stuft Zeile 222 ausdrücklich als unmarkierte, aber anwendbare Normform ein.
  Entscheidend ist die konkrete normative Bedeutung, nicht allein ein Schlüsselwort.
- Die Wire-Prüfung ist im Archiv vom 10.08. enthalten. Deshalb nicht pauschal behaupten,
  es habe in Kampagnen überhaupt keine fremde Gegenprobe gegeben.

Die weiteren Literatur- und Sprachhinweise des Zweitberichts sind noch nicht alle erneut verifiziert.
Thesis-Text, Literaturdatei und PDF bleiben unverändert. Der nächste Schritt ist eine konsolidierte
Überarbeitung auf Grundlage der bestätigten Befunde, anschließend Neubau und erneute PDF-Kontrolle.

## Ergebnis und Reichweite

Kapitel 4 ist in Aufbau und fachlicher Grundrichtung tragfähig. Die Zahlen der Normauswertung,
der Anforderungsumfang, die FF1-Kategorien und die wesentlichen Technologiebegründungen sind bestätigt.
Vor einer uneingeschränkten Freigabe sind vier konkrete Punkte zu korrigieren oder zu präzisieren:
F01 Messpunkte, F02 Testvorgabe, F03 Silbentrennung und F04 Literaturangaben.
F01 ist ein belegter Widerspruch zum eigenen Messaufbau. F02 betrifft die Reichweite eines Prozessnachweises,
F03 die deutsche Worttrennung und F04 die bezeichnete Ausgabe einer Quelle.
Die zusätzlichen Empfehlungen L01 bis L12 sind keine zwölf weiteren Sachfehler.
Eine vollständige Neugliederung oder Streichung ganzer Abschnitte ist nicht begründet.

Alle 24 Kriterien wurden auf ihre Anwendbarkeit geprüft und die relevanten Aspekte bearbeitet.
Erfasst wurden 198 Einheiten: 94 Sätze beziehungsweise einleitende Texteinheiten, 85 Tabellenzellen,
9 Überschriften, 8 Beschriftungs-/Diagrammeinheiten und 2 Fußnoten. Die Satzprüfung berücksichtigt jeweils
auch die Nachbarsätze und den Absatz. Die 27 Werte der Abbildung sind gemeinsam als Dateneinheit erfasst.

Die Prüfung umfasst die Aussagen des Kapitels, ihre angegebenen Quellen und die dafür benötigten Code-,
Historien- und Messbelege. Sie ist keine erneute Ausführung aller Implementierungstests und Messkampagnen.
Die externe 67-zeilige Matrix wurde auf Stand, Inhalt, Aufbau, Summen und ihre Verwendung in Kapitel 4 geprüft;
die fünf abgedruckten Zeilen wurden einzeln am RFC gegengeprüft. Eine neue End-to-End-Konformitätsprüfung
aller 67 Implementierungsurteile gehört nicht zu diesem Kapitelreview und wurde nicht behauptet.

## Geprüfter Stand

- Thesis: Stand vom 10.09.2026 auf `main`.

- Implementierung: Stand vom 03.09.2026; für historische Aussagen zusätzlich die benannten älteren Stände.

- SHA-256 `thesis/chapters/04_analyse.tex`: `a19c3926f9d981437d98ed9ff351d0c5ca33c05e529029567db1b208474ac2f2`.

- SHA-256 `thesis/main.pdf`: `0c41959d09350c45ea65f43b4a80ac6135a2e2bf0c291419538e60ec729601af`.

- SHA-256 `AGENTS.md`: `bfefe7d7a9270d9015aae940520b470a2011f1da53d961bbad111788ff18cec2`.

- Bereits vorhanden: uncommittete Ergänzung der 24 Prüfkriterien in `AGENTS.md`; unverändert beibehalten.
- Kapitel 4: PDF-Seiten 42 bis 49, Druckseiten 36 bis 43. Übergänge auf PDF-Seiten 41 und 50 zusätzlich angesehen.
- Alle acht Kapitelseiten visuell geprüft, einschließlich vier Tabellen, einer Abbildung und beider Fußnoten.
- Gesamter Neubau in einer temporären Kopie: drei LaTeX-Läufe, Biber und makeglossaries, jeweils Exitcode 0.
- Im letzten LaTeX-Lauf keine Warnungen, undefinierten Verweise, Overfull- oder Underfull-Meldungen.
- Ausgelesener PDF-Text des gesamten Neubaus identisch zur vorhandenen 95-seitigen PDF.
- Alle 24 unterschiedlichen Querverweisziele des Kapitels existieren; die angekündigten Inhalte wurden mitgeprüft.
- Thesis-Quellen, vorhandene PDF, Implementierung und Insights-Inbox wurden nicht geändert.

Lokale QA-Artefakte und Build-Protokolle: `/var/folders/sx/6w30525112jgcghk1y5gp1840000gn/T/udp-k4-review-6x1smcul`. Dieser temporäre Pfad ist kein dauerhafter Literaturbeleg.

## 24-Kriterien-Matrix

„Offen“ bedeutet hier: geprüft, aber ein dokumentierter Befund ist noch nicht umgesetzt.
„Geprüft“ bedeutet keine Garantie absoluter Fehlerfreiheit. Kein Kriterium wurde ausgelassen.

| Nr. | Kriterium | Status | Nachweis / Ergebnis |
|---|---|---|---|
| 1 | Fachliche Richtigkeit | offen | Norm- und Technologieaussagen gegengeprüft; F01, Präzisierung F02. |
| 2 | Quellen und Belege | offen | Primärquellen und Projektbelege geprüft; Ausgabe der NSA-Quelle F04. |
| 3 | Verbindlichkeit | geprüft | BCP 14, unmarkierte Festlegungen, bedingte Empfehlungen und Sender-/Empfängerrollen getrennt. |
| 4 | Persönlicher Schreibstil | offen | Satzprüfung abgeschlossen; L01 bis L12 und F02 zur Vereinfachung. |
| 5 | Einzelne Sätze | offen | Alle 198 Einheiten geprüft; konkrete Ersatzformulierungen unten. |
| 6 | Zweck und Ursache | offen | Insbesondere Extraktion, Arbeitsindex, Sprachauswahl und Prüfmittel; L01, L02, L06, L11. |
| 7 | Zusammenhang | offen | Absätze, Übergänge und Nachbarsätze geprüft; F01 und F02 betreffen auch Nachbarsätze. |
| 8 | Relevanz und Wiederholungen | geprüft | Alle vier Hauptteile haben eine Funktion; optionale Straffung statt Abschnittsstreichung. |
| 9 | Begriffe | offen | FF1/FF2 konsistent; „Parsefläche“, „Um-eins-“ und einige abstrakte Begriffe vereinfachen. |
| 10 | Fußnoten | geprüft | GitHub-Verweis gültig; unsafe/UNSAFE-Unterscheidung richtig und kurz. |
| 11 | Ziel und Umfang | geprüft | Linux/IPv4/Benutzerraum, Pflichtoptionen und Messinfrastruktur stimmen mit den Anschlusskapiteln überein. |
| 12 | Ergebniszuordnung | offen | Beobachtung und Zuschreibung grundsätzlich richtig; Verallgemeinerung der Messpunkte F01. |
| 13 | IPv4, MTU und Fragmentierung | geprüft | Shim-Grenze, Protocol 17, Raw-Sendepfad und MTU geprüft; keine Wiederholung sachfremder Grundlagen nötig. |
| 14 | UDP und Prüfsummen | geprüft | OCS/UDP-Verhältnis und Zuständigkeiten geprüft; keine neue Prüfsummenarithmetik im Kapitel. |
| 15 | Surplus Area und Optionen | geprüft | Tabellenauszug, Formatgrenzen, NOP, Reservierungen und Pflichtoptionen geprüft; L03 erläutert UEXP. |
| 16 | Betriebssystem und Netzpfad | geprüft | Raw-Zugang, Alternativen und konkrete Codeangaben gegengeprüft; Plattformgrenzen bleiben erhalten. |
| 17 | Messbedingungen | offen | Versuchsunterlagen und zwei Archiv-Siegel geprüft; zusätzlicher Mitschnitt belegt F01. |
| 18 | Methodik | geprüft | 103 Absätze sind Kontrollzahl, nicht vollständige Anforderungsmenge; FF1 und FF2 bleiben getrennt. |
| 19 | Aussagekraft der Nachweise | geprüft | Modell/Rust, Tests/Fehlerfreiheit, technische Erfüllbarkeit/Umsetzung und Messgrenzen geprüft. |
| 20 | Entwicklungs- und Prüfablauf | offen | Historischer Fehler und eingeführte Regel belegt; universale Durchführungsaussage F02 präzisieren. |
| 21 | Abbildungen, Tabellen, Verweise | geprüft | Alle Werte und Zellen gelesen; keine fehlenden Ziele; optionale Präzisierung der Sprachtabelle L08. |
| 22 | PDF-Lesbarkeit | geprüft | Acht Seiten plus Übergänge visuell geprüft; keine abgeschnittenen Inhalte; optionale Umbrüche P01. |
| 23 | Silbentrennung | offen | 30 Trenn-/Bindestrichstellen an Blockzeilenenden geprüft; ein Fehler F03. |
| 24 | Abschlusskontrolle | geprüft | Separater vollständiger Build erfolgreich; Textvergleich und Unverändertheit geprüft. Nach Umsetzung neu prüfen. |

## Belege und bestätigte Ergebnisse

### E01: Normauswertung und Abbildung

Primärtext: `literature/rfc9868.txt`, insbesondere Abschnitte 2, 6 bis 10, 11.2, 12 und 25.2.
Die Absatzanfänge mit `>>` wurden unabhängig von der TikZ-Liste gezählt und dem jeweiligen RFC-Hauptabschnitt
zugeordnet. Ergebnis: 103. Die Verteilung ist exakt
`0,0,0,0,0,0,0,2,5,21,44,3,9,6,5,1,0,0,2,0,0,0,0,0,4,1,0` für Abschnitte 1 bis 27.
Alle Balkenwerte stimmen. `21 + 44 = 65`; `65 / 103 = 63,11 %`, also knapp zwei Drittel.
Abschnitte 1 bis 7 enthalten keine Markierung. Abschnitt 7 nennt dennoch die Shim-Längenregel.
Die fehlende Markierung schränkt die normative Bedeutung nicht automatisch ein.
Das bestätigt [RFC 8174, Abschnitt 2](https://datatracker.ietf.org/doc/html/rfc8174#section-2).
Die Stärke von MUST/SHOULD/MAY wurde nach [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.html) geprüft.

### E02: Anforderungen, Historie und Konformitätsdatei

`../udp-transport-options/docs/requirements.md`: genau 49 FR-Zeilen, FR-01 bis FR-50 ohne FR-47,
und zwölf NFR-Zeilen. Die Datei ist seit dem 30.05.2026 vorhanden; die Umsetzung der
Prüfsummenprimitive folgte am 10.06.2026. Die Aussage zur frühen Anlage ist damit belegt.
Die weitere Historie enthält die Fortschreibungen.

Der veröffentlichte
[CSV-Verweis](https://github.com/ab7z/mcs-thesis-docs/blob/main/thesis/daten/konformitaet-kategorien.csv) ist über die
GitHub-API erreichbar. Die lokale Datei unterscheidet sich nur in der ersten Kommentarzeile, nicht in Daten oder
Bewertungen. Sie enthält 67 Zeilen: Implementierung 50 vollständig, 7 teilweise, 10 nicht anwendbar;
technische Erfüllbarkeit 57 vollständig, 10 nicht anwendbar. Die Kapitel-6-Summen stimmen damit überein.
Die beiden Urteile werden dort getrennt ausgewiesen. Kein vermeintlicher Widerspruch zwischen
„57 technisch vollständig“ und „50 vollständig umgesetzt“ wurde als Fehler gemeldet.

Die fünf Zeilen von Tabelle 4.1 wurden jeweils gegen den Arbeitsindex und den Primärtext geprüft:

| Zeile | Ergebnis |
|---|---|
| Abschnitt 8 / FR-05 | Null-Pad und Verwerfen der Optionen stimmen. Im Satz ist kein Verwerfen der Nutzdaten behauptet. |
| Abschnitt 9 / FR-21 | Nichtnull-OCS bei Nichtnull-UDP-Prüfsumme stimmt. |
| Abschnitt 10 / FR-09, FR-14 | Grenze 254 und kleinstes Format stimmen; `local strict receive` ist Projektauskunft. |
| Abschnitt 11.2 / FR-16, NFR-05 | Mischung mit der Ressourcenempfehlung aus 25.2 wird im Folgeabsatz ausdrücklich erklärt. |
| Abschnitt 12 / FR-39 | Alle drei Kennungen sind reserviert, UEXP speziell für Experimente; L03 ist eine Präzisierung. |

Die [Errata-Liste zu RFC 9868](https://www.rfc-editor.org/errata/rfc9868) führt EID 8834 als Verified/Technical
und verweist für die Überlängenbehandlung auf Abschnitt 10. Die geprüften Verweise aus Kapitel 3 und der
Matrix sind damit vereinbar. Nicht aus einem SHOULD ein MUST gemacht und keine lokale Parserstrenge als RFC-Pflicht ausgegeben.

### E03: FF1, FF2 und Messaufbau

Abgleich mit Kapitel 1, Abschnitt 1.3; Kapitel 3, Forschungsdesign und Tabelle 3.1; Kapitel 6,
Testkonzept, kontrollierte Stufen, Zugangspfad und Soll-Ist-Abgleich.
Der FF1-Maßstab betrifft technische Erfüllbarkeit unter eigenen Umfangsvorgaben. FF2 betrifft gerichtete
Szenarien und die Erhaltung der Surplus Area. Die Kategorien und die Sonderklasse ungültiger Läufe passen.
Einzelne FRAG-Datagramme sind nicht automatisch getrennte Untersuchungseinheiten.

Die fünf Pfadstufen und die breitere Messinfrastruktur sind in den Versuchsunterlagen wiederzufinden.
WireGuard ist eine Kapselungskontrolle, kein Beleg für native Surplus-Durchlässigkeit des äußeren Pfads.
Der macOS-Beobachtungspunkt und native IPv6-Kontrollen machen macOS/IPv6 nicht zur Bibliotheksplattform.
`lernnotizen/ff2-ttl-pfad/bericht.md`, Abschnitt 7, beschreibt zusätzliche Grenzmitschnitte.
Die SHA-256-Siegel der Archive `external-campaign-20260810T200118Z.tar.zst` und
`bidir-campaign-20260811.tar.zst` wurden erneut erfolgreich geprüft. Im zweiten Archiv liegen
`raw/mac-en0.pcap` sowie getrennte `raw/achim/`- und `raw/mcs/`-Mitschnitte und Manifeste.
Das ist direkte Artefaktevidenz gegen die pauschale Zweipunktbehauptung; F01.
Keine neue Netzwerkverbindung zu Messendpunkten und keine neue Kampagne wurde dafür gestartet.

### E04: Sprachauswahl und Sicherheitsangaben

- Microsoft: [MSRC-Beitrag vom 16.07.2019](https://www.microsoft.com/en-us/msrc/blog/2019/07/a-proactive-approach-to-more-secure-code/)
  bestätigt Datenerfassung seit 2004, Bezug auf Millers BlueHat-Vortrag 2019 und rund 70 % der jährlich
  mit CVE versehenen Schwachstellen. Das Video selbst war nicht abrufbar; der offizielle Beitrag trägt die Aussage.
- [Chromium Memory Safety](https://www.chromium.org/Home/chromium-security/memory-safety/)
  bestätigt die Bezugsmenge von 912 hohen/kritischen Stable-Channel-Sicherheitsfehlern seit 2015 und rund 70 %.
- [NSA Software Memory Safety](https://media.defense.gov/2022/Nov/10/2003112742/-1/-1/0/CSI_SOFTWARE_MEMORY_SAFETY.PDF)
  nennt Rust unter speichersicheren Sprachen und beschreibt Grenzen und statische/dynamische Prüfungen.
  Die Aussage stimmt, die ausgelieferte Dokumentfassung ist jedoch April 2023, Version 1.1; F04.
- Das [Rust-Buch zu Ownership](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html),
  [zu Bounds-Panics](https://doc.rust-lang.org/book/ch09-01-unrecoverable-errors-with-panic.html)
  und das [Rustonomicon zu Leaks](https://doc.rust-lang.org/nomicon/leaking.html) tragen die
  Unterscheidung von Speicherzugriffsschutz, Speicherverwaltung und weiterhin möglichen Leaks.
- [Rust 1.0 vom 15.05.2015](https://blog.rust-lang.org/2015/05/15/Rust-1.0/) bestätigt den Tabellenwert.
- [Zig 0.16.0, Build Modes und Illegal Behavior](https://ziglang.org/documentation/0.16.0/#Build-Mode)
  bestätigt die modusabhängigen Laufzeitprüfungen. „Vor 1.0“ passt zur zitierten Fassung;
  die Aussage sollte auf diesen Stand bezogen bleiben und ist kein Reife- oder Sicherheitsbeweis.
- [WG14 N1570](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf), 6.5.6 und J.2,
  bestätigt undefiniertes Verhalten bei unzulässigen Arrayzugriffen. Der öffentlich verfügbare
  Standardentwurf wurde für diese unveränderte Grundregel herangezogen, nicht als gekaufte ISO-Ausgabe ausgegeben.
- [GCC-Instrumentierung](https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html) und
  [Linux-Entwicklungswerkzeuge](https://www.kernel.org/doc/html/v5.10/dev-tools/index.html)
  zeigen verfügbare statische und dynamische Hilfen. Die Tabellenzeile „Schutzmechanismus“ ist deshalb
  erklärungsbedürftig, wenn „keiner“ als völliges Fehlen von Schutzwerkzeugen verstanden wird; L08.
- [Buns eigener Migrationsbericht](https://bun.com/blog/bun-in-rust) bestätigt den Referenzfall.
  Kapitel 4 leitet daraus keine allgemeine Wirksamkeit von KI oder vollständige Fehlerfreiheit von Rust ab.

### E05: Implementierung, Betriebssystemzugang und Prüfmittel

Gezielt gelesene Codebelege im Implementierungsrepository:
`src/wire/ip.rs:47-101` (IHL, Längen, Protocol 17, IP-Prüfsumme),
`src/options/parse.rs:13-80` (geliehene Slices, Iterator und Fehler),
`src/socket/send.rs:112-139` sowie `src/socket/recv.rs:169` (die zwei produktiven unsafe-Blöcke),
`docs/plan/steps/02-wire-model.md:92-117` (23 Tests, PR-Fund, ergänzte gemeinsame Invarianten),
`CLAUDE.md:168-172` (neue oder geänderte Paketverarbeitung, neue oder erweiterte Fuzz-Ziele).
Die Angaben zu selbst geschriebenen Parsern und begrenztem unsafe stimmen. `enum`/`Result` sind
geeignete Darstellungsmittel; sie allein beweisen keine Vollständigkeit der Protokollmodellierung.

[raw(7)](https://man7.org/linux/man-pages/man7/raw.7.html) bestätigt IP-Header beim Empfang,
`IP_HDRINCL` beim Senden und fehlende Fragmentierung bei gesetzter Option. Die MTU-Aussage ist richtig.
[packet(7)](https://man7.org/linux/man-pages/man7/packet.7.html),
[TUN/TAP unter Linux 5.10](https://www.kernel.org/doc/html/v5.10/networking/tuntap.html) und
[AF_XDP unter Linux 5.10](https://www.kernel.org/doc/html/v5.10/networking/af_xdp.html)
tragen den Vergleich der Zugänge. Packet Sockets haben auch eine SOCK_DGRAM-Form ohne übergebenen
Link-Layer-Header, bleiben aber auf Geräteebene; die Raw-Socket-Wahl bleibt nachvollziehbar.
Die gegengeprüfte allgemeine raw(7)-Dokumentation wurde nicht als erfolgreicher Abruf des
bibliografisch angegebenen, hier zugriffsbeschränkten Git-Links zur Version 6.18 ausgegeben.

Wireshark-Quelltext am Tag `v4.6.0`, `epan/dissectors/packet-udp.c:562-579,1333-1351`, begrenzt
Nutzdaten auf UDP Length und enthält dort keine RFC-9868-Auswertung. Er wurde über die GitHub-API gelesen.
`../udp-transport-options/scripts/wire-check.sh:144-149` und `wire-check.py:363-392,594-616`
belegen die Rollen: tcpdump zeichnet auf, der Python-Prüfer berechnet OCS/Optionsstruktur,
tshark vergleicht IP-/UDP-Felder und Prüfsummenstatus. Die aktuelle Beschreibung dieser Arbeitsteilung stimmt.

[LLVM libFuzzer](https://llvm.org/docs/LibFuzzer.html#introduction),
`fuzz/fuzz_targets/options_tlv.rs` und `tests/common_options/mod.rs:112-156` bestätigen
abdeckungsgeleitete Eingaben gegen den tatsächlichen Parser und explizite Invarianten.
`formal/lean-rfc9868/Rfc9868/Wire.lean:3-20` bezeichnet das Modell ausdrücklich als handgeschrieben
und nicht aus Rust extrahiert; die Theoreme darunter tragen die genannten Modellbehauptungen.
Der Stand vom 02.08.2026 dokumentiert den nachträglichen RFC-Korrekturschritt.
Kein neuer Gesamt-Testlauf und kein neuer vollständiger Lean-Bau wurde als Teil dieses Reviews behauptet.

## Vor der Freigabe zu bearbeiten

### F01: Messpunkte nicht auf genau zwei festlegen

**Art:** Korrektur. **Fundstelle:** S035 bis S041, Zeilen 145 bis 154; PDF 45 / Druck 39. **Kriterien:** 1, 7, 12, 17.

„Jede Messung hat dabei genau zwei eigene Messpunkte“ ist zu absolut. Tabelle 4.3 nennt selbst einen zusätzlichen macOS-Messpunkt. Für den 10./11.08. liegen Gast-, macOS- und Zielmitschnitte vor. Die folgenden Aussagen „Alles dazwischen“ und „die einzige belegbare Aussage“ müssen deshalb ebenfalls an die verfügbaren Messpunkte gebunden werden. Die grundsätzliche Begrenzung der Ursachenzuordnung bleibt richtig.

**Beleg:** E03; Kapitel 4, Tabelle 4.3; Kapitel 6, Abbildung zum Zugangspfad; versiegeltes Bidir-Archiv mit `raw/mac-en0.pcap`.

**Vorschlag:**

```latex
Die \textbf{Auswertung} verknüpft für jedes gerichtete Szenario die vorhandenen Sende- und
Empfangsbelege. Bei vollständigen Kampagnen sind dies Sendeversuch, Sendemanifest,
Sender-PCAP, Empfänger-PCAP und Empfängerausgabe. Sie helfen, Senderfehler, Abweichungen
auf dem Pfad und Verwerfungen durch die Empfängerimplementierung zu unterscheiden.
Zusätzliche Mitschnitte, etwa am macOS-Messpunkt aus \tabref{tab:scope-messung}, können
Teile des Pfads weiter eingrenzen. Ein Befund wird nur dem Abschnitt zwischen den
Messpunkten zugeschrieben, die ihn tatsächlich begrenzen. Dieser Abschnitt heißt
\textbf{Attributionsintervall}. Liegen nur Mitschnitte an den beiden Endpunkten vor,
umfasst es den gesamten Pfad dazwischen. Ein konkretes Gerät oder dessen interner
Mechanismus lässt sich daraus nicht bestimmen.
```

### F02: Eingeführte Prüfregel statt unbelegter universaler Durchführung

**Art:** Beleg- und Formulierungspräzisierung. **Fundstelle:** S078, Zeilen 290 bis 291; PDF 48 / Druck 42. **Kriterien:** 2, 4, 9, 19, 20.

„Danach erhielt jeder Schritt mit neuer Parsefläche …“ ist zugleich unverständlich und stärker als die dafür herangezogene Arbeitsvorgabe. Die dokumentierte Regel erfasst neue oder geänderte Paketverarbeitung und erlaubt neue oder erweiterte Fuzz-Ziele. Der Step-2-Bericht belegt die Einführung und die dortigen Ergänzungen, nicht allein schon die lückenlose Einhaltung bei jedem späteren Schritt. Das ist kein Nachweis, dass ein späterer Schritt die Regel verletzt hat.

**Beleg:** E05; Step-2-Bericht Zeilen 105 bis 117 und `CLAUDE.md:168-172`; Kapitel 3 unterscheidet ebenfalls Vorgabe und Ausführungsnachweis.

**Vorschlag:**

```latex
Danach wurde als Prüfvorgabe festgelegt, neue oder geänderte Paketverarbeitung durch
Property-Tests und neue oder erweiterte Fuzz-Ziele abzusichern (\secref{sec:pruefkette}).
```

### F03: Falsche Trennung von Optionsstruktur

**Art:** Silbentrennung. **Fundstelle:** S088, Quellzeile 315; PDF 49 / Druck 43. **Kriterien:** 23, 24.

Die aktuelle PDF trennt „Optionss- / truktur“. Dadurch wird das Wortglied „Struktur“ zerschnitten. Richtig ist „Options- / struktur“. Es genügt eine gezielte manuelle Trennstelle; korrekte andere Trennungen bleiben erhalten.

**Beleg:** Visuelle Prüfung der PDF und unabhängige Text-/Blockextraktion. Genau eine fehlerhafte Stelle unter 30 geprüften Blockzeilenenden.

**Vorschlag:**

```latex
Options\-struktur
```

### F04: NSA-Ausgabe passend zu den Literaturangaben bezeichnen

**Art:** Bibliografische Korrektur; Codeblock zeigt BibLaTeX-Felder. **Fundstelle:** S063/S067; Literaturdatensatz nsa-memory-safety, Zeilen 225 bis 235. **Kriterien:** 2, 21.

Der Link enthält zwar einen URL-Pfad vom November 2022, liefert derzeit aber „APR 2023 Ver. 1.1“ mit Kennung PP-23-0782. Der Datensatz nennt weiterhin 2022-11-10 und keine Version. Die Empfehlung für Rust bleibt inhaltlich belegt. Für die tatsächlich verlinkte Ausgabe sollten Datum, Version und Kennung angepasst werden; der Monat reicht, ein unbekannter Tag wird nicht erfunden.

**Beleg:** E04; offizielle NSA-PDF, Seitenfuß mit April 2023, Version 1.1. Die Behauptung im Fließtext benötigt keine neue Sicherheitsstatistik.

**Vorschlag:**

```latex
date        = {2023-04},
version     = {1.1},
number      = {U/OO/219936-22; PP-23-0782},
```

## Sprachliche Empfehlungen

Die Vorschläge sind zusammen mit den bezeichneten Nachbarsätzen zu lesen. Sie sind optional, soweit sie nicht mit F01 bis F04 zusammenfallen.

### L01: Normregel und Projektentscheidung einfacher auseinanderhalten

**Einheiten:** S009 S010. **Quellzeilen:** 46 bis 51. **Kriterien:** 3, 4, 6, 7.

Der sehr lange Satz springt von der Häufigkeitsverteilung zu „einer Vorgabe des Projektumfangs“. Der RFC legt den Projektumfang nicht selbst fest. Die folgenden Aussagen machen die Entscheidung zwar klar, der Übergang sollte sie aber direkt zuordnen.

**Vorschlag:**

```latex
Knapp zwei Drittel der markierten Absätze (65 von 103) liegen in den Abschnitten~10
und 11. Sie betreffen das Optionsformat, seine Verarbeitung und die einzelnen Optionen.
Bis einschließlich Abschnitt~7 gibt es keine markierten Absätze. Dort steht dennoch
eine für die Arbeit relevante Längenregel: Vor dem UDP-Header liegende Shim-Header
verringern den für UDP verfügbaren Raum. Diese Implementierung verarbeitet nur
\texttt{Protocol}~17 und verfolgt keine Shim-Ketten. Das ist eine Umfangsgrenze der
Arbeit, keine Einschränkung des RFC.
```

### L02: Anforderungskatalog und eigene Bewertung konkret erklären

**Einheiten:** S011 S012 S013 S014 S016 S017. **Quellzeilen:** 57 bis 70 und 99 bis 101. **Kriterien:** 4, 5, 6, 7.

Der erste Satz bündelt Zahlen, Nummernlücke, Matrix und Entstehung. „Arbeitsindex“, „Einzelzuordnung“ und „tragen die Umsetzung“ erschweren danach die Zuordnung. Die Trennung von Repository-Selbstauskunft und eigener Bewertung muss erhalten bleiben. Zwei Ersatzblöcke ersetzen die jeweiligen Absätze; Fußnote und Tabelle bleiben an ihrem Platz.

**Vorschlag:**

```latex
Das Implementierungs-Repository führt in \texttt{docs/requirements.md} 49 funktionale
Anforderungen und zwölf nichtfunktionale Anforderungen. Die Kennungen reichen von
\texttt{FR-01} bis \texttt{FR-50}, wobei \texttt{FR-47} entfallen ist, sowie von
\texttt{NFR-01} bis \texttt{NFR-12}. Die Datei entstand vor dem ersten Funktionsschritt
und wurde während der Umsetzung fortgeschrieben. Ihre Konformitätsmatrix dient als
Arbeitsindex: Sie ordnet RFC-Aussagen den Anforderungen und ihrem Umsetzungsstand zu.
Da sie neben Normsätzen auch Beschreibungen und Leitlinien enthält, wird jede Zeile
für diese Arbeit erneut am RFC eingeordnet. Die Ergebnisse stehen in der geprüften
Einzelzuordnung.
% Hier die vorhandene Fußnote beibehalten.
Zeilen mit mehreren Aussagen bleiben im Prüfraster zusammengefasst. Bewertet wird
jeweils der Anteil, der zu FF1 gehört.

% Nach der Tabelle anstelle von S016 und S017:
Die Tabelle gibt die Selbstauskunft des Arbeitsindex wieder. Die eigene Bewertung
kann davon abweichen, wenn der Vergleich mit dem RFC eine andere Einordnung ergibt.
```

### L03: UEXP als Experimentierkennung kenntlich machen

**Einheiten:** T027. **Quellzeilen:** 94. **Kriterien:** 4, 9, 15.

Kein gesicherter Sachfehler: Abschnitt 12.3 verwendet selbst „reserved for experiments“. Die gleiche Kurzbezeichnung verdeckt aber den Unterschied zu den noch reservierten Kompressions- und Verschlüsselungsmechanismen. Nur die übersetzte Inhaltszelle präzisieren; die als Originalauskunft gekennzeichneten Spalten nicht still verändern.

**Vorschlag:**

```latex
UCMP und UENC sind für Kompression und Verschlüsselung reserviert; UEXP ist für Experimente vorgesehen
```

### L04: Definition der vollständigen Erfüllbarkeit kürzen

**Einheiten:** S021. **Quellzeilen:** 106 bis 110. **Kriterien:** 4, 5.

Die Definition ist richtig, wiederholt aber zwei Umfangsverweise in einem langen Satz. Die Voraussetzungen sollen weiterhin ausdrücklich stehen.

**Vorschlag:**

```latex
\textbf{Vollständig} erfüllbar ist eine Anforderung, wenn sie im gewählten Rahmen ohne
Abstriche umsetzbar ist. Dieser Rahmen umfasst Linux, IPv4 und Raw Sockets im
Benutzerraum sowie die Beschränkung auf \texttt{Protocol}~17 ohne Shim-Ketten
(\secref{sec:zielsetzung}, \secref{sec:extraktionsmethode}).
```

### L05: Kapselung anschaulicher beschreiben

**Einheiten:** S031. **Quellzeilen:** 133 bis 135. **Kriterien:** 4, 6.

„Unbesehen“ ist bildhaft und erklärt nicht, warum diese Kontrollstufe anders ist. Keine Zustellgarantie für den äußeren Pfad formulieren.

**Vorschlag:**

```latex
\item \textbf{Tunnel:} WireGuard kapselt das innere Datagramm samt Surplus Area.
Der äußere Pfad transportiert die verschlüsselten Tunnelpakete zwischen den
Tunnelendpunkten.
```

### L06: Bibliotheksentscheidung ohne lange Einschübe begründen

**Einheiten:** S046 S047. **Quellzeilen:** 212 bis 216. **Kriterien:** 4, 5, 6.

Die Entscheidung ist sinnvoll. „Schmale“ Programme und die lange Verkettung aus RFC, Verweis und späteren Anwendungen bremsen den Satz. Der RFC lässt auch andere Umsetzungsformen zu; die Bibliothek passt zu seinen Prinzipien, wird nicht von ihnen vorgeschrieben.

**Vorschlag:**

```latex
Die Implementierung entsteht als einbindbare \textit{Bibliothek} mit Mess- und
Beispielprogrammen. Das passt zu den Entwurfsprinzipien von RFC~9868: Zustände und
Antworten werden grundsätzlich von der Anwendung oder einer für sie arbeitenden
Schicht verwaltet (\secref{subsec:surplus-prinzipien}) \cite[Sec.~3 und 6]{rfc9868}.
Die Bibliothek lässt sich dadurch sowohl in den Messprogrammen dieser Arbeit als
auch in späteren Anwendungen verwenden.
```

### L07: Sprachanforderungen in klaren Einzelsätzen erklären

**Einheiten:** S050 S051 S052 S053 S054 S055 S056. **Quellzeilen:** 222 bis 239. **Kriterien:** 4, 5, 6.

Die vier Bedingungen sind relevant. Besonders die dritte und vierte sind lang. „Ohne Laufzeitumgebung“ sollte eine obligatorische verwaltete Umgebung meinen, nicht das Fehlen jeglichen Laufzeitcodes. Der bewusste Ausschluss von Go/Java bleibt eine Projektentscheidung.

**Vorschlag:**

```latex
Erstens muss die Bibliothek auf das vollständige IP-Datagramm einschließlich der
Surplus Area zugreifen können (\secref{sec:netzpfad}). Den gewählten Zugang begründet
\secref{subsec:surplus-zugang}. Zweitens muss sie das Paketformat bytegenau umsetzen.
Der Serialisierer schreibt die Felder in Netzwerkbyteordnung; native Speicherabbilder
mit möglichem Padding werden nicht als Paketformat verwendet. Drittens verarbeitet
der Parser auch Pakete unbekannter oder bösartiger Absender. Er muss deshalb
fehlerhafte und gezielt konstruierte Eingaben sicher behandeln. Er liegt damit an
einer \textit{Vertrauensgrenze}, an der eingehende Daten als potentiell bösartig
behandelt werden. Viertens soll die
Bibliothek ohne obligatorische verwaltete Laufzeitumgebung und ohne Garbage Collector
auskommen. Das erleichtert ihre Einbindung und vermeidet GC-Pausen, garantiert aber
kein allgemein vorhersagbares Zeitverhalten. Die ersten beiden Punkte beschreiben
den benötigten Zugriff und das Paketformat; die letzten beiden sind Qualitätsziele
der Arbeit.

C, C++, Zig und Rust erlauben den benötigten Zugriff auf Speicher und
Betriebssystemschnittstellen und erfüllen die Vorgabe, ohne Garbage Collector
auszukommen. Go und Java werden wegen dieser ausdrücklich gewählten Vorgabe nicht
weiter betrachtet.
```

### L08: Sprachvergleich auf vergleichbare Eigenschaften begrenzen

**Einheiten:** T071 T072 T073 T074 T075 T081 T082 T083 T084 T085 S065. **Quellzeilen:** 262 bis 264 und 269 bis 272. **Kriterien:** 1, 4, 9, 21.

„Schutzmechanismus: keiner/optional“ nennt weder Ebene noch Mechanismus. Auch C kann mit Schutzwerkzeugen geprüft werden. Die Zeile mischt Sprachgarantien und Werkzeugoptionen; die vorherige Zeile und der Fließtext erklären den entscheidenden Unterschied bereits. Empfehlung: diese Zeile streichen. „Sprachfassung“ mischt ISO-Normierung und Versionsalter und kann ebenfalls entfallen, ohne die Sprachwahl zu schwächen. Der folgende Vergleich sollte die Garantie benennen, statt Rust mit „Safe-Rust-Garantien“ zu definieren.

**Vorschlag:**

```latex
% In Tabelle 4.4 die Zeilen Schutzmechanismus und Sprachfassung entfernen.
% Die übrigen Zeilen und den Titel erhalten.

Rust bietet im sicheren Sprachumfang Schutz vor unzulässigen Speicherzugriffen,
ohne dafür einen Garbage Collector zu benötigen. Ein Zugriff außerhalb eines
geprüften Bereichs löst einen \textit{panic} aus \cite{rust-lang,rust-book}.
In C kann ein solcher Zugriff undefiniertes Verhalten verursachen \cite{iso-c}.
```

### L09: Rust-Mittel und historischen Fehler direkt benennen

**Einheiten:** S071 S072 S073 S077. **Quellzeilen:** 280 bis 282 und 288 bis 290. **Kriterien:** 4, 5, 6, 9.

„Drei Rust-Mittel“, „geborgte Byte-Ausschnitte“ und „Um-eins- und Offsetfehler“ sind unnötig abstrakt. enum/Result belegen für sich keine vollständige Umsetzung aller RFC-Arten. Die Aussage ist im gewählten Umfang plausibel, sollte aber auf die Darstellung bezogen werden.

**Vorschlag:**

```latex
Der Parser verwendet geliehene Slices und muss die Optionsbytes deshalb nicht
kopieren. Die Lebensdauer dieser Slices ist an den Empfangspuffer gebunden
\cite{rust-book}. \texttt{enum} stellt die Optionsarten dar; \texttt{Result}
unterscheidet erfolgreiche Ergebnisse von Fehlern.

% S076 „Safe Rust verhindert keine Protokollfehler“ bleibt davor erhalten:
Ein um ein Byte verschobener Startoffset der Surplus Area überstand 23
selbstgeschriebene Tests und wurde erst bei der Pull-Request-Prüfung entdeckt.
Der Fehler betraf das Paketformat, nicht die Speichersicherheit.
```

### L10: Linux-Entscheidung und Prüfaufgaben einfacher formulieren

**Einheiten:** S080 S082 S083 S084. **Quellzeilen:** 297 bis 307. **Kriterien:** 4, 5, 6, 9.

Raw Sockets sind nachvollziehbar gewählt. „Unterbau“, „trägt diese Entscheidung“ und „Der Preis ist“ ersetzen keine konkrete Erklärung. Packet Sockets sollten als Geräteebene beschrieben werden, da sie nicht in jeder Betriebsart einen Link-Layer-Header an die Anwendung liefern.

**Vorschlag:**

```latex
Packet Sockets arbeiten auf Geräteebene, TUN/TAP benötigt ein virtuelles Netzgerät,
und AF\_XDP verlangt für den Empfang ein XDP-Programm sowie Speicherbereiche und
Warteschlangen \cite{man7packet,linux510tuntap,linux510afxdp}.

% S081 zum ausgeschlossenen Kernelmodul beibehalten.
Raw Sockets geben der Bibliothek ohne eigenes Netzgerät Zugriff auf das vollständige
IP-Datagramm. Sie sind damit für den gewählten Umfang der einfachste passende Zugang
\cite{man7raw}.

Die Bibliothek nutzt diesen Zugang unter Linux. Sein Verhalten ist dokumentiert und
im Kernelquelltext nachprüfbar; außerdem laufen die Sende- und Empfangsprogramme der
Kampagnen unter Linux (\secref{sec:ff2-pfadmodell}). Die Bibliothek prüft dabei
IPv4-Header, Längen, UDP-Prüfsumme und Optionen selbst.
```

### L11: Werkzeugrollen in getrennten Sätzen erklären

**Einheiten:** S087 S088 S089. **Quellzeilen:** 314 bis 318. **Kriterien:** 4, 5, 6, 9, 23.

Die Arbeitsteilung ist fachlich richtig. „Beweisdateien“ ist unnötig stark; „OCS und Optionsstruktur nachrechnen“ vermischt Prüfsummenberechnung und Formatprüfung. Den Versionsbezug und die begrenzte tshark-Rolle erhalten. Der Vorschlag berücksichtigt F03.

**Vorschlag:**

```latex
Die Kampagnenskripte zeichnen den Verkehr mit \texttt{tcpdump} in PCAP-Dateien auf.
Der eigene Prüfer aus \secref{sec:pruefkette} berechnet die OCS aus den aufgezeichneten
Bytes und prüft die Options\-struktur. Diese Auswertung übernimmt Wireshark in der
verwendeten Version~4.6 noch nicht (\secref{sec:netzpfad}). \texttt{tshark} prüft
unabhängig davon die IPv4- und UDP-Felder.
```

### L12: Fuzzing und Modellbeweis verständlicher einleiten

**Einheiten:** S090 S091 S092 S094. **Quellzeilen:** 323 bis 332. **Kriterien:** 4, 5, 6, 7.

Die Grenzen sind richtig beschrieben und müssen bleiben. „Die vierte Entscheidung“, „mutiert … abdeckungsgeleitet“ und „die Norm selbst Prüfgegenstand“ sind weniger klar als die konkreten Handlungen. Der Audit-Fund betrifft den erneuten Abgleich mit der Norm, nicht zwingend einen Normfehler.

**Vorschlag:**

```latex
Fuzzing und formale Gegenproben ergänzen die Testsuite. Sie sollen Fehler aufdecken,
die bei der KI-gestützten Entwicklung und ihren bisherigen Prüfungen unentdeckt
bleiben können (\secref{sec:gefahrenmodell}). Das über \texttt{cargo-fuzz} eingebundene
libFuzzer verändert Eingaben und bevorzugt solche, die zusätzliche Codepfade erreichen.
Es prüft den tatsächlichen Parser auf Abstürze und verletzte Invarianten \cite{libfuzzer}.
Mit Lean werden ausgewählte Eigenschaften handgeschriebener Modelle unter den
Voraussetzungen der jeweiligen Theoreme bewiesen (\secref{subsec:pruefmittel}).
% S093 mit den Grenzen von Fuzzing und Lean unverändert anschließen.

Auch erfolgreiche Prüfungen ersetzen den Abgleich mit dem RFC nicht. In der
Schlussphase deckte ein erneuter Vergleich trotz grüner Prüfkette weitere
Konformitätslücken auf. Sie wurden in einem eigenen Korrekturschritt bearbeitet
(\secref{sec:soll-ist}).
```

## PDF, Umbrüche und Silbentrennung

Alle acht Kapitelseiten wurden als PNG gerendert und visuell gelesen. Tabellen und Abbildung sind
vollständig sichtbar. Der Diagrammmaßstab passt zu den Zahlen; fehlende Balken bedeuten tatsächlich null.
Die Beschriftungen sind klein, aber lesbar. Die vier Tabellen enthalten keine abgeschnittenen Zellen.
Eine zunächst optisch vermutete Berührung zwischen „optional“ und „Übersetzung“ wurde durch die
PDF-Koordinaten verworfen: Die Wörter überlappen nicht. Kein Layoutfehler wird daraus konstruiert.

**P01, optional:** Auf PDF-Seite 43 endet der FF1-Einleitungssatz erst auf Seite 44; auf Seite 48
steht der Schluss von „Diese Folgen bestimmen den Entwurf in Kapitel 5“ erst auf Seite 49.
Das sind keine fachlichen oder formalen Abgabeblocker. Nach einer ohnehin vorgenommenen Kürzung prüfen,
ob beide Sätze zusammenbleiben können. Keine pauschalen Seitenumbrüche vor allen Unterabschnitten einfügen.
Die angrenzenden PDF-Seiten 41 und 50 wurden für den Kapitelübergang zusätzlich angesehen.

Für die Silbentrennung wurden 26 Zeilenenden des layoutgetreuen Textauszugs und vier weitere
Trennstellen innerhalb von Tabellenspalten geprüft, zusammen 30. Darin sind reguläre Bindestriche
enthalten. „Fund-/stelle“, „Speichersicher-/heit“, „Schutzmechanis-/mus“ und
„Speicherverwal-/tung“ sind korrekt. Bei „Provider-/Kanten“, „IPv4-/Header“, „PCAP-/Beweisdateien“
und „Parser-/codes“ wird ein vorhandener Bindestrich beibehalten. Nur „Optionss-/truktur“ ist falsch.
Beide Fußnoten wurden vollständig gelesen; dort kein zusätzlicher Trennfehler.

## Vollständiges Verzeichnis der Einzelprüfung

Die Zitate stammen aus dem eigenen Kapitelquelltext; LaTeX-Makros bleiben zur eindeutigen Zuordnung sichtbar.
„Belassen“ bedeutet: innerhalb des angegebenen Belegs und Zusammenhangs kein Änderungsbedarf.
Die separaten Fußnotentexte sind aus den umgebenden Satz-Zitaten herausgenommen.

### H001 · Überschrift · Zeilen 5 bis 5

**Urteil:** Belassen. **Beleg/Zusammenhang:** E01 / Kapitel 3.

> Analyse und Anforderungsmodell

### S001 · Satz · Zeilen 8 bis 8

**Urteil:** Belassen. **Beleg/Zusammenhang:** E01 / Kapitel 3.

> \chapref{chap:methodik} legt die Quellenregeln fest.

### S002 · Satz · Zeilen 8 bis 11

**Urteil:** Belassen. **Beleg/Zusammenhang:** E01 / Kapitel 3.

> Dieses Kapitel wendet sie auf RFC~9868 an (\secref{sec:extraktionsmethode}), überführt den Anforderungskatalog
> in den FF1-Maßstab (\secref{sec:anforderungsmatrix}) und bildet das FF2-Pfad- und Auswertungsmodell
> (\secref{sec:ff2-pfadmodell}).

### S003 · Satz · Zeilen 11 bis 12

**Urteil:** Belassen. **Beleg/Zusammenhang:** E01 / Kapitel 3.

> Die Technologieauswahl (\secref{sec:technologieauswahl}) schließt die Analyse ab.

### H002 · Überschrift · Zeilen 14 bis 14

**Urteil:** Belassen. **Beleg/Zusammenhang:** E01 / Kapitel 3.

> Anwendung der Extraktionsmethode

### S004 · Satz · Zeilen 17 bis 17

**Urteil:** Belassen. **Beleg/Zusammenhang:** E01 / Kapitel 3.

> Die Auswertung wendet die in \secref{sec:rfc-auswertung} festgelegte Methode auf den Primärtext an.

### S005 · Satz · Zeilen 17 bis 19

**Urteil:** Belassen. **Beleg/Zusammenhang:** E01 / Kapitel 3.

> Die 103 mit \texttt{>{}>} markierten Absätze dienen als Kontrollzahl; unmarkierte normative Festlegungen bleiben
> Teil des Maßstabs \cite{rfc2119,rfc8174}.

### S006 · Satz · Zeilen 19 bis 20

**Urteil:** Belassen. **Beleg/Zusammenhang:** E01 / Kapitel 3.

> Extrahiert wird satzgenau und nicht absatzweise, denn ein markierter Absatz kann mehrere Pflichten mit
> verschiedenen Adressaten bündeln.

### S007 · Satz · Zeilen 20 bis 22

**Urteil:** Belassen. **Beleg/Zusammenhang:** E01 / Kapitel 3.

> Jede extrahierte Aussage wird zu einem Prüfpunkt für den Anforderungsbestand des Implementierungs-Repositorys
> (\secref{sec:anforderungsmatrix}).

### S008 · Texteinheit · Zeilen 24 bis 24

**Urteil:** Belassen. **Beleg/Zusammenhang:** E01 / Kapitel 3.

> \figref{fig:normverteilung} zeigt, wie sich die 103 markierten Absätze auf die Abschnitte verteilen:

### B001 · Abbildungsdaten · Zeilen 26 bis 44

**Urteil:** Belassen. **Beleg/Zusammenhang:** E01 / Kapitel 3.

> Abschnitte 1..27: 0,0,0,0,0,0,0,2,5,21,44,3,9,6,5,1,0,0,2,0,0,0,0,0,4,1,0; Balken und Zahlenbeschriftungen.

### B002 · Abbildungslabel · Zeilen 39 bis 39

**Urteil:** Belassen. **Beleg/Zusammenhang:** E01 / Kapitel 3.

> Abschnitte 1 bis 7:\\ keine

### B003 · Abbildungslabel · Zeilen 40 bis 40

**Urteil:** Belassen. **Beleg/Zusammenhang:** E01 / Kapitel 3.

> Nummer des RFC-Abschnitts

### B004 · Beschriftung · Zeilen 42 bis 42

**Urteil:** Belassen. **Beleg/Zusammenhang:** E01 / Kapitel 3.

> Verteilung der markierten normativen Absätze über die Abschnitte

### S009 · Satz · Zeilen 46 bis 49

**Urteil:** Vorschlag L01. **Beleg/Zusammenhang:** E01 / Kapitel 3.

> Knapp zwei Drittel der markierten Absätze (65 von 103) liegen in den Abschnitten~10 und 11, also beim
> Optionsformat mit seinen Verarbeitungsregeln und bei den einzelnen Optionen; der Vorspann bis einschließlich
> Abschnitt~7 enthält keinen einzigen markierten Absatz, wohl aber eine Vorgabe des Projektumfangs: Abschnitt~7
> verringert die Obergrenze der \texttt{UDP Length} um vorangehende Shim-Header.

### S010 · Satz · Zeilen 49 bis 51

**Urteil:** Vorschlag L01. **Beleg/Zusammenhang:** E01 / Kapitel 3.

> Die Implementierung verfolgt Shim-Ketten nicht und verarbeitet nur \texttt{Protocol}~17; das ist eine
> ausdrückliche Umfangsvorgabe dieser Arbeit, kein Verbot des RFC.

### H003 · Überschrift · Zeilen 53 bis 53

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> Anforderungskatalog und FF1-Maßstab

### S011 · Satz · Zeilen 57 bis 61

**Urteil:** Vorschlag L02. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> Das Implementierungs-Repository (\chapref{chap:entwurf}) führt in \texttt{docs/requirements.md} 49 funktionale
> und zwölf nichtfunktionale Anforderungen (\texttt{FR-01} bis \texttt{FR-50} ohne die entfallene Nummer
> \texttt{FR-47}, \texttt{NFR-01} bis \texttt{NFR-12}) sowie eine Konformitätsmatrix; die Datei entstand vor dem
> ersten Funktionsschritt und wurde parallel zur Umsetzung fortgeschrieben.

### S012 · Satz · Zeilen 61 bis 63

**Urteil:** Vorschlag L02. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> Die Matrix ist der Sache nach ein Arbeitsindex: Sie mischt markierte Normsätze, unmarkierte normative
> Festlegungen, Beschreibungen und Leitlinien.

### S013 · Satz · Zeilen 63 bis 65

**Urteil:** Vorschlag L02. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> Die Prüfung aus \secref{sec:extraktionsmethode} stuft deshalb jede Zeile am Primärtext ein und überführt sie in
> die geprüfte Einzelzuordnung.

### F001 · Fußnote · Zeilen 65 bis 68

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02.

> Vollständige Konformitätsmatrix als \href{https://github.com/ab7z/mcs-thesis-docs/blob/%
> main/thesis/daten/konformitaet-kategorien.csv}{Datei im öffentlichen
> GitHub-Repository} (Stand: 30.08.2026).

### S014 · Satz · Zeilen 69 bis 70

**Urteil:** Vorschlag L02. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> Zeilen, die mehrere Normsätze oder Adressaten bündeln, etwa die Zeilen zu den Abschnitten 11.2, 16 und 19 sowie
> 25.2 bis 25.4, bleiben eine Zeile und werden nur mit ihrem FF1-Anteil bewertet.

### S015 · Texteinheit · Zeilen 70 bis 72

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> \tabref{tab:anforderungsmatrix} zeigt eine eigene übersetzte Auswahl; Normstufe und Abdeckung stehen im Wortlaut
> der Datei:

### B005 · Beschriftung · Zeilen 76 bis 76

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> Auszug aus dem RFC-Arbeitsindex des Implementierungs-Repositorys

### T001 · Tabellenzelle · Zeilen 82 bis 83

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> \textbf{Fund\-stelle}

### T002 · Tabellenzelle · Zeilen 83 bis 83

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> \textbf{Normative Aussage}

### T003 · Tabellenzelle · Zeilen 83 bis 83

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> \textbf{Norm\-stufe}

### T004 · Tabellenzelle · Zeilen 83 bis 83

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> \textbf{Abdeckung}

### T005 · Tabellenzelle · Zeilen 83 bis 84

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> \textbf{FR/NFR}

### T006 · Tabellenzelle · Zeilen 84 bis 86

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> Sec.~8

### T007 · Tabellenzelle · Zeilen 86 bis 87

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> Ausrichtungsbyte vor dem OCS ist null; sonst alle Optionen ignorieren und die Surplus Area still verwerfen

### T008 · Tabellenzelle · Zeilen 87 bis 87

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> \texttt{MUST}

### T009 · Tabellenzelle · Zeilen 87 bis 87

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> \texttt{yes}

### T010 · Tabellenzelle · Zeilen 87 bis 87

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> FR-05

### T011 · Tabellenzelle · Zeilen 87 bis 88

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> Sec.~9

### T012 · Tabellenzelle · Zeilen 88 bis 88

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> OCS ungleich null, wenn die UDP-Prüfsumme ungleich null ist

### T013 · Tabellenzelle · Zeilen 88 bis 88

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> \texttt{MUST}

### T014 · Tabellenzelle · Zeilen 88 bis 88

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> \texttt{yes}

### T015 · Tabellenzelle · Zeilen 88 bis 89

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> FR-21

### T016 · Tabellenzelle · Zeilen 89 bis 90

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> Sec.~10

### T017 · Tabellenzelle · Zeilen 90 bis 90

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> Optionen über 254~Byte nutzen das erweiterte Format; das kleinste Format ist empfohlen

### T018 · Tabellenzelle · Zeilen 90 bis 91

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> \texttt{MUST/} \texttt{SHOULD}

### T019 · Tabellenzelle · Zeilen 91 bis 91

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> \texttt{yes (send); local strict receive}

### T020 · Tabellenzelle · Zeilen 91 bis 91

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> FR-09, FR-14

### T021 · Tabellenzelle · Zeilen 91 bis 92

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> Sec.~11.2

### T022 · Tabellenzelle · Zeilen 92 bis 92

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> Höchstens sieben NOPs in Folge; übermäßige Folgen protokollieren und Ressourcen begrenzen

### T023 · Tabellenzelle · Zeilen 92 bis 93

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> \texttt{SHOULD}

### T024 · Tabellenzelle · Zeilen 93 bis 93

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> \texttt{partial}

### T025 · Tabellenzelle · Zeilen 93 bis 93

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> FR-16, NFR-05

### T026 · Tabellenzelle · Zeilen 93 bis 94

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> Sec.~12

### T027 · Tabellenzelle · Zeilen 94 bis 94

**Urteil:** Vorschlag L03. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> UCMP, UENC und UEXP sind reservierte UNSAFE-Optionen

### T028 · Tabellenzelle · Zeilen 94 bis 94

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> \texttt{reserved}

### T029 · Tabellenzelle · Zeilen 94 bis 94

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> \texttt{out}

### T030 · Tabellenzelle · Zeilen 94 bis 94

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> FR-39

### S016 · Satz · Zeilen 99 bis 100

**Urteil:** Vorschlag L02. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> Aus \tabref{tab:anforderungsmatrix} geht die Arbeitsteilung der Datei hervor: Die Konformitätsmatrix hält die
> Normseite fest, die FR- und NFR-Zeilen tragen die Umsetzung.

### S017 · Satz · Zeilen 100 bis 101

**Urteil:** Vorschlag L02. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> Die Auswahl zeigt zugleich die Grenzen des Arbeitsindex.

### S018 · Satz · Zeilen 101 bis 102

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> Die Zeile zu Abschnitt~11.2 bündelt die Ressourcengrenze aus Abschnitt~25.2 mit den NOP-Pflichten
> \cite[Sec.~25.2]{rfc9868}.

### S019 · Satz · Zeilen 104 bis 105

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> Bewertet wird gegen den Maßstab von FF1: welche Anforderungen sich unter Linux und IPv4 im Benutzerraum
> \zitat{vollständig, teilweise oder nicht} erfüllen lassen (\secref{sec:zielsetzung}).

### S020 · Satz · Zeilen 105 bis 106

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> Die Bewertung nutzt drei Kategorien und eine Sonderklasse, die \tabref{tab:operationalisierung} bereits
> verankert.

### S021 · Satz · Zeilen 106 bis 110

**Urteil:** Vorschlag L04. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> \textbf{Vollständig} erfüllbar ist eine Anforderung, wenn sie unter den eigenen Vorgaben der Arbeit ohne
> Abstriche umsetzbar ist; diese Vorgaben sind die Plattform aus \secref{sec:zielsetzung} (Linux, IPv4,
> Benutzerraum mit Raw Sockets) und die Protokollgrenze aus \secref{sec:extraktionsmethode} (nur
> \texttt{Protocol}~17, keine Shim-Ketten).

### S022 · Satz · Zeilen 110 bis 112

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> \textbf{Teilweise} erfüllbar ist sie, wenn nur ein Teil erreichbar bleibt und die Ursache der Einschränkung
> belegt ist.

### S023 · Satz · Zeilen 112 bis 113

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> \textbf{Nicht erfüllbar} ist sie, wenn dokumentiertes Betriebssystem- oder Schnittstellenverhalten die Umsetzung
> im Benutzerraum grundsätzlich ausschließt.

### S024 · Satz · Zeilen 113 bis 115

**Urteil:** Belassen. **Beleg/Zusammenhang:** E02 / Kapitel 1 und 3.

> \textbf{Nicht anwendbar} bleibt als Sonderklasse sichtbar, wird aber nicht bewertet; hierhin gehören Aussagen
> außerhalb des Umfangs und nicht gewählte \texttt{MAY}-Funktionen.

### H004 · Überschrift · Zeilen 117 bis 117

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> FF2-Pfad- und Auswertungsmodell

### S025 · Satz · Zeilen 120 bis 121

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> FF2 fragt, in welchem Umfang die Surplus Area auf realen Pfaden bis zur Gegenstelle erhalten bleibt
> (\secref{sec:zielsetzung}).

### S026 · Satz · Zeilen 121 bis 123

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> Ausgewertet wird je Pfad, Richtung und Messzeitpunkt ein kontrolliertes Szenario aus Kontroll- und
> Optionsverkehr, das mehrere Wiederholungen oder bei FRAG mehrere Wire-Datagramme umfassen kann
> (\tabref{tab:operationalisierung}).

### S027 · Satz · Zeilen 123 bis 126

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> Ein gültiger Lauf endet mit \textbf{erhalten}, \textbf{verändert}, \textbf{entfernt} oder \textbf{verworfen};
> fehlerhafte Messungen erhalten den Status \textbf{Lauf ungültig} und gehen nicht in die Bewertung ein
> (\secref{sec:testkonzept}).

### S028 · Texteinheit · Zeilen 126 bis 127

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> Die fünf \textbf{Pfadstufen} bilden getrennte Messklassen mit unterschiedlicher externer Netzbeteiligung:

### S029 · Satz · Zeilen 130 bis 131

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> \textbf{Loopback:} Sende- und Empfangspfad auf demselben Host; prüft Bibliothek und Messwerkzeuge ohne fremde
> Akteure.

### S030 · Satz · Zeilen 131 bis 133

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> \textbf{Lokale virtuelle Testumgebung:} Eine Ubuntu-VM unter VMware Fusion, mit Linux-Netzwerk-Namensräumen und
> \texttt{veth}.

### S031 · Satz · Zeilen 133 bis 135

**Urteil:** Vorschlag L05. **Beleg/Zusammenhang:** E03.

> \textbf{Tunnel:} Kapselung über einen realen Pfad (WireGuard); der äußere Pfad transportiert das innere
> Datagramm samt Surplus Area unbesehen zwischen den Tunnelendpunkten.

### S032 · Satz · Zeilen 135 bis 137

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> \textbf{Öffentliche Pfade in Europa:} Cloud-Endpunkte in Deutschland und Finnland sowie ein
> Mobilfunk-Zugangsnetz; reale Zugangs-, Transit- und Provider-Kanten.

### S033 · Satz · Zeilen 137 bis 139

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> \textbf{Interkontinentale Pfade:} Endpunkte in Nordamerika und Asien-Pazifik; lange Transitketten und die
> Netzstrukturen großer Cloud-Anbieter.

### S034 · Satz · Zeilen 142 bis 143

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> Vorversuche ohne beidseitige Mitschnitte und Ablaufprotokolle bleiben Piloten und werden nicht verallgemeinert
> (\secref{sec:testkonzept}).

### S035 · Satz · Zeilen 145 bis 146

**Urteil:** Vorschlag F01. **Beleg/Zusammenhang:** E03.

> Die \textbf{Auswertung} verknüpft für jedes gerichtete Szenario Sendeversuch, Sendemanifest, Sender-PCAP,
> Empfänger-PCAP und Empfängerausgabe.

### S036 · Satz · Zeilen 146 bis 147

**Urteil:** Vorschlag F01. **Beleg/Zusammenhang:** E03.

> Dadurch lassen sich Senderfehler, Veränderungen oder Verluste auf dem Pfad sowie Verwerfungen durch die
> Empfängerimplementierung unterscheiden.

### S037 · Satz · Zeilen 147 bis 148

**Urteil:** Vorschlag F01. **Beleg/Zusammenhang:** E03.

> Jede Messung hat dabei genau zwei eigene Messpunkte: den Mitschnitt beim Sender und den Mitschnitt beim
> Empfänger.

### S038 · Satz · Zeilen 148 bis 149

**Urteil:** Vorschlag F01. **Beleg/Zusammenhang:** E03.

> Alles dazwischen, auf realen Pfaden etwa Zugangs-, Transit- und Provider-Kanten, hat keinen eigenen Messpunkt.

### S039 · Satz · Zeilen 149 bis 151

**Urteil:** Vorschlag F01. **Beleg/Zusammenhang:** E03.

> Verlässt ein Datagramm den Sender nachweislich korrekt und kommt beim Empfänger verändert oder gar nicht an, ist
> die einzige belegbare Aussage: Die Abweichung ist irgendwo zwischen diesen zwei Punkten entstanden.

### S040 · Satz · Zeilen 151 bis 153

**Urteil:** Vorschlag F01. **Beleg/Zusammenhang:** E03.

> Dieses Pfadstück zwischen den vorhandenen Messpunkten heißt \textbf{Attributionsintervall}, das Intervall, dem
> ein Befund zugeschrieben (attribuiert) werden darf.

### S041 · Satz · Zeilen 153 bis 154

**Urteil:** Vorschlag F01. **Beleg/Zusammenhang:** E03.

> Einem einzelnen Gerät wird ein Befund nie zugeschrieben; dafür fehlen Messpunkte unmittelbar davor und dahinter.

### S042 · Satz · Zeilen 156 bis 157

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> Die Vorversuche dienten darüber hinaus dazu, mögliche Ursachen für beobachtete Veränderungen und Verluste zu
> formulieren und gezielte Folgemessungen zu planen.

### S043 · Satz · Zeilen 157 bis 159

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> Da diese Hypothesen aus Messbeobachtungen entstanden, gehören die daraus abgeleiteten Mechanismenklassen zu den
> Ergebnissen dieser Arbeit; sie werden mit ihren Belegen in \chapref{chap:evaluation} dargestellt.

### S044 · Texteinheit · Zeilen 161 bis 162

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> Zwei Tabellen grenzen abschließend den Geltungsbereich ab: \tabref{tab:scope-implementierung} den
> Implementierungsumfang, \tabref{tab:scope-messung} die bewusst breitere Messinfrastruktur:

### B006 · Beschriftung · Zeilen 166 bis 166

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> Implementierungsumfang

### T031 · Tabellenzelle · Zeilen 170 bis 171

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> \textbf{Merkmal}

### T032 · Tabellenzelle · Zeilen 171 bis 171

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> \textbf{Festlegung}

### T033 · Tabellenzelle · Zeilen 171 bis 171

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> \textbf{außerhalb des Umfangs}

### T034 · Tabellenzelle · Zeilen 171 bis 173

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> Betriebssystem

### T035 · Tabellenzelle · Zeilen 173 bis 173

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> Linux

### T036 · Tabellenzelle · Zeilen 173 bis 173

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> andere Betriebssysteme

### T037 · Tabellenzelle · Zeilen 173 bis 174

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> Vermittlungsschicht

### T038 · Tabellenzelle · Zeilen 174 bis 174

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> IPv4

### T039 · Tabellenzelle · Zeilen 174 bis 174

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> IPv6

### T040 · Tabellenzelle · Zeilen 174 bis 175

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> Ausführungsort

### T041 · Tabellenzelle · Zeilen 175 bis 175

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> Benutzerraum mit Raw Sockets

### T042 · Tabellenzelle · Zeilen 175 bis 175

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> Kernelimplementierungen

### T043 · Tabellenzelle · Zeilen 175 bis 176

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> Artefakt

### T044 · Tabellenzelle · Zeilen 176 bis 176

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> Bibliothek mit Mess- und Beispielprogrammen

### T045 · Tabellenzelle · Zeilen 176 bis 177

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> eigenständiger Dienst; Protokollautomaten für REQ/RES und TIME

### T046 · Tabellenzelle · Zeilen 177 bis 178

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> Optionsumfang

### T047 · Tabellenzelle · Zeilen 178 bis 179

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> acht \textit{must-support}-Optionen sowie generische Empfangsregeln für unbekannte SAFE- und UNSAFE-Arten

### T048 · Tabellenzelle · Zeilen 179 bis 180

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> typisierte Erzeugung und Verarbeitung weiterer Arten wie TIME, AUTH, EXP, UCMP, UENC und UEXP

### B007 · Beschriftung · Zeilen 187 bis 187

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> Messinfrastruktur

### T049 · Tabellenzelle · Zeilen 191 bis 192

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> \textbf{Baustein}

### T050 · Tabellenzelle · Zeilen 192 bis 192

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> \textbf{Rolle in der Messung}

### T051 · Tabellenzelle · Zeilen 192 bis 195

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> Linux-Endpunkte: lokale virtuelle Maschine und Cloud-Instanzen in Europa, Nordamerika und Asien-Pazifik

### T052 · Tabellenzelle · Zeilen 195 bis 195

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> Sende- und Empfangsendpunkte der Kampagnen; Mitschnitt mit \texttt{tcpdump}

### T053 · Tabellenzelle · Zeilen 195 bis 196

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> Mobilfunk-Zugang über einen Hotspot

### T054 · Tabellenzelle · Zeilen 196 bis 197

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> reale Zugangsnetzkette mit Hotspot-NAT; der Anteil eines möglichen CGNAT bleibt ohne zusätzlichen Messpunkt
> offen

### T055 · Tabellenzelle · Zeilen 197 bis 198

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> macOS-Messpunkt \texttt{en0} (\texttt{access\_bpf})

### T056 · Tabellenzelle · Zeilen 198 bis 199

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> zusätzlicher Beobachtungspunkt am Zugangsnetz; keine Implementierungsplattform

### T057 · Tabellenzelle · Zeilen 199 bis 200

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> native IPv6-Kontrollen

### T058 · Tabellenzelle · Zeilen 200 bis 200

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> Einordnung einzelner Pfadbefunde; außerhalb der Bibliothek

### T059 · Tabellenzelle · Zeilen 200 bis 201

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> WireGuard-Tunnel

### T060 · Tabellenzelle · Zeilen 201 bis 201

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> Kontrollpfad mit Kapselung (Pfadstufe~3)

### S045 · Satz · Zeilen 206 bis 207

**Urteil:** Belassen. **Beleg/Zusammenhang:** E03.

> macOS-Messpunkt, IPv6-Kontrollen und WireGuard-Tunnel erweitern nur die Messinfrastruktur; FF2 bewertet
> weiterhin Datagramme über IPv4 (\tabref{tab:scope-messung}).

### H005 · Überschrift · Zeilen 209 bis 209

**Urteil:** Belassen. **Beleg/Zusammenhang:** E01 / E05.

> Technologieauswahl

### S046 · Satz · Zeilen 212 bis 213

**Urteil:** Vorschlag L06. **Beleg/Zusammenhang:** E01 / E05.

> Die Implementierung entsteht als einbindbare \textit{Bibliothek} mit schmalen Mess- und Beispielprogrammen,
> nicht als eigenständiger Dienst und nicht als Kernelmodul.

### S047 · Satz · Zeilen 213 bis 216

**Urteil:** Vorschlag L06. **Beleg/Zusammenhang:** E01 / E05.

> Diese Form folgt den Entwurfsprinzipien von RFC~9868, die nötigen Zustand und jede Antwort in der Anwendung oder
> einer in ihrem Auftrag arbeitenden Bibliothek verorten (\secref{subsec:surplus-prinzipien}) \cite[Sec.~3 und
> 6]{rfc9868}, und eignet sich für die Messprogramme dieser Arbeit ebenso wie für spätere Anwendungen.

### S048 · Satz · Zeilen 216 bis 217

**Urteil:** Belassen. **Beleg/Zusammenhang:** E01 / E05.

> Zu begründen sind die Sprache, der Zugang zur Surplus Area, die Messwerkzeuge sowie Fuzzing und formale
> Gegenproben.

### H006 · Überschrift · Zeilen 219 bis 219

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> Programmiersprache

### S049 · Satz · Zeilen 222 bis 222

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> Die Wahl der Programmiersprache folgt aus vier Bedingungen.

### S050 · Satz · Zeilen 222 bis 224

**Urteil:** Vorschlag L07. **Beleg/Zusammenhang:** E04.

> Erstens braucht die Bibliothek im Benutzerraum Zugriff auf das vollständige IP-Datagramm über die durch
> \texttt{UDP Length} begrenzten Nutzdaten hinaus (\secref{sec:netzpfad}); den gewählten Zugang begründet
> \secref{subsec:surplus-zugang}.

### S051 · Satz · Zeilen 224 bis 226

**Urteil:** Vorschlag L07. **Beleg/Zusammenhang:** E04.

> Zweitens verlangt das Wire-Format bytegenaue Kontrolle: Der Serialisierer schreibt jedes Feld ausdrücklich in
> Netzwerkbyteordnung; native Strukturabbilder mit möglichem Padding dienen nicht als Wire-Format.

### S052 · Satz · Zeilen 226 bis 229

**Urteil:** Vorschlag L07. **Beleg/Zusammenhang:** E04.

> Drittens verarbeitet der Parser Pakete, die jeder beliebige Absender im Netz erzeugt haben kann; er liegt damit
> an der \textit{Vertrauensgrenze} des Systems, an der eingehende Daten als potentiell bösartig gelten müssen, und
> muss auch fehlerhafte oder gezielt konstruierte Pakete robust verarbeiten.

### S053 · Satz · Zeilen 229 bis 232

**Urteil:** Vorschlag L07. **Beleg/Zusammenhang:** E04.

> Viertens soll die Bibliothek ohne eigene Laufzeitumgebung und ohne automatische Speicherbereinigung (Garbage
> Collector) auskommen; das erleichtert das Einbetten und vermeidet GC-Pausen, macht das Zeitverhalten aber nicht
> allgemein vorhersagbar.

### S054 · Satz · Zeilen 232 bis 233

**Urteil:** Vorschlag L07. **Beleg/Zusammenhang:** E04.

> Die ersten beiden Bedingungen folgen aus der Umsetzung im Benutzerraum, die letzten beiden sind Qualitätsziele
> dieser Arbeit.

### S055 · Satz · Zeilen 235 bis 237

**Urteil:** Vorschlag L07. **Beleg/Zusammenhang:** E04.

> Diese Bedingungen erfüllen \textit{Systemprogrammiersprachen} wie C, C++, Zig und Rust: Sprachen mit
> hardwarenahem Zugriff auf Speicher und Betriebssystemschnittstellen, die ohne obligatorische Laufzeitumgebung zu
> nativem Maschinencode übersetzt werden.

### S056 · Satz · Zeilen 237 bis 239

**Urteil:** Vorschlag L07. **Beleg/Zusammenhang:** E04.

> Sprachen mit Garbage Collector wie Go oder Java scheiden an der vierten Bedingung aus; das ist kein
> Eignungsurteil, sondern die Folge des bewusst gesetzten Qualitätsziels.

### S057 · Satz · Zeilen 241 bis 241

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> Alle vier Kandidaten bieten die nötige Kontrolle.

### S058 · Satz · Zeilen 241 bis 242

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> Den Ausschlag gibt die Speichersicherheit an der Vertrauensgrenze.

### S059 · Satz · Zeilen 242 bis 243

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> Sie schließt Zugriffe außerhalb eines Speicherbereichs (\textit{Buffer Overflow}), auf freigegebenen Speicher
> (\textit{Use-after-free}) und doppelte Freigaben (\textit{Double Free}) aus.

### S060 · Satz · Zeilen 243 bis 244

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> Ein \textit{Memory Leak} gewährt dagegen keinen unzulässigen Zugriff und bleibt auch in Rust möglich.

### S061 · Satz · Zeilen 244 bis 246

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> Miller berichtete 2019 auf Grundlage der seit 2004 gepflegten MSRC-Daten, dass rund 70~Prozent der jährlich von
> Microsoft mit CVE versehenen Schwachstellen Speicherfehler sind.

### S062 · Satz · Zeilen 246 bis 247

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> Chromium nennt rund 70~Prozent unter 912 seit 2015 erfassten Stable-Channel-Fehlern hoher oder kritischer
> Schwere.

### S063 · Satz · Zeilen 247 bis 248

**Urteil:** Vorschlag F04. **Beleg/Zusammenhang:** E04.

> Die NSA empfiehlt speichersichere Sprachen, darunter Rust
> \cite{microsoft-memory,chromium-memory,nsa-memory-safety}.

### S064 · Texteinheit · Zeilen 250 bis 250

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> Die entscheidungsrelevanten Eigenschaften fasst \tabref{tab:sprachvergleich} zusammen:

### B008 · Beschriftung · Zeilen 254 bis 254

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> Vergleich der Sprachkandidaten

### T061 · Tabellenzelle · Zeilen 258 bis 259

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> \textbf{Kriterium}

### T062 · Tabellenzelle · Zeilen 259 bis 259

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> \textbf{C}

### T063 · Tabellenzelle · Zeilen 259 bis 259

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> \textbf{C++}

### T064 · Tabellenzelle · Zeilen 259 bis 259

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> \textbf{Zig}

### T065 · Tabellenzelle · Zeilen 259 bis 259

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> \textbf{Rust}

### T066 · Tabellenzelle · Zeilen 259 bis 261

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> Speichersicherheit

### T067 · Tabellenzelle · Zeilen 261 bis 261

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> nein

### T068 · Tabellenzelle · Zeilen 261 bis 261

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> nein

### T069 · Tabellenzelle · Zeilen 261 bis 261

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> teilweise

### T070 · Tabellenzelle · Zeilen 261 bis 261

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> ja in Safe Rust; \texttt{unsafe} vertragsabhängig

### T071 · Tabellenzelle · Zeilen 261 bis 262

**Urteil:** Vorschlag L08. **Beleg/Zusammenhang:** E04.

> Schutzmechanismus

### T072 · Tabellenzelle · Zeilen 262 bis 262

**Urteil:** Vorschlag L08. **Beleg/Zusammenhang:** E04.

> keiner

### T073 · Tabellenzelle · Zeilen 262 bis 262

**Urteil:** Vorschlag L08. **Beleg/Zusammenhang:** E04.

> optional

### T074 · Tabellenzelle · Zeilen 262 bis 262

**Urteil:** Vorschlag L08. **Beleg/Zusammenhang:** E04.

> Übersetzung, modusabhängige Laufzeit

### T075 · Tabellenzelle · Zeilen 262 bis 262

**Urteil:** Vorschlag L08. **Beleg/Zusammenhang:** E04.

> Compiler, Laufzeit

### T076 · Tabellenzelle · Zeilen 262 bis 263

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> Speicherverwaltung

### T077 · Tabellenzelle · Zeilen 263 bis 263

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> manuell

### T078 · Tabellenzelle · Zeilen 263 bis 263

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> manuell, RAII

### T079 · Tabellenzelle · Zeilen 263 bis 263

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> Allokatoren

### T080 · Tabellenzelle · Zeilen 263 bis 263

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> Ownership

### T081 · Tabellenzelle · Zeilen 263 bis 264

**Urteil:** Vorschlag L08. **Beleg/Zusammenhang:** E04.

> Sprachfassung

### T082 · Tabellenzelle · Zeilen 264 bis 264

**Urteil:** Vorschlag L08. **Beleg/Zusammenhang:** E04.

> ISO-Norm

### T083 · Tabellenzelle · Zeilen 264 bis 264

**Urteil:** Vorschlag L08. **Beleg/Zusammenhang:** E04.

> ISO-Norm

### T084 · Tabellenzelle · Zeilen 264 bis 264

**Urteil:** Vorschlag L08. **Beleg/Zusammenhang:** E04.

> vor 1.0

### T085 · Tabellenzelle · Zeilen 264 bis 264

**Urteil:** Vorschlag L08. **Beleg/Zusammenhang:** E04.

> 1.0 seit 2015

### S065 · Satz · Zeilen 269 bis 272

**Urteil:** Vorschlag L08. **Beleg/Zusammenhang:** E04.

> Rust verbindet als einziger Kandidat der Tabelle Safe-Rust-Garantien mit einer Speicherverwaltung ohne Garbage
> Collector; Bereichsprüfungen lösen zur Laufzeit einen definierten \textit{panic} statt undefinierten Verhaltens
> aus \cite{rust-lang,rust-book}, während der C-Standard bei Pufferüberläufen undefiniertes Verhalten kennt
> \cite{iso-c}.

### S066 · Satz · Zeilen 272 bis 273

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> Diese Garantien setzen korrekte Verträge an jeder \texttt{unsafe}-Grenze voraus.

### S067 · Satz · Zeilen 273 bis 275

**Urteil:** Vorschlag F04. **Beleg/Zusammenhang:** E04.

> Statische Werkzeuge können Quelltext ohne ausgeführten Programmpfad prüfen; nur dynamische Prüfungen und Fuzzing
> bleiben auf erreichte Pfade beschränkt \cite{kernel-devtools,nsa-memory-safety}.

### S068 · Satz · Zeilen 275 bis 276

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> Zig prüft auch zur Übersetzungszeit; seine Laufzeitprüfungen hängen vom Build-Modus ab, und die Sprache hat noch
> keine Fassung~1.0 erreicht \cite{zig-lang}.

### S069 · Satz · Zeilen 276 bis 278

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> Die Migration von Bun von Zig nach Rust bildet dazu den Referenzfall aus \secref{sec:externe-faelle}
> \cite{bun-in-rust}.

### S070 · Satz · Zeilen 278 bis 278

**Urteil:** Belassen. **Beleg/Zusammenhang:** E04.

> Für die Vertrauensgrenze dieser Bibliothek fiel die Wahl deshalb auf Rust.

### S071 · Satz · Zeilen 280 bis 280

**Urteil:** Vorschlag L09. **Beleg/Zusammenhang:** E05.

> Drei Rust-Mittel tragen die Implementierung.

### S072 · Satz · Zeilen 280 bis 281

**Urteil:** Vorschlag L09. **Beleg/Zusammenhang:** E05.

> Der Parser liest die Surplus Area ohne Kopie als geborgte Byte-Ausschnitte, die ihren Empfangspuffer nicht
> überdauern können \cite{rust-book}.

### S073 · Satz · Zeilen 281 bis 282

**Urteil:** Vorschlag L09. **Beleg/Zusammenhang:** E05.

> \texttt{enum} und \texttt{Result} bilden Optionsarten und Fehler vollständig ab.

### S074 · Satz · Zeilen 282 bis 285

**Urteil:** Belassen. **Beleg/Zusammenhang:** E05.

> Wenige \texttt{unsafe} -Blöcke kapseln die Systemgrenzen; ihre Verträge prüft \chapref{chap:entwurf}.

### F002 · Fußnote · Zeilen 283 bis 284

**Urteil:** Belassen. **Beleg/Zusammenhang:** E05 / Kapitel 2.

> Das Rust-Schlüsselwort \texttt{unsafe} ist von der UNSAFE-Optionsklasse aus \secref{subsec:surplus-prinzipien}
> zu unterscheiden.

### S075 · Satz · Zeilen 285 bis 286

**Urteil:** Belassen. **Beleg/Zusammenhang:** E05.

> Externe Parser-Bibliotheken entfallen, weil die Mechanik von RFC~9868 selbst Untersuchungsgegenstand ist.

### S076 · Satz · Zeilen 288 bis 288

**Urteil:** Belassen. **Beleg/Zusammenhang:** E05.

> Safe Rust verhindert keine Protokollfehler.

### S077 · Satz · Zeilen 288 bis 290

**Urteil:** Vorschlag L09. **Beleg/Zusammenhang:** E05.

> Ein Um-eins- und Offsetfehler bei ungeradem Beginn der Surplus Area überstand 23 selbstgeschriebene Tests und
> fiel erst im Pull-Request auf; er verletzte die Protokolllogik, nicht die Speichersicherheit.

### S078 · Satz · Zeilen 290 bis 291

**Urteil:** Vorschlag F02. **Beleg/Zusammenhang:** E05.

> Danach erhielt jeder Schritt mit neuer Parsefläche Property-Tests und ein Fuzz-Ziel (\chapref{chap:entwurf}).

### H007 · Überschrift · Zeilen 293 bis 293

**Urteil:** Belassen. **Beleg/Zusammenhang:** E05.

> Zugang zur Surplus Area

### S079 · Satz · Zeilen 296 bis 297

**Urteil:** Belassen. **Beleg/Zusammenhang:** E05.

> Ein gewöhnlicher UDP-Socket kann die Surplus Area weder füllen noch auslesen (\secref{sec:netzpfad})
> \cite[Sec.~18]{rfc9868}.

### S080 · Satz · Zeilen 297 bis 299

**Urteil:** Vorschlag L10. **Beleg/Zusammenhang:** E05.

> Packet Sockets, TUN/TAP und \texttt{AF\_XDP} bieten zwar Zugriff auf vollständige Rahmen oder IP-Pakete,
> erfordern aber die Behandlung der Verbindungsschicht, ein virtuelles Netzgerät oder ein XDP-Programm samt
> Speicher- und Warteschlangenaufbau \cite{man7packet,linux510tuntap,linux510afxdp}.

### S081 · Satz · Zeilen 299 bis 300

**Urteil:** Belassen. **Beleg/Zusammenhang:** E05.

> Ein Kernelmodul liegt außerhalb des Projektumfangs.

### S082 · Satz · Zeilen 300 bis 302

**Urteil:** Vorschlag L10. **Beleg/Zusammenhang:** E05.

> Raw Sockets geben der Benutzerraumbibliothek dagegen ohne eigenes Netzgerät Zugriff auf das vollständige
> IP-Datagramm und bilden daher den kleinsten geeigneten Unterbau \cite{man7raw}.

### S083 · Satz · Zeilen 304 bis 306

**Urteil:** Vorschlag L10. **Beleg/Zusammenhang:** E05.

> Als Betriebssystem trägt Linux diese Entscheidung: Dort ist der Weg dokumentiert und im quelloffenen Kernel
> nachprüfbar, und dieselbe Plattform stellt alle Endpunkte der Kampagnen (\secref{sec:ff2-pfadmodell}).

### S084 · Satz · Zeilen 306 bis 307

**Urteil:** Vorschlag L10. **Beleg/Zusammenhang:** E05.

> Der Preis ist, dass die Bibliothek IPv4-Header, Längen, UDP-Prüfsumme und Optionen selbst prüft.

### S085 · Satz · Zeilen 307 bis 308

**Urteil:** Belassen. **Beleg/Zusammenhang:** E05.

> Beim Senden liefert sie mit \texttt{IP\_HDRINCL} den IPv4-Header; da dieser Pfad nicht fragmentiert, muss jedes
> Optionsdatagramm in die MTU passen (\secref{sec:netzpfad}).

### S086 · Satz · Zeilen 308 bis 309

**Urteil:** Belassen. **Beleg/Zusammenhang:** E05.

> Diese Folgen bestimmen den Entwurf in \chapref{chap:entwurf}.

### H008 · Überschrift · Zeilen 311 bis 311

**Urteil:** Belassen. **Beleg/Zusammenhang:** E05.

> Mitschnitt und Auswertung

### S087 · Satz · Zeilen 314 bis 314

**Urteil:** Vorschlag L11. **Beleg/Zusammenhang:** E05.

> Die Kampagnenskripte zeichnen den Verkehr mit \texttt{tcpdump} in archivierbaren PCAP-Beweisdateien auf.

### S088 · Satz · Zeilen 314 bis 317

**Urteil:** Vorschlag L11, F03. **Beleg/Zusammenhang:** E05.

> Der eigene Prüfer aus \secref{sec:pruefkette} rechnet OCS und Optionsstruktur aus den Bytes nach, weil Wireshark
> in der verwendeten Version~4.6 die Surplus Area nicht dekodiert (\secref{sec:netzpfad}); \texttt{tshark} prüft
> unabhängig davon die IPv4- und UDP-Felder.

### S089 · Satz · Zeilen 317 bis 318

**Urteil:** Vorschlag L11. **Beleg/Zusammenhang:** E05.

> Aufzeichnen, Deuten und Gegenprüfen liegen damit bei drei verschiedenen Werkzeugen.

### H009 · Überschrift · Zeilen 320 bis 320

**Urteil:** Belassen. **Beleg/Zusammenhang:** E05.

> Fuzzing und formale Gegenprobe

### S090 · Satz · Zeilen 323 bis 324

**Urteil:** Vorschlag L12. **Beleg/Zusammenhang:** E05.

> Die vierte Entscheidung stellt der Testsuite zwei Gegenproben zur Seite, die auf das Gefahrenmodell der
> KI-gestützten Entwicklung antworten (\secref{sec:gefahrenmodell}).

### S091 · Satz · Zeilen 324 bis 326

**Urteil:** Vorschlag L12. **Beleg/Zusammenhang:** E05.

> Das über \texttt{cargo-fuzz} eingebundene libFuzzer-Fuzzing mutiert Eingaben des echten Parsercodes
> abdeckungsgeleitet und sucht Abstürze und verletzte Invarianten \cite{libfuzzer}.

### S092 · Satz · Zeilen 326 bis 328

**Urteil:** Vorschlag L12. **Beleg/Zusammenhang:** E05.

> Lean beweist ausgewählte Eigenschaften handgeschriebener Modelle unter den Voraussetzungen der jeweiligen
> Theoreme; den Begriff führt \secref{subsec:pruefmittel} ein.

### S093 · Satz · Zeilen 328 bis 329

**Urteil:** Belassen. **Beleg/Zusammenhang:** E05.

> Fuzzing beweist keine Fehlerfreiheit, und ein Lean-Beweis gilt nicht automatisch für den Rust-Code, der das
> Modell umsetzt.

### S094 · Satz · Zeilen 329 bis 332

**Urteil:** Vorschlag L12. **Beleg/Zusammenhang:** E05.

> Dass daneben auch die Norm selbst Prüfgegenstand bleiben muss, zeigte die Schlussphase der Implementierung: Ein
> nachträglicher RFC-Abgleich fand trotz grüner Prüfkette noch Konformitätslücken und wurde als eigener
> Korrekturschritt umgesetzt (\secref{sec:soll-ist}).

## Abschlussbedingungen nach der Umsetzung

1. F01 bis F04 korrigieren beziehungsweise den stärkeren Prozessnachweis zu F02 vollständig belegen.
2. Die gewählten sprachlichen Vorschläge im Zusammenhang umsetzen; keine richtige Einschränkung verlieren.
3. Gesamte Thesis neu bauen und die dann aktuellen Kapitel-4-Seiten erneut visuell prüfen.
4. Insbesondere Optionsstruktur sowie alle neu entstandenen Trennungen und verschobenen Tabellen prüfen.
5. Änderungen an Literatur, Verweisen und angrenzenden Seiten kontrollieren und erst dann den neuen Stand freigeben.

Die Prüfung dieses Ausgangsstands ist abgeschlossen. Die vorgeschlagenen Änderungen sind noch nicht umgesetzt;
der Bericht ist daher keine Freigabe einer korrigierten Fassung.
