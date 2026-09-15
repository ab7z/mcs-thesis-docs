# Kapitel 4: Codex-Review des Claude-Diffs vom 13. September 2026

Unveränderter Wortlaut des Codex-Berichts (gpt-6-astra, Effort ultra, read-only, 15:40 bis 15:50 Uhr), nur auf 120
Zeichen je Zeile umgebrochen. Prüfgegenstand war der Diff zwischen dem Codex-Stand vom 13.09.2026 und dem von Claude
eingearbeiteten Stand; Auftrag und Einordnung stehen in `kapitel-4-neubewertung-2026-09-13.md`.

## 1. Urteil

GreenCodeDoesntSmell, **Freigabe mit Auflagen**: Der aktuelle Stand ist im geprüften Diffumfang noch nicht
uneingeschränkt abgabereif. Von 18 Hunks sind 16 richtig; zwei benötigen eine Anpassung: die zu absolute Aussage über
gemeinsame Testinvarianten und die falsche Kennzeichnung der C++ Core Guidelines als undatiert. Die Änderungen an
RFC-Auslegung, Messbegriffen und Querverweisen sind tragfähig und entfernen keine notwendige normative Einschränkung.
Nach den beiden Korrekturen und ihrer erneuten Build- und PDF-Kontrolle ist der Diffumfang freigabefähig; die
vorbestehende Begründungslücke zur CSV-Kennung 226 bleibt gesondert offen.

Geprüft wurde die übergebene Codex-Kopie gegen den aktuellen Arbeitsbaum auf Basis des Stands vom 10.09.2026. Der Patch
rekonstruiert alle drei betroffenen Textdateien exakt; `03_methodik.tex` ist gegenüber der Kopie unverändert. Das
Nachbarrepositorium steht sauber auf dem Stand vom 03.09.2026. Alle folgenden Zeilenangaben beziehen
sich auf den aktuellen Stand; Implementierungsbelege liegen unter `../udp-transport-options`.

## 2. Prüfung jedes Hunks in Diff-Reihenfolge

**Hunk 1, `04_analyse.tex:18–23`: richtig.**  
RFC 9868 erläutert die `>>`-Konvention in `literature/rfc9868.txt:126–129`. Die eigene Auszählung bestätigt 103
markierte Absätze, davon 21 in Abschnitt 10 und 44 in Abschnitt 11. Das zusätzliche Zitat trägt die
Markierungskonvention; die Kontrollzahl stammt aus der Auszählung. Die Einbeziehung unmarkierter normativer
Festlegungen bleibt erhalten.

**Hunk 2, `04_analyse.tex:49–52`: richtig.**  
Die neue Formulierung benennt Größe und Abzug genau entsprechend `literature/rfc9868.txt:353–366`. Der Verweis trifft
die passende Formel samt Shim-Fußnote in `02_grundlagen.tex:92–104`. Die Implementierungsgrenze ist separat belegt:
`src/wire/ip.rs:70–71` weist andere Protokollnummern zurück. Aus einer RFC-Festlegung wird keine allgemeine Pflicht
zum Verzicht auf Shim-Header gemacht.

**Hunk 3, `04_analyse.tex:66–68`: richtig.**  
Die CSV unterscheidet tatsächlich Implementierungsstand und technische Erfüllbarkeit:
`konformitaet-kategorien.csv:4–9`, Spalten `kategorie` und `technisch`. Der neue Verweis auf `sec:soll-ist` trifft
deren Erläuterung in `06_evaluation.tex:876–893`. Die Trennung von Arbeitsindex, eigener Einzelzuordnung und
FF1-Maßstab bleibt konsistent mit Kapitel 3 und 7. Die offene Einzelbewertung 226 betrifft die Begründung eines
Datensatzes, nicht die Richtigkeit dieser Dateibeschreibung.

**Hunk 4, `04_analyse.tex:140–151`: richtig.**  
Die Trennhilfen verändern keinen Inhalt und ergeben in der PDF korrekte Trennungen. „Ohne beidseitige Mitschnitte oder
Sendemanifest“ entspricht den Beweiskraftstufen in `06_evaluation.tex:32–40`: Fehlende Senderaufzeichnung führt dort
ebenfalls zum Pilotniveau. Das neue „oder“ beseitigt zudem die mögliche Lesart, erst das gemeinsame Fehlen beider
Belegarten mache einen Vorversuch zum Piloten.

**Hunk 5, `04_analyse.tex:165–168`: richtig.**  
Die Herkunft der Mechanismenklassen entspricht nun ausdrücklich `06_evaluation.tex:698–702`. Die Streichung von
„Aussagegrenzen“ aus der Ankündigung entfernt keine geltende Grenze: `04_analyse.tex:159–163` begrenzt die Zuordnung
weiterhin auf das beobachtete Intervall; Kapitel 6 schließt einen Gerätenachweis ausdrücklich aus.

Dem Workflowbefund A7 widerspreche ich teilweise: Die alte Fassung enthielt keinen belegten fachlichen Widerspruch.
Vorversuche können Hypothesen und Mechanismenklassen begründen, ohne ihre Ergebnisse zu verallgemeinern. Die neue
Fassung verdeutlicht den Zusammenhang sinnvoll.

**Hunk 6, `04_analyse.tex:209–211`: richtig.**  
Die Einschränkung entspricht `01_einleitung.tex:151–154`; Kapitel 6 nennt IPv6 in Zeile 54 als Messumfang, enthält
aber keine eigene Ergebnisreihe.

Die Gegenprobe ist im Archiv `external-campaign-20260810T200118Z.tar.zst` belegt: intern
`matrix/send-ipv6-probe.py:53–102` für die Erzeugung außerhalb der Rust-Bibliothek und
`analysis/ipv6-bridge.md:18–21,29–32,50–58` für Vergleich und Aussagegrenzen. Die dortigen Gast-, `en0`- und
Zielmitschnitte stützen den beschriebenen Einzelversuch. Vorhandene Header- und Prüfsummenprüfungen sind keine
vollständige RFC-Konformitätsprüfung. Claude hat die Aussage somit angemessen eingeschränkt.

**Hunk 7, `04_analyse.tex:223–227`: richtig.**  
Anwendung, beauftragte Schicht oder Bibliothek sowie die begrenzte Reassemblierungsausnahme entsprechen
`literature/rfc9868.txt:274–284`. „Einzige“ stellt den Wortlaut des RFC genauer dar. Der Zusammenhang beschränkt die
Ausnahme auf den von UDP Options eingeführten Zustand; er behauptet nicht, Anwendungen dürften keinen anderen Zustand
führen.

**Hunk 8, `04_analyse.tex:248–249`: richtig.**  
Es wurden ausschließlich Trennhilfen ergänzt. Die aktuelle PDF trennt „Speicher-sicherheit“ und „Speicher-bereichs“
korrekt. Eine fachliche Änderung liegt nicht vor.

**Hunk 9, `04_analyse.tex:270–306`: richtig.**  
Die Vergleichsaussage bleibt ausdrücklich auf C, C++, Zig und Rust beschränkt. Rusts Speichersicherheit ohne Garbage
Collector ist belegt; Zig überträgt die Verantwortung für Speicherlebensdauern dem Programmierer. Der Vorbehalt zu den
`unsafe`-Grenzen bleibt unmittelbar erhalten. Die statische Ownership- und Lebensdauerprüfung ist ebenfalls richtig
beschrieben. Belege: [Rust-Buch, Ownership](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html),
[Lebensdauern](https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html), [Zig 0.16, Lifetime and
Ownership](https://ziglang.org/documentation/0.16.0/#Lifetime-and-Ownership).

Die Bun-Präzisierung stimmt mit `03_methodik.tex:50–53` und der vom Projekt genannten Begründung überein. A2 bewertet
den Codex-Ausdruck allerdings zu hart: „Wechsel von Bun zu Rust“ war missverständlich, aber im Zusammenhang kein
nachgewiesener Sachfehler. Die neue Fassung benennt Projekt und Ausgangssprache eindeutig. [Bun: Rewriting Bun in
Rust](https://bun.com/blog/bun-in-rust)

Die Korrektur der `unsafe`-Ankündigung ist erforderlich und richtig: `05_entwurf_implementierung.tex:87–90` nennt die
Lage der zwei Blöcke, prüft jedoch keine Sicherheitsverträge. Die Kommentare stehen tatsächlich in
`src/socket/send.rs:129–139` und `src/socket/recv.rs:168–169`.

Auch der neue Abbildungsverweis stimmt: `03_methodik.tex:284–285` enthält die Vorgabe zu Property-Tests und
Fuzz-Zielen. Der historische Anlass einschließlich der 23 Tests ist in `docs/plan/steps/02-wire-model.md:99–109`
dokumentiert.

A3 und der sprachliche Teil von A14 sind dagegen Verdeutlichungen, keine belegten fachlichen Reparaturen. Der
Codex-Stand begründete die Auswahl bereits mit Speichersicherheit; eine Tabellenzelle benötigt keinen vollständigen
Satz.

**Hunk 10, `04_analyse.tex:315–324`: richtig.**  
„Im Gegenzug“ hebt den zusätzlichen Prüfaufwand hervor. Die Bibliothek prüft IPv4-Felder und Prüfsumme in
`src/wire/ip.rs:48–75`, anschließend UDP-Längen und UDP-Prüfsumme in `src/recv/pipeline.rs:211–248`.

Die Formulierung behauptet keine Umgehung sämtlicher Kernelprüfungen. Deren verbleibende Rolle erläutert
`02_grundlagen.tex:869–884`. Die Grenze des Sendepfads bei `IP_HDRINCL` entspricht weiterhin
[raw(7)](https://man7.org/linux/man-pages/man7/raw.7.html). Die Trennhilfen sind korrekt.

**Hunk 11, `04_analyse.tex:330–343`: richtig.**  
„UDP-Optionen nicht dekodiert“ benennt die fehlende semantische Auswertung genauer als die alte Formulierung über die
gesamte Surplus Area. Der offizielle
[Wireshark-4.6.0-UDP-Dissektor](https://raw.githubusercontent.com/wireshark/wireshark/v4.6.0/epan/dissectors/packet-udp.c)
begrenzt die Weitergabe auf `UDP Length` und enthält keine entsprechende Optionsauswertung. Die Sichtbarkeit der
Paketbytes wird damit nicht ausgeschlossen.

„Lokale Referenzläufe“ passt zu `06_evaluation.tex:37,137–139`. Die OCS-Nachrechnung steht in
`scripts/eval-check.py:233–250`. Ihr Einsatz am 10. August ist durch die vier archivierten Metadateien
`logs/hetzner-eval/02-eval-veth.meta` bis `05-eval-filter.meta`, jeweils Zeilen 2–6, mit Datum, Aufruf und Exitcode 0
belegt.

**F1-evalcheck-10aug wurde deshalb zu Recht abgelehnt:** Die fünf gescheiterten Aufrufe waren nicht sämtliche
Einsätze. Auch **B18 darf nicht pauschal übernommen werden**: Das archivierte
`matrix/analyze-pcap-pair.py:55–62,131–136` verwendet die importierte Prüffunktion für Sender- und Empfängerpakete.

„Sendebelege“ ist als Oberbegriff richtig, weil die Auswerter neben Manifesten auch Versandresultate und `send.log`
verwenden. Die Verknüpfung und Übernahme der Empfängerberichte stehen in `scripts/p0-eval.py:255–275`,
`p1-eval.py:121–122,372–385` und `p2-eval.py:170–196`. Der neue Verweis trifft die Kampagnenkennungen und
Werkzeugangaben in `06_evaluation.tex:61–64,130–137`.

**Hunk 12, `04_analyse.tex:348–352`: anpassen.**  
Die gemeinsamen Testmodule sind belegt, beispielsweise durch `fuzz/fuzz_targets/wire_datagram.rs:17–20` und
`tests/properties_wire.rs:175–187`. Daraus folgt jedoch keine zwangsläufige Unentdeckbarkeit einer falsch formulierten
Invariante. Eine falsche Assertion kann gerade an einem korrekten Ergebnis scheitern; außerdem enthalten die
Property-Tests zusätzliche Prüfungen (`tests/properties_wire.rs:119–171`). Die gemeinsamen Assertions selbst sind in
`tests/common/mod.rs:19–60` sichtbar.

Die absolute Folgerung aus A20 ist daher zurückzuweisen. Belegt ist ein gemeinsames Fehlerrisiko, wie es
`03_methodik.tex:440–444` bereits bedingt beschreibt. Vollständiger Ersatz für den geänderten Einleitungsabsatz:

```latex
Fuzzing und formale Gegenproben ergänzen die Unit-, Integrations- und Property-Tests
(\secref{subsec:pruefmittel}). Sie sollen Fehler aufdecken, die bei der KI-gestützten Entwicklung und
ihren bisherigen Prüfungen unentdeckt bleiben können (\secref{sec:gefahrenmodell}).
Fuzz-Ziele und Property-Tests verwenden dabei gemeinsame Testmodule. Fehlerhafte Annahmen in diesen
Modulen können deshalb in beiden Prüfverfahren unentdeckt bleiben.
```

**Hunk 13, `06_evaluation.tex:114–116`: richtig.**  
Der zusätzliche `tcpdump`-Satz verbindet die Werkzeugbeschreibung mit den folgenden Betriebsregeln. Die
Erfassungsbefehle stehen in `scripts/p0-campaign.sh:76`, `p1-campaign.sh:69` und `p2-campaign.sh:70`. Die Grenze der
OCS-Auswertung bleibt unverändert und entspricht den unter Hunk 11 genannten Codebelegen.

**Hunk 14, `06_evaluation.tex:856`: richtig.**  
Die Tabelle summiert die eigene Einzelzuordnung, nicht die Selbstauskunft des RFC-Arbeitsindex. Die neue Beschriftung
stimmt mit `06_evaluation.tex:850–851,891–896` überein. Eine lesende CSV-Auswertung bestätigt die dargestellten Summen
50/7/10 und 57/10. Das bestätigt ihre rechnerische Herkunft, nicht die noch offene Begründung der Kennung 226.

**Hunk 15, `literatur.bib:230–239`, einschließlich Entfernung von `microsoft-memory`: richtig.**  
Die NSA-Veröffentlichungsmeldung vom 10. November 2022 verlinkt die verwendete Adresse; diese liefert die Fassung
April 2023, Version 1.1. Der Hinweis erklärt die unterschiedlichen Datumsangaben zutreffend.
[NSA-Veröffentlichungsmeldung](https://www.nsa.gov/Press-Room/News-Highlights/Article/Article/3215760/nsa-releases-guidance-on-how-to-protect-against-software-memory-safety-issues/),
[NSA-Dokument](https://media.defense.gov/2022/Nov/10/2003112742/-1/-1/0/CSI_SOFTWARE_MEMORY_SAFETY.PDF)

`microsoft-memory` ist weder im Codex-Textstand noch im aktuellen Text zitiert; eine Einbindung über `\nocite` besteht
ebenfalls nicht. Der verbleibende
[MSRC-Blog](https://www.microsoft.com/en-us/msrc/blog/2019/07/a-proactive-approach-to-more-secure-code/) trägt die
verwendete Aussage. Es geht kein benötigter Beleg verloren.

**Hunk 16, `literatur.bib:248–255`: anpassen.**  
„Undatierte“ ist neu und falsch. Die offizielle Seite nennt unmittelbar unter dem Titel den **14. Juni 2026**. Dem
Workflowbefund A18 widerspreche ich ausdrücklich: Die Vereinheitlichung einer bibliografischen Formel rechtfertigt
keine falsche Quellenangabe. [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines)

Vollständiger Ersatz des Eintrags:

```bibtex
@online{cpp-core-guidelines,
    author       = {Stroustrup, Bjarne and Sutter, Herb},
    title        = {{C++ Core Guidelines}},
    date         = {2026-06-14},
    note         = {Fortlaufend gepflegte Online-Fassung, insbesondere Regel R.1 zur Ressourcenverwaltung},
    url          = {https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines},
    urldate      = {2026-09-13},
}
```

**Hunk 17, Anschlussstelle `literatur.bib:282–285`, Entfernung von `kernel-devtools`: richtig.**  
Der Schlüssel ist in keiner aktuellen `.tex`-Datei und auch im Codex-Textstand nicht mehr zitiert. Die Entfernung
beseitigt keinen verwendeten Quellenbeleg und verlangt keine Textänderung.

**Hunk 18, `literatur.bib:424–431`: richtig.**  
Der Beitrag nennt Jarred Sumner als Autor und den 8. Juli 2026 als Veröffentlichungsdatum. Beide Ergänzungen stimmen;
die aktualisierte Zugriffsangabe passt zum erneuten Abruf. [Bun-Beitrag](https://bun.com/blog/bun-in-rust)

## 3. Verbliebene Mängel und nicht umgesetzte Workflow-Befunde

**Abgaberelevant außerhalb des Diffs bleibt die Begründung zur CSV-Kennung 226.**  
`konformitaet-kategorien.csv:74` bindet das SHOULD ausdrücklich an das nicht gewählte vorhergehende MAY.
`literature/rfc9868.txt:2113–2116` richtet beide Aussagen dagegen an Implementierungen mit Bedenken wegen verdeckter
Kanäle; die Empfangsempfehlung hängt nicht ausdrücklich von der Ausübung des MAY ab.

Damit ist die Begründung unzureichend, aber die Endkategorie noch nicht sicher falsch. Vor einer Gesamtfreigabe muss
das maßgebliche Schutzziel geklärt und die Einstufung entsprechend begründet werden. Ersatzsummen lassen sich daraus
noch nicht ableiten. Die Nichtbearbeitung von K4-S2-05 ist als Grenze dieses Kapitel-4-Diffs vertretbar; eine
uneingeschränkte Freigabe der Kapitel-6-Einzelbewertungen wäre es nicht. Der Punkt steht bereits in
`insights-inbox.md:21–29` und im Neubewertungsbericht, Zeilen 267–271 und 282–283.

**Die übrigen Nichtumsetzungen sind vertretbar.**  
Bei A8 entfiel der zusätzliche Satz über Beweiskraftstufen; der erhaltene Verweis führt unmittelbar zu deren
Definition in `06_evaluation.tex:32–40`. Bei A25 fehlt weiterhin der ausdrückliche Tunnelprüfzweck. Das Seitenziel
allein wäre dafür kein sachlicher Grund; tragfähig ist aber die vorhandene Erklärung in `04_analyse.tex:142–143,212`
und `06_evaluation.tex:274–277`, einschließlich der Grenze gegenüber nativem Transport.

Die Ablehnungen von F1-evalcheck-10aug und B18 sind durch die Archivbelege bestätigt, siehe Hunk 11. Für O2-08 ist
kein konkreter Ergebnisfehler belegt: `03_methodik.tex:160–162` und `04_analyse.tex:127–132` bestimmen das
kontrollierte Szenario als Untersuchungseinheit; `06_evaluation.tex:142–149` beschreibt die Auswertbarkeit der
Kampagnenläufe.

O2-16 verlangt keine notwendige Änderung: „Sein Verhalten“ bezieht sich verständlich auf den Raw-Socket-Zugang. Die
bei B13/O2-12 verlangte Kürzung der Fuzzing-Erklärung ist ebenfalls optional; die Passage erklärt den Unterschied
zwischen ausgeführtem Parsercode und Lean-Modell.

**Optionale Stil- und Umfangspunkte sind keine Freigabehindernisse.**  
Das betrifft Repository/Repositorium (O2-14), „grüne Prüfkette“ außerhalb des Diffs (B15), die nicht wieder
aufgenommenen Angaben zum Sprachreifegrad sowie die vorbestehende lange Zeile in `AGENTS.md` (A28). Der alleinstehende
Ausdruck „nach“ in der Zig-Tabellenzelle bleibt eine kosmetische Umbruchfrage. Die im Bericht noch als offen
aufgeführten Bib-Löschungen und die IPv6-Einschränkung sind tatsächlich umgesetzt.

Die abweichende Aussage in `../udp-transport-options/docs/evaluation.md:31–33` zur fehlenden OCS-Nachrechnung bleibt
bestehen und widerspricht `scripts/eval-check.py:233–250`. Der Thesistext folgt hier richtig dem Code. Die
Nichtänderung des Nachbarrepositoriums ist innerhalb dieses Auftrags vertretbar.

## 4. Prüfgrenzen und Abschlusskontrolle

Die vorhandene [Thesis-PDF](</Users/ab/Library/Mobile
Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/main.pdf>) wurde auf den physischen Seiten
**42–49, 64, 79 und 92–94** visuell geprüft. Kapitel 4, seine Fußnoten und Tabellen sowie die betroffenen
Folgeänderungen sind lesbar; die geänderten Trennhilfen ergeben korrekte Umbrüche. Die drei geänderten Quelldateien
bleiben vollständig unter 120 Zeichen je Zeile; die Ergänzungen enthalten keine Gedankenstriche.

Die PDF umfasst 95 Seiten und stammt vom 13. September 2026, 15:38 Uhr. Die geänderten Formulierungen und
Literaturangaben sind darin enthalten; die vorhandenen LaTeX- und Biber-Protokolle zeigen keine einschlägigen
Warnungen. Das ist eine Prüfung der vorhandenen Ausgabe, **kein eigener Neubau**.

Kriterien 1–21 wurden im jeweiligen Diffumfang geprüft; die Befunde zu Quellenangaben und Aussagekraft bleiben bis zur
Korrektur offen. Kriterien 22 und 23 sind im genannten PDF-Umfang geprüft. Kriterium 24 ist hinsichtlich Diff,
vorhandener Protokolle und PDF geprüft; der Neubau nach den vorgeschlagenen Ersatztexten bleibt offen.

Nicht erneut ausgeführt wurden Rust-Tests, Fuzzing, Lean-Beweise oder Messkampagnen. Nicht vollständig neu bewertet
wurden sämtliche 67 CSV-Zeilen oder der gesamte Messkorpus. Für die geänderten Messangaben wurden die einschlägigen
Archivbelege gelesen; beim Archiv vom 10. August stimmt der äußere SHA-256-Wert. Eine historische Wireshark-Binärdatei
wurde nicht ausgeführt.

Es wurden keine Dateien angelegt oder geändert, keine Archive ins Dateisystem entpackt und kein Build ausgeführt.

# Zweiter Review nach der Kürzungsrunde (16:09 bis 16:18 Uhr)

Unveränderter Wortlaut des zweiten Codex-Berichts über den Gesamtdiff gegen den Codex-Stand (einschließlich
01_einleitung.tex gegen den Stand vom 10.09.2026), nur auf 120 Zeichen je Zeile umgebrochen; überlange URL-Zeilen
bleiben.

**1. Urteil.** GreenCodeDoesntSmell, **Freigabe: ja, Kapitel 4 ist im geprüften Diff-Umfang abgabereif.** Alle 21
Hunks sind richtig; keiner muss angepasst oder zurückgenommen werden. Die Kürzungen erhalten die Begründung der
Technologieauswahl, die Aussagegrenzen der Messungen und die Verbindungen zu den anderen Kapiteln. Außerhalb des Diffs
bleibt die bereits bekannte fehlerhafte Begründung zu CSV-Kennung 226 bestehen; sie verhindert eine uneingeschränkte
Freigabe des abschließenden FF1-Ergebnisses in Kapitel 6.

**2. Einzelprüfung in Diff-Reihenfolge.**

Geprüft wurde der Arbeitsbaum auf Basis des Stands vom 10.09.2026, die Implementierung auf dem Stand vom 03.09.2026. Das
Anwenden des bereitgestellten Diffs auf die Codex-Kopie ergibt exakt die aktuellen fünf Quelldateien; für Kapitel 1
wurde wie vorgegeben der Stand vom 10.09.2026 verwendet. Die folgenden Zeilenangaben bezeichnen den aktuellen
Arbeitsbaum; Implementierungspfade beziehen sich auf `../udp-transport-options`.

**Hunk 1, `03_methodik.tex:186`: richtig.** Die Begriffsänderung erhält die Aussage und vereinheitlicht die
Bezeichnung mit Kapitel 6, etwa `06_evaluation.tex:835`.

**Hunk 2, `03_methodik.tex:246 bis 252`: richtig.** Bezeichnung und Genitiv sind korrekt. Commit, Dokumentpfade und
Aussage über die Adressaten bleiben unverändert; der zusätzliche Quelltextumbruch verändert den gesetzten Satz nicht.

**Hunk 3, `04_analyse.tex:17 bis 23`: richtig.** Der ergänzte Beleg trifft die Markierungskonvention in [RFC 9868,
Zeilen 120 bis 129](</Users/ab/Library/Mobile
Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/literature/rfc9868.txt:120>). Die erneute Zählung
ergibt 103 Markierungen. Unmarkierte normative Festlegungen bleiben ausdrücklich einbezogen.

**Hunk 4, `04_analyse.tex:47 bis 72`: richtig.** Die Obergrenze und ihre Verringerung um die gesamte Shim-Länge
entsprechen `rfc9868.txt:353 bis 366`; Kapitel 2 enthält die angekündigte Formel (`02_grundlagen.tex:92 bis 99`).
`src/wire/ip.rs:70 bis 75` bestätigt die Beschränkung auf Protokoll 17. Die kompakten Kennungen ergeben weiterhin 49
funktionale Anforderungen ohne FR-47 und zwölf nichtfunktionale Anforderungen. Die Ergänzung „Implementierungsstand“
entspricht den getrennten CSV-Spalten `kategorie` und `technisch`; das neue Verweisziel erklärt beide Bewertungen
(`06_evaluation.tex:876 bis 904`).

**Hunk 5, `04_analyse.tex:81`: richtig.** Die Tabellenbeschriftung bezeichnet weiterhin den RFC-Arbeitsindex. Nur der
Repositoriumsbegriff wird vereinheitlicht.

**Hunk 6, `04_analyse.tex:139 bis 151`: richtig.** Die Trennhilfen verändern keine Aussage. Die Formulierung mit „oder
Sendemanifest“ entspricht der Abgrenzung von Pilot und vollständiger Kampagne in `06_evaluation.tex:32 bis 40`.

**Hunk 7, `04_analyse.tex:165 bis 166`: richtig.** Kapitel 6 erläutert tatsächlich die aus Vorversuchen und Messungen
gewonnenen Mechanismenklassen (`06_evaluation.tex:695 bis 702`). Nichtverallgemeinerung und Grenzen der
Gerätezuordnung bleiben unmittelbar davor erhalten (`04_analyse.tex:150 bis 163`). **Workflow-Befund A7 überbewertet
den Codex-Stand:** Nicht verallgemeinerbare Vorversuche dürfen Hypothesen liefern; darin lag kein nachgewiesener
Sachfehler.

**Hunk 8, `04_analyse.tex:201 bis 220`: richtig.** Die IPv6-Streichung beseitigt die nicht eingelöste
Vergleichsankündigung. Die verbliebene IPv6-Zelle in Tabelle 4.2 kennzeichnet ausschließlich den ausgeschlossenen
Umfang. Anwendung beziehungsweise Schicht oder Bibliothek, initiierte Antworten und die einzige begrenzte
Zustandsausnahme entsprechen `rfc9868.txt:272 bis 284`. „Einbindbare Bibliothek“ begründet die Artefaktform auch ohne
den gestrichenen Wiederverwendbarkeitssatz.

**Hunk 9, `04_analyse.tex:239 bis 247`: richtig.** Die gestrichene Aussage über die vier Kandidaten steht bereits in
Zeilen 235 bis 237. Die Entscheidungskriterien und die belegten Speicherfehlerzahlen bleiben unverändert; die
Trennhilfen ändern keine Bedeutung.

**Hunk 10, `04_analyse.tex:261 bis 295`: richtig.** Der Rust-Vergleich ist auf die vier Kandidaten und den sicheren
Sprachumfang begrenzt; die Voraussetzung korrekter `unsafe`-Grenzen bleibt erhalten. Ownership-Prüfung und fehlender
Garbage Collector sind durch das [Rust-Buch](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html) belegt,
die Sicherheitsgrenze durch das [Rustonomicon](https://doc.rust-lang.org/nomicon/safe-unsafe-meaning.html); Zigs
Prüfungen ergeben keine vollständige Speichersicherheitsgarantie
([Zig-Dokumentation](https://ziglang.org/documentation/0.16.0/#Illegal-Behavior)).

Genau zwei `unsafe`-Blöcke mit Sicherheitskommentaren stehen in `src/socket/send.rs:129 bis 139` und
`src/socket/recv.rs:168 bis 169`. Kapitel 5 nennt ihre Lage (`05_entwurf_implementierung.tex:87 bis 90`); die frühere
Ankündigung einer dortigen Vertragsprüfung ist damit korrekt ersetzt. Der neue Abbildungsverweis trifft die verlangte
Ergänzung von Property-Tests und Fuzz-Zielen (`03_methodik.tex:284 bis 286`). Das Bun-Beispiel bleibt in Kapitel 3
behandelt und ist für die technische Sprachentscheidung entbehrlich.

**A3 und A14 waren Verdeutlichungen, keine Reparaturen fachlich falscher Aussagen.** Auch A2 belegt keinen falschen
Bun-Sachverhalt: Der [Originalbeitrag](https://bun.com/blog/bun-in-rust) beschreibt tatsächlich die Migration von Zig
nach Rust.

**Hunk 11, `04_analyse.tex:304 bis 314`: richtig.** „Im Gegenzug“ kennzeichnet den Prüfaufwand der gewählten
Schnittstelle. Die Prüfungen sind in `src/wire/ip.rs:40 bis 75` und `src/recv/pipeline.rs:205 bis 305` vorhanden. Die
unveränderte MTU-Grenze entspricht [raw(7)](https://man7.org/linux/man-pages/man7/raw.7.html).

**Hunk 12, `04_analyse.tex:319 bis 332`: richtig.** „UDP-Optionen nicht dekodiert“ bezeichnet die fehlende Funktion
genauer. Im Augustarchiv dokumentiert `logs/hetzner-eval/summary.md:9` TShark 4.6.4;
`artifacts/01-wire/tshark-verbose.txt:157 bis 195` zeigt die fehlende Optionsdekodierung am damaligen Datagramm.

Vier Metadateien unter `logs/hetzner-eval/02-eval-veth` bis `05-eval-filter` belegen erfolgreiche Läufe.
`matrix/analyze-pcap-pair.py:55 bis 67,131 bis 136` verwendet die importierte Surplus-Prüfung für Sender und
Empfänger. Die Ablehnungen von S1-F1 und B18 sind deshalb richtig.

**A4 enthält dagegen eine falsche Gleichsetzung:** Sendeprotokoll und Sendemanifest sind verschiedene Artefakte.
`scripts/p1-eval.py:372,383 bis 385` liest `send.log` und `manifest.jsonl` getrennt. Die jetzige Sammelbezeichnung
„Sendebelege“ ist richtig. P0/P1/P2 treffen mit dem neuen Verweis die Kampagnen und Auswerter in `06_evaluation.tex:61
bis 63,130 bis 139`.

**Hunk 13, `04_analyse.tex:337 bis 344`: richtig.** Gemeinsame Testmodule sind unmittelbar belegt, beispielsweise
durch `fuzz/fuzz_targets/wire_datagram.rs:17 bis 20` und `tests/properties_wire.rs:9`. „Können … unentdeckt bleiben“
wahrt die Aussagegrenze. Die frühere absolute Workflow-Folgerung war falsch: Gemeinsame fehlerhafte Annahmen erzwingen
kein gemeinsames Übersehen; die Property-Tests enthalten außerdem zusätzliche Prüfungen.

**Hunk 14, `06_evaluation.tex:54`: richtig.** „IPv4, Tunnel“ benennt die weiterhin ausgewerteten Teile der Kampagne.
Daraus folgt keine Behauptung, dass das historische Archiv keine zusätzlichen IPv6-Proben enthält. Die Tabellenzelle
passt zur neuen Umfangsabgrenzung in Kapitel 1.

**Hunk 15, `06_evaluation.tex:114 bis 116`: richtig.** Die Kampagnenskripte verwenden `tcpdump`. Der Übergang zu den
anschließenden Betriebsregeln ist verständlich; die Einschränkung zur übernommenen OCS-Bewertung bleibt erhalten.
Belege sind unter anderem `scripts/p0-eval.py:269 bis 275` und `scripts/p2-eval.py:259 bis 260`.

**Hunk 16, `06_evaluation.tex:856`: richtig.** Die Tabelle summiert die geprüfte Einzelzuordnung, nicht die
Selbstauskunft des Arbeitsindex. Die Zahlen stimmen mit der CSV überein. Das bestätigt ihre korrekte Übertragung,
nicht automatisch jede zugrunde liegende Einstufung; Kennung 226 bleibt gesondert zu behandeln.

**Hunk 17, `literatur.bib:225 bis 237`, einschließlich Löschung von `microsoft-memory`: richtig.** Die
[NSA-PDF](https://media.defense.gov/2022/Nov/10/2003112742/-1/-1/0/CSI_SOFTWARE_MEMORY_SAFETY.PDF) nennt April 2023
und Version 1.1; die [Erstveröffentlichung vom 10. November
2022](https://www.nsa.gov/Press-Room/News-Highlights/Article/Article/3215760/nsa-releases-guidance-on-how-to-protect-against-software-memory-safety-issues/)
verlinkt dieselbe Adresse. Der gelöschte Bib-Schlüssel wird nicht mehr verwendet; der weiterhin zitierte
[MSRC-Beitrag](https://www.microsoft.com/en-us/msrc/blog/2019/07/a-proactive-approach-to-more-secure-code/) trägt die
Speicherfehlerzahl.

**Hunk 18, `literatur.bib:248 bis 255`: richtig.** Der [Dokumentkopf der C++ Core
Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) nennt den 14. Juni 2026. **A18 war sachlich
falsch**, soweit der Workflow daraus eine undatierte Quelle machte. Die Korrektur aus Runde 1 ist umgesetzt.

**Hunk 19, `literatur.bib:282 bis 285`, Löschung von `kernel-devtools`: richtig.** Der Schlüssel wird in keiner
Thesis-Quelldatei mehr zitiert. Es entsteht kein fehlender Literaturverweis.

**Hunk 20, `literatur.bib:424 bis 431`: richtig.** Autor Jarred Sumner und Veröffentlichungsdatum 8. Juli 2026 stehen
im [Bun-Originalbeitrag](https://bun.com/blog/bun-in-rust). Die Quelle bleibt in `03_methodik.tex:50 bis 53`
verwendet.

**Hunk 21, `01_einleitung.tex:151 bis 153`: richtig.** Die Umfangsaussage passt zu den ausgewerteten IPv4-Pfaden.
Kapitel 2 grenzt IPv6 aus (`02_grundlagen.tex:786`), Kapitel 7 nennt es als künftige Untersuchung (`07_fazit.tex:71
bis 73`). Der entfernte Verweis hinterlässt keine offene Ergebnisankündigung.

Die übrigen Nichtumsetzungen des Workflows sind vertretbar: Der zusätzliche Evidenzstufen-Text aus A8 steht am
Verweisziel; der zusätzliche Tunnelzweck aus A25 ergibt sich aus Tabelle 4.3 und `06_evaluation.tex:274 bis 277`. A11
ist durch die beauftragte Umfangsreduktion erledigt, O2-14 durch die Begriffsvereinheitlichung. O2-08, O2-16,
B13/O2-12, B15, A28 und die nicht wiederhergestellten Sprachvergleichszeilen begründen keine belegte Abgabehürde. A19
und A20 sind mit sachlich ausreichenden, gekürzten Fassungen umgesetzt.

**3. Verbliebener abgaberelevanter Befund außerhalb des Diffs.**

**CSV-Kennung 226: Die Begründung der Nichtanwendbarkeit ist falsch.** Betroffen sind [CSV-Zeile
74](</Users/ab/Library/Mobile
Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/daten/konformitaet-kategorien.csv:74>),
`thesis/tikz/gen/ff1-kategorien.py:187 bis 189` und `06_evaluation.tex:971 bis 973`.

RFC 9868, Zeilen 2113 bis 2116, richtet das SHOULD an Implementierungen mit Bedenken wegen verdeckter Kanäle. Die
Nichtwahl der vorher genannten optionalen Optionsbegrenzung hebt diese Empfehlung nicht auf. Die Empfangsausgabe wird
auch nicht unabhängig umgeordnet: `src/recv/pipeline.rs:528 bis 638` sammelt Optionen in Empfangsreihenfolge;
`src/api/mod.rs:447 bis 484` reicht sie weiter.

Vollständiger Ersatz für die beiden Sätze beginnend mit „Zeile 226 betrifft“:

```latex
Zeile 226 betrifft die bedingte Empfehlung zur empfangsseitigen Referenzordnung aus Abschnitt~25.2.
Sie richtet sich an Implementierungen mit Bedenken wegen verdeckter Kanäle und hängt nicht davon ab,
ob die im vorangehenden \texttt{MAY} genannte Begrenzung von Optionen gewählt wurde
\cite[Sec.~25.2]{rfc9868}. Die Bibliothek ordnet die Empfangsausgabe nicht unabhängig von der
empfangenen Optionsfolge; ihre kanonische Sendereihenfolge erfüllt diese Empfehlung nicht.
Die Nichtanwendbarkeit ist in der Einzelzuordnung nicht hinreichend begründet. Die Einstufung
dieser Zeile und die davon abhängigen Summen bleiben deshalb vorläufig.
```

Dieser Ersatz beseitigt die falsche Begründung, liefert aber noch keine endgültige Einstufung. Dafür fehlt eine
belegte Umfangsentscheidung; eine neue Kategorie oder geänderte Summen wären geraten. Die Vertagung ist für diesen
begrenzten Kapitel-4-Review vertretbar, für eine endgültige Freigabe der FF1-Ergebnisse nicht.

Weitere abgaberelevante Fehler habe ich im geprüften Zusammenhang nicht belegt. Die falsche OCS-Beschreibung in
`../udp-transport-options/docs/evaluation.md:31 bis 33` wird vom ausführbaren Prüfer widerlegt; die Thesis beschreibt
dessen Verhalten richtig.

**4. Prüfgrenzen.**

Die vorhandene [PDF](</Users/ab/Library/Mobile
Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/main.pdf>) vom 13. September 2026, 16:09
Uhr, enthält die Änderungen. Visuell geprüft wurden die physischen Seiten 42 bis 49 vollständig sowie die betroffenen
Seiten 10, 34, 35, 63, 64, 79 und 92 bis 94. Dabei ergaben sich keine abgaberelevanten Layout- oder Trennungsfehler.
Alle fünf geprüften Quelldateien halten 120 Zeichen je Zeile ein; fehlende Bib-Schlüssel wurden nicht gefunden.

Kein Neubau, keine Tests, Fuzz-Läufe, Lean-Beweise oder Messkampagnen wurden ausgeführt. Die vorhandenen LaTeX- und
Biber-Protokolle enthalten keine entsprechenden Referenz- oder Boxwarnungen; das Glossarprotokoll meldet lediglich die
leere `main.glo`. Die Messprüfung umfasste gezielte Belege aus dem August-10-Archiv und dem P0/P1/P2-Archiv vom
14./15. August, keine vollständige PCAP-Neuauswertung. Eine erneute vollständige Faktenprüfung aller 67
Einzelzuordnungen oder sämtlicher Kapitel war nicht Gegenstand dieses Reviews.

Es wurden keine Dateien angelegt oder verändert.

# Dritter Review nach der Sprachrunde (16:26 bis 16:37 Uhr)

Unveränderter Wortlaut des dritten Codex-Berichts (Gesamtdiff, 29 Hunks, plus vollständige Sprachprüfung von Kapitel
4), nur auf 120 Zeichen je Zeile umgebrochen; Tabellen- und URL-Zeilen bleiben.

1. GreenCodeDoesntSmell, **Freigabe: ja. Kapitel 4 ist im geprüften Umfang abgabereif.** Alle 29 Hunks sind im
Zusammenhang richtig; keiner muss zurückgenommen oder fachlich korrigiert werden. Die Kürzungen erhalten die
Begründungen, Aussagegrenzen und Kapitelverbindungen. Die vollständige Sprachprüfung ergibt die unten genannten
Vereinfachungen, aber keinen neuen Abgabemangel; der bekannte Begründungsfehler zu CSV-Kennung 226 bleibt ein
gesonderter K6-Punkt.

2. Geprüft wurde der aktuelle Arbeitsbaum auf Basis des Stands vom 10.09.2026. Der bereitgestellte Patch lässt sich
vollständig aus dem Codex-Stand rekonstruieren und entspricht den aktuellen Dateien. Kapitel 4 hat SHA-256
`4df564b2c72688163db71df6f054050c197b9a644b581a88a22ee16676e77e88`; die Implementierung steht auf
dem Stand vom 03.09.2026. In der Stellenliste bezeichnet „RFC“ die Datei `literature/rfc9868.txt`;
Implementierungspfade beziehen sich auf das Nachbarrepositorium.

| Hunk | Stelle im aktuellen Stand | Urteil und Begründung |
|---:|---|---|
| 1 | `03_methodik.tex:186` | **Richtig.** „Repository der Implementierung“ bezeichnet dieselbe Quelle; Aussage und Zuordnung bleiben unverändert. |
| 2 | `03_methodik.tex:246–252` | **Richtig.** Die Vereinfachung erhält Dokumentart, Adressaten und historischen Beleg. `CLAUDE.md` im Stand vom 14.08.2026 nennt tatsächlich das Modellwerkzeug und menschliche Mitwirkende. |
| 3 | `04_analyse.tex:17–23` | **Richtig.** RFC, Z. 126–129, erklärt die Markierung. Die eigene Nachzählung bestätigt 103 markierte Absätze. Die neue Quellenangabe ergänzt den passenden Beleg. |
| 4 | `04_analyse.tex:47–75` | **Richtig.** Die Shim-Regel entspricht RFC, Z. 353–366; `src/wire/ip.rs:70–71` begrenzt den Parser auf Protocol 17. Nachgezählt: 49 FR, zwölf NFR, 67 CSV-Datensätze. CSV-Z. 9 enthält beide Bewertungsspalten; das neue Verweisziel `06_evaluation.tex:876–904` erklärt deren Unterschied. Die verlinkte CSV im Stand vom 03.09.2026 ist mit der lokalen Datei identisch. |
| 5 | `04_analyse.tex:81` | **Richtig.** Die Beschriftung bezeichnet weiterhin den Arbeitsindex. Sie verwechselt ihn nicht mit der eigenen Einzelzuordnung. |
| 6 | `04_analyse.tex:105–107` | **Richtig.** Die NOP-Empfehlungen stehen in RFC, Z. 863–871; die bedingte Ressourcenempfehlung steht in Z. 2125–2131. Bedingung und Empfehlungsstärke bleiben erhalten. |
| 7 | `04_analyse.tex:115–121` | **Richtig.** Die Definition der technischen Nichterfüllbarkeit ändert sich nicht. Sie passt zur Trennung von Erfüllbarkeit und Implementierungsstand in K3 und K6. |
| 8 | `04_analyse.tex:138–158` | **Richtig.** „Oder“ entspricht der Pilotdefinition in `06_evaluation.tex:32–40`. „Verwerfungen im Empfänger“ bleibt im vorsichtigen Satz „helfen … zu unterscheiden“ korrekt; die folgende Begrenzung des Attributionsintervalls bleibt bestehen. Die Trennhilfen verändern keine Aussage. |
| 9 | `04_analyse.tex:163–167` | **Richtig.** `06_evaluation.tex:698–702` leitet die Mechanismenklassen ebenfalls aus Vorversuchen und Messungen ab. Nichtverallgemeinerung und Grenzen der Zuordnung stehen weiterhin unmittelbar davor in K4:151–164. |
| 10 | `04_analyse.tex:183` | **Richtig.** „Umsetzung im Kernel“ bezeichnet denselben ausgeschlossenen Ausführungsort. `src/lib.rs:22–27` bestätigt diese Umfangsgrenze. |
| 11 | `04_analyse.tex:204–221` | **Richtig.** Die IPv6-Streichung beseitigt die nicht eingelöste Vergleichsankündigung. Unter „Rolle in der Messung“ beschreibt „die Bibliothek läuft dort nicht“ den tatsächlichen macOS-Messbetrieb, keine allgemeine Portabilitätsgarantie. RFC, Z. 272–284, trägt Anwendung, Schicht oder Bibliothek sowie die einzige begrenzte Zustandsausnahme. Der gestrichene Wiederverwendungssatz war richtig, aber für die Begründung entbehrlich. |
| 12 | `04_analyse.tex:236–251` | **Richtig.** „Systemschnittstellen“ erhält die Bedeutung; der gestrichene Kontrollsatz wiederholte den vorherigen Absatz. Die historischen Bezugsmengen der Sicherheitszahlen bleiben korrekt. Belege: [MSRC](https://www.microsoft.com/en-us/msrc/blog/2019/07/a-proactive-approach-to-more-secure-code/), [Chromium](https://www.chromium.org/Home/chromium-security/memory-safety/). |
| 13 | `04_analyse.tex:262–296` | **Richtig.** Rusts Garantie bleibt durch die Sicherheitsbedingungen für `unsafe` begrenzt; [Rust](https://doc.rust-lang.org/book/ch20-01-unsafe-rust.html) und [Zig 0.16](https://ziglang.org/documentation/0.16.0/#Lifetime-and-Ownership) tragen den Vergleich. Genau zwei Blöcke mit Sicherheitskommentaren stehen in `socket/send.rs:129–139` und `socket/recv.rs:168–169`. K5:87–90 nennt ihre Lage; `fig:stepzyklus` enthält in K3:284–286 tatsächlich die Property-/Fuzz-Vorgabe. Das Bun-Beispiel bleibt in K3:50–53 erhalten. |
| 14 | `04_analyse.tex:305–315` | **Richtig.** „Im Gegenzug“ macht die eigene Validierungsarbeit als Folge der Zugangswahl deutlich. `recv/pipeline.rs:211–275` und `wire/ip.rs:37–75` belegen die Prüfungen. Die MTU-Grenze bei `IP_HDRINCL` bestätigt [raw(7)](https://man7.org/linux/man-pages/man7/raw.7.html). |
| 15 | `04_analyse.tex:320–346` | **Richtig.** „UDP-Optionen“ bezeichnet die fehlende Dekodierung genauer. `eval-check.py:233–250` rechnet OCS nach; sein Einsatz am 10.08. ist archiviert. P0/P1/P2 lesen `ocs_reports` aus Empfängerausgaben. Gemeinsame Testmodule sind etwa durch `fuzz_targets/wire_datagram.rs:17` und `tests/properties_wire.rs:177–187` belegt. „Können … unentdeckt bleiben“ erhält die notwendige Aussagegrenze. |
| 16 | `06_evaluation.tex:54` | **Richtig.** „IPv4, Tunnel“ entspricht dem jetzt dargestellten Untersuchungsumfang. Die archivierten IPv6-Vorversuche müssen deshalb nicht gelöscht oder als ausgewertete Ergebnisreihe angekündigt werden. |
| 17 | `06_evaluation.tex:91` | **Richtig.** Die neue Bezeichnung erhält die Zuordnung der Commit-Kennungen zum Repository der Implementierung. |
| 18 | `06_evaluation.tex:109–119` | **Richtig.** Die Repository-Bezeichnung bleibt eindeutig. Die tcpdump-Ergänzung passt zu den folgenden Betriebsregeln; die OCS-Abhängigkeit entspricht K4 und den drei Auswertern. |
| 19 | `06_evaluation.tex:134–137` | **Richtig.** Nur die Repository-Bezeichnung ändert sich. Treiber, Zellplan und Auswerter bleiben eindeutig benannt und vorhanden. |
| 20 | `06_evaluation.tex:835` | **Richtig.** „Arbeitsindex der Implementierung“ erhält die ausdrücklich folgende Abgrenzung vom vollständigen Verzeichnis aller RFC-Pflichten. |
| 21 | `06_evaluation.tex:856` | **Richtig.** Die Tabelle summiert die eigenen CSV-Bewertungen. Die neue Beschriftung passt zu K6:850–851 und den CSV-Spalten `kategorie` und `technisch`. |
| 22 | `06_evaluation.tex:999` | **Richtig.** Die sprachliche Änderung erhält die Zuordnung der beiden unveränderten Commit-Belege. |
| 23 | `06_evaluation.tex:1096–1099` | **Richtig.** Die unterschiedlichen Ablageorte von Implementierungsbelegen und Befundregister bleiben klar getrennt. |
| 24 | `06_evaluation.tex:1137` | **Richtig.** „Außerhalb des Repositorys“ bezeichnet denselben Ort und ist grammatisch korrekt. |
| 25 | `literatur.bib:225–237` | **Richtig.** Die [NSA-PDF](https://media.defense.gov/2022/Nov/10/2003112742/-1/-1/0/CSI_SOFTWARE_MEMORY_SAFETY.PDF) trägt April 2023, Version 1.1; die [Erstveröffentlichung](https://www.nsa.gov/Press-Room/News-Highlights/Article/Article/3215760/nsa-releases-guidance-on-how-to-protect-against-software-memory-safety-issues/) erfolgte am 10.11.2022. `microsoft-memory` wird nirgends mehr zitiert; seine Entfernung lässt keinen Beleg fehlen. |
| 26 | `literatur.bib:248–255` | **Richtig.** Der Kopf der [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) nennt ausdrücklich den 14. Juni 2026. |
| 27 | `literatur.bib:283–285` | **Richtig.** Der entfernte Schlüssel `kernel-devtools` wird in keiner aktuellen Thesis-`.tex`-Datei verwendet. |
| 28 | `literatur.bib:424–431` | **Richtig.** Der [Bun-Beitrag](https://bun.com/blog/bun-in-rust) nennt Jarred Sumner und den 8. Juli 2026. K3 verwendet die Quelle weiterhin. |
| 29 | `01_einleitung.tex:151–153` | **Richtig.** Der neue Satz passt zu K4 und K6 und entfernt den Verweis auf einen gestrichenen Vergleich. Die verbleibenden IPv6-Erwähnungen grenzen den Umfang ab oder gehören zum Ausblick in K7. |

Bei der Neubewertung widerspreche ich folgenden Bewertungen ausdrücklich:

- **A18 war sachlich falsch:** Die C++-Quelle ist datiert. Die aktuelle Umsetzung korrigiert diesen Workflowfehler.
- **S1-F1 und O1-B18 wurden zu Recht abgelehnt:** Im Archiv `external-campaign-20260810T200118Z.tar.zst` dokumentieren
  die vier Dateien `logs/hetzner-eval/02-eval-veth.meta` bis `05-eval-filter.meta` erfolgreiche Auswertungen.
  `matrix/analyze-pcap-pair.py:55–66,131–136` verwendet die OCS-Prüfung für Sender und Empfänger. Eine pauschale
  Beschränkung auf gescheiterte Aufrufe oder die Senderseite wäre falsch.
- **A2, A3, A7 und A14 belegen nicht durchgehend Sachfehler des Codex-Stands.** Teilweise handelt es sich um
  Verdeutlichungen. Insbesondere widerspricht die Nutzung von Vorversuchen als Hypothesenquelle keiner begrenzten
  Aussagekraft dieser Vorversuche.

Die Nichtumsetzung der zusätzlichen Beweiskrafterklärung aus **A8**, des Entkapselungszusatzes aus **A25** und der
ausführlicheren Fassungen von **A7/A9** ist vertretbar: Die benötigten Informationen stehen weiterhin im Text oder am
Verweisziel. Ebenso vertretbar sind die Ablehnungen **O2-08**, **O2-16**, **B13/O2-12** und **B15**: Sie begründen
keinen nachgewiesenen Widerspruch oder fehlenden Nachweis in Kapitel 4. **A28** betrifft eine vorbestehende Zeile in
`AGENTS.md`; die gestrichenen Tabellenkriterien zum Sprachreifegrad sind keine notwendige Voraussetzung der nun
begründeten Sprachwahl.

3. **Außerhalb des Diffs bleibt ein abgaberelevanter Begründungsfehler in Kapitel 6:** `06_evaluation.tex:971–973`,
CSV-Z. 74 und `thesis/tikz/gen/ff1-kategorien.py:21–22,187–189` binden das SHOULD aus Abschnitt 25.2 an die Nutzung
des vorherigen MAY. RFC, Z. 2113–2116, bindet es tatsächlich an Bedenken wegen verdeckter Kanäle. Auch die spätere
Aussage im Workflowbericht, ohne neu aufgenommenes Schutzziel bleibe die Nichtanwendbarkeit bestehen, ist durch keine
ausdrückliche Umfangsentscheidung belegt.

Vollständiger sachlich belegbarer Ersatz für die K6-Passage von „Zeile 226 betrifft …“ bis „… empfangsseitige Ordnung.“:

```latex
Zeile~226 betrifft die bedingte Empfehlung zur empfangsseitigen Referenzordnung
aus Abschnitt~25.2. Sie gilt für Implementierungen mit Bedenken wegen verdeckter Kanäle:
Diese sollen Optionen unabhängig von ihrer Reihenfolge im empfangenen Paket ausgeben
\cite[Sec.~25.2]{rfc9868}. Die Nichtwahl des dort genannten \texttt{MAY} hebt diese
Empfehlung nicht auf. Die kanonische Sendereihenfolge erfüllt sie ebenfalls nicht.
Die Einstufung als nicht anwendbar ist damit noch nicht begründet; die zugehörigen Summen
bleiben bis zur Klärung der Anwendbarkeit vorläufig.
```

Dieser Ersatz berichtigt die Normauslegung und legt die verbleibende Grenze offen. Eine endgültige Kategorie samt
geänderten Summen lässt sich aus den vorhandenen Belegen nicht bestimmen; CSV und Generator müssen dieselbe begründete
Entscheidung abbilden.

Die zusätzliche vollständige Sprachprüfung von Kapitel 4 ergibt folgende einfachere Formulierungen. Sie sind **keine
Freigabeauflagen**; eingeführte Fachbegriffe und normale technische Zusammensetzungen bleiben unbeanstandet.

| Stelle | Vorhandene Wendung | Einfacherer Ersatz |
|---|---|---|
| K4:19–20 | „Extrahiert wird satzgenau und nicht absatzweise“ | „Die Auswertung erfasst Aussagen Satz für Satz statt Absatz für Absatz“ |
| K4:21–22 | „Jede extrahierte Aussage“ | „Jede erfasste Aussage“ |
| K4:135 | „mit unterschiedlicher externer Netzbeteiligung“ | „mit unterschiedlicher Beteiligung fremder Netze“ |
| K4:187 | „generische Empfangsregeln“ | „allgemeine Empfangsregeln“ |
| K4:207 | „die Bibliothek läuft dort nicht“ | „die Bibliothek wird dort nicht eingesetzt“ |
| K4:231–232 | „Viertens soll die Bibliothek ohne obligatorische verwaltete Laufzeitumgebung und ohne automatische Speicherbereinigung (Garbage Collector) auskommen.“ | „Viertens soll die Bibliothek keine verwaltete Laufzeitumgebung voraussetzen und ohne automatische Speicherbereinigung (Garbage Collector) auskommen.“ |
| K4:263 | `\texttt{unsafe} vertragsabhängig` | `bei \texttt{unsafe} nur mit erfüllten Sicherheitsbedingungen` |
| K4:287 | „kapseln die Systemgrenzen“ | „stehen an den Schnittstellen zum Betriebssystem“ |
| K4:289–290 | „weil die Mechanik von RFC~9868 selbst Untersuchungsgegenstand ist“ | „weil diese Arbeit die Mechanik von RFC~9868 selbst untersucht“ |

Die macOS-Formulierung verdient dabei die Klarstellung des **Einsatzes**: Die reinen Bibliotheksmodule sind portabel;
nur der Raw-Socket-Betrieb ist Linux-spezifisch (`README.md:52–53`, `src/lib.rs:13–20`). Im bestehenden
Tabellenkontext entsteht daraus jedoch kein fachlicher Fehler. „Verwerfungen im Empfänger“ bleibt angemessen
vorsichtig; „aus der Empfängerausgabe“ benennt die tatsächliche Datenquelle sogar genauer.

4. Die vorhandene [PDF](</Users/ab/Library/Mobile
Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/main.pdf>) habe ich für Kapitel 4
vollständig auf den physischen Seiten 42 bis 49 visuell und anhand der tatsächlichen Zeilenumbrüche geprüft,
einschließlich Tabellen, Beschriftungen und Fußnoten. Keine fehlerhafte deutsche Trennung, Überlagerung oder
abgeschnittene Darstellung festgestellt. Alle geänderten Quelldateien halten 120 Zeichen ein; Quellen- und
Querverweise lösen auf. Die vorhandenen Build-Protokolle enthalten keine einschlägigen Warnungen.

**Nicht ausgeführt:** Neubau, Tests, Fuzzing, Lean-Beweise, Messkampagnen oder eine vollständige erneute Prüfung aller
Archivdateien und 67 Einzelbewertungen. Die übrigen Kapitel wurden an den betroffenen Aussagen und Verweiszielen
geprüft, nicht vollständig neu freigegeben. Die SHA-Angaben am Ende des Workflowberichts sind für K3, K4, K6 und PDF
veraltet; maßgeblich war der live geprüfte, patchidentische Stand. Keine Datei wurde angelegt oder geändert.


