# Kapitel 3: Schreibstil und Leserlichkeit

**Umsetzung am 10. September 2026:** Die Empfehlungen wurden auf Anweisung des Autors in Kapitel 3
übernommen. Die folgenden Befunde dokumentieren den ursprünglichen Prüfstand vor dieser Änderung;
Originalzitate, Zeilen- und Seitenangaben beziehen sich auf diesen Stand. Die Umsetzung ist am Ende
festgehalten.

Stand: 10. September 2026. Geprüft wurden alle Prosasätze in
`thesis/chapters/03_methodik.tex`, einschließlich Fußnoten, Tabellen und Diagrammbeschriftungen.
Zusätzlich wurden alle elf Kapitelseiten der aktuellen PDF angesehen (PDF-Seiten 31 bis 41,
Druckseiten 25 bis 35). Kapiteltext und PDF wurden nicht verändert.

Die Prüfung verwendet den aus den Rückfragen zu Kapitel 2 abgeleiteten Maßstab: konkrete Aussagen,
erkennbare Handelnde und Zwecke, verständliche Begriffe sowie passende Nachbarsätze. Sie ist keine
erneute vollständige Faktenprüfung der zitierten Forschungsfälle oder des Implementierungsstands.
Die folgenden Befunde sind sprachliche Empfehlungen, keine Liste nachgewiesener fachlicher Fehler.

## Einschätzung

Die Gliederung ist nachvollziehbar. Die Rollen von Normauswertung, Implementierung, Messung und Prüfung
werden sinnvoll getrennt. Viele Absätze können bleiben. Eine vollständige Neufassung oder eine neue
Gliederung ist aus dieser Prüfung nicht begründet.

Gezielte Änderungen sind vor allem in Abschnitt 3.2 und beim Prüfskript in Abschnitt 3.4.2 sinnvoll.
Dort erschweren abstrakte Formulierungen, wechselnde Bezeichnungen und einzelne unklare Bezüge das Lesen.
Abschnitt 3.5 ist bereits knapp und verständlich. Die Grenzen der Nachweise sollen bei jeder Kürzung erhalten
bleiben, insbesondere die Trennung von Modellbeweis und Rust-Implementierung sowie von vorgesehenen und
nachweislich ausgeführten Prüfungen.

## Was bleiben sollte

- **Kapitelauftakt:** Die Einsatzgebiete der Sprachmodelle sowie Prüfung und Verantwortung werden konkret genannt.
- **Abschnitt 3.1:** Die neun Fälle haben eine benannte Funktion. Die Einschränkung, dass sie keine systematische
  Literaturübersicht oder allgemeine Wirksamkeitsaussage ergeben, ist sinnvoll. Daraus folgt kein Anlass, den
  ganzen Abschnitt zu streichen.
- **Abschnitt 3.2:** Die unterschiedliche Rolle der Bibliothek für FF1 und FF2 ist klar erklärt. Tabelle 3.1
  und die Reihenfolge von Anwendbarkeit, MUST, SHOULD und gewähltem MAY sollten erhalten bleiben.
- **Zuordnung der Nachweise, [Zeile 343](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:343>):** RFC-Aussagen, Implementierung, Pfadbefunde und Literatur werden jeweils
  passenden Nachweisen zugeordnet. Auch die begrenzte Aussage eines Hashwerts ist verständlich erklärt.
- **Abschnitt 3.4.1:** Der Property-Test wird anschaulich erklärt. Das Beispiel gemeinsamer Formatannahmen
  von Implementierung und Test ist nützlich. Die Einschränkung des Lean-Nachweises ist notwendig.
- **Abschnitt 3.5:** Der kurze Schluss unterscheidet technische Ergebnisse von der nicht vollständig
  reproduzierbaren Folge von Modellausgaben und führt sinnvoll zu Kapitel 4.

## Konkrete Verständnishürden und Vorschläge

### K01: Das Prüfprogramm direkt benennen

**Stelle:** [Zeile 32](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:32>), FunSearch.

**Original:** „Ein Sprachmodell erzeugte ausführbare Programmkandidaten, die ein ausführbarer Auswerter
 einzeln bewertete; das Ergebnis gilt nur für die kodierte Bewertungsfunktion.“

„Ausführbarer Auswerter“ benennt die prüfende Instanz unnötig indirekt. Ein verständlicher Ersatz mit
unveränderter Einschränkung wäre:

> Ein Sprachmodell erzeugte ausführbare Programmkandidaten. Ein Prüfprogramm bewertete jeden Kandidaten;
> das Ergebnis gilt nur für die im Programm festgelegte Bewertungsfunktion.

Der Quellenbeleg bleibt an dieser Aussage.

### K02: Den Bezug von „gemeinsamer“ klären

**Stelle:** [Zeile 41](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:41>), Zeta-Schranke.

**Original:** „Ein Modell lieferte ein mathematisches Ergebnis samt gemeinsamer Lean-Formalisierung …“

Es bleibt offen, mit wem oder wofür die Formalisierung gemeinsam entstand. Falls nur die Zugehörigkeit
zum Ergebnis gemeint ist, passt „samt zugehöriger Lean-Formalisierung“. Falls eine Zusammenarbeit gemeint
ist, müssen deren Beteiligte aus der Quelle hervorgehen. Diese Bedeutung darf bei einer Überarbeitung
nicht geraten werden. Die anschließenden Angaben zu den Prüfenden und zum fehlenden dokumentierten
Blindvergleich bleiben erhalten.

### K03: Kontroll- und Optionsdatagramm unterscheiden

**Stelle:** [Zeile 162](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:162>).

**Original:** „Ein Szenario kann ein einzelnes Kontroll- und Optionsdatagramm, mehrere Wiederholungen
oder bei FRAG mehrere Wire-Datagramme enthalten.“

Der Singular lässt offen, ob ein Datagramm beide Rollen erfüllt oder je ein Datagramm gemeint ist.
Abschnitt 4.3 beschreibt Kontroll- und Optionsverkehr; Kapitel 6 beschreibt deren Vergleich.
Deutlicher wäre:

> Ein Szenario kann je ein Kontroll- und ein Optionsdatagramm, mehrere Wiederholungen oder bei FRAG
> mehrere übertragene Datagramme enthalten.

Damit bleibt die Unterscheidung zwischen Szenario und Zahl der übertragenen Datagramme erhalten.

### K04: Den gemeinsam bewerteten Endpunkt verständlich beschreiben

**Stelle:** [Zeile 171](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:171>).

**Original:** „Der neben der Erfüllbarkeit berichtete Umsetzungsstand bewertet den Endpunkt aus
Bibliothek und aufrufender Schicht …“

Der Einschub und die abstrakte Bezeichnung verdecken den Prüfgegenstand. Vorschlag:

> Neben der Erfüllbarkeit wird der Umsetzungsstand berichtet. Dafür werden die Bibliothek und die
> Software, die sie aufruft, gemeinsam bewertet; die zugehörige Regel definiert Abschnitt 6.3.

Im LaTeX-Ersatz bleibt statt der ausgeschriebenen Abschnittsnummer `\secref{sec:soll-ist}` erhalten.

### K05: Quellen und Dokumente mit Namen nennen

**Stellen:** [Zeile 187](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:187>) und [Zeile 192](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:192>).

„Zwei Nachbarquellen bleiben davon getrennt“ führt eine nicht erklärte Kategorie und einen unklaren
Rückbezug ein. Direkt wäre:

> RFC 9869 und die Errata zu RFC 9868 werden gesondert behandelt.

Die nachfolgenden unterschiedlichen Entscheidungen bleiben ausdrücklich erhalten: RFC 9869 liegt
außerhalb des Implementierungsumfangs, EID 8834 ist angewendet und EID 8708 zurückgestellt.
Bei EID 8708 sollte „für eine spätere Dokumentausgabe“ durch „für eine spätere Ausgabe des RFC“ ersetzt
werden, damit kein Bezug auf eine spätere Thesisfassung entsteht. Der vorhandene Bibliografieeintrag
beschreibt diesen Status als „Held for Document Update“.

### K06: Die Normauswertung ohne „Zuflüsse“ erklären

**Stelle:** [Zeile 239](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:239>) bis zum Ende des Absatzes.

„Zwei getrennt gehaltene Zuflüsse“, „normative Lesung“ und „die Kontrollzahl sichert den normativen
Zufluss … ab“ beschreiben die Arbeit abstrakter als nötig. Konkreter wäre:

> Abbildung 3.2 zeigt die beiden Grundlagen des Maßstabs: die Anforderungen des RFC unter
> Berücksichtigung der Errata und die davon getrennt erfassten eigenen Projekt-, Schnittstellen- und
> Plattformvorgaben. Die eigenen Vorgaben sind ausdrücklich gekennzeichnet. Diese Trennung verhindert,
> dass eine lokale Entwurfsentscheidung nachträglich als Forderung des RFC erscheint. Die Zahl der
> markierten Absätze wurde mit zwei Zählverfahren geprüft: Die Erstzählung ergab 96 Absätze; erst das
> zweite Verfahren deckte den Fehler auf. Zählung und Einordnung erfolgten beim Lesen des RFC-Texts.
> Ein Werkzeug zur automatischen Zerlegung des Texts wurde dafür nicht eingesetzt.

Der letzte Satz beschränkt die Aussage auf diese Arbeit. Das ursprüngliche „gibt es nicht“ kann dagegen
als allgemeine Aussage über die Existenz solcher Werkzeuge gelesen werden. Der Abbildungsverweis bleibt
im LaTeX-Text ein `\figref`.

### K07: „Vertragsdatei“ durch die konkrete Funktion erklären

**Stelle:** [Zeile 247](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:247>) bis zum Ende des Absatzes.

Die Funktion der versionierten Dokumente ist sinnvoll, „Vertragsdatei“ und „Vertragsdokumente“ sind
jedoch nicht eingeführt. Gemeint sind Dateien mit Arbeitsvorgaben. Vorschläge:

- „Die zentrale Datei mit Arbeitsvorgaben …“ statt „Die zentrale Vertragsdatei …“.
- „Die Dokumente halten den Wissensstand über die Arbeitssitzungen hinweg fest und dienen als Maßstab
  für die Prüfung der Modellausgaben.“
- „Ein Abgleich am Primärtext fand vier falsche RFC-Angaben in vier Dokumenten mit Arbeitsvorgaben zugleich.“

Die Fußnote mit Commit und Dateipfaden bleibt erhalten. Auch der konkrete Vier-Fehler-Befund bleibt;
nur die bildhafte Einleitung „Der Preis dieser mehrfachen Ablage“ kann entfallen.

### K08: Menschliche Freigabe und Grenzen der Historie direkt benennen

**Stelle:** [Zeile 259](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:259>) bis zum Ende des Absatzes.

„Masterplan mit einem Menschen in der Schleife“ erklärt die menschliche Aufgabe nicht. Direkt wäre:

> Die Roadmap beschreibt einen Gesamtplan mit menschlicher Freigabe: Jeder Schritt soll mit einem
> geprüften Commit abgeschlossen werden.

Der Folgesatz zu Plan, Maßstab, Abschlusskriterien und Freigabe bleibt sinnvoll. Für die beiden Grenzen
ist „Die Sammelcommits verschmelzen die innere Reihenfolge“ schwer verständlich. Ersatz:

> Aus den Sammelcommits lässt sich die Reihenfolge der Arbeiten innerhalb eines Schritts nicht
> rekonstruieren. Die Commit-Historie zeigt außerdem nicht, welchen Beitrag Autor und Werkzeug zu einer
> einzelnen Änderung geleistet haben.

Damit bleiben beide Grenzen der Nachvollziehbarkeit erhalten.

### K09: Zweck der Herstellertrennung und Rolle des Zweitprüfers klären

**Stelle:** [Zeile 337](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:337>) bis zum Ende des Absatzes.

„Vollständig gleiche Fehlermuster verringern“ lässt offen, welches Risiko kleiner werden soll. Vorschlag:

> Der Einsatz von Modellen verschiedener Hersteller soll das Risiko verringern, dass ihre Fehlermuster
> vollständig übereinstimmen. Unabhängige Prüfungen sind damit jedoch nicht belegt.

Auch „zählen dann nicht als Prüfung desselben Ergebnisses“ hat einen unklaren Bezug. Vorschlag:

> Wenn der Zweitprüfer selbst Änderungen vornimmt, braucht er dafür einen eigenen, vom Autor freigegebenen
> Auftrag. Diese Änderungen zählen nicht als getrennte Zweitprüfung des bearbeiteten Ergebnisses.

Die vorangehende Abgrenzung einer Prüfung durch dasselbe Modell bleibt erhalten.

### K10: Die Handelnden bei den Verfahrensregeln nennen

**Stelle:** [Zeile 401](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:401>).

**Original:** „Die Antworten der Tabelle sind Verfahrensregeln, und Verfahrensregeln führen Menschen
und Modelle aus. Ohne weiteres Zutun urteilen nur die ausführbaren Prüfungen und der Beweisprüfer.“

Die ungewöhnliche Satzstellung und das Wort „urteilen“ erschweren die Zuordnung. Vorschlag:

> Menschen und Modelle müssen die Verfahrensregeln aus der Tabelle anwenden. Ausführbare Prüfungen und
> der Beweisprüfer liefern nach ihrem Start automatisch ein Ergebnis.

Der folgende Übergang zur Testarchitektur bleibt erhalten. Die fachliche Reichweite dieser Ergebnisse
wird weiterhin in Abschnitt 3.4.1 begrenzt.

### K11: Implementierung und Entwicklungsprozess unterscheiden

**Stelle:** [Zeile 412](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:412>).

„Prüfung der Entwicklung“ kann eine Untersuchung des Entwicklungsprozesses meinen; „Nachweisseite von
FF1“ löst diese Mehrdeutigkeit nicht auf. Vorschlag:

> Dieser Abschnitt beschreibt, wie die Implementierung während der Entwicklung für FF1 geprüft wird.

Die anschließende Trennung von Entwicklungstests und Pfadmessungen erfüllt eine eigene Aufgabe und bleibt.

### K12: Den gemeinsamen Fehler konkret erklären

**Stelle:** [Zeile 440](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:440>).

**Original:** „Ein gemeinsamer Entwurfsfehler in diesen Annahmen kann deshalb jeden Test bestehen.
Die Wire-Prüfung verringert diese Selbstbezüglichkeit …“

Gemeint sind Tests mit denselben fehlerhaften Formatannahmen. Das sollte ausdrücklich gesagt werden:

> Tests, die auf denselben fehlerhaften Annahmen beruhen, können den Entwurfsfehler deshalb übersehen.
> Bei der Wire-Prüfung zeichnet `tcpdump` die tatsächlich gesendeten Bytes für eine getrennte Auswertung auf.

Der folgende Satz zum getrennten Python-Programm erklärt diese Auswertung. Das vorausgehende Beispiel
mit Kind-Werten und Längenkonstanten bleibt erhalten.

### K13: Den Absatz zum Prüfskript neu formulieren

**Stelle:** [Zeile 449](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:449>) bis einschließlich des Satzes zu den 18 Prüfläufen.

Dies ist die deutlichste sprachliche Schwachstelle des Kapitels. „Das lokale Gate pre-pr.sh Skript fährt“
ist grammatisch unklar. „Test-Bahnen“, „Lean-Tor“, „Bahnen“ und „Prüfläufe“ wechseln ohne Nutzen die
Bezeichnung. „aka achim“ passt nicht zum sonstigen wissenschaftlichen Deutsch.

Vorschlag mit unveränderter Zahl und Aufteilung der Prüfungen:

> Das lokale Prüfskript `pre-pr.sh` führt neun feste Prüfläufe aus: Formatierung, statische Analyse,
> Dokumentationsbau, Tests mit Property-Fällen, Prüfung des eigenen Auswerters, Lean-Prüfung und drei
> Prüfläufe auf einem separaten Linux-Zielsystem. Dieses Zielsystem ist die lokale virtuelle Maschine
> `achim`. Dort werden die Cross-Kompilierung, die Raw-Socket-Integration mit Root-Rechten und die
> tatsächlich gesendeten Pakete geprüft. Für jedes Fuzz-Ziel kommt ein weiterer Prüflauf hinzu.
> Insgesamt ergeben sich die 18 Prüfläufe aus Abbildung 3.3.

Die nachfolgenden Sätze zur CI und zu den zwei angefragten Prüfungen können bleiben. Im LaTeX-Text bleibt
`\figref{fig:stepzyklus}` erhalten.

### K14: Durchführung und Nachweis auseinanderhalten

**Stelle:** [Zeile 530](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:530>).

**Original:** „Ob eine Prüfung tatsächlich stattfand, entscheidet allein ihre Protokollierung …“

Die Protokollierung entscheidet nicht über das tatsächliche Stattfinden. Sie ist die hier geforderte
Grundlage dafür, eine Durchführung nachzuweisen. Vorschlag:

> In dieser Arbeit gilt eine Prüfung nur dann als belegt, wenn sie protokolliert ist. Die Grenzen dieser
> Protokollierung behandelt der folgende Abschnitt.

Das passt zur anschließenden Aussage, dass die Belastbarkeit der Prozessbeschreibung von den vorhandenen
Protokollen abhängt. Der Satz soll keine allgemeine Behauptung darüber aufstellen, welche anderen Formen
von Nachweisen grundsätzlich möglich sind.

### K15: Die Diagramme sprachlich an den Fließtext angleichen

**Stellen:** [Zeile 282](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:282>), [Zeile 286](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:286>), [Zeile 288](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:288>), [Zeile 498](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:498>) und [Zeile 500](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:500>).

- „Step-Datei: Plan und Definition of Done“ kann „Schrittdatei: Plan und Abschlusskriterien“ heißen.
- „Parsefläche“ ist nicht erklärt. Der Text sollte konkret benennen, dass neu hinzugekommene Parserteile
  ebenfalls Property-Tests und ein Fuzz-Ziel benötigen; bei der Umsetzung die Bedeutung der Arbeitsvorgabe erhalten.
- „lokales Gate“ kann „lokale Prüfung“ heißen.
- „Kreuzbau, Rohsocket, Wire-Prüfung“ sollte dieselben Bezeichnungen wie der Fließtext verwenden:
  „Cross-Kompilierung, Raw-Socket-Test, Wire-Prüfung“.
- „Host-Stufen“ kann „Lokale Prüfungen“ heißen.

Die Begriffe „Parsefläche“ und die wechselnden Namen für dieselben Prüfungen erschweren den Bezug
zwischen Text und Abbildung. Die übrigen Vorschläge sind optionale sprachliche Vereinheitlichungen.
Der Platzbedarf muss nach einer Änderung in der gerenderten Abbildung geprüft werden.

## Optionale Straffungen

Diese Stellen sind verständlich und müssen nicht allein für eine höhere Änderungszahl umgeschrieben werden.

- **[Zeile 11](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:11>), [Zeile 61](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:61>) und [Zeile 170](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:170>):** Die Reihenfolge „Regeln vor Ergebnisbewertung“ wird mehrfach angekündigt.
  Der methodische Grund soll bleiben; zusätzliche Sätze über die Anordnung der Kapitel und Absätze können entfallen.
- **[Zeile 17](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:17>):** Statt „nicht beiläufig erwähnt, sondern …“ direkt sagen, dass der KI-Einsatz offengelegt wird
  und Regeln zur Prüfung der Ergebnisse festgelegt werden.
- **[Zeile 50](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:50>), Bun-Migration:** Den langen Satz in drei Sätze teilen: Erzeugung und Prüfung durch Modelle;
  übersehener Fehler; Meldung nach dem Merge und Aufnahme von Miri. Alle Einschränkungen und Belege erhalten.
- **[Zeile 181](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:181>):** „Quellenverweis“ statt des abstrakteren „Zitatmarkers“ verwenden. Die Pflicht zur Abschnittsangabe bleibt.
- **[Zeile 265](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:265>):** „Denselben Aufbau hat der Plan“ kann entfallen; der folgende Satz beschreibt den Aufbau unmittelbar.
- **[Zeile 349](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:349>):** Der Vergleich mit unerfahrenen Entwicklern kann entfallen. Die Prüfpflicht und die drei
  konkreten Arbeitsregeln tragen den Gedanken bereits.
- **[Zeile 366](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:366>) und [Zeile 424](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:424>):** Die Wiederholung der Überschrift sowie „Drei weitere Prüfmittel tragen besondere
  Aufgaben“ können entfallen; Tabelle beziehungsweise folgende Definitionen liefern den Inhalt.
- **[Zeile 423](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:423>) bis [Zeile 435](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:435>):** Property-Tests, Fuzzing und Lean in getrennten Absätzen erklären. Den Fuzzing-Satz
  mit Definition und Funktionsweise teilen. Die Erklärungen selbst und ihre Grenzen sind sinnvoll.
- **[Zeile 430](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:430>):** Sachlicher als „Fuzzing findet Fehler, aber keine Fehlerfreiheit“ ist: „Fuzzing kann Fehler
  finden, aber keine Fehlerfreiheit beweisen.“ Die lokale Pflicht und der Ausschluss aus der CI bleiben.
- **[Zeile 461](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/03_methodik.tex:461>):** Die abstrakte Ankündigung zur „Grenze ihrer technischen Erzwingung“ kann entfallen; nach der
  Abbildung wird die fehlende technische Merge-Bedingung konkret erklärt. Die Erklärung der Diagrammsymbole bleibt.

## Absatzfolge und PDF

Die technischen Abbildungen und Tabellen sind lesbar und nicht abgeschnitten. Folgende Umbrüche könnten
bei einer ohnehin vorgenommenen Überarbeitung verbessert werden:

- Der AlphaProof-Listenpunkt endet mit einer einzelnen Restzeile auf PDF-Seite 32.
- Abbildung 3.1 steht auf PDF-Seite 33 innerhalb der über den Seitenwechsel laufenden Erläuterung:
  Der Satz beginnt auf Seite 32 mit „Für FF1 …“ und endet erst nach der Abbildung mit „Messmittel“.
  Eine gemeinsame Platzierung von Erläuterungsabsatz und Abbildung würde die Zuordnung erleichtern.
- Auf PDF-Seite 35 beginnt der Absatz zum Plan mit nur einer Zeile vor dem Seitenwechsel.
- Tabelle 3.3 steht allein auf PDF-Seite 38; ihre Erklärung steht bereits auf Seite 37.
  Das ist kein Satzfehler. Bei einer Kürzung sollte ihre Platzierung näher an der Erklärung geprüft werden.

Diese Layoutpunkte rechtfertigen keine inhaltliche Neufassung. Nach Textänderungen ist der aktuelle Umbruch
neu zu beurteilen; die genannten Seitenzahlen gelten für den hier geprüften Stand.

## Empfehlung

Grundstruktur, Tabelle 3.1, zentrale Erklärungen und wissenschaftliche Einschränkungen beibehalten.
Die konkreten Verständnishürden gezielt überarbeiten, besonders K06, K08, K10, K13 und K14.
Optionale Straffungen nur übernehmen, wenn der Absatz dadurch leichter lesbar wird. K02 benötigt vor
seiner Umsetzung eine eindeutige Klärung des gemeinten Bezugs; eine Beteiligung darf nicht erfunden werden.

## Umsetzung

Die Empfehlungen K01 bis K15 wurden in Kapitel 3 umgesetzt. Die optionalen Straffungen wurden dort
übernommen, wo sie Wiederholungen oder unnötige Einleitungen beseitigen. Die Gliederung, Tabelle 3.1,
Quellenbelege, Verweise und Einschränkungen der Nachweise blieben erhalten.

Bei drei Stellen wurde der Vorschlag anhand der zugrunde liegenden Quellen präzisiert:

- **K02:** Die Lean-Formalisierung entstand durch Zusammenarbeit des Modells mit dem Anthropic-Mitarbeiter
  Eric Easley. Dieser Beteiligte wird nun ausdrücklich genannt. Die Primärquelle nennt ihn im letzten
  Absatz von „Claude’s methodology“:
  [Anthropic-Beitrag](https://www.anthropic.com/research/riemann-zeta).
  Die Einschränkung zum Blindvergleich lautet nun „ein Blindvergleich ist nicht dokumentiert“.
- **K13:** Die Cross-Kompilierung erfolgt auf dem Entwicklungsrechner; die Testprogramme laufen auf
  `achim`. Der Absatz und das Sequenzdiagramm unterscheiden diese Orte. Die neun festen Prüfläufe und
  die neun Fuzz-Ziele wurden in `scripts/pre-pr.sh` des Implementierungs-Repositorys geprüft;
  `docs/plan/ROADMAP.md` und `scripts/vm-ubuntu-server.sh` bestätigen den Ausführungsort.
- **K15:** Die Arbeitsvorgabe in `CLAUDE.md` des Implementierungs-Repositorys umfasst neue oder geänderte
  Paketverarbeitung, einschließlich OCS, Empfangspipeline und FRAG. Deshalb wurde „Parsefläche“ durch
  diese Beschreibung ersetzt. Property-Tests und Fuzz-Ziele sind zu ergänzen; bestehende Fuzz-Ziele
  können dabei erweitert werden.

Abbildung 3.1 und Tabelle 3.3 wurden so platziert, dass die Abbildung keinen Erklärungssatz mehr
unterbricht und die Tabelle mit dem anschließenden Text auf derselben Seite steht.

Validierung: vollständiger Build mit drei LaTeX-Läufen, Biber und makeglossaries erfolgreich; keine
LaTeX- oder Bibliografiewarnungen. Alle elf Kapitelseiten sowie beide angrenzenden Seiten wurden visuell
geprüft. Quellenbelege, Verweise und Labels stimmen mit dem Ausgangsstand überein. Außerhalb von Kapitel 3
änderte sich nur die Seitenzahl von Abbildung 3.4 im Abbildungsverzeichnis; die Thesis hat weiterhin 95 Seiten.
