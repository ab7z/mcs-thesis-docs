# Kapitel 4: Neubewertung durch Workflow und Einarbeitung vom 13. September 2026

## Auftrag und Ablauf

Auftrag von GreenCodeDoesntSmell: die Codex-Prüfung von Kapitel 4 nach den 24 Kriterien aus AGENTS.md (Abschnitt
"Kapitelprüfung und Freigabe") mit einem Workflow aus 1x Fable 5.1, 2x Opus 5 und 3x Sonnet 5 erneut prüfen und neu
bewerten; die daraus folgenden Änderungen anschließend von Codex (gpt-6-astra, Effort ultra) prüfen lassen.

Ausgangsstand: Commit `80022ba` mit den uncommitted Codex-Änderungen vom 13.09.2026 (SHA-256 der fünf Dateien
identisch mit `reviews/kapitel-4-abschluss-2026-09-13.md`). Implementierung `../udp-transport-options` bei `503c6c8`,
Arbeitsbaum sauber. Dieser Codex-Stand liegt für den Diff als Kopie im Sitzungs-Scratchpad.

Workflow `wf_41d33dff-e3e` (Claude Code, 53 Minuten, 418 Werkzeugaufrufe, Roll call 6 von 6):

- S1 (Sonnet 5): Implementierungs- und Messbelege an Code, Git-Historie, PR #12 und entpackten Archiven.
- S2 (Sonnet 5): Normtext, Einzelzuordnung (CSV), Querverweise, Ankündigungen und Begriffe über Kapitelgrenzen.
- S3 (Sonnet 5): Neubau in Scratchpad-Kopie, Layout der Seiten 41 bis 50, Silbentrennung, externe Literatur live.
- O1 (Opus 5): adversarialer Review jedes Codex-Hunks (behalten, anpassen, zurücknehmen) und der Berichtsaussagen.
- O2 (Opus 5): unabhängige Vollprüfung nach allen 24 Kriterien ohne Kenntnis der Berichte in `reviews/`.
- F (Fable 5.1): Dubletten entfernt, jeden Fehler- und Mangelbefund selbst an der Quelle verifiziert, Ersatztexte
  formuliert, Kriterienmatrix und Freigabeurteil erstellt. 47 Lane-Befunde, 31 Änderungsvorschläge, 8 Ablehnungen.

## Urteil des Adjudikators

Freigabe: **mit Auflagen**. Kapitel 4 ist fachlich tragfähig: Alle von mir am RFC-Primärtext, am Implementierungscode
(HEAD 503c6c8), an der Git-Historie und am Archiv vom 10.08. nachvollzogenen Norm-, Code- und Messaussagen halten
stand, und die sachlichen Codex-Korrekturen sind belegt. Das Codex-Urteil "freigabefähig, keine offenen
abgaberelevanten Befunde" ist dennoch nicht haltbar: Die Ankündigung "ihre Verträge prüft Kapitel 5" (04:292) wird von
Kapitel 5 nicht eingelöst, Kapitel 4 führt die Kürzel P0/P1/P2 und das Wort "Sendeprotokolle" uneingeführt ein
(04:332), die tragende Begründungspassage der Sprachwahl hat zwei bezugslose "ebenfalls" und benennt den Bun-Wechsel
falsch (04:282-287), und die K6-Beschriftung "Summen der Konformitätsmatrix" (06:856) widerspricht der im Diff selbst
eingeführten Begriffstrennung. Nach diesen vier Pflichtänderungen, den empfohlenen Präzisierungen sowie Neubau und
erneuter Trennungskontrolle ist das Kapitel im geprüften Umfang freigabefähig.

## 24 Kriterien nach der Adjudikation

- 1. geprüft: Keine fachlichen Fehler: RFC Sec. 2, 6, 7 und 25.2 selbst gelesen (literature/rfc9868.txt:126-129,
  265-284, 361-366, 2113-2131), 67 Matrixzeilen, 49 FR ohne FR-47 und zwölf NFR selbst gezählt, zwei unsafe-Blöcke und
  die OCS-Nachrechnung in eval-check.py am Code bestätigt; die 103-Verteilung und RFC Table 1 nach übereinstimmender
  Auszählung von S2 und O2 übernommen.
- 2. geprüft: Belege tragen die Aussagen; Bun-Blog heute selbst abgerufen (Jarred Sumner, 08.07.2026), der Bib-Eintrag
  nennt weder Autor noch Tagesdatum (A16); die >>-Konvention steht in RFC 9868 Sec. 2 und wird in 04:18 nicht belegt
  (A10); NSA- und C++-Einträge nur formal (A18, A19 optional); zwei Bib-Einträge sind durch den Diff unzitiert
  geworden (A17 optional).
- 3. geprüft: MUST/SHOULD/MAY in Tabelle 4.1 und im Text erhalten, das bedingte SHOULD aus Sec. 25.2 korrekt als
  bedingt gekennzeichnet; einzige Abschwächung ist 'eine begrenzte Ausnahme' statt 'the only limited exception' (RFC
  Z. 275-277, A6).
- 4. geprüft: Keine Gedankenstriche, keine Zeile über 120 Zeichen in den vier Textdateien (awk-Prüfung); Anglizismen
  sind RFC- oder Rust-Begriffe, einzig 'Testsuite' (04:340) ist ein nicht eingeführter Fremdbegriff (A20 optional).
- 5. geprüft: Drei unklare Bezüge: 'Sie' in 04:222 (A6), die Kette aus zwei 'ebenfalls' mit 'Wechsel von Bun zu Rust'
  in 04:283-286 (A2, pflicht) und das bezugslose 'Auch'/'daraus' in 04:163-164 (A7); Fußnoten und Beschriftungen
  einbezogen.
- 6. geprüft: Werkzeugrollen und Raw-Socket-Wahl sind begründet; verloren ging der komparative Kern der Rust-
  Entscheidung ('als einziger Kandidat', A3) und die Kennzeichnung der Selbstprüfung als Preis der Raw-Socket-Wahl
  (A23 optional); Pfadstufe 3 nennt als einzige keinen Prüfzweck (A25 optional, Beleg 06:276).
- 7. geprüft: Scheinwiderspruch Nichtverallgemeinerung/Ergebnisstatus der Vorversuche (04:148 gegen 04:163-165) bleibt
  vom Leser aufzulösen (A7); Bezugskette der Sprachwahl (A2); in Kapitel 6 fehlt nach dem Diff die tcpdump-Brücke zu
  den Betriebsregeln (A22 optional).
- 8. geprüft: Keine störenden Wiederholungen; die Shim-Wiederholung aus Kapitel 2 ist begründet, die 1,5 Sätze zur
  libFuzzer-Arbeitsweise (04:342-344) tragen die K4-spezifische Aussage 'des tatsächlichen Parsercodes' und bleiben
  (B13/O2-12 abgelehnt).
- 9. geprüft: Arbeitsindex/Einzelzuordnung sind in K4 sauber getrennt, aber 'Sendeprotokolle' (einziges Vorkommen,
  sonst Sendemanifest) und die uneingeführten Kürzel P0/P1/P2 (A4, pflicht), 'Ablaufprotokolle' (einziges Vorkommen,
  A8), die K6-Beschriftung 06:856 (A5, pflicht) und 'kontrollierte Pfadversuche' statt 'lokale Referenzläufe' (A27
  optional) verletzen die Durchgängigkeit; Repository/Repositorium bleibt thesisweit offen.
- 10. geprüft: Beide Fußnoten beantworten je eine Nebenfrage; Fußnote 1 verweist auf Commit b8a5277 (Typ commit, auf
  origin/main, git diff b8a5277 HEAD für die CSV leer), Fußnote 2 trennt Rust-unsafe von der UNSAFE-Klasse; der Satz
  vor Fußnote 1 nennt nur eine FF1-Bewertung, die Datei trägt zwei Urteilsspalten (A9).
- 11. geprüft: Linux, IPv4, Raw Sockets im Benutzerraum, Protocol 17 ohne Shim-Ketten und der Optionsumfang bleiben
  erhalten und lösen 01:141 und 01:154 ein; die in tab:scope-messung angekündigte IPv6-Gegenprobe erscheint in Kapitel
  6 nur als Umfangsangabe (06:54) ohne Ergebnis (A11).
- 12. geprüft: Fremde Ergebnisse, eigene Messungen und Schlüsse sind getrennt, Selbstauskunft des Arbeitsindex und
  eigenes Urteil ausdrücklich unterschieden, keine Gerätezuschreibung (04:160-161); die CSV führt kategorie
  (Implementierungsstand) und technisch als zwei Urteile (Kopfzeilen 3-6), K4 nennt nur eines (A9).
- 13. geprüft: MTU-Aussage zu IP_HDRINCL stimmt mit raw(7) und 05:234-236 überein; die Shim-Regel ist gegenüber RFC Z.
  365-366 und der alten Fassung unschärfer ('verfügbaren Raum' ohne Betrag) und schreibt 'IP-' statt 'IPv4-' wie 02:94
  (A12).
- 14. geprüft: OCS- und UDP-Prüfsummenrollen richtig: eval-check.py rechnet OCS in _validate_surplus (Z. 233-251)
  selbst, wire-check.py ebenso, die Kampagnenauswerter übernehmen ocs_reports (p0-eval.py-Kopf, Codebefunde S1/O1/O2
  übereinstimmend); die Tabellenzeile zu Sec. 9 entspricht RFC Z. 524.
- 15. geprüft: Lage der Surplus Area, Pad-Regel, 254-Byte-Grenze, NOP-Grenze, must-support-Liste (acht) und UEXP-
  Einordnung sind laut übereinstimmender Prüfung von S2 und O1 am RFC belegt; Reassemblierungsausnahme und
  Sec.-25.2-Bedingung selbst am RFC bestätigt; keine Abweichung.
- 16. geprüft: Raw Sockets werden nicht mit Umgehung aller Prüfungen gleichgesetzt (04:315); genau zwei unsafe-Blöcke
  (src/socket/send.rs:131, recv.rs:169) mit SAFETY-Kommentaren, Kapitel 5 nennt sie (05:87-88), prüft aber keine
  Verträge; Implementierungscode nirgends als Normquelle verwendet.
- 17. geprüft: Archiv vom 10.08. selbst entpackt: vier eval-check-Läufe mit Exitcode 0 (logs/hetzner-
  eval/0[2-5]-eval-*.meta, summary.md), fünf gescheiterte CLI-Aufrufe auf externen Paarmitschnitten, analyze-pcap-
  pair.py mit importierter Prüffunktion; en0-Belege des 12./13.08. nach O1 und S1; CGNAT-Vorbehalt korrekt gesetzt.
- 18. geprüft: FF1-Kategorien und FF2-Status stimmen wörtlich mit tab:operationalisierung (03:151-155) überein; die
  Sonderklasse ist am CSV-Bestand belegt (Zeilen 222, 223, 227); die Einheit 'Lauf' gegen 'Szenario' ist in K3 und K4
  gleich lose und bleibt Autorenentscheidung.
- 19. geprüft: Modellbeweis/Rust-Code, Fuzzing/Fehlerfreiheit und übernommener OCS-Status sind korrekt abgegrenzt; die
  angekündigte Vertragsprüfung in Kapitel 5 fehlt (A1, pflicht); Fuzz-Ziele und Property-Tests teilen dieselben Orakel
  (alle neun Ziele include! tests/common*/mod.rs, dieselben Module in tests/properties_*.rs), was K4 nicht nennt (A20
  optional).
- 20. geprüft: Die Vorgabe steht wörtlich in ../udp-transport-options/AGENTS.md:168-171, der Startoffset-Fehler und
  die 23 Tests in docs/plan/steps/02-wire-model.md:99-107; der Verweis (sec:pruefkette) zeigt aber nicht auf den Ort
  der Vorgabe (fig:stepzyklus, 03:284-286, A13); der eval-check-Einsatz am 10.08. ist belegt (S1-F1 abgelehnt).
- 21. geprüft: Alle Verweise lösen auf, Abbildung und vier Tabellen stimmen mit dem Text; drei Ziele enthalten den
  angekündigten Inhalt nicht: Kapitel 5 ohne Vertragsprüfung (A1), Beschriftung 06:856 (A5), IPv6-Rolle ohne
  Ergebnisreihe (A11); sec:pruefkette ohne die Vorgaberegel (A13).
- 22. geprüft: pdftotext der physischen Seiten 42-49 und Seitenbild 47 (110 dpi) geprüft: keine abgeschnittenen
  Inhalte, Fußnoten auf ihrer Seite, Tabellen nicht zerrissen; die Rust-Zelle in Tabelle 4.4 liest sich ohne Prädikat
  ('in Safe Rust;') und die Zig-Zelle bricht mit dem Einzelwort 'nach' um (A14, kosmetisch).
- 23. geprüft: 35 Zeilenendstriche auf den Seiten 42-49 nachgezählt (31 im Fließtext, vier in Tabellenzellen), alle
  Duden-konform; nach der Hausregel brechen neun innerhalb eines Kompositumsbestandteils (Speichersicher-heit,
  Speicherverwal-tung, Objektlebensdau-er, Spei-chersicherheit, Adressum-setzung, Tun-nelendpunkten, Beispielpro-
  grammen, Ker-nelmodul, Emp-fangsprogramme); A14/A15 empfohlen, A25/A26 optional.
- 24. geprüft: Diff vollständig gelesen, keine unbeabsichtigte Bedeutungsänderung außer den genannten
  Präzisionsverlusten (A3, A12); main.log ohne Overfull/Underfull, 95 Seiten, Zeitstempel von Quelle, Log und PDF
  identisch (13.09. 10:18); kein eigener Neubau, aber S3 und O2 haben unabhängig textidentisch gebaut; nach Umsetzung
  der Änderungen sind Neubau, Umbruch- und Trennungskontrolle Pflicht.

## Eingearbeitete Änderungen

Claude (Orchestrator) hat jeden angenommenen Befund vor der Einarbeitung selbst geprüft (RFC-Zeilen, Kapitel 3, 5 und
6, CSV, `src/socket/*.rs`, `scripts/p0-eval.py` bis `p2-eval.py`, `fuzz/fuzz_targets`, Bun-Blog per curl). Kennungen
wie im Adjudikationsergebnis; Wortlaut teils gegenüber dem Vorschlag gestrafft.

- A1 (pflicht, 04_analyse.tex, Z. 291-293, Druckseite 42): Die Ankündigung 'ihre Verträge prüft Kapitel 5' wird nicht
  eingelöst: Kapitel 5 nennt die zwei unsafe-Blöcke nur, prüft keine Sicherheitsbedingungen (Kriterium 21, 19, 7).
- A2 (pflicht, 04_analyse.tex, Z. 282-287, Druckseite 42): Tragende Begründungspassage der Sprachwahl: der Satz über
  statische Werkzeuge hat keinen Anschluss an Rust, zwei 'ebenfalls' haben keinen Bezugspunkt, und 'Wechsel von Bun zu
  Rust' benennt Bun (Projekt) statt Zig (verlassene Sprache) als Ausgangspunkt (Kriterien 5, 7, 2).
- A3 (empfohlen, 04_analyse.tex, Z. 275-276, Druckseite 41): Der angekündigte Ausschlag ('Den Ausschlag gibt die
  Speichersicherheit', 04:245) wird nicht mehr als Vergleich der vier Kandidaten ausgesprochen; die alte Fassung sagte
  'als einziger Kandidat der Tabelle' (Kriterium 6).
- A4 (pflicht, 04_analyse.tex, Z. 332-333, Druckseite 43): 'Sendeprotokolle' ist ein drittes Wort für das Artefakt,
  das 04:152-153, 03:153, 03:413 und 06:33 'Sendemanifest' nennen (einziges Vorkommen in der Thesis); die Kürzel P0,
  P1 und P2 werden hier zwei Druckseiten vor Kapitel 6 ohne Anker eingeführt und nirgends definiert (Kriterium 9).
- A5 (pflicht, 06_evaluation.tex, Z. 856 (Beschriftung tab:eval-sollist-summe), Druckseite 79): Die Tabelle summiert
  die eigenen Urteile der geprüften Einzelzuordnung (50/7/10, 57 V), trägt aber weiterhin den Namen des Arbeitsindex;
  der im Diff geänderte Satz zwei Zeilen davor sagt bereits 'Einzelzuordnung' (Kriterien 9, 21).
- A6 (empfohlen, 04_analyse.tex, Z. 221-224, Druckseite 40): 'Sie' kann sich auf die Anwendung oder die Schicht
  beziehen; 'eine begrenzte Ausnahme' schwächt 'the only limited exception' ab; das für die Bibliotheksform tragende
  Wort 'library' des RFC fehlt (Kriterien 3, 5, 6).
- A7 (empfohlen, 04_analyse.tex, Z. 163-166, Druckseite 39): 'Auch' hat nach dem Absatz über das Attributionsintervall
  keinen Bezug; 'daraus' schreibt die Mechanismenklassen den gerade als nicht verallgemeinerbar bezeichneten
  Vorversuchen zu (04:148), während Kapitel 6 sie aus Vorversuchen und Messungen ableitet (Kriterien 7, 5, 12).
- A8 (empfohlen, 04_analyse.tex, Z. 148-149, Druckseite 39): 'Ablaufprotokolle' kommt in der Thesis nur hier vor und
  wird nirgends eingeführt; Kapitel 6 definiert den Pilot als Funktionsprobe 'ohne Mitschnitt oder Manifest' und kennt
  weitere Stufen der Beweiskraft (Kriterien 9, 7).
- A9 (empfohlen, 04_analyse.tex, Z. 65-66 mit Fußnote 1, Druckseite 37): Der Text nennt eine 'FF1-Bewertung', die
  verlinkte Datei trägt zwei getrennte Urteile (kategorie = Implementierungsstand, technisch = Erfüllbarkeit) mit
  denselben Etiketten; Kapitel 3 kündigt den zweiten Wert an, Kapitel 4 führt die Datei ein und verschweigt ihn
  (Kriterien 12, 18, 21).
- A10 (empfohlen, 04_analyse.tex, Z. 17-20, Druckseite 36): Die >>-Markierungskonvention stammt aus RFC 9868 Sec. 2
  und ist nicht belegt; RFC 2119/8174 tragen nur die Bedeutung der Schlüsselwörter (Kriterium 2; eigene Belegform-
  Regel 03:180-182).
- A11 (empfohlen, 04_analyse.tex, Z. 207-208 (tab:scope-messung), Druckseite 40): Die Tabelle schreibt den
  IPv6-Kontrollen die Rolle 'Vergleich mit IPv4-Befunden' zu; Kapitel 6 berichtet keinen solchen Vergleich (IPv6 nur
  als Umfangsangabe in 06:54), obwohl Kapitel 1 den Leser dafür nach sec:ff2-pfadmodell schickt (Kriterien 21, 11).
- A12 (empfohlen, 04_analyse.tex, Z. 48-51, Druckseite 36): Die Shim-Längenregel ist unschärfer als der Primärtext und
  die alte Fassung (welche Größe um welchen Betrag verringert wird, fehlt), und 'IP- und UDP-Header' weicht von 'IPv4-
  und UDP-Header' in der K2-Fußnote ab (Kriterien 15, 13, 9).
- A13 (empfohlen, 04_analyse.tex, Z. 299-300, Druckseite 42): Der Verweis für die Vorgabe zeigt auf sec:pruefkette,
  das die Prüfmittel und die 18 Prüfläufe beschreibt, die Regel selbst aber nicht formuliert; sie steht im Kernzyklus
  fig:stepzyklus unter sec:rfc-auswertung (Kriterium 21).
- A14 (empfohlen, 04_analyse.tex, Z. 267-270 (tab:sprachvergleich), Druckseite 41): Die Rust-Zelle 'in Safe Rust;' hat
  nach dem Streichen des 'ja' kein Prädikat mehr und bricht die Parallelität zu 'nicht garantiert'; im Druck trennen
  die Zellen 'Speichersicher-heit', 'Speicherverwal-tung' und 'Objektlebensdau-er' innerhalb eines
  Kompositumsbestandteils, letzteres mit zwei Buchstaben in der Folgezeile (Kriterien 21, 22, 23).
- A15 (empfohlen, 04_analyse.tex, Z. 245, Druckseite 41): Im Druck bricht 'Spei-/chersicherheit' um; der erste
  Bestandteil des zentralen Begriffs wird zerlegt (Kriterium 23, Hausregel).
- A16 (empfohlen, literatur.bib, Eintrag bun-in-rust (Z. 442-448)): Der Blogbeitrag hat einen Autor (Jarred Sumner)
  und ein Tagesdatum (08.07.2026); der Eintrag nennt weder Autor noch Datum (Kriterium 2).
- A17a (optional, literatur.bib, Eintrag microsoft-memory (Z. 238-246)): Durch die Umstellung auf msrc-memory-blog ist
  der Eintrag in keiner .tex-Datei mehr zitiert (Kriterien 2, 24; frühere Runden haben tote Einträge entfernt).
- A17b (optional, literatur.bib, Eintrag kernel-devtools (Z. 293-301)): Seit der Streichung aus 04:283 nirgends mehr
  zitiert; die Quelle trug die methodische Aussage ohnehin nicht (Kriterien 2, 24).
- A18 (optional, literatur.bib, Eintrag cpp-core-guidelines, note-Feld (Z. 260)): Der neue Eintrag weicht von der im
  Verzeichnis eingeführten Formel für undatierte Quellen ab ('Undatierte, fortlaufend gepflegte ...', vgl. rust-book,
  rust-lang, chromium-memory, libfuzzer).
- A19 (optional, literatur.bib, Eintrag nsa-memory-safety (Z. 231-232)): Datum April 2023/Version 1.1 steht im Druck
  neben einer Adresse unter /2022/Nov/10/; der Widerspruch ist nur scheinbar (die Adresse liefert Ver. 1.1), eine Note
  löst ihn auf (Kriterium 2).
- A20 (optional, 04_analyse.tex, Z. 340-342, Druckseite 43): 'Testsuite' ist der einzige nicht eingeführte
  Fremdbegriff des Kapitels; außerdem prüfen Fuzz-Ziele und Property-Tests dieselben, aus dem Puffer abgeleiteten
  Orakel, sodass eine falsch formulierte Invariante beiden entginge, was Kriterium 19 ausdrücklich verlangt zu
  unterscheiden (Kriterien 4, 19).
- A22 (optional, 06_evaluation.tex, Z. 113-115, Druckseite 58): Nach dem Wegfall des Werkzeugkettensatzes beginnt der
  Absatz mit dem Prüfumfang der Auswerter und springt ohne Übergang zu den tcpdump-Betriebsregeln, deren Werkzeug im
  Absatz nicht mehr eingeführt wird (Kriterium 7).
- A23 (optional, 04_analyse.tex, Z. 315, Druckseite 42): Die alte Fassung kennzeichnete die Selbstprüfung als Preis
  der Raw-Socket-Wahl; der neue Satz liest sich als neutrale Beschreibung, die Abwägung verliert ihre Gegenseite
  (Kriterium 6).
- A24 (optional, 04_analyse.tex, Z. 324, Druckseite 43): Kapitel 2 und 3 formulieren enger ('dekodieren UDP Options
  nach RFC 9868 nicht', 'keinen Dissektor für UDP-Optionen'); Wireshark zeigt die überzähligen Bytes, es fehlt der
  Dissektor (Kriterium 9).
- A25 (optional, 04_analyse.tex, Z. 140-141, Druckseite 38): Pfadstufe 3 nennt als einzige Stufe nicht, was sie prüft;
  die Aussagegrenze steht erst in Kapitel 6; zugleich bricht 'Tun-/nelendpunkten' im Druck innerhalb des Bestandteils
  'Tunnel' um (Kriterien 6, 23).
- A26a (optional, 04_analyse.tex, Z. 138, Druckseite 38): Im Druck 'Adressum-/setzung': Duden-konform, aber die
  Vorsilbe 'um' wandert an 'Adress' und bildet das Fragment 'Adressum' (Kriterium 23, Hausregel).
- A26b (optional, 04_analyse.tex, Z. 220, Druckseite 40): Im Druck 'Beispielpro-/grammen' innerhalb des Bestandteils
  'Programmen' (Kriterium 23, Hausregel).
- A26c (optional, 04_analyse.tex, Z. 309, Druckseite 42): Im Druck 'Ker-/nelmodul' innerhalb des Bestandteils 'Kernel'
  (Kriterium 23, Hausregel).
- A26d (optional, 04_analyse.tex, Z. 314, Druckseite 42): Im Druck 'Emp-/fangsprogramme' innerhalb des Bestandteils
  'Empfangs' (Kriterium 23, Hausregel).
- A27 (optional, 04_analyse.tex, Z. 329-330, Druckseite 43): 'kontrollierte Pfadversuche' ist eine weitere Bezeichnung
  für das, was Kapitel 6 'Referenzlauf' beziehungsweise 'lokale Referenzläufe' nennt (Kriterium 9).
- A28 (optional, AGENTS.md, Z. 187): Einzige Zeile über 120 Zeichen (121) in den geprüften Dateien; vorbestehend,
  nicht Teil des Diffs (Kriterium 24, Formatregel).

Abweichend vom Vorschlag umgesetzt oder nicht umgesetzt:

- A8: "ohne beidseitige Mitschnitte oder Sendemanifest" (Kapitel 6 definiert den Pilot mit "oder"); der Zusatz zu den
  Stufen der Beweiskraft entfiel zugunsten des Seitenumbruchs, der Verweis auf Abschnitt 6.1 bleibt.
- A13: Verweis nur auf `fig:stepzyklus`; die Regel steht in Kapitel 3 allein in dieser Abbildung, nicht in Prosa.
- A17a/A17b: `microsoft-memory` und `kernel-devtools` sind nach der Codex-Umstellung unzitiert und wurden entfernt.
  Der MSRC-Blog ist laut S3 live erreichbar (HTTP 200) und trägt die zitierte 70-Prozent-Formulierung wörtlich;
  Millers Vortrag wird deshalb nicht mehr zusätzlich zitiert.
- A18: nach dem Codex-Review nicht als undatiert geführt, sondern mit dem Datum des Dokumentkopfs (14. Juni 2026).
- A19: Note verkürzt auf "Unter der Adresse der Erstveröffentlichung vom 10. November 2022" (Version und Datum stehen
  bereits in den Feldern).
- A20: "Testsuite" ersetzt durch "Unit-, Integrations- und Property-Tests (Abschnitt 3.4.1)"; der Satz zu den
  gemeinsamen Testmodulen wurde aufgenommen (alle neun Fuzz-Ziele binden per `include!` dieselben
  `tests/common*/mod.rs` ein wie die Property-Tests) und nach dem Codex-Review abgeschwächt formuliert.
- A25: nur die Trennhilfe `Tunnel\-endpunkten`; der Zusatz "prüft die Zustellung nach der Entkapselung" entfiel, weil
  er Tabelle 4.2 auf die Folgeseite schob (Seitenziel).
- A7, A9: Wortlaut gestrafft, damit Kapitel 4 weiter auf den Druckseiten 36 bis 43 endet.
- A28 (AGENTS.md Zeile 187, 121 Zeichen): nicht geändert, vorbestehend und außerhalb des Kapitels.
- Zusätzliche Trennhilfen nach der Hausregel, weil neue Umbrüche entstanden: `Speicher\-bereichs`,
  `Sicherheits\-bedingungen`, `Empfänger\-ausgaben` (Kapitel 4) und `Empfänger\-ausgabe` (Kapitel 6, Zeile 115). Eine
  Trennhilfe `Umsetzungs\-stand` erzeugte eine Overfull-Box und wurde zurückgenommen.

## Abgelehnte Befunde

- F1-evalcheck-10aug (S1): eval-check.py sei in der Kampagne vom 10. August nur mit gescheiterten CLI-Aufrufen (5 x
  Exitcode 1) vertreten; die Prüfung habe ein archivinternes Hilfsskript übernommen, der Satz 04:329-330 sei deshalb
  ungenau (mangel). Grund: Das entpackte Archiv external-campaign-20260810T200118Z enthält neben den fünf
  gescheiterten CLI-Aufrufen auf externen Paarmitschnitten vier erfolgreiche eval-check-Auswertungen: logs/hetzner-
  eval/02-eval-veth bis 05-eval-filter (.meta jeweils exit_code=0, verdicts.jsonl mit fünf Szenarien, summary.md 'alle
  fünf Szenarien intact' bzw. 'dropped', Commit 7b11140, 2026-08-10T20:47Z). Die externen Paare wertete
  matrix/analyze-pcap-pair.py mit der importierten Funktion eval_check._validate_surplus aus (Z. 14-20, 55-62). Der
  Satz 'in der Kampagne vom 10. August eingesetzt' ist damit richtig; S1 hat die hetzner-eval-Lanes übersehen. Nur der
  Begriff 'kontrollierte Pfadversuche' wird optional angeglichen (A27).
- B18 (O1): eval-check.py rechne OCS nur auf der Senderaufzeichnung nach und vergleiche die Empfängerseite byteweise;
  das sei zu präzisieren (optional). Grund: Für die CLI trifft das zu (validate_sender_groups ruft _validate_surplus,
  classify vergleicht Surplus-Zeichenketten), für die Kampagne vom 10.08. nicht: analyze-pcap-pair.py wendet
  surplus_validation auf Sender- und Empfängerpakete an. Die vorgeschlagene Formulierung wäre für den im Satz
  genannten 10.08.-Einsatz falsch; die Abstraktionsebene von Kapitel 4 genügt.
- O2-08 (O2): Der Satz zu den FF2-Ergebnisklassen (04:127-131) wechsle die Einheit von 'Szenario' auf 'Lauf' und lasse
  offen, ob je Szenario oder je Kampagne entschieden wird (mangel). Grund: 'Lauf ungültig' und die Ergebnisklassen
  stammen wörtlich aus tab:operationalisierung (03_methodik.tex:154-155: 'Surplus erhalten, verändert oder entfernt;
  Datagramm verworfen oder Lauf ungültig'); Kapitel 4 spiegelt Kapitel 3. Die vorgeschlagene Neufassung behauptet eine
  Regel (Ungültigkeit je Messlauf, dessen Szenarien ausscheiden), die 06:142-147 so nicht formuliert. Eine
  Vereinheitlichung der Einheit wäre eine K3/K6-Entscheidung und steht unter 'offen'.
- O2-16 (O2): 'Sein Verhalten' in 04:313 könne sich auf den Zugang oder auf Linux beziehen (optional). Grund: Der
  nächstliegende Bezug ist 'diesen Zugang' (Raw Sockets), und genau dessen Verhalten ist dokumentiert (raw(7),
  man7raw) und im Kernelquelltext nachprüfbar (linux510udp); der zweite Halbsatz begründet zusätzlich die Plattform.
  Der Bezug ist eindeutig genug, keine Änderung nötig.
- O2-14 (O2): 'Implementierungs-Repository' und 'Thesis-Repositorium' stehen in Kapitel 4 nebeneinander; Kapitel 6
  schreibt 'Implementierungsrepositorium' (optional). Grund: Kapitel 3 verwendet 'Implementierungs-Repository' dreimal
  (03:186, 247, 249), Kapitel 4 dreimal, Kapitel 6 fünfmal die andere Form. Eine Angleichung nur in Kapitel 4
  vergrößert die Inkonsistenz zu Kapitel 3; das ist eine thesisweite Entscheidung außerhalb des K4-Auftrags (unter
  'offen' geführt).
- B13 / O2-12 (O1, O2): Kapitel 4 wiederhole die Fuzzing-Erklärung aus subsec:pruefmittel (optional, Kürzung um bis zu
  drei Zeilen). Grund: Die 1,5 Sätze (04:342-344) tragen die K4-spezifische Aussage, dass libFuzzer den tatsächlichen
  Parsercode und nicht ein Modell prüft; die Wiederholung gegenüber 03:428-432 ist knapp. Kürzung ist Geschmack; eine
  Umformulierung von A20 berührt dieselben Zeilen und würde mit dieser Kürzung kollidieren.
- B15 (O1): Die Metapher 'grüne Prüfkette' stehe in Kapitel 6 dreimal, Kapitel 4 sage jetzt 'bestandene Prüfkette'
  (optional). Grund: Kapitel 6 (1008, 1016, 1119) und Kapitel 7 (82, 'grüner Implementierungstest') verwenden die
  Metapher konsistent; die K4-Formulierung ist nicht falsch. Die Wortwahl in Kapitel 6 und 7 gehört zu deren Prüfung,
  nicht zur Freigabe von Kapitel 4.
- K4-S2-05 (S2): CSV-Zeile 226 (Sec. 25.2) bindet das SHOULD an die Nichtwahl des MAY; die Einstufung 'nicht
  anwendbar' sei nicht zwingend (mangel). Grund: Am RFC bestätigt (literature/rfc9868.txt:2113-2116: 'Such
  implementations' bezieht sich auf 'Implementations concerned with ... a covert channel'), aber kein
  Kapitel-4-Befund: Kapitel 4 trifft keine Aussage zu Zeile 226. Codex hat den Punkt als offenen K6-Prüfpunkt
  dokumentiert (Abschlussbericht, 'Gesonderter offener Prüfpunkt'); er bleibt unter 'offen'.

## Offene Punkte für den Autor

- Strenge der Silbentrennungs-Hausregel: Alle 35 Trennungen der Seiten 42-49 sind Duden-konform; neun brechen
  innerhalb eines Kompositumsbestandteils. Ob das als Verstoß gegen 'Wortbestandteile erhalten' gilt, entscheidet der
  Autor (A14/A15 empfohlen, A25/A26 optional). Nach jeder Umsetzung: Neubau und erneute Umbruch- und
  Trennungskontrolle der Seiten 42-49 (AGENTS.md:59-60).
- IPv6-Kontrollen: entweder die Einschränkung in tab:scope-messung (A11) oder ein Satz in Kapitel 6 mit dem Datenpunkt
  aus dem Archiv vom 10.08. (evidence/README.md:95-96: je ein gebridgtes IPv4- und IPv6-Paket bis en0 intakt, nicht
  auf Hetzner eth0 beobachtet).
- CSV-Zeile 226 (Sec. 25.2): Begründungslücke der Einstufung 'nicht anwendbar' bleibt ein K6-Punkt (laut Codex in
  insights-inbox); die Summen 50/7/10 und 57 V hängen davon ab.
- Tote Bib-Einträge microsoft-memory und kernel-devtools: löschen (A17) oder Millers Vortrag als Zweitquelle neben dem
  MSRC-Blog behalten; bei Änderungen am Literaturverzeichnis Nummern im Text prüfen (biber-Lauf).
- Thesisweite Vereinheitlichung 'Implementierungs-Repository' (K3 3x, K4 3x) gegen 'Implementierungsrepositorium' (K6
  5x).
- Einheit der FF2-Entscheidung: tab:operationalisierung, Kapitel 4 und Kapitel 6 verwenden 'Lauf' sowohl für die
  Untersuchungseinheit ('Lauf ungültig') als auch für den Kampagnenlauf; eine Präzisierung wäre in K3 und K6
  gleichzeitig vorzunehmen.
- Wegfall der Tabellenzeilen 'Schutzmechanismus' und 'Sprachfassung' in Tabelle 4.4: sachlich vertretbar, aber der
  Reifegrad der Sprache (Rust 1.0 seit 2015, Zig vor 1.0) ist damit als Entscheidungskriterium aus dem Kapitel
  verschwunden; Autorenentscheidung.
- docs/evaluation.md:28-33 im Nachbarrepo beschreibt eval-check.py weiterhin unzutreffend ('does not independently
  validate OCS'), obwohl _validate_surplus (Z. 233-251) OCS nachrechnet; betrifft die Belegkette, nicht den Thesis-
  Text.
- Nicht wiederholt: Rust-Tests, Fuzz-Läufe, Lean-Beweise, Messkampagnen; nicht selbst entpackt: bidir-20260811,
  piloten-und-nachtraege (en0-Belege nach O1/S1), hel/p0p1p2/ff2-Archive; nicht selbst abgerufen: MSRC-Blog, NSA-CSI,
  C++ Core Guidelines, Zig- und Rust-Dokumentation, Linux-Quelltext (nach S3 live geprüft); RFC Table 1 und die
  103-Verteilung nur über die übereinstimmenden Auszählungen von S2 und O2.

## Bau, PDF und Silbentrennung

Vollbau mit `make -C thesis pdf` (pdflatex, biber, makeglossaries, zweimal pdflatex), Exitcode 0, keine Overfull-,
Underfull-, Referenz- oder Biber-Warnungen. 95 Seiten wie zuvor; Kapitel 4 unverändert auf den physischen Seiten 42
bis 49 (Druckseiten 36 bis 43), Literaturverzeichnis ab physischer Seite 91. Ein Zwischenstand mit 97 Seiten (Tabelle
4.2 auf der Folgeseite, Kapitel 4 mit 16-Zeilen-Schlussseite) wurde durch Straffung der Einfügungen behoben.

Silbentrennung: alle 37 Zeilenendstriche der Seiten 42 bis 49 sowie die geänderten Absätze in Kapitel 6 (physische
Seiten 64 und 79) aus dem Neubau geprüft; Trennungen zusammengesetzter Fachwörter liegen jetzt an den Wortfugen
(Speicher-sicherheit, Speicher-verwaltung, Objektlebens-dauer, Adress-umsetzung, Tunnel-endpunkten, Beispiel-
programmen, Kernel-modul, Empfangs-programme, Empfänger-ausgaben, Sicherheits-bedingungen). Die Seiten 45, 46, 47 und
49 wurden gerendert und visuell geprüft: Tabellen 4.2 und 4.4 folgen direkt auf ihre Ankündigung, Tabelle 4.3 steht
oben auf der Folgeseite wie zuvor.

## Codex-Review (gpt-6-astra, Effort ultra, read-only)

Lauf am 13.09.2026 von 15:40 bis 15:50 Uhr mit `codex exec -s read-only -c model_reasoning_effort=ultra`, Diff per
stdin, Prompt aus Datei, Endnachricht per `-o`. Vollständiger Wortlaut: `kapitel-4-codex-diffreview-2026-09-13.md`.
Nach dem Lauf zeigte `git status` in beiden Repositorien keine Fremdänderungen.

Urteil: Freigabe mit Auflagen. 16 von 18 Hunks richtig, zwei anzupassen; beide wurden umgesetzt:

- Hunk 12 (Abschnitt 4.4.4): Die Folgerung "eine falsch formulierte Invariante bliebe deshalb in beiden unentdeckt"
  war zu absolut, weil eine falsche Assertion auch an einem korrekten Ergebnis scheitern kann und die Property-Tests
  zusätzliche Prüfungen enthalten (`tests/properties_wire.rs:119-171`). Neuer Wortlaut: "Fuzz-Ziele und Property-Tests
  verwenden dabei gemeinsame Testmodule; fehlerhafte Annahmen in diesen Modulen können deshalb in beiden Prüfverfahren
  unentdeckt bleiben."
- Hunk 16 (Bib `cpp-core-guidelines`): "Undatierte" war falsch; der Dokumentkopf nennt den 14. Juni 2026 (von Claude
  am Quelltext der Seite verifiziert, Herausgeber Stroustrup und Sutter). Jetzt `date = {2026-06-14}` und Note ohne
  "Undatierte". Der Workflow-Befund A18 war damit sachlich falsch.

Codex widersprach drei Bewertungen des Workflows, ohne Textänderung zu verlangen: A7 (die alte Fassung war kein
belegter Sachfehler, die neue verdeutlicht sinnvoll), A2 ("Wechsel von Bun zu Rust" war missverständlich, aber kein
nachgewiesener Sachfehler), A3 und der Wortlaut von A14 (Verdeutlichungen, keine Reparaturen). Die Ablehnungen von
S1-F1 und O1-B18 bestätigte Codex an den Archivbelegen (vier eval-check-Metadateien mit Exitcode 0;
`matrix/analyze-pcap-pair.py` prüft Sender- und Empfängerpakete). Die IPv6-Einschränkung in Tabelle 4.3 stützte Codex
zusätzlich auf `matrix/send-ipv6-probe.py` und `analysis/ipv6-bridge.md` im Archiv vom 10.08. Als abgaberelevant
außerhalb des Diffs bleibt die Begründung der CSV-Kennung 226 (Kapitel-6-Punkt, siehe `thesis/insights-inbox.md`).

Nach den beiden Anpassungen: Neubau mit Exitcode 0, 95 Seiten, keine Warnungen, Kapitel 4 weiter auf den physischen
Seiten 42 bis 49, Trennungen der Seite 49 erneut geprüft. Nicht committet und nicht gepusht; die Implementierung wurde
nicht geändert.

## Kürzungsrunde und IPv6-Entfernung (Autorenanweisung vom 13.09.2026)

Anweisung: IPv6 ist aus der Arbeit entfernt; Beschreibungen in Kapitel 4 vollständig streichen und den roten Faden
anpassen; den Text allgemein kürzen und Flächen für Rückfragen, Unverständlichkeit und Widersprüche entfernen.

- IPv6: Zeile "native IPv6-Kontrollen" in Tabelle 4.3 und der Schlusssatz nach der Tabelle gestrichen; Kapitel 1
  (Zeilen 151 bis 153) sagt jetzt "Die Implementierung, ihre Konformitätsprüfung und die Pfadmessungen beziehen sich
  daher auf IPv4" ohne Verweis auf 4.3; Tabelle 6.1 nennt für die Kampagne vom 10.08. "IPv4, Tunnel". Die Umfangszeile
  "Vermittlungsschicht: IPv4, außerhalb: IPv6" in Tabelle 4.2 bleibt als Abgrenzung; ebenso die Abgrenzungen in
  Kapitel 2 (Zeile 786) und der Ausblick in Kapitel 7 (Zeile 72).
- Kürzungen in Kapitel 4: Absatz zu den Vorversuchen als Hypothesenquelle auf einen Satz reduziert; Satz zur
  Wiederverwendbarkeit der Bibliothek in 4.4 gestrichen; "Alle vier Kandidaten bieten die nötige Kontrolle" gestrichen
  (stand bereits im Absatz davor); Bun-Beispiel in 4.4.1 gestrichen (Kapitel 3 behandelt den Fall, `bun-in-rust`
  bleibt dort zitiert); Kennungen der Anforderungen kompakt in Klammern.
- Begriff vereinheitlicht: "Implementierungs-Repository" in Kapitel 3 (Zeilen 186, 247, 249) und Kapitel 4 (Zeilen 22,
  58, Beschriftung Tabelle 4.1) zu "Implementierungsrepositorium" wie in Kapitel 6.
- Trennhilfe `Speicher\-fehler` ergänzt (neuer Umbruch "Spei-cherfehler" nach der Kürzung).

Neubau: Exitcode 0, keine Warnungen, 95 Seiten, Kapitel 4 weiter auf den physischen Seiten 42 bis 49 (Schlussseite
jetzt 24 Zeilen), Tabellen 4.2 und 4.4 direkt nach ihrer Ankündigung, Tabelle 4.3 oben auf der Folgeseite; Trennungen
der Seiten 42 bis 49 und der geänderten Seite in Kapitel 1 (physisch 10) geprüft; Seiten 45, 46 und 49 gerendert und
gesichtet. Zweiter Codex-Review über den Gesamtdiff: siehe unten.

## Codex-Review 2 (Gesamtdiff nach der Kürzungsrunde)

Lauf am 13.09.2026 von 16:09 bis 16:18 Uhr, gleiche Aufrufform wie Runde 1, Diff mit 21 Hunks einschließlich Kapitel
1. Wortlaut im Anhang von `kapitel-4-codex-diffreview-2026-09-13.md`. `git status` in beiden Repositorien danach ohne
Fremdänderungen.

Urteil: "Freigabe: ja, Kapitel 4 ist im geprüften Diff-Umfang abgabereif." Alle 21 Hunks richtig, keiner anzupassen.
Codex bestätigte: IPv6-Streichung beseitigt die nicht eingelöste Vergleichsankündigung; die Kürzungen erhalten
Begründung der Technologieauswahl, Aussagegrenzen der Messungen und Kapitelverbindungen; die Trennhilfen und
Beschriftungen sind korrekt; PDF-Seiten 42 bis 49 sowie 10, 34, 35, 63, 64, 79 und 92 bis 94 ohne Layout- oder
Trennungsfehler.

Einziger verbliebener abgaberelevanter Punkt außerhalb des Diffs und außerhalb von Kapitel 4: die Begründung der
Nichtanwendbarkeit von CSV-Kennung 226 (RFC 9868, Abschnitt 25.2) in `06_evaluation.tex` Zeilen 971 bis 973, in
`thesis/daten/konformitaet-kategorien.csv` Zeile 74 und in `thesis/tikz/gen/ff1-kategorien.py`. Das SHOULD gilt für
Implementierungen mit Bedenken wegen verdeckter Kanäle; die Nichtwahl des vorangehenden MAY trägt die Einstufung
nicht. Bewusst nicht in dieser Runde geändert: Die CSV ist über den Commit `b8a5277` in der Fußnote von Abschnitt 4.2
verankert, eine Änderung gehört in die Kapitel-6-Runde zusammen mit CSV, Generator und Fußnote. Ergebnisrelevant wird
sie erst, wenn der Autor ein Schutzziel gegen verdeckte Kanäle in den Umfang aufnimmt; sonst bleibt "nicht anwendbar"
mit korrigierter Begründung.

## Sprachrunde: einfache Wörter statt Wortungetüme (Autorenanweisung vom 13.09.2026)

Anweisung: "Implementierungsrepositorium" ist unmöglich; die Sprache einfach halten, solche zusammengesetzten Wörter
entfernen, vereinheitlichen oder vereinfachen, danach erneut prüfen und reviewen.

- Thesisweit ersetzt: "Implementierungsrepositorium" und "Implementierungs-Repository" durch "Repository der
  Implementierung" oder "der Implementierung" (Kapitel 3: Zeilen 186, 247, 250; Kapitel 4: Zeilen 22, 58, Beschriftung
  Tabelle 4.1; Kapitel 6: Zeilen 91, 134, 835, 999, 1096); "Thesis-Repositorium", "Arbeitsrepositoriums" und
  "Repositorium der Arbeit" durch "Repository dieser Arbeit" (Kapitel 4 Fußnote, Kapitel 6 Zeilen 109 und 1098); "des
  Repositoriums" durch "des Repositorys" (Kapitel 6 Zeile 1137).
- Kapitel 4 zusätzlich vereinfacht: "Kernelimplementierungen" zu "Umsetzung im Kernel"; "keine
  Implementierungsplattform" zu "die Bibliothek läuft dort nicht"; "Betriebssystemschnittstellen" zu
  "Systemschnittstellen"; "Verwerfungen durch die Empfängerimplementierung" zu "Verwerfungen im Empfänger"; "aus der
  Empfängerimplementierung" zu "aus der Empfängerausgabe"; "entscheidungsrelevanten" zu "für die Entscheidung
  wichtigen"; "Betriebssystem- oder Schnittstellenverhalten" zu "Verhalten des Betriebssystems oder seiner
  Schnittstellen"; "bedingten Ressourcenempfehlung" zu "bedingten Empfehlung, Ressourcen zu begrenzen". Trennhilfe
  `System\-schnittstellen` ergänzt.
- Geprüft und belassen: eingeführte Fachbegriffe (Surplus Area, Attributionsintervall, Arbeitsindex, Einzelzuordnung,
  Vertrauensgrenze, Pfadstufe) und gewöhnliche Zusammensetzungen (Anforderungskatalog, Messinfrastruktur,
  Netzwerkbyteordnung, Speicherbereinigung).

Neubau: Exitcode 0, keine Warnungen, 95 Seiten, Kapitel 4 auf den physischen Seiten 42 bis 49, Tabellen an ihren
Ankündigungen, Trennungen der Seiten 42 bis 49 geprüft. Dritter Codex-Review: siehe unten.

## Codex-Review 3 (Sprachrunde)

Lauf am 13.09.2026 von 16:26 bis 16:37 Uhr über den Gesamtdiff (29 Hunks) mit zusätzlicher vollständiger Sprachprüfung
von Kapitel 4. Wortlaut im Anhang von `kapitel-4-codex-diffreview-2026-09-13.md`. `git status` in beiden Repositorien
danach ohne Fremdänderungen.

Urteil: "Freigabe: ja. Kapitel 4 ist im geprüften Umfang abgabereif." Alle 29 Hunks richtig; keine Vereinfachung
verändert eine Bedeutung. Neun optionale Vereinfachungen (keine Freigabeauflagen) wurden anschließend übernommen:
"erfasst Aussagen Satz für Satz statt Absatz für Absatz", "erfasste Aussage", "Beteiligung fremder Netze", "allgemeine
Empfangsregeln", "die Bibliothek wird dort nicht eingesetzt", "keine verwaltete Laufzeitumgebung voraussetzen", "bei
unsafe nur unter Bedingungen", "stehen an den Schnittstellen zum Betriebssystem", "weil diese Arbeit die Mechanik von
RFC 9868 selbst untersucht"; dazu eigene: "reales Zugangsnetz" statt "Zugangsnetzkette", "Datagramm mit Optionen"
statt "Optionsdatagramm". Trennhilfen `Speicher\-bereinigung` und `\mbox{Garbage}` gegen die Umbrüche
"Spei-cherbereinigung" und "Garba-ge". Abschließender Neubau: Exitcode 0, keine Warnungen, 95 Seiten, Kapitel 4 auf
den physischen Seiten 42 bis 49, Tabellen an ihren Ankündigungen, Trennungen der Seiten 42 bis 49 geprüft.

Codex bestätigte erneut die Ablehnung von S1-F1 und O1-B18 an den Archivbelegen und stufte A2, A3, A7 und A14 als
Verdeutlichungen ein. Verbleibender Punkt außerhalb von Kapitel 4: Begründung der CSV-Kennung 226 in Kapitel 6 (siehe
Codex-Review 2); Codex' Ersatztext liegt im Anhang und wird in der Kapitel-6-Runde zusammen mit CSV, Generator und
Fußnoten-Commit bearbeitet.

## Identifikation des ausgelieferten Standes

- `thesis/chapters/01_einleitung.tex`
  SHA-256: `c9cf1862b97342732872568ee1d36c56ff9a3974373ae9699cd42806e3d86681`
- `thesis/chapters/03_methodik.tex`
  SHA-256: `31ae430f7bd398a12ec17fa377d3683c90f61e50f6903a2e647b7aaded384ca4`
- `thesis/chapters/04_analyse.tex`
  SHA-256: `15b53a83ee781f8b4d0b932bceb653580ee6fd097f8599915dc4c44e91767727`
- `thesis/chapters/06_evaluation.tex`
  SHA-256: `8b2254237f35d1aae0bc8a07ebd0de9a0a493d2e62e6552de28ade8efe7c21e2`
- `thesis/literatur.bib`
  SHA-256: `6b0fe92b76f89b73b7d7f502c53eac16b92e390fc2a4b4093c99a0145023a938`
- `thesis/main.pdf`
  SHA-256: `1b193757a1eb6c4f6d7eef3d3dd3a092b79987c4d317bbf00f33b8dedaaa5939`

Nicht committet und nicht gepusht; AGENTS.md unverändert gegenüber dem Codex-Stand; Implementierung unverändert.
