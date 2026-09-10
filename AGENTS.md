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
