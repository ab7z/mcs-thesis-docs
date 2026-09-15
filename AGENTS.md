# AGENTS.md

This file provides guidance to Codex (Codex.ai/code) when working with code in this repository.

## Project Overview

Master's thesis at FernUniversität in Hagen (LG Kooperative Systeme)

Title: **UDP Transport Options**
Subtitle: _Implementierung und Analyse von RFC 9868 in Rust_

The thesis involves implementing RFC 9868 (Transport Options for UDP, published October 2025) in Rust.

Stand 2026-08-26: Kapitel 1 bis 7 sind geschrieben. `thesis/insights-inbox.md` ist gegen diesen
Textstand abgeglichen. Der RFC-Lernmodus in `lernnotizen/` ist ein paralleler Bildungsprozess und
kein Schreibtor mehr.

## Build Commands

LaTeX compilation (when thesis files are present):

```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

## Key Technical Context

- **RFC 9868** extends UDP with options placed in the "surplus area" between UDP payload end and IP datagram end
- **Core UDP Options**: OCS (Options Checksum), FRAG (Fragmentation), TIME (Timestamps), AUTH (Authentication)
- **Implementation stack**: Rust for implementation

## Language

Thesis and documentation are written in German.

### Writing style for the thesis

- Avoid anglicisms when a common German technical term exists (e.g., do not write
  „untrusteter"; prefer „eingehender" or „potentiell bösartiger"). Established Rust
  and networking terms kept in English are fine (`Ownership`, `Borrow Checker`,
  `Buffer Overflow`, `Data Race`, `Memory Safety`).
- Do not use em-dashes or en-dashes (`--`, `---` in LaTeX, or the literal `—`/`–`
  characters). Prefer parentheses, a colon, or a comma. ASCII art inside `verbatim`
  blocks is exempt.

### Silbentrennung (verbindlich)

- Bei jeder Prüfung und Überarbeitung der Thesis zusätzlich die deutsche Silbentrennung prüfen.
  Maßgeblich sind die tatsächlichen Zeilen- und Seitenumbrüche in der aktuellen PDF, einschließlich
  Fußnoten, Tabellen und Abbildungsbeschriftungen, nicht allein der LaTeX-Quelltext.
- Besonders bei zusammengesetzten Fachwörtern die Wortbestandteile erhalten: korrekt sind etwa
  `Prüfsummen- / arithmetik` und `Einerkomplement- / arithmetik`; falsch sind
  `Prüfsumme- / narithmetik` und `Einerkomplemen- / tarithmetik`.
- Fehlerhafte Trennungen gezielt mit manuellen LaTeX-Trennstellen wie `Prüfsummen\-arithmetik`
  korrigieren. Korrekte Trennungen sowie reguläre Binde- und Ergänzungsstriche beibehalten.
- Nach Textkorrekturen die gesamte Thesis neu bauen und die betroffenen Umbrüche erneut in der PDF
  prüfen. Auch neu entstandene Trennungen kontrollieren, bevor die Überarbeitung als abgeschlossen gilt.

## Kapitelprüfung und Freigabe (verbindlich)

Diese Prüfkriterien wurden aus der gemeinsamen Durchsicht von Kapitel 1 bis 3 abgeleitet und am
12. September 2026 von GreenCodeDoesntSmell zur Verwendung für weitere Kapitel bestätigt. Kriterium 25 kam am
13. September 2026 auf Anweisung von GreenCodeDoesntSmell hinzu.
Sie sind bei weiteren Kapitelprüfungen anzuwenden. Bei gezielten Überarbeitungen den beauftragten Umfang
einhalten und betroffene Kriterien prüfen; daraus keine vollständige Kapitelprüfung ableiten.

### Prüfkriterien

1. **Fachliche Richtigkeit:** Definitionen, Erklärungen, Voraussetzungen, Regeln und Ausnahmen gegen
   Primärquellen prüfen. Zu pauschale Aussagen einschränken; richtige Aussagen als richtig anerkennen.
2. **Quellen und Belege:** Prüfen, ob die Quelle die konkrete Aussage trägt und RFC, Abschnitt, Datum und
   Zuschreibung stimmen. Endgültige Standards, frühere Entwürfe und ältere Untersuchungen unterscheiden.
3. **Verbindlichkeit:** Anforderungen, Empfehlungen und Möglichkeiten sowie MUST, SHOULD und MAY sauber
   unterscheiden. Beim Vereinfachen Bedingungen, Ausnahmen und die Stärke einer Aussage erhalten.
4. **Persönlicher Schreibstil:** Kurz, konkret und verständlich schreiben. Die Rückfragen aus der
   gemeinsamen Durchsicht als Maßstab nutzen; abstrakte Begriffe, unnötige Anglizismen und Metaphern vermeiden.
5. **Einzelne Sätze:** Satz für Satz auf Grammatik, klare Handelnde, eindeutige Bezüge und lesbare Satzlänge
   prüfen. Fußnoten, Definitionen und Beschriftungen einbeziehen, nicht nur den Fließtext.
6. **Zweck und Ursache:** Neben der Definition erklären, wofür etwas gebraucht wird, wer es verwendet und
   warum eine Handlung erfolgt. Bedeutung, Zweck und mögliche Entscheidungsgründe nicht vermischen.
7. **Zusammenhang:** Änderungen mit den vorherigen und nachfolgenden Sätzen sowie dem gesamten Absatz lesen.
   Erklärungslücken, unklare Übergänge und Widersprüche zwischen einzeln richtigen Sätzen vermeiden.
8. **Relevanz und Wiederholungen:** Den Beitrag jedes Absatzes zum Verständnis der Arbeit prüfen.
   Unnötige Vergleiche, Vorbemerkungen und Wiederholungen streichen; benötigte Erklärungen erhalten.
9. **Begriffe:** Fachbegriffe verständlich einführen und durchgängig verwenden. Insbesondere Header, Nutzlast,
   Nutzdaten, Altempfänger, Altsystem und optionsfähiger Empfänger sowie FF1/FF2-Kategorien konsistent halten.
10. **Fußnoten:** Eine konkrete Nebenfrage kurz beantworten. Keine unklaren Begriffe oder zusätzlichen
    Nebenfragen einführen; notwendige Erklärungen des Hauptarguments im Fließtext belassen.
11. **Ziel und Umfang:** Motivation, Problemstellung, Forschungsfragen, Untersuchung und angekündigte
    Ergebnisse aufeinander abstimmen. Grenzen wie Linux, IPv4, Raw Sockets und Optionsumfang erhalten.
12. **Ergebniszuordnung:** Fremde Ergebnisse, eigene Messungen und Schlussfolgerungen unterscheiden.
    Fehlende Angaben nicht erfinden; beobachtetes Verhalten nicht mit einem identifizierten Gerät gleichsetzen.
13. **IPv4, MTU und Fragmentierung:** Bei relevanten Aussagen Headerlänge, IHL, Optionen, zusätzliche Header,
    Längengrenzen, Fragmentzuordnung und Verlustfolgen prüfen. Aussagen über NATs und Firewalls qualifizieren.
14. **UDP und Prüfsummen:** Bei relevanten Aussagen Felder, Nullwerte und fehlende UDP-Garantien prüfen.
    IPv4-Headerprüfsumme, UDP-Prüfsumme, Pseudo-Header, Berechnung und NAT-Auswirkungen auseinanderhalten.
15. **Surplus Area und Optionen:** Bei relevanten Aussagen Lage, Längen, Einheiten, Formeln, Rechenbeispiele,
    Byte-Offsets, Ausrichtung, Padding, OCS, TLV, NOP/EOL, unbekannte Optionen und Fehlerfälle prüfen.
    Verwerfen von Optionen, Nutzdaten und Datagrammen unterscheiden; FRAG, UNSAFE und Errata berücksichtigen.
16. **Betriebssystem und Netzpfad:** Zuständigkeiten von Anwendung, UDP, IP, Kernel und Filtern unterscheiden.
    Raw Sockets nicht mit der Umgehung aller vorherigen Prüfungen gleichsetzen. Implementierungsangaben
    gezielt am passenden Code und dessen Stand prüfen; Implementierungscode ist keine normative Quelle.
17. **Messbedingungen:** Aussagen mit tatsächlicher Konfiguration, Messdaten und Paketmitschnitten abgleichen,
    etwa bei MTU oder Shim-Headern. Messpunkt, Pfad, Richtung und Zeitpunkt sowie Beobachtungsgrenzen beachten.
    Fehlende Beobachtung ist kein allgemeiner Ausschluss; eine Prüfung ersetzt keine nicht ausgeführte Messung.
18. **Methodik:** Untersuchungsgegenstand, Verfahren, Bewertung und Nachweise nachvollziehbar zuordnen.
    Normauswertung, Implementierung und Messung sowie die Rollen der Bibliothek für FF1 und FF2 unterscheiden.
    Normative Anforderungen von eigenen Projekt-, Schnittstellen- und Plattformentscheidungen trennen.
    Anwendbarkeit und Bewertungskategorien konsistent mit den Analyse- und Evaluationskapiteln halten.
19. **Aussagekraft der Nachweise:** Modellbeweis und Rust-Code, gemeinsame Fehlerannahmen von Code und Tests,
    Hashwert und inhaltliche Richtigkeit sowie Reproduzierbarkeit und unabhängige Prüfung unterscheiden.
    Einschränkungen der jeweiligen Nachweise auch bei sprachlichen Kürzungen erhalten.
20. **Entwicklungs- und Prüfablauf:** Menschliche Verantwortung, Modellbeteiligung, Reviewrollen und Freigaben
    klar benennen. Geplante und nachweislich ausgeführte Prüfungen unterscheiden; relevante Angaben zu
    Prüfskripten, Cross-Kompilierung, Ausführungsorten und Fuzz-Tests gegen die tatsächlichen Abläufe prüfen.
21. **Abbildungen, Tabellen und Verweise:** Beschriftungen, Zahlen, Begriffe und Abläufe mit dem Text abgleichen.
    Nach Änderungen auch Kapitelankündigungen, Querverweise und Verzeichnisse prüfen. Ein aufgelöster Verweis
    reicht nicht aus, wenn das Ziel den angekündigten Inhalt nicht mehr enthält.
22. **PDF-Lesbarkeit:** Die aktuelle PDF auf Überschriftenabstände, Seitenumbrüche, Fußnoten, Tabellen,
    Abbildungen und abgeschnittene Inhalte prüfen. Erklärungen und zugehörige Darstellungen sinnvoll anordnen.
23. **Silbentrennung:** Die tatsächlichen deutschen Zeilen- und Seitenumbrüche einschließlich Fußnoten,
    Tabellen und Beschriftungen nach den verbindlichen Regeln oben prüfen. Fehler gezielt korrigieren und
    nach dem Neubau auch neu entstandene Trennungen kontrollieren.
24. **Abschlusskontrolle:** Nach Änderungen am Thesis-Text die gesamte Thesis einschließlich Literatur und
    Glossar neu bauen. Build-Warnungen, Referenzen und die aktuelle PDF prüfen. Den Diff auf unbeabsichtigte
    Bedeutungsänderungen kontrollieren; Quellstand und ausgelieferte PDF müssen zusammenpassen.
25. **Versionsangaben:** Keine Commit-Hashes, Kurzkennungen, Branch- oder Tag-Namen in irgendeiner Datei
    des Repositorys dieser Arbeit: nicht im Thesistext, nicht in Fußnoten, Tabellen, Beschriftungen und Links,
    nicht in Datendateien, Generatoren, der Evidenz-README und den Berichten. Stände über Datum, Bezeichnung des
    Laufs oder die abgegebene Fassung benennen; Links auf Repositorys ohne Commit-Bezug setzen.

### Prüfumfang und Freigabe

- Bei einer vollständigen Kapitelprüfung alle Kriterien berücksichtigen. Technische Einzelthemen nur dort
  prüfen, wo sie für das Kapitel relevant sind; keine sachfremden Inhalte ergänzen, um die Liste abzuarbeiten.
- Im Prüfbericht je Kriterium festhalten: geprüft, nicht anwendbar, offen oder nicht geprüft. Den Textstand,
  die verwendeten Belege und den Umfang der PDF-Prüfung nennen. Alte Freigaben nicht ungeprüft übertragen.
- Fachliche Fehler und abgaberelevante Mängel von optionalen sprachlichen Verbesserungen unterscheiden.
  Korrekte, verständliche Passagen beibehalten und keine Befunde erfinden, um Änderungen zu rechtfertigen.
- Eine Freigabe nur auf den tatsächlich geprüften und korrigierten Stand beziehen. Verbleibende Mängel und
  Grenzen ausdrücklich nennen. Sprachprüfung, gezielte Quellenprüfung, vollständige Faktenprüfung,
  PDF-Build und erneute Ausführung von Tests oder Messungen nicht gleichsetzen.
- Vorhandene Test- und Messbelege nachvollziehen. Ganze Testserien oder Messkampagnen nur erneut ausführen,
  wenn eine Änderung, ein Befund oder eine offene Frage dies erfordert.
- Historischer Umfang: Kapitel 3 wurde zuletzt vollständig sprachlich und visuell sowie an einzelnen Stellen
  fachlich geprüft. Das war keine erneute vollständige Prüfung aller Forschungsfälle oder Implementierungstests.
  Die systematische Silbentrennungsprüfung aller drei Kapitel erfolgte in einem zusätzlichen Abschlussdurchgang.

## Insights-Inbox (verbindlich)

- `thesis/insights-inbox.md` ist die Sammelstelle für Erkenntnisse und Edge-Cases aus der
  RFC-9868-Implementierung. Vor jeder Arbeit an den Thesis-Kapiteln diese Datei lesen.
- Die dortigen Punkte sind verbindlich: relevante Insights MÜSSEN in das jeweils genannte Zielkapitel der
  Thesis eingearbeitet werden, nicht nur erwähnt.
- Nach dem Einarbeiten den Punkt in `insights-inbox.md` abhaken (`- [x]`) oder entfernen, damit der
  Inbox-Stand den Thesis-Stand widerspiegelt.

## RFC-9868-Lernmodus (verbindlich)

- Bei der gemeinsamen absatzweisen Lektüre von RFC 9868 vor jeder Antwort die Datei
  `RFC9868_LEARNING_MODE.md` vollständig lesen und befolgen.
- Nach jedem vollständig besprochenen Absatz den Lesefortschritt und neu zurückgestellte Fragen in
  `RFC9868_LEARNING_MODE.md` aktualisieren.
- Wenn Codex den Lernprozess führt, vor dem ersten Lernbeitrag zu jedem neuen RFC-Abschnitt
  GreenCodeDoesntSmell den vollständigen Claude-Prüfauftrag geben und auf das zurückgegebene Ergebnis warten.
  GreenCodeDoesntSmell führt Claude mit `--model sonnet --effort max` als read-only Zweitprüfer aus. Codex ruft
  Claude nur nach einer neuen ausdrücklichen Anweisung selbst auf. Das lokal aufgelöste Modell ist
  `claude-sonnet-5`.
- Bei einem als "Codex-Zweitprüfung" bezeichneten Aufruf read-only arbeiten, keine Dateien verändern und nicht
  erneut Claude aufrufen. Stattdessen den strukturierten Evidenzbericht an den führenden Claude zurückgeben.
- Die Zweitprüfung muss den RFC-Text Satz für Satz auslegen und passende Stellen in
  `../udp-transport-options` schrittweise gegenprüfen. Ablauf und Ablage stehen in
  `RFC9868_LEARNING_MODE.md` und `lernnotizen/abgleich.md`.
- Ergebnisse des Zweitprüfers sind eine Zweitmeinung. Der führende Agent prüft sie selbst gegen Primärtext und
  Repository-Evidenz, benennt Meinungsunterschiede und pflegt den gemeinsamen Fortschritt.
- Der RFC-Primärtext ist maßgeblich. Das Geschwisterprojekt `../udp-transport-options` darf nur vorsichtig als
  Anschauungsmaterial verwendet werden und ist keine normative Quelle.

## Literature

RFC documents stored in `literature/`:

- RFC 675 (Internet Transmission Control Program, 1974): https://www.rfc-editor.org/rfc/rfc675.txt
- RFC 768 (original UDP spec, 1980): https://www.rfc-editor.org/rfc/rfc768.txt
- RFC 791 (Internet Protocol, 1981): https://www.rfc-editor.org/rfc/rfc791.txt
- RFC 1071 (Computing the Internet Checksum, 1988): https://www.rfc-editor.org/rfc/rfc1071.txt
- RFC 4380 (Teredo: Tunneling IPv6 over UDP through NATs, 2006): https://www.rfc-editor.org/rfc/rfc4380.txt
- RFC 6081 (Teredo Extensions, 2011): https://www.rfc-editor.org/rfc/rfc6081.txt
- RFC 7126 (Filtering of IPv4 Packets Containing IPv4 Options, BCP 186, 2014): https://www.rfc-editor.org/rfc/rfc7126.txt
- RFC 8085 (UDP Usage Guidelines, BCP 145, 2017): https://www.rfc-editor.org/rfc/rfc8085.txt
- RFC 8200 (Internet Protocol, Version 6, 2017): https://www.rfc-editor.org/rfc/rfc8200.txt
- RFC 9000 (QUIC Transport, 2021): https://www.rfc-editor.org/rfc/rfc9000.txt
- RFC 9114 (HTTP/3): https://www.rfc-editor.org/rfc/rfc9114.txt
- RFC 9293 (Transmission Control Protocol, 2022, obsoletes RFC 793): https://www.rfc-editor.org/rfc/rfc9293.txt
- RFC 9868 (Transport Options for UDP): https://www.rfc-editor.org/rfc/rfc9868.txt
- RFC 9869 (DPLPMTUD for UDP Options): https://www.rfc-editor.org/rfc/rfc9869.txt

## Workflow Guidelines

- Format the file to keep the line width of 120.
- call me GreenCodeDoesntSmell at EVERY response and answer always in German.
