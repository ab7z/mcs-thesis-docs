# Codex-Review zu Kapitel 5 vom 13. September 2026 (gpt-6-astra, Effort ultra, read-only)

Wörtliche Ausgabe von `codex exec` (codex-cli 0.154.0, Sitzung 01a09b92-5c32-76b3-8b19-b67722359f6f, 18:20 bis
18:33 Uhr), nur auf 120 Zeichen je Zeile umbrochen. Auftrag: neutrale Vollprüfung des Arbeitsbaums nach den 24
Kriterien aus AGENTS.md,
ohne Diff und ohne Nennung der Workflow-Befunde; Prompt siehe `reviews/kapitel-5-vollpruefung-2026-09-13.md`.

---

**1. Urteil**

GreenCodeDoesntSmell, mein Urteil lautet **Freigabe mit Auflagen**: Der unveränderte Stand ist noch nicht
uneingeschränkt abgabereif. Architektur, Rechenbeispiele, Empfangsverarbeitung und wesentliche Betriebsgrenzen stimmen
mit den geprüften Quellen und dem Code überein. Zu korrigieren sind fehlende Bedingungen, eine ungenaue Beschreibung von
RDOS, ein Verweis aus Kapitel 6 und Verstöße gegen deine Wortregel. Die damaligen Empfangsergebnisse des frühen
Vorversuchs konnte ich ohne ursprüngliches Laufprotokoll nicht unabhängig bestätigen. Geprüft wurde der aktuelle
Arbeitsbaum bei Thesis-HEAD `49dd36a`, Kapiteldatei mit SHA-256-Präfix `c6317f9e48ae`, gegen den sauberen
Implementierungsstand `503c6c83b7c8ec41810c2145054a582cf865e02a`.

**2. Abgaberelevante Befunde**

Im Folgenden bezeichnet **K5** die Datei [thesis/chapters/05_entwurf_implementierung.tex](</Users/ab/Library/Mobile
Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/05_entwurf_implementierung.tex>).
Codepfade beginnen jeweils im Nachbarrepository `../udp-transport-options`.

**2.1 Ausnahme bei der Optionsreihenfolge fehlt**

Stelle: `thesis/chapters/05_entwurf_implementierung.tex:203–208`.

Zitat: „Bei mehreren Einträgen stellt er die Pflichtoptionen vor andere SAFE-Optionen […] und legt die Bytes danach in
einer festen eigenen Reihenfolge ab.“

Befund: NOP und EOL sind von dieser Anforderung ausdrücklich ausgenommen. K5 zählt beide später selbst zu den
Pflichtoptionen und nennt die Ausnahme in Zeilen 633–634 korrekt. Die frühere Erklärung muss dieselbe Einschränkung
enthalten.

Beleg: `literature/rfc9868.txt:793–796`; `src/options/serialize.rs:74–83` fügt NOP zwischen Einträgen und EOL am Ende
ein, die Rangfolge steht dort in Zeilen 173–182.

Vollständiger Ersatz für den Absatz:

```latex
Der gemeinsame Optionskern erzeugt Zustand~2. Er prüft, ob die Option unterstützt wird und ihre Länge stimmt.
Er stellt die Pflichtoptionen außer NOP und EOL vor andere SAFE-Optionen \cite[Sec.~10]{rfc9868}
und ordnet die Einträge nach einer festen eigenen Reihenfolge. Im Beispiel entsteht ein Bereich von acht
Byte; der MDS-Wert \texttt{0x05C0} entspricht 1.472~Byte. Beim Empfang liest derselbe Optionskern
diesen Aufbau wieder zurück.
```

**2.2 Eigener Absenderfilter und Empfangsfrist sind optional**

Stelle: `thesis/chapters/05_entwurf_implementierung.tex:400–411`.

Zitat: „Die heutige Fassung überspringt in einer Empfangsschleife Datagramme mit unlesbarem Header, eigenem Absender
oder nicht passenden Ports.“ Außerdem: „Für diese Schleife gilt eine einzige Gesamtfrist.“

Befund: Der Filter für die eigene Quelladresse arbeitet nur bei gesetztem `own_src`; `Peer` aktiviert ihn ausdrücklich
nicht. Auch die Empfangsfrist ist optional und bei `PeerConfig::new` standardmäßig ausgeschaltet. Die Zusammenfassung
verschiedener Ausgänge als „kein Datagramm“ ist dagegen richtig.

Beleg: `src/socket/recv.rs:32–51,130–159`; `src/api/mod.rs:248–258,279–280,322–334`. Die einschlägigen Tests setzen den
Absenderfilter beziehungsweise die Frist ausdrücklich: `tests/raw_socket_loopback.rs:91–105,110–130`.

Vollständiger Ersatz für Zeilen 400–411:

```latex
Vor dieser Verarbeitung sucht die Socket-Schicht ein passendes Datagramm. Ein Raw Socket sieht auch
fremden UDP-Verkehr. Früher beendete bereits das erste fremde Datagramm den Empfangsaufruf ohne Ergebnis;
eine laufende Messung konnte dadurch still enden. Heute überspringt die Empfangsschleife Datagramme mit
unlesbarem Header oder nicht passenden Ports. Ein Filter für die eigene Quelladresse ist optional;
\texttt{Peer} aktiviert ihn nicht.

Eine gesetzte Empfangsfrist gilt für den ganzen Aufruf; ohne Frist wartet die Schleife bis zu einem Treffer.
Bei gesetzter Frist erhält der Socket vor jedem Leseversuch nur die Restzeit; fremder Verkehr verlängert sie nicht.
Bei Fristablauf meldet die Socket-Schicht \zitat{kein Datagramm}. \texttt{Peer} meldet ebenso Dekodierfehler,
unvollständige Fragmente, Verwerfen und Ausfiltern. Diese Ursachen bleiben dort ununterscheidbar.
```

Die historische Aussage über die frühere Fassung bleibt dabei erhalten; ihre Grenze als Prüfgegenstand steht in
Abschnitt 5 dieses Berichts.

**2.3 RDOS bezeichnet den Anfang der Surplus Area**

Stelle: `thesis/chapters/05_entwurf_implementierung.tex:435–436`.

Zitat: „Dieser Zeiger markiert im wiederhergestellten Datagramm das Ende der Nutzdaten und den Beginn der
Datagrammoptionen.“

Befund: RDOS zeigt genau auf den Anfang der Surplus Area. Bei ungeradem RDOS steht dort zunächst das Pad-Byte vor OCS.
Die bisherige Formulierung verwischt diesen Unterschied; die FRAG-Rechnung selbst ist richtig.

Beleg: `literature/rfc9868.txt:1041–1046`; `src/frag/split.rs:185–195,205–217`.

Vollständiger Ersatz nur dieses Satzes:

```latex
Dieser Zeiger markiert im wiederhergestellten Datagramm das Ende der Nutzdaten und den Beginn der Surplus Area.
```

**2.4 Kapitel 6 verweist auf einen in Kapitel 5 nicht enthaltenen Inhalt**

Stelle: `thesis/chapters/06_evaluation.tex:346–349`.

Zitat: „Ferner überstand das goldene Prüfszenarien-Set aus \chapref{chap:entwurf} den Pfad von mcs nach 1blue
unverändert: elf Szenarien mit 15 Datagrammen und 0 bis 308 Byte Surplus“.

Befund: K5 beschreibt dieses Set nicht. Seine drei Leitbeispiele ersetzen keine Darstellung der elf Prüfszenarien. Die
Korrektur betrifft den eingehenden Verweis in Kapitel 6; Kapitel 5 muss dafür nicht erweitert werden.

Beleg: K5:108–111 und der vollständige Kapiteltext; die Wire-Prüfung wird in `03_methodik.tex:441–449` und
`04_analyse.tex:318–325` erklärt.

Vollständiger Ersatz des betreffenden Satzes:

```latex
Ferner überstand das goldene Prüfszenarien-Set der Wire-Prüfung den Pfad von mcs nach 1blue unverändert:
elf Szenarien mit 15 Datagrammen und 0 bis 308 Byte Surplus, an beiden Enden aufgezeichnet und in elf
von elf Szenarien bestanden; als Vorstufe belegt das Pfadtransparenz, nicht die Zustellung an die Anwendung.
```

**2.5 Die ausdrücklich gesetzte Wortregel ist noch nicht erfüllt**

Stellen und wörtliche Zitate stehen in der folgenden Liste. Dies sind Abweichungen von deinem Sprachmaßstab, keine
Protokollfehler. Ich wende die Regel auch auf kurze Zusammensetzungen wie „Nutzdatenbytes“ an; die Fachbegriffe
„Nutzdaten“ und „Prüfsumme“ bleiben erhalten.

Die Ersatzspalte enthält jeweils den vollständigen LaTeX-Ersatz für genau das zitierte Textstück.

| Stelle in K5 | Wörtliches Zitat | Vollständiger Ersatz |
|---|---|---|
| 74 | `Netz-Systemaufrufen` | `Socket-Aufrufen` |
| 87 | `Netz-Systemaufrufe` | `Socket-Aufrufe` |
| 109 | `Nutzdatenprüfsumme` | `Prüfsumme der Nutzdaten` |
| 117, 211, 244, 380, 452, 570 | `Nutzdatenbytes` | `Byte Nutzdaten` |
| 228 | `IP-Headerprüfsumme` | `Prüfsumme des IP-Headers` |
| 246 | `in Netzwerkbytefolge` | `mit dem höchstwertigen Byte zuerst` |
| 533 | `nach der Nutzdatenposition im wiederhergestellten Datagramm` | `nach der Position innerhalb der Nutzdaten` |

Beleg für die Sprachabweichung sind die genannten Textstellen und die Vorgabe des Prüfauftrags. Die fachliche Bedeutung
bleibt erhalten: APC schützt die Nutzdaten und verwendet die angegebene Bytefolge (`literature/rfc9868.txt:880–896`);
die Pufferposition wird abzüglich des UDP-Headers berechnet (`src/frag/reassembly.rs:612–623`).

Die Pflichtkorrekturen innerhalb von K5 verkürzen den LaTeX-Quelltext zusammen um **245 Zeichen**. Auch nach ihrer
rechnerischen Anwendung überschreitet keine Quelltextzeile 120 Zeichen. Die spätere Seitenzahl ist ohne Neubau nicht
bestätigt.

**Ausdrücklich richtig und beizubehalten**

Das MDS-Beispiel einschließlich `1.472` Byte, neun Byte Surplus, 40 Byte Gesamtlänge und OCS `0xF632` stimmt. Ebenso
stimmen APC `0xE3069283` sowie die FRAG-Aufteilung `2.918 = 1.460 + 1.458` mit Offsets 8 und 1468 und RDOS 2926. Direkte
Belege sind `src/socket/send.rs:38–81`, `src/options/ocs.rs:43–59`, `src/options/typed.rs:328–332` und
`src/frag/split.rs:469–487`.

Richtig sind auch die getrennten Folgen von Datagrammfehlern, Optionsfehlern und APC-Fehlschlägen sowie die ausdrücklich
als eigene Entscheidung bezeichnete strenge Behandlung des erweiterten Längenformats. Die Beschreibung des gemeinsamen
Cache-Limits bei gleichen Ports ist ebenfalls korrekt: Verschiedene Adresspaare teilen die Mengengrenze, ihre
Fragmentdaten werden intern weiterhin über vollständige Schlüssel unterschieden (`src/api/mod.rs:279–286`;
`src/frag/reassembly.rs:241–254`).

**3. Optionale sprachliche Hinweise**

**3.1 Die Bezugspunkte der Längen unmittelbar zeigen**

Stelle: `thesis/chapters/05_entwurf_implementierung.tex:357–358`.

Zitat: „Im Beispiel liegen zwischen \texttt{UDP Length} 17 und \texttt{IP Total Length} 48 elf Byte, beginnend bei Byte
37.“

Befund: Die Zahlen stimmen. Die Formulierung verlangt aber, den unterschiedlichen Ursprung beider Längen gedanklich zu
ergänzen.

Beleg: `literature/rfc768.txt:69–76`; `literature/rfc9868.txt:454–461`; `src/wire/surplus.rs:53–59`.

Vollständiger Ersatz dieses Satzes:

```latex
Im Beispiel beginnt sie bei Byte 37 ($20 + 17$) und umfasst $48 - 37 = 11$ Byte.
```

**3.2 Den Bezug von „sie“ auf MRDS festlegen**

Stelle: `thesis/chapters/05_entwurf_implementierung.tex:445–447`.

Zitat: „Empfangene MRDS-Werte übernimmt die Bibliothek ebenso wenig automatisch in ihre Sendekonfiguration wie
empfangene MDS-Werte. Der Aufrufer muss sie selbst in \texttt{PeerFragmentLimits} übertragen.“

Befund: „sie“ kann beim Lesen beide Wertarten meinen. `PeerFragmentLimits` enthält jedoch ausschließlich die aus MRDS
abgeleitete Größe und Fragmentzahl. Der Vergleich im ersten Satz ist richtig.

Beleg: `src/frag/split.rs:23–27`.

Vollständiger Ersatz des Absatzes:

```latex
Die Bibliothek übernimmt weder MRDS- noch MDS-Werte automatisch in ihre Sendekonfiguration.
Der Aufrufer muss MRDS-Werte selbst in \texttt{PeerFragmentLimits} übertragen.
Auch MRDS lässt sich je Sendung erzeugen.
```

**3.3 Die gemeinte öffentliche Schnittstelle benennen**

Stelle: `thesis/chapters/05_entwurf_implementierung.tex:635–636`.

Zitat: „Die öffentliche Schnittstelle weist wiederholte meldefähige Optionen dagegen ab; FRAG darf schon im Optionskern
nur einmal vorkommen“.

Befund: Im vorherigen Kontext bezeichnet „öffentliche Schnittstelle“ den Typ `Peer`; so ist die Aussage verständlich.
Die ebenfalls öffentliche Funktion `api::build_datagram` erlaubt dagegen gewöhnliche Duplikate. Der konkrete Typname
beseitigt diese Mehrdeutigkeit.

Beleg: `src/api/mod.rs:348–351,581–606`; `src/options/serialize.rs:95–105`.

Vollständiger Ersatz des Satzes:

```latex
\texttt{Peer} weist wiederholte meldefähige Optionen dagegen ab; FRAG darf schon im Optionskern nur
einmal vorkommen \cite[Sec.~10]{rfc9868}.
```

**4. Prüfung nach den 24 Kriterien**

„Geprüft“ bezeichnet den ausgeführten Prüfschritt; festgestellte Mängel stehen in Abschnitt 2.

1. **Fachliche Richtigkeit: geprüft.** Die Aussagen wurden gegen RFC-Primärtext und tatsächliche Verarbeitungspfade
   geprüft; die erforderlichen Präzisierungen betreffen Reihenfolge, Empfangskonfiguration und RDOS.

2. **Quellen und Belege: geprüft.** RFC-Abschnitte, einschlägige Einträge in `literatur.bib` und Implementierungsbelege
   wurden abgeglichen; die Grenze des historischen Messbelegs bleibt unter Kriterium 17 offen.

3. **Verbindlichkeit: geprüft.** Anforderungen, Empfehlungen und lokale Entscheidungen wurden unterschieden; die
   Ausnahme für NOP und EOL fehlt nur an der unter 2.1 genannten Stelle.

4. **Persönlicher Schreibstil: geprüft.** Der Text wurde auf Verständlichkeit, unnötige Anglizismen, Gedankenstriche und
   lange Zusammensetzungen geprüft; die Wortregel erfordert die Änderungen aus 2.5.

5. **Einzelne Sätze: geprüft.** Alle Sätze einschließlich Bildbeschriftungen und Erklärungen zum Listing wurden auf
   Grammatik, Handelnde und Bezüge gelesen.

6. **Zweck und Ursache: geprüft.** Die Zwecke von MDS, APC, Kennungsgenerator, zusätzlichem UDP-Socket und
   Empfangsprüfungen werden verständlich erklärt; die lokale FRAG-Notwendigkeit wird nicht als Entstehungsgrund des RFC
   ausgegeben.

7. **Zusammenhang: geprüft.** Die Aussagen wurden im jeweiligen Absatz und über Abschnittsgrenzen hinweg gelesen;
   insbesondere wurden die allgemeinen Formulierungen mit später genannten Ausnahmen abgeglichen.

8. **Relevanz und Wiederholungen: geprüft.** Der Aufbau entlang der Datenpfade trägt das Kapitel; weitere Kürzungen sind
   möglich, aber keine umfassende Umgestaltung ist erforderlich.

9. **Begriffe: geprüft.** Header, Nutzlast und Nutzdaten stimmen mit `01_einleitung.tex:17–25` überein; die beiden
   optionalen Präzisierungen zu MRDS und `Peer` vermeiden mehrdeutige Bezüge.

10. **Fußnoten: nicht anwendbar.** Kapitel 5 enthält keine Fußnoten.

11. **Ziel und Umfang: geprüft.** Linux, IPv4, Raw Sockets und der Optionsumfang stimmen mit Kapitel 1 und 4 sowie den
    Schlussfolgerungen in Kapitel 7 überein.

12. **Ergebniszuordnung: geprüft.** Leitbeispiele, eigene Implementierungsentscheidungen und der historische Vorversuch
    sind unterscheidbar; aus den Beispielen wird keine allgemeine Pfaddurchlässigkeit abgeleitet.

13. **IPv4, MTU und Fragmentierung: geprüft.** Headerlängen, Kapazitäten, Fragmentzahlen, Offsets und Reassemblierung
    wurden nachgerechnet und am Code sowie an passenden Testquellen geprüft.

14. **UDP und Prüfsummen: geprüft.** Schutzbereiche, Pseudo-Header und Nullwerte stimmen mit
    `literature/rfc768.txt:69–95` und den einschlägigen RFC-9868-Regeln überein.

15. **Surplus Area und Optionen: geprüft.** Längen, Ausrichtung, Padding, OCS, TLV, Duplikate, SAFE/UNSAFE und Fehlerfolgen wurden geprüft; die Behandlung des Überlängenfalls entspricht auch der beim RFC Editor angezeigten Korrektur durch [Erratum 8834](https://www.rfc-editor.org/rfc/inline-errata/rfc9868.html).

16. **Betriebssystem und Netzpfad: geprüft.** Bibliothekscode und Kernelwirkungen wurden getrennt geprüft; `IP_HDRINCL`, Empfangsreihenfolge, Rechte und MTU-Grenze sind in [Linux man-pages 6.18, raw(7), Seiten 3811–3813](https://www.kernel.org/pub/linux/docs/man-pages/book/man-pages-6.18.pdf#page=3811) belegt.

17. **Messbedingungen: offen.** Generator, MTU-Konfiguration und Auswertungslogik des Vorversuchs sind nachvollziehbar;
    ein ursprüngliches Laufprotokoll für die berichteten Empfangsergebnisse wurde nicht gefunden.

18. **Methodik: geprüft.** Die Bibliothek wird konsistent als Prüfgegenstand für FF1 und Messmittel für FF2 eingeordnet;
    normative Vorgaben und lokale Grenzen bleiben getrennt.

19. **Aussagekraft der Nachweise: geprüft.** K5 behauptet weder einen Beweis des Rust-Codes durch Lean noch unabhängige
    Bestätigung durch gemeinsam erzeugte Testdaten; die begrenzte Erfassung des Vorversuchs ist korrekt beschrieben.

20. **Entwicklungs- und Prüfablauf: offen.** Aktuelle Verarbeitung und vorhandene Testquellen wurden geprüft; die
    Aussage über das Verhalten einer früheren Fassung wurde ohne Untersuchung der ausdrücklich ausgeschlossenen
    Änderungshistorie nicht unabhängig bestätigt.

21. **Abbildungen, Tabellen und Verweise: geprüft.** Alle vier Abbildungen und Listing 5.1 stimmen mit Text und Code
    überein; der unter 2.4 genannte Verweis aus Kapitel 6 trifft seinen angekündigten Inhalt nicht.

22. **PDF-Lesbarkeit: geprüft.** Die physischen Seiten 50 bis 61 der [vorhandenen PDF](</Users/ab/Library/Mobile
    Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/main.pdf>) wurden vollständig visuell
    geprüft; es wurden keine Überlagerungen oder abgeschnittenen Inhalte festgestellt.

23. **Silbentrennung: geprüft.** Alle tatsächlichen Trennungen dieser zwölf Seiten einschließlich Beschriftungen wurden
    kontrolliert; auch die Trennungen über Seiten hinweg sind korrekt.

24. **Abschlusskontrolle: geprüft.** Kapiteltext und PDF wurden abgeglichen, ihre Hashwerte blieben während der Prüfung
    unverändert, und `main.log:1893` bestätigt die vorhandene PDF mit 95 Seiten und 920.322 Byte; Fehler, undefinierte
    Verweise sowie Overfull-/Underfull-Warnungen wurden im Log nicht gefunden.

**5. Was ich nicht prüfen konnte**

Für K5:340–349 bestätigt der Generator tatsächlich **97 Fälle**, davon **69 innerhalb der MTU**, **28 darüber** und **42
innerhalb der MTU mit abweichend vorgegebener IPv4-Gesamtlänge** (`examples/support/common.rs:72–135`). Das
Empfangsprogramm erfasst Längen und Surplus-Bytes und vergleicht keinen vollständigen Empfangspuffer
(`examples/spike_server.rs:168–175,209–221`). Diese Zahlen sind daher kein festgestellter Rechenfehler.

Ein ursprüngliches Laufprotokoll der damaligen Ausführung fand sich jedoch weder in den untersuchten lokalen
Textbeständen noch bei der Suche in den elf Messarchiven. Die dokumentierte Durchführung in
`docs/plan/steps/00b-spike.md` ersetzt für diese Prüfung keinen unabhängigen Rohbeleg. Ob damals genau alle berichteten
Fälle ankamen, bleibt deshalb offen.

Die Änderungshistorie, eine erneute Linux-Ausführung, Tests und Messkampagnen wurden nicht geprüft beziehungsweise
ausgeführt. Die übrigen Kapitel wurden als Zusammenhang von K5 gelesen; daraus folgt keine neue vollständige Freigabe
dieser Kapitel.

Es wurden keine Dateien angelegt oder verändert und kein Build ausgeführt. Deshalb sind die Ersatztexte inhaltlich und
hinsichtlich ihrer Quelltextlänge geprüft, ihre späteren PDF-Umbrüche und die Einhaltung von höchstens zwölf
Kapitelseiten aber noch nicht bestätigt.


