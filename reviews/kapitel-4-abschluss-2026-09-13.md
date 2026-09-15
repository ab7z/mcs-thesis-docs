# Kapitel 4: Umsetzung und Abschlussprüfung vom 13. September 2026

## Urteil und geprüfter Stand

Kapitel 4 ist nach Umsetzung der bestätigten Befunde im hier dokumentierten Prüfumfang freigabefähig.
Die Freigabe betrifft den aktuellen Arbeitsstand auf Basis des Stands vom 10.09.2026, nicht den unveränderten
Commit allein. Sie ist keine Freigabe der gesamten Thesis oder aller 67 externen Einzelbewertungen.
Es bestehen keine offenen abgaberelevanten Befunde am geprüften Kapitel-4-Text.
Eine Begründungslücke in der Bewertung einer Kapitel-6-Matrixzeile bleibt gesondert offen (unten).

Thesis-Text und PDF wurden tatsächlich geändert; dies ist kein weiterer Bericht mit bloßen Vorschlägen.
Nicht committet und nicht gepusht. Die schon vorhandene Änderung an `AGENTS.md` blieb unverändert.
Die Implementierung unter `../udp-transport-options` wurde nicht geändert.

Dieser Bericht ersetzt die vorläufige Freigabebewertung des Erstberichts und dessen ersten Nachtrag.
Der ursprüngliche [Erstbericht](kapitel-4-vollpruefung-2026-09-12.md) und die unverändert gesicherte
[Claude-Zweitmeinung](kapitel-4-zweitmeinung-2026-09-13.md) bleiben als Prüfhistorie erhalten.

## Was geändert wurde

- Abschnitt 4.1: unmarkierte RFC-Längenregel und eigene Shim-Umfangsgrenze klar getrennt.
- Abschnitt 4.2: 67-zeiligen RFC-Arbeitsindex und eigene geprüfte Einzelzuordnung eindeutig eingeführt;
  Fußnote mit Dateipfad, Thesis-Repositorium und passendem veröffentlichtem Stand vom 03.09.2026.
  UEXP als Experimentoption präzisiert; Bewertungs- und Sonderklassen verständlicher erklärt.
- Abschnitt 4.3: Auswertung nach vorhandener Evidenz, zusätzliche Messpunkte und deren Aussagegrenzen;
  keine pauschale Behauptung genau zweier Mitschnitte. IPv6-Kontrollen auf dieselbe Versuchsanordnung
  bezogen, nicht auf einen angeblich identischen IPv4-/IPv6-Netzpfad.
- Abschnitt 4.4: Sprachwahl, Bedingungen, Rust-Mittel und Prüfablauf in kürzeren Sätzen erklärt.
  Die unklaren Tabellenzeilen „Schutzmechanismus“ und „Sprachfassung“ entfernt; verbleibende Angaben
  präzisiert und belegt. Speicherlecks bleiben ausdrücklich auch in Rust möglich.
- Werkzeugrollen: `wire-check.py` und `eval-check.py` rechnen OCS selbst nach. P0/P1/P2-Auswerter
  übernehmen dagegen OCS-Berichte aus der Empfängerimplementierung. Keine pauschale Zusage eines
  vollständigen Surplus-Bytevergleichs oder einer überall ausgeführten tshark-Gegenprüfung.
- Quellen: MSRC-Aussage direkt am Blog belegt, Bun-Bezug auf Speicherverwaltung begrenzt,
  NSA-Ausgabe auf April 2023/Version 1.1 korrigiert; N2310 zutreffend als C2x-Arbeitsentwurf bezeichnet.
  C++ Core Guidelines als Beleg für die Speicherverwaltung ergänzt.
- Notwendige Folgeänderungen in Kapitel 3 und 6: unterschiedliche Auswerter, konsistente
  Dateibezeichnungen, UEXP und zusätzliche en0-Mitschnitte.
- Layout: Sprachtabelle unterbricht den folgenden Absatz nicht mehr; die lange erste Fußnote
  erhält lokalen Flattersatz. Falsche Trennungen gezielt durch `Options\-struktur`,
  `Empfänger\-ausgabe` und `Start\-offset` verhindert. Keine globalen Warnungen unterdrückt.

## Was die vertiefte Gegenprüfung zusätzlich geklärt hat

Drei getrennte Teilprüfungen betrafen Norm/Matrix, Code/Messbelege sowie Sprache/Prozess/Quellen.
Die Ergebnisse wurden gegen Primärtext, Code und Artefakte abgeglichen. Anschließend wurden die
umgesetzten Diffs erneut geprüft. Die abschließende Silbentrennungsprüfung und die visuellen Kontrollen
sind vom vorherigen Quellenreview getrennt dokumentiert.

- Claudes F1 ist in seinem Kern bestätigt, aber auch sein Ersatztext war zu pauschal:
  P0/P1 vergleichen nicht die vollständigen Surplus-Bytes. P2 hat eigene Prüfungen von FRAG-Feldern
  und einer Legacy-Prüfsummenfaltung, aber keine unabhängige OCS-Nachrechnung.
- `docs/evaluation.md:28-33` beschreibt `eval-check.py` nicht mehr zutreffend. Die unabhängige
  OCS-Rechnung steht in dessen Code (`_validate_surplus`, Zeilen 234 bis 251) und bereits im
  historischen Messstand vom 10.08.2026. Diese Dokumentationsstelle trägt den ersten Nachtrag nicht.
- Im Archiv vom 10.08. gibt es tshark-Feldexporte auch außerhalb der Wire-Prüfung:
  `captures/port-matrix-capture/controller-script.sh` sowie `sender-fields.csv`/`receiver-fields.csv`.
  `matrix/analyze-pcap-pair.py` verwendet die unabhängige OCS-Prüfung aus `eval-check.py`.
  Daher kein allgemeiner Ausschluss solcher Prüfungen aus Kampagnen.
- en0-Mitschnitte liegen auch in Piloten vom 12./13.08. vor. Die K6-Abbildung beschränkt sie deshalb
  nicht mehr ausschließlich auf den 10./11.08.
- Claudes V3 „Prüfer nirgends eingeführt“ ist nicht bestätigt: Kapitel 3.4.1 erklärt das getrennte
  Python-Programm bereits. Geändert wurde die zu pauschale Behauptung seiner Wiederverwendung.
- Der ursprüngliche F02 ist kein belegter historischer Ausführungsfehler. In den Ständen
  vom 20.06., 21.06., 29.06., 05.07. (drei Schritte) und 02.08.2026 finden sich die
  jeweiligen Property-Module sowie neue oder erweiterte Fuzz-Ziele. Der Text beschreibt die
  eingeführte Regel jetzt präziser. Die 23 Tests und der falsch berechnete Startoffset bleiben belegt.
- UEXP ist laut RFC 12.3 tatsächlich für Experimente reserviert; die neue Formulierung verdeutlicht
  den Unterschied zu UCMP/UENC. Die alten Sammelworte waren kein eindeutiger Normwiderspruch.
- Fehlende BCP-14-Schlüsselwörter allein begründen keine Nichtanwendbarkeit. Die Sonderklasse wurde
  entsprechend nicht um ein solches falsches Ausschlusskriterium erweitert.

## Quellen und Nachweise

Normative Grundlage ist `literature/rfc9868.txt`, insbesondere Abschnitte 6 bis 12, 15, 18 und 25.2,
zusammen mit RFC 2119/8174. Implementierungsstand: 03.09.2026.
Codebelege betreffen `scripts/wire-check.py`, `wire-check.sh`, `eval-check.py`, `p0-eval.py`,
`p1-eval.py`, `p2-eval.py`, `src/wire/ip.rs`, `src/options/parse.rs` und die dokumentierte Historie.
Die drei für den vertieften Messabgleich benutzten Archive wurden gegen ihre SHA-256-Sollwerte geprüft:
`external-campaign-20260810T200118Z.tar.zst`, `bidir-campaign-20260811.tar.zst` und
`piloten-und-nachtraege-20260810-15.tar.zst`. Keine neue Kampagne wurde gestartet.

Die geänderten externen Quellen sind in `thesis/literatur.bib` konkret belegt:
`msrc-memory-blog` (MSRC/Gavin Thomas, 16.07.2019), `nsa-memory-safety` (April 2023, Version 1.1),
`iso-c` (WG14 N2310, 06.11.2018), `cpp-core-guidelines` (Regel R.1), `bun-in-rust` und `zig-lang`.
Linux v5.10 `net/ipv4/udp.c` trägt Sende- und Empfangsaussage zum gewöhnlichen UDP-Socket;
RFC 18 wird nicht mehr als alleiniger Sendebeleg angegeben.

## 24 Kriterien am abschließend geprüften Kapitelstand

„Geprüft“ bezieht sich auf den Umfang dieses Kapitelreviews. Die Matrix ist kein Ersatz für eine
vollständige neue Konformitätsbewertung sämtlicher Implementierungsfälle.

| Nr. | Kriterium | Status | Ergebnis |
|---|---|---|---|
| 1 | Fachliche Richtigkeit | geprüft | Norm, Code und Aussagegrenzen abgeglichen. |
| 2 | Quellen und Belege | geprüft | Zuschreibungen und verlinkte Ausgaben korrigiert. |
| 3 | Verbindlichkeit | geprüft | Normstufen und bedingte Regeln erhalten. |
| 4 | Persönlicher Schreibstil | geprüft | Konkrete Sätze; unnötige Begriffe reduziert. |
| 5 | Einzelne Sätze | geprüft | Geänderte Sätze und vollständiger Kapiteltext gelesen. |
| 6 | Zweck und Ursache | geprüft | Werkzeugrollen und Entscheidungsgründe erklärt. |
| 7 | Zusammenhang | geprüft | Nachbarsätze und erforderliche Folgeänderungen geprüft. |
| 8 | Relevanz und Wiederholungen | geprüft | Unklare Vergleichszeilen entfernt; nötige Grenzen erhalten. |
| 9 | Begriffe | geprüft | Arbeitsindex und Einzelzuordnung eindeutig getrennt. |
| 10 | Fußnoten | geprüft | Beide in Text und aktueller PDF geprüft. |
| 11 | Ziel und Umfang | geprüft | Linux, IPv4, Raw Sockets und Optionsumfang erhalten. |
| 12 | Ergebniszuordnung | geprüft | Empfängermeldung und unabhängige Nachrechnung getrennt. |
| 13 | IPv4, MTU und Fragmentierung | geprüft | Shim-Längenregel und Schnittstellen-MTU präzisiert. |
| 14 | UDP und Prüfsummen | geprüft | OCS- und UDP-Prüfung mit tatsächlichen Rollen abgeglichen. |
| 15 | Surplus Area und Optionen | geprüft | Tabellenauszug, UEXP und FRAG-Ausnahme geprüft. |
| 16 | Betriebssystem und Netzpfad | geprüft | Linux-Socket-Zugang und Alternativen korrekt eingegrenzt. |
| 17 | Messbedingungen | geprüft | Zusatzmitschnitte und unterschiedliche Messstufen erhalten. |
| 18 | Methodik | geprüft | Kapitel-4-Maßstab geprüft; externe Einzelurteile nicht alle neu bewertet. |
| 19 | Aussagekraft der Nachweise | geprüft | Modell, Tests, Empfängermeldung und Messbeleg getrennt. |
| 20 | Entwicklungs- und Prüfablauf | geprüft | Regel, historische Nachweise und Audit korrekt beschrieben. |
| 21 | Abbildungen, Tabellen, Verweise | geprüft | Vier Tabellen, Abbildung und 24 Verweisziele geprüft. |
| 22 | PDF-Lesbarkeit | geprüft | Acht Kapitelseiten, Übergänge und Folgeänderungen geprüft. |
| 23 | Silbentrennung | geprüft | 35 aktuelle Blockzeilenenden; keine falsche Trennung. |
| 24 | Abschlusskontrolle | geprüft | Vollbau, Literatur, Glossar, Diff und PDF geprüft. |

## Build, PDF und Silbentrennung

Der letzte vollständige Bau führte `pdflatex`, `biber`, `makeglossaries` sowie zwei weitere
`pdflatex`-Läufe aus. Alle fünf Kommandos endeten mit Exitcode 0. Im letzten LaTeX- und Biber-Protokoll
stehen keine Warnungen, undefinierten Verweise sowie Overfull-/Underfull-Meldungen. Das leere
separate Glossar wird von makeglossaries erwartungsgemäß gemeldet; das Abkürzungsverzeichnis wurde gebaut.

Die PDF hat 95 Seiten. Kapitel 4 belegt unverändert die physischen Seiten 42 bis 49
(Druckseiten 36 bis 43). Alle acht Seiten wurden gerendert und vollständig visuell geprüft.
Zusätzlich: Übergänge auf 41/50, Folgeänderungen auf 39/64/73/79/80/82/85 und Literatur auf 93/94.
Die en0-Anmerkung in Abbildung 6.6 passt ohne Überlagerung. Die Sprachtabelle unterbricht keinen Absatz.

Unabhängige Nachprüfung der Kapitel-4-Trennungen: 35 Blockzeilenenden, davon 29 Worttrennungen und
sechs reguläre Binde-/Ergänzungsstriche. Vier Worttrennungen stehen in Tabellenzellen.
Beide Fußnoten und Seitenübergänge wurden einbezogen. Die richtige Trennung lautet jetzt
`Empfänger- / ausgabe` und `Start- / offset`; `Optionsstruktur` bleibt im letzten Umbruch ungetrennt.
Auch die geänderten Absätze außerhalb von Kapitel 4 wurden auf ihre tatsächlichen Umbrüche geprüft.

Alle 24 unterschiedlichen Kapitel-4-Verweisziele und alle 18 zitierten Literaturkennungen sind vorhanden.
`git diff --check` ist sauber. Die Änderung führte keinen Implementierungscode und keine Messdatenänderung ein.
Keine neue Rust-Testserie, kein neuer Lean-Gesamtbau und keine neue Messung wurden ausgeführt.

## Gesonderter offener Prüfpunkt für Kapitel 6

CSV-Zeile mit Kennung 226 wird als nicht anwendbar bewertet. Ihre derzeitige Begründung bindet das
SHOULD zur Ausgabe empfangener Optionen an die Nichtwahl des vorhergehenden MAY. RFC 9868, Abschnitt
25.2, adressiert jedoch Implementierungen mit Bedenken wegen verdeckter Kanäle; er knüpft das SHOULD
nicht ausdrücklich an die tatsächliche Ausübung des MAY. Die Nichtwahl allein reicht daher als
Begründung nicht aus.

Eine Nichtanwendbarkeit könnte durch das konkrete Schutzziel begründet sein. Dafür wurde bei dieser
Prüfung keine eindeutige Umfangsfestlegung gefunden. Die kanonische Sendereihenfolge ersetzt keine
unabhängige Reihenfolge bei der Empfangsausgabe. Es ist eine belegte Begründungslücke, noch kein
hinreichender Nachweis für eine andere Endkategorie. Bei der vollständigen K6-Prüfung ist das Schutzziel
zu klären und erst danach über Kategorie und Summen zu entscheiden. CSV und Summen wurden nicht verändert.
Der Punkt steht auch in `thesis/insights-inbox.md` für Kapitel 6.

## Identifikation des ausgelieferten Standes

- `thesis/chapters/03_methodik.tex`
  SHA-256: `0f08a9f0959650843d932803e545db4bf6f1c0be1e34270b40f20f35b285a1e7`
- `thesis/chapters/04_analyse.tex`
  SHA-256: `1ee4615ec2520faf438dcf2677f46f9731b5a0c38f24636d43279594fd68e903`
- `thesis/chapters/06_evaluation.tex`
  SHA-256: `f02aeccd0b85967f697a58cdca91d570a275e5ae400f090bea6957bcf0269594`
- `thesis/literatur.bib`
  SHA-256: `cf22550783ecaaa5407b30c929274f6a1338ba9df4f0f0c42e50a99dcb2fa4c1`
- `thesis/main.pdf`
  SHA-256: `d3d04e3e3173355d7b55c0950faf5aaedeefc888d65bd69620e1974017809666`

Temporäre Prüfartefakte: `/var/folders/sx/6w30525112jgcghk1y5gp1840000gn/T/udp-k4-final-hxk5v9gn`. Die dauerhaften Belege sind die benannten Quellen und dieser Bericht.
