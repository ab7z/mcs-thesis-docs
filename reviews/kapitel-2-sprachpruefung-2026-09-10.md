# Kapitel 2: Sprachprüfung Satz für Satz

Stand: 10. September 2026. Geprüft wurde der aktuelle Text nach den drei zuletzt umgesetzten Korrekturen.
Der Kapiteltext und die PDF bleiben unverändert. Die Ersatzfassungen in diesem Bericht sind Vorschläge.

Diese Prüfung betrifft Verständlichkeit, Wortwahl und Zusammenhang. Die vorangegangene fachliche Prüfung
wird dadurch nicht ersetzt. Eine sprachliche Empfehlung bedeutet nicht, dass die ursprüngliche Aussage
fachlich falsch ist. Die Vorschläge müssen insbesondere die bereits geklärten Ausnahmen zu UDP-Prüfsumme,
OCS, FRAG, UNSAFE und vorgeschalteten Filtern erhalten.

## Maßstab aus deinen Rückmeldungen

Das folgende Stilprofil ist aus deinen Fragen in dieser Aufgabe abgeleitet, nicht aus einer allgemeinen
Vorstellung davon, wie eine Thesis klingen sollte.

| Deine Rückmeldung im Chat | Maßstab für diese Prüfung |
|---|---|
| Zum Pseudo-Header fehlt dir, „wofür man sie braucht oder was UDP oder wer auch immer damit macht“. | Den Zweck erklären und nennen, wer welche Daten verwendet. |
| Zur Prüfsumme fragst du mehrfach nach dem Warum, nicht nur nach der Bedeutung des Nullwerts. | Definition, Zweck und Grund einer Entscheidung unterscheiden. Eine Definition allein beantwortet keine Warum-Frage. |
| Die Fußnote zur „Fehlersuche“ war für dich „noch verwirrender als vorher“. | Eine Fußnote soll die konkrete Frage kurz beantworten und möglichst keine zusätzlichen Begriffe benötigen. |
| Bei „Demultiplexierung“ fragst du nach Bedeutung und Relevanz für die Arbeit. | Die benötigte Funktion verständlich erklären. Einen Fachbegriff nicht allein deshalb aufnehmen, weil er fachlich korrekt ist. |
| Die Aussagen zu anderen Protokollen bieten aus deiner Sicht „keinen Mehrwert“ und schaffen Raum für weitere Fragen. | Vergleiche, Hintergrundwissen und Einleitungssätze nur behalten, wenn sie den folgenden Gedanken tragen. |
| „UDP Length bleibt eine Länge“ und die „zusätzliche Bedeutung“ waren dir zu schwer lesbar. | Konkrete Größen, Positionen und Handlungen nennen statt abstrakt über die Bedeutung von Feldern zu sprechen. |
| Bei Änderungen sollen die Sätze vorher und nachher beachtet werden. | Einen Satz nicht isoliert verbessern: Bezug, Übergang und Funktion im Absatz müssen erhalten bleiben. |

Daraus folgt kein Verbot von Fachbegriffen, längeren Sätzen oder Wiederholungen. Begriffe wie UDP-Header,
Surplus Area und OCS gehören zum Thema. Auch eine Wiederholung ist sinnvoll, wenn sie eine neue Folge
erklärt oder Sender und Empfänger klar unterscheidet. Problematisch sind unklare Bezüge, mehrere neue
Regeln in einem Satz, unnötige Nebenpfade und bildhafte Formulierungen anstelle einer technischen Aussage.

## Ergebnis der Einzelprüfung

Der Text passt noch nicht durchgängig zu dem aus deinen Rückmeldungen abgeleiteten Stil. Die Gliederung
ist nachvollziehbar, und viele konkrete Erklärungen sind verständlich. Änderungsbedarf liegt vor allem bei langen
Regelsätzen,
unklaren Bezügen, zusätzlichen Fachbegriffen und bildhaften oder wiederholenden Einleitungen.

Geprüft wurden **265 Sätze einschließlich vier Fußnotensätzen sowie 15 zusätzliche nominale Definitionen
und Unterschriften**, insgesamt 280 Einheiten. Dazu gehören auch Sätze mit einer nachfolgenden Formel oder
einem Doppelpunkt vor einer Abbildung. Semikolons wurden nicht als Satzgrenzen behandelt.

| Ergebnis | Einheiten | Bedeutung |
|---|---:|---|
| Belassen | 153 | Verständlich und im Zusammenhang sinnvoll. |
| Konkrete Verständnishürde | 65 | Bezug, Handlung, Begriff oder Regelabfolge sollte klarer werden. |
| Optionale Straffung | 62 | Bereits verständlich; Kürzung oder sachlichere Wortwahl ist möglich. |

Die Änderungen teilen sich in 105 Vorschläge zum Vereinfachen und 22
optionale Streichvorschläge auf. Diese Zahlen sind **keine Liste fachlicher Fehler oder Abgabeblocker**.
Vor allem die optionalen Vorschläge sind keine Aufforderung, möglichst viele Sätze umzuschreiben.

Vorrang haben A020 (Shim-Fußnote), A068 (Zuordnung zur Anwendung), A077/A080/A082/A093 (Prüfsummen und NAT),
B053 bis B058 (OCS-Erklärung), B071/B072 (TLV-Felder), B081/B091 (Empfangsregeln) sowie
C037/C045/C052/C060 (Aufgaben von Kernel und Anwendung). Verständliche Sätze im Umfeld dieser Stellen
sollen erhalten bleiben.

Die Originalzitate sind für die Lesbarkeit von Schriftbefehlen und Belegklammern befreit;
interne Verweise sind mit den aktuellen Nummern aufgelöst. Der übrige Wortlaut bleibt erhalten.
Den vollständigen LaTeX-Text mit seinen Belegen öffnet jeweils der Link zur Quellzeile.
Die überschriftenartige Listenankündigung „Die vier Felder im Einzelnen:“ ist zusammen mit der folgenden
Liste geprüft, wird aber wie die Abschnittsüberschriften nicht als eigener Satz gezählt.

## Zusammenhang der Absätze

1. **Die Reihenfolge der Hauptabschnitte funktioniert.** IPv4 erklärt den äußeren Rahmen, UDP den inneren
   Aufbau, die Surplus Area die Erweiterung und der Netzpfad die Bedingungen der Messung. Diese Struktur
   sollte erhalten bleiben. Der Auftaktsatz muss diese Reihenfolge allerdings als Kapitelaufbau benennen:
   „gefolgt von“ verbindet dort derzeit Protokolle mit Themenbereichen.
2. **In 2.1 sind vor allem einzelne Sätze überladen.** Die Verbindung von Headerlängen, MTU und
   Fragmentierung ist nachvollziehbar. Bei der Fragmentierung sollten Handlungsschritte getrennt werden:
   Wer zerlegt das Datagramm, welche Angaben tragen die Fragmente, und wer setzt sie wieder zusammen?
3. **Die wiederholten UDP-Grundeigenschaften brauchen unterschiedliche Aufgaben.** Die Einleitung von
   2.2 darf das Protokoll kurz einordnen. Abschnitt 2.2.2 sollte die Folgen erklären. Verbindungsaufbau,
   Zustellung, Reihenfolge und Verantwortung der Anwendung müssen nicht an beiden Stellen gleich
   ausführlich stehen. Die Erklärung der Folgen eines Verlusts hat dagegen eigenen Mehrwert.
4. **Die Zweck- und Rollenklärung beim Pseudo-Header soll bleiben.** Dass Sender und Empfänger ihn jeweils
   bilden und verwenden, beantwortet genau deine frühere Frage. Diese Erklärung sollte nicht aus reinem
   Kürzungswillen entfallen. Schwieriger sind die kompakten Rechensätze und die abstrakte Beschreibung der
   beiden Nullwerte.
5. **Aufbau, OCS, Empfangsentscheidung und Optionsklassen ergänzen sich.** Die Grundregel „Optionen
   verwerfen, Nutzdaten weitergeben“ wird dort mehrfach gebraucht. Zuerst muss sie vollständig und mit
   ihren Voraussetzungen erklärt werden; spätere Stellen können sich kürzer darauf beziehen. Die
   Sonderregeln dürfen bei einer Straffung nicht verloren gehen.
6. **Die Empfangsentscheidung ist der deutlichste Fall für kürzere Regelsätze.** Der Satz zu
   Längenfehlern, mehrfachem FRAG, der Reihenfolge von must-support-Optionen und der Nullfüllungsprüfung
   enthält unterschiedliche Bedingungen und Verbindlichkeitsstufen. Diese Regeln sollten getrennt
   formuliert werden. Die Abbildung hilft, ersetzt diese Trennung im Text aber nicht.
7. **In 2.3.5 lenken einzelne Nebenpfade vom Grundgedanken ab.** Die sechs Prinzipien sind eine sinnvolle
   Ordnung. Die zusätzliche Erklärung zum Missbrauch automatischer Antworten, die historischen Größenvergleiche und
   bloße Merksätze
   sollten jedoch auf ihren Mehrwert geprüft werden. SAFE und UNSAFE brauchen anschließend vor allem
   eine klare Erklärung der Folgen für die Nutzdaten.
8. **In 2.4 ist die technische Aufgabenverteilung wichtiger als ihre bildhafte Beschreibung.** Die
   Abbildungen sowie die Unterscheidung zwischen UDP-Socket und Raw Socket sollen bleiben. Wendungen wie
   „Arbeitsteilung kippt“, „Unterbau“ und „aus seiner Obhut“ lassen sich durch die konkreten Aufgaben von
   Anwendung und Kernel ersetzen oder entfallen lassen. Details zu korrigierten Funktionsnamen einer
   fremden Vorlage unterbrechen dagegen den Erklärungsweg.
9. **Abbildungsbezüge sind sinnvoll, aber ihre Einleitungen wiederholen sich.** „Aus Abbildung … geht
   hervor“ ist für sich verständlich. Es ist kein Grund, jeden solchen Satz zu ändern. Wo danach nur eine
   bereits erklärte Aussage wiederholt wird, reicht eine kürzere Bezugnahme; wo eine Rechnung oder Folge
   erklärt wird, muss diese Erklärung erhalten bleiben.

## Leseschlüssel

- **Belassen:** Der Satz ist für seinen Zweck ausreichend klar und passt zum Zusammenhang.
- **Vereinfachen, Klarheit:** Eine konkrete Formulierung erschwert das Verständnis; der Inhalt soll erhalten bleiben.
- **Vereinfachen, optional:** Verständlich, aber knapper oder sachlicher formulierbar.
- **Streichen, optional:** Der Satz ist verständlich, trägt an dieser Stelle aber keinen eigenständigen Gedanken.

Die Reihenfolge der Einzelprüfung folgt dem Quelltext. Die Kennungen A, B und C teilen den Bericht nur
in handhabbare Bereiche. Zu jeder Einheit führt ein Link an den Anfang der zugehörigen Quellstelle.
Fußnoten, Felddefinitionen und Bildunterschriften sind zusätzlich erfasst. Nominale Beschriftungen und
Definitionen sind keine vollständigen Sätze und werden bei der Auswertung entsprechend getrennt gezählt.
Reiner TikZ-Zeichencode und numerische Tabellenzellen sind keine sprachlichen Sätze.

Bei gemeinsam zu überarbeitenden Nachbarsätzen müssen die Vorschläge zusammen gelesen werden. Quellen
und Querverweise sind bei einer späteren Umsetzung an den zugehörigen Aussagen zu erhalten; eine knappe
Ersatzformulierung ist kein Auftrag, Belege zu entfernen.

## Zusammengehörige Änderungen

- A079 bis A082: Die beiden Darstellungen der Null und ihre Bedeutung zusammen lesen.
- B036/B037: Allgemeine Fehlerregel und konkreter Pad-Fehler bleiben beide erhalten; gemeinsam umformulieren.
- B052 bis B055: Bei der optionalen Streichung der Ankündigung auch „Erstens/Zweitens“ anpassen.
- B080 bis B083 sowie B085/B086: Nach dem Wegfall einer Ankündigung müssen die Folgesätze selbstständig beginnen.
- C028 bis C031: Ohne die Ankündigung der zwei Folgen entfallen auch „Erstens/Zweitens“.
- C036/C037: Der Ersatz nennt UDP-Socket und Kernel ausdrücklich und bleibt so auch ohne C036 verständlich.
- C049 bis C052: Bei einer Kürzung bleiben die Gemeinsamkeiten der Sendewege und alle verbliebenen Kernelaufgaben
erhalten.

## Zwei ergänzende Befunde zu Diagrammbeschriftungen

- **Abbildung 2.8, [Zeile 687](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:687>):** „Kein listenweiter Ablehnungsgrund?“ lässt sich als „Kein Grund, die gesamte Optionsliste zu verwerfen?“ ausdrücken. Das erklärt den Geltungsbereich des Ablehnungsgrunds ohne das zusätzliche Wort „listenweit“.
- **Abbildung 2.9, [Zeile 849](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:849>):** „Längen bündig“ kann „UDP füllt die IP-Nutzlast“ heißen. Damit ist die gemeinte Übereinstimmung unmittelbar benannt. Die standardisierten englischen Feldnamen in den Headerabbildungen sollen dagegen erhalten bleiben.

Diese zwei kurzen Beschriftungsbefunde sind zusätzlich zur Satzliste erfasst. Bei einer späteren Umsetzung ist ihr
Platzbedarf in den Diagrammen zu prüfen.

## Vollständige Einzelprüfung

### Kapitelauftakt

**A001 · Satz · [Zeile 8](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:8>) · Vereinfachen, Klarheit**

> IPv4 und UDP sind die beteiligten Protokolle (Abschnitt 2.1, Abschnitt 2.2), gefolgt von der Surplus Area (Abschnitt
> 2.3) sowie Betriebssystem und Netzpfad (Abschnitt 2.4).

**Bewertung:** „Gefolgt von“ verbindet Protokolle mit Themenbereichen. Als knappe Orientierung ist der Auftakt sinnvoll,
wenn er ausdrücklich den Aufbau des Kapitels beschreibt.

**Vorschlag:** Dieses Kapitel erklärt zunächst IPv4 und UDP (Abschnitt 2.1, Abschnitt 2.2). Danach folgen die Surplus
Area (Abschnitt 2.3) sowie Betriebssystem und Netzpfad (Abschnitt 2.4).

### 2.1 IPv4

**A002 · Satz · [Zeile 15](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:15>) · Belassen**

> Das Internet Protocol (IP) vermittelt Datagramme zwischen Endsystemen und bildet die Vermittlungsschicht für UDP.

**Bewertung:** Der Satz benennt IP als handelndes Protokoll und ordnet seine Aufgabe gegenüber UDP ein.

**A003 · Satz · [Zeile 16](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:16>) · Vereinfachen, Klarheit**

> Für RFC 9868 ist es nötig, weil erst UDP Length und das durch den IP-Header bestimmte Datagrammende Lage und Größe der
> Surplus Area festlegen.

**Bewertung:** „Es“ verweist nur mittelbar auf IP, und „für RFC 9868 nötig“ benennt nicht den konkreten Zweck der
Längenangaben.

**Vorschlag:** UDP Length und das durch den IP-Header bestimmte Datagrammende legen Lage und Größe der Surplus Area
fest.

**A004 · Satz · [Zeile 19](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:19>) · Belassen**

> Entsprechend der Abgrenzung in Abschnitt 1.4 behandelt dieser Abschnitt nur die für RFC 9868 und die Messung nötigen
> IPv4-Felder: IHL, Total Length, Protocol, Adressen, Header-Prüfsumme, Fragmentierungsfelder und Time to Live.

**Bewertung:** Die Aufzählung legt den begrenzten Umfang fest und nennt genau die Felder, die das folgende Bild und die
Absätze erklären.

**A005 · Satz · [Zeile 23](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:23>) · Vereinfachen, optional**

> Den Ausgangspunkt bildet der Header; seinen Aufbau zeigt Abbildung 2.1.

**Bewertung:** „Den Ausgangspunkt bildet“ beschreibt nur den Textaufbau; der konkrete Bildverweis genügt.

**Vorschlag:** Abbildung 2.1 zeigt den Aufbau des IPv4-Headers.

**A006 · Definition/Beschriftung · [Zeile 66](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:66>) · Belassen**

> Der IPv4-Header nach RFC 791.

**Bewertung:** Die nominale Bildunterschrift nennt Gegenstand und Quelle; ein zusätzlicher vollständiger Satz wäre
unnötig.

**A007 · Satz · [Zeile 66](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:66>) · Belassen**

> Hervorgehoben sind die beiden Längenangaben, auf denen die Bestimmung der Surplus Area beruht; gestrichelte Felder
> sind nur vorhanden, wenn IHL über dem Minimalwert 5 liegt.

**Bewertung:** Beide Teilsätze erklären konkrete grafische Merkmale; die gemeinsame Bildunterschrift hält Farbe und
gestrichelte Umrandung verständlich auseinander.

**A008 · Satz · [Zeile 73](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:73>) · Streichen, optional**

> Im Zentrum stehen die beiden Längenangaben der ersten Zeile.

**Bewertung:** Die Bildunterschrift hat diese Hervorhebung bereits erklärt; der nächste Satz beginnt unmittelbar mit
Total Length.

**Vorschlag:** Satz entfernen; die Begründung und etwaige Nachbarsätze oben beachten.

**A009 · Satz · [Zeile 73](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:73>) · Belassen**

> Total Length gibt die Gesamtlänge des Datagramms in Byte an, Header und Nutzlast zusammen; als 16-Bit-Feld erlaubt es
> höchstens 65 535 Byte.

**Bewertung:** Feld, Einheit, enthaltene Bereiche und Obergrenze stehen in einer zusammenhängenden Erklärung.

**A010 · Satz · [Zeile 76](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:76>) · Belassen**

> Die zweite Längenangabe, die IHL (Internet Header Length), beziffert die Länge des Headers.

**Bewertung:** IHL wird ausgeschrieben und unmittelbar auf die Headerlänge bezogen; „zweite“ knüpft eindeutig an Total
Length an.

**A011 · Satz · [Zeile 76](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:76>) · Vereinfachen, Klarheit**

> Sie zählt dabei nicht in Byte, sondern in 32-Bit-Wörtern zu je 4 Byte: Das 4-Bit-Feld erreicht höchstens den Wert 15,
> und erst die Zählung in Wörtern deckt damit Header bis 60 Byte ab.

**Bewertung:** Der Satz wechselt zwischen Zähleinheit, Feldbreite und erreichbarer Headerlänge; getrennte Sätze machen
die Rechnung nachvollziehbarer.

**Vorschlag:** IHL zählt in 32-Bit-Wörtern zu je 4 Byte. Das 4-Bit-Feld erreicht höchstens den Wert 15 und kann damit
Headerlängen bis 60 Byte angeben.

**A012 · Satz · [Zeile 78](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:78>) · Belassen**

> Die Headerlänge ergibt sich daher als Headerlänge = IHL × 4 Byte.

**Bewertung:** Der Satz führt die Formel direkt aus der zuvor erläuterten Zähleinheit her; die Formel in Zeile 81 gehört
zu diesem Satz.

**A013 · Satz · [Zeile 84](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:84>) · Belassen**

> Der Minimalwert 5 entspricht dem optionslosen 20-Byte-Header.

**Bewertung:** Der konkrete Minimalwert macht die Formel ohne zusätzliche Erklärung anwendbar.

**A014 · Satz · [Zeile 84](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:84>) · Vereinfachen, optional**

> Eine IPv4-Headerlänge ist damit stets ein Vielfaches von 4; diese unscheinbare Eigenschaft kehrt bei der Ausrichtung
> der UDP Options wieder.

**Bewertung:** „Unscheinbare Eigenschaft“ kann sachlicher formuliert werden. Der Hinweis auf die spätere Ausrichtung
soll erhalten bleiben, weil er die Relevanz der Zahl erklärt.

**Vorschlag:** Eine IPv4-Headerlänge ist damit stets ein Vielfaches von 4. Diese Eigenschaft ist für die Ausrichtung der
UDP Options wichtig.

**A015 · Satz · [Zeile 87](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:87>) · Belassen**

> Zwischen festem Header und Nutzlast können zudem IP-Optionen liegen: zusätzliche Steuerfelder für Sonderfälle, die die
> gewöhnliche Kommunikation nicht braucht; Record Route etwa sammelt die Adressen der durchlaufenen Router ein.

**Bewertung:** Der Satz erklärt Lage und Zweck und liefert mit Record Route sofort ein konkretes Beispiel; Doppelpunkt
und Semikolon ordnen diese drei zusammengehörigen Schritte.

**A016 · Satz · [Zeile 89](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:89>) · Vereinfachen, Klarheit**

> In der Praxis werden solche Optionen kaum genutzt, ihre Verarbeitung belastet je nach Architektur und Konfiguration
> den allgemeinen Prozessor des Routers, und das Verwerfen optionstragender Pakete ist verbreitete Praxis.

**Bewertung:** Seltene Nutzung, Prozessorbelastung und Verwerfen sind drei verschiedene Aussagen; die lange Kommakette
erschwert ihre Zuordnung.

**Vorschlag:** IP-Optionen werden in der Praxis kaum genutzt. Ihre Verarbeitung belastet je nach Architektur und
Konfiguration den allgemeinen Prozessor des Routers. Zudem ist das Verwerfen von Paketen mit IP-Optionen verbreitet.

**A017 · Satz · [Zeile 91](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:91>) · Belassen**

> Der Beginn der Nutzlast folgt damit stets aus der IHL, nie aus einer Konstante.

**Bewertung:** Der Satz zieht eine konkrete Folgerung aus der variablen Headerlänge; der Gegensatz erklärt, warum der
Leser nicht immer mit 20 Byte rechnen darf.

**A018 · Satz · [Zeile 94](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:94>) · Vereinfachen, Klarheit**

> Aus den beiden Längenangaben Total Length und IHL ergibt sich die Größe, auf die sich RFC 9868 durchgängig bezieht:
> Die Nutzlast eines IPv4-Datagramms beginnt nach IHL × 4 Byte und endet bei Total Length.

**Bewertung:** „Die Größe, auf die sich RFC 9868 durchgängig bezieht“ lässt die bezeichnete Größe zunächst offen; die
konkrete Nutzlast kann sofort genannt werden.

**Vorschlag:** Total Length und IHL bestimmen die Größe der IPv4-Nutzlast: Sie beginnt nach IHL × 4 Byte und endet bei
Total Length.

**A019 · Satz · [Zeile 96](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:96>) · Belassen**

> Für ein UDP-Datagramm fordert RFC 9868 deshalb UDP Length ≤ Total Length − Headerlänge.

**Bewertung:** Die Ungleichung sagt unmittelbar, welche Längenbeziehung gelten muss; die Formel in Zeile 102 ist hier
mit dem einleitenden Satz erfasst, die eingeschobene Fußnote separat.

**A020 · Fußnotensatz · [Zeile 97](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:97>) · Vereinfachen, Klarheit**

> In Ausnahmefällen liegen zwischen IPv4- und UDP-Header noch Shim-Header, etwa bei IPsec oder IPComp; das Feld Protocol
> zeigt dann nicht UDP an, und die Obergrenze verringert sich zusätzlich um die Gesamtlänge dieser Shim-Header.

**Bewertung:** Die Frage nach der „Obergrenze“ wird durch den konkret verfügbaren Platz beantwortet. Die zusätzlichen
Beispiele IPsec und IPComp werden für die danach ausdrücklich ausgeschlossenen Fälle hier nicht benötigt.

**Vorschlag:** Zusätzliche Header zwischen IPv4- und UDP-Header (Shim-Header) verringern den für das UDP-Datagramm
verfügbaren Platz um ihre Gesamtlänge; das Feld Protocol zeigt dann nicht UDP an.

**A021 · Fußnotensatz · [Zeile 100](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:100>) · Belassen**

> Diese Arbeit betrachtet solche Ketten nicht weiter.

**Bewertung:** Nach der Formel-Ausnahme schließt dieser Satz den bewusst ausgeschlossenen Sonderfall ab, statt eine
weitere Erklärung zu versprechen.

**A022 · Satz · [Zeile 105](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:105>) · Belassen**

> Die rechte Seite der Ungleichung ist der Platz hinter dem IP-Header, die linke die Länge, die das UDP-Datagramm für
> sich beansprucht: Das UDP-Datagramm muss vollständig in die Nutzlast des IP-Datagramms passen.

**Bewertung:** Der Satz übersetzt beide Seiten der Formel in räumlich verständliche Größen und erklärt anschließend die
Bedingung in Worten.

**A023 · Satz · [Zeile 107](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:107>) · Belassen**

> Bei Gleichheit füllt es sie exakt aus; das Datagramm hat dann keine Surplus Area.

**Bewertung:** „Es“ und „sie“ beziehen sich unmittelbar auf UDP-Datagramm und IP-Nutzlast; der zweite Teilsatz nennt die
konkrete Folge der Gleichheit.

**A024 · Satz · [Zeile 107](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:107>) · Vereinfachen, optional**

> Bleibt UDP Length dagegen zurück, ist die Differenz genau der Raum, den Abschnitt 2.3 als Surplus Area einführt.

**Bewertung:** „Zurückbleiben“ und „der Raum, den der Abschnitt einführt“ umschreiben die Längendifferenz und ihre
Bezeichnung unnötig.

**Vorschlag:** Ist UDP Length kleiner, bildet die Differenz die Surplus Area (Abschnitt 2.3).

**A025 · Satz · [Zeile 110](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:110>) · Streichen, optional**

> Von den übrigen Feldern braucht die Arbeit nur wenige.

**Bewertung:** Die Auswahl der benötigten Felder steht bereits in Zeilen 19–21; der nächste Satz kann direkt Protocol
erklären.

**Vorschlag:** Satz entfernen; die Begründung und etwaige Nachbarsätze oben beachten.

**A026 · Satz · [Zeile 110](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:110>) · Belassen**

> Protocol benennt das Transportprotokoll der Nutzlast; der Wert 17 steht für UDP.

**Bewertung:** Der Satz verbindet die Funktion des Feldes mit dem hier verwendeten Wert, ohne einen neuen Nebenbegriff
einzuführen.

**A027 · Satz · [Zeile 111](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:111>) · Belassen**

> Die Header Checksum sichert ausschließlich den Header, nicht die Nutzlast; deren Fehlererkennung bleibt der
> UDP-Prüfsumme überlassen (Abschnitt 2.2.1).

**Bewertung:** Die beiden Prüfbereiche werden direkt gegenübergestellt; „deren“ hat mit der unmittelbar vorangehenden
Nutzlast einen eindeutigen Bezug.

**A028 · Satz · [Zeile 112](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:112>) · Belassen**

> Quell- und Zieladresse geben Absender und Empfänger des Datagramms an; die UDP-Prüfsumme bezieht beide später über
> einen sogenannten Pseudo-Header in ihre Berechnung ein.

**Bewertung:** Die Adressfelder werden erst erklärt und danach an die spätere Prüfsummenbeschreibung angebunden; die
Bedeutung des neuen Begriffs wird dort ausgeführt.

**A029 · Satz · [Zeile 115](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:115>) · Belassen**

> Version und Type of Service berühren den Optionsmechanismus nicht.

**Bewertung:** Der knappe Ausschluss erklärt, warum zwei im Bild sichtbare Felder anschließend nicht vertieft werden.

**A030 · Satz · [Zeile 117](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:117>) · Vereinfachen, optional**

> Auch Time to Live spielt für die Optionen keine Rolle, kehrt in der Evaluation aber als Messgröße wieder.

**Bewertung:** „Kehrt... wieder“ spricht über die Kapitelabfolge; für den Leser ist die konkrete Verwendung als
Messgröße ausreichend.

**Vorschlag:** Die Evaluation nutzt Time to Live als Messgröße.

**A031 · Satz · [Zeile 118](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:118>) · Vereinfachen, Klarheit**

> Jede weiterleitende Instanz verringert den Wert um mindestens eins und verwirft das Datagramm bei null.

**Bewertung:** „Weiterleitende Instanz“ bleibt abstrakt; im beschriebenen IPv4-Pfad sind die Router die konkrete
handelnde Stelle.

**Vorschlag:** Jeder weiterleitende Router verringert Time to Live um mindestens eins und verwirft das Datagramm bei
null.

**A032 · Satz · [Zeile 119](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:119>) · Vereinfachen, Klarheit**

> Die Differenz zwischen gesendetem und empfangenem Wert entspricht deshalb nur unter der Annahme eines Dekrements von
> genau eins je Weiterleitung der Zahl der durchlaufenen IPv4-Router; Kapitel 6 nutzt sie unter dieser Annahme, um die
> Stabilität der Messpfade zu prüfen.

**Bewertung:** Die notwendige Bedingung steckt zwischen Subjekt und Vergleichsgröße; „Dekrement“ erschwert zusätzlich
die ohnehin wichtige Einschränkung.

**Vorschlag:** Wenn jeder Router den Wert bei der Weiterleitung um genau eins verringert, entspricht die Differenz
zwischen gesendetem und empfangenem Wert der Zahl der durchlaufenen IPv4-Router. Diese Arbeit nutzt die Differenz unter
dieser Annahme, um die Stabilität der Messpfade zu prüfen (Kapitel 6).

**A033 · Satz · [Zeile 121](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:121>) · Vereinfachen, optional**

> Die zweite Zeile des Headers schließlich (Identification, Flags, Fragment Offset) gehört vollständig zur
> Fragmentierung, der sich der Rest dieses Abschnitts widmet.

**Bewertung:** „Schließlich“ und „der sich der Rest... widmet“ erläutern die Textfolge statt die Funktion der Felder.

**Vorschlag:** Identification, Flags und Fragment Offset in der zweiten Headerzeile dienen der Fragmentierung.

**A034 · Satz · [Zeile 125](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:125>) · Belassen**

> Wie groß ein Datagramm praktisch werden kann, entscheidet allerdings nicht das 16-Bit-Längenfeld, sondern der
> Übertragungsweg.

**Bewertung:** Der Satz leitet vom theoretischen Feldmaximum zur praktisch relevanten Begrenzung durch den Pfad über;
der Gegensatz hat hier eine konkrete Funktion.

**A035 · Satz · [Zeile 126](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:126>) · Belassen**

> Die Maximum Transmission Unit (MTU) begrenzt die Größe eines IP-Pakets, das eine Verbindung ohne Fragmentierung
> übertragen kann.

**Bewertung:** Der neue Fachbegriff wird ausgeschrieben und direkt durch seine Wirkung erklärt.

**A036 · Satz · [Zeile 127](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:127>) · Belassen**

> Bei Ethernet beträgt sie üblicherweise 1500 Byte.

**Bewertung:** Das kurze Zahlenbeispiel macht die MTU greifbar; „sie“ bezieht sich unmittelbar auf den vorherigen Satz.

**A037 · Satz · [Zeile 127](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:127>) · Belassen**

> Ein Datagramm kann mehrere Netze mit unterschiedlichen MTUs durchqueren; IP muss deshalb festlegen, was mit einem zu
> großen Datagramm geschieht.

**Bewertung:** Die wechselnden MTUs begründen die anschließende Erklärung der Fragmentierung und des DF-Falls; der Satz
stellt eine beantwortete Frage.

**A038 · Satz · [Zeile 131](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:131>) · Streichen, optional**

> IPv4 beantwortet das mit Fragmentierung.

**Bewertung:** Der unmittelbar folgende Satz erklärt bereits vollständig, wann die IP-Schicht fragmentiert; die
zusätzliche Ankündigung verzögert diese Erklärung.

**Vorschlag:** Satz entfernen; die Begründung und etwaige Nachbarsätze oben beachten.

**A039 · Satz · [Zeile 131](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:131>) · Belassen**

> Ist ein Datagramm größer als die MTU und das Flag DF (Don't Fragment) nicht gesetzt, zerlegt die IP-Schicht es in
> mehrere Fragmente; bei IPv4 darf das auch jeder Router unterwegs.

**Bewertung:** Bedingung, handelnde Schicht und mögliche Stelle im Pfad sind klar benannt; die Länge entsteht aus den
nötigen Voraussetzungen.

**A040 · Satz · [Zeile 133](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:133>) · Vereinfachen, Klarheit**

> Jedes Fragment erhält einen eigenen IP-Header; Identification, Fragment Offset und das Flag MF (More Fragments)
> steuern die Zuordnung, und der Empfänger setzt das Datagramm anhand von Quelladresse, Zieladresse, Protokoll und
> Identification vor der Übergabe an die Transportschicht wieder zusammen.

**Bewertung:** Eine lange Satzkette verbindet Headeraufbau, drei Steuerfelder, vier Zuordnungsmerkmale und den Zeitpunkt
der Zusammensetzung; kurze Sätze trennen diese Aufgaben.

**Vorschlag:** Jedes Fragment erhält einen eigenen IP-Header. Identification, Fragment Offset und das Flag MF (More
Fragments) steuern die Zuordnung. Der Empfänger setzt das Datagramm anhand von Quelladresse, Zieladresse, Protokoll und
Identification wieder zusammen, bevor er es an die Transportschicht übergibt.

**A041 · Satz · [Zeile 136](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:136>) · Belassen**

> Ist DF dagegen gesetzt, verwirft ein Router das zu große Datagramm und meldet dies dem Absender per ICMP; auf dieser
> Rückmeldung baut die Path MTU Discovery auf, mit der ein Sender die kleinste MTU seines Pfades ermittelt.

**Bewertung:** Der Satz führt Ursache, Routerreaktion und Nutzen der Rückmeldung in der richtigen Reihenfolge zusammen;
der Zweck von Path MTU Discovery wird unmittelbar erklärt.

**A042 · Satz · [Zeile 141](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:141>) · Vereinfachen, optional**

> Für diese Arbeit ist an der Fragmentierung vor allem eine Konsequenz bedeutsam: Der UDP-Header gehört aus Sicht von IP
> zur Nutzlast und landet deshalb vollständig im ersten Fragment.

**Bewertung:** Die Wertung „für diese Arbeit... bedeutsam“ sagt noch nichts über die Konsequenz; der zweite Teil enthält
bereits die vollständige Erklärung.

**Vorschlag:** Der UDP-Header gehört aus Sicht von IP zur Nutzlast und liegt deshalb vollständig im ersten Fragment.

**A043 · Satz · [Zeile 142](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:142>) · Belassen**

> Was das für die übrigen Fragmente bedeutet, zeigt Abbildung 2.2.

**Bewertung:** Der Verweis nennt eine konkrete Betrachtungsfrage für das folgende Bild: die Ausstattung der
Folgefragmente.

**A044 · Definition/Beschriftung · [Zeile 177](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:177>) · Belassen**

> Schematische Zerlegung eines UDP-Datagramms in drei IPv4-Fragmente

**Bewertung:** Die nominale Bildunterschrift benennt Vorgang und gezeigte Anzahl; sie benötigt keinen zusätzlichen
erklärenden Satz.

**A045 · Satz · [Zeile 181](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:181>) · Belassen**

> Aus Abbildung 2.2 geht hervor, dass nur das erste Fragment den UDP-Header enthält: Alle Folgefragmente tragen keine
> Portnummern.

**Bewertung:** Die Bildauswertung benennt genau die für den folgenden NAT-/Firewall-Absatz wichtige Folge; sie ist mehr
als ein bloßer Abbildungsverweis.

**A046 · Satz · [Zeile 182](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:182>) · Vereinfachen, Klarheit**

> Manche NATs und Firewalls benötigen für ihre Verarbeitung vollständige IP-Pakete, implementieren jedoch keine
> Zusammensetzung der Fragmente und verwerfen diese deshalb pauschal; zudem macht der Verlust eines einzelnen Fragments
> das gesamte Datagramm unbrauchbar.

**Bewertung:** Der Verlust eines Fragments ist ein zweites, unabhängiges Problem; im selben Satz kann er fälschlich wie
eine Folge des beschriebenen NAT-Verhaltens wirken.

**Vorschlag:** Manche NATs und Firewalls benötigen vollständige IP-Pakete, setzen Fragmente jedoch nicht zusammen und
verwerfen sie deshalb pauschal. Außerdem macht der Verlust eines einzelnen Fragments das gesamte Datagramm unbrauchbar.

**A047 · Satz · [Zeile 184](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:184>) · Belassen**

> RFC 8085 beschreibt diese Probleme und rät UDP-Anwendungen deshalb, IP-Fragmentierung zu vermeiden.

**Bewertung:** Die Empfehlung wird auf die unmittelbar zuvor genannten Probleme zurückgeführt; „diese“ hat einen klaren
Absatzbezug.

**A048 · Satz · [Zeile 186](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:186>) · Vereinfachen, Klarheit**

> Dass der Rat gerade an UDP geht, hat einen Grund: Während TCP seinen Datenstrom selbst in passende Segmente zerlegt
> und der IP-Fragmentierung so meist entgeht, erzeugt UDP je Nachricht genau ein Datagramm (Abschnitt 2.2.2); ein zu
> großes Datagramm kann bislang nur die IP-Schicht zerteilen.

**Bewertung:** Die rhetorische Einleitung verzögert den begründeten Vergleich; im langen Während-Satz muss der Leser
drei Protokollaufgaben auseinanderhalten.

**Vorschlag:** TCP zerlegt seinen Datenstrom selbst in passende Segmente und vermeidet so meist IP-Fragmentierung. UDP
erzeugt je Nachricht genau ein Datagramm (Abschnitt 2.2.2). Ein zu großes UDP-Datagramm kann bislang nur die IP-Schicht
zerteilen.

**A049 · Satz · [Zeile 189](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:189>) · Belassen**

> Genau diese Lücke schließt die FRAG-Option von RFC 9868: Sie verlagert die Fragmentierung auf die Transportschicht und
> wiederholt die Portnummern in jedem Fragment; den Verlust einzelner Fragmente behebt allerdings auch FRAG nicht.

**Bewertung:** „Diese Lücke“ bezieht sich auf die gerade erläuterte fehlende UDP-Fragmentierung; der Satz nennt die
Leistung von FRAG und grenzt sie im selben Zusammenhang ab.

**A050 · Satz · [Zeile 192](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:192>) · Streichen, optional**

> Darauf kommt Kapitel 6 zurück.

**Bewertung:** „Darauf“ kann Fragmentverlust, wiederholte Ports oder die gesamte FRAG-Funktion meinen; die pauschale
Kapitelankündigung hilft hier nicht beim Verständnis.

**Vorschlag:** Satz entfernen; die Begründung und etwaige Nachbarsätze oben beachten.

### 2.2 Das User Datagram Protocol (UDP)

**A051 · Satz · [Zeile 197](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:197>) · Belassen**

> Das User Datagram Protocol (UDP) ist ein verbindungsloses, nachrichtenorientiertes Transportprotokoll.

**Bewertung:** Die knappe Definition nennt die beiden Grundmerkmale, die der nächste Satz und der Abschnitt
Eigenschaften konkret erklären.

**A052 · Satz · [Zeile 197](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:197>) · Vereinfachen, optional**

> Es arbeitet ohne vorherigen Handshake und bietet selbst keine Garantie für Zustellung, Reihenfolge oder
> Duplikaterkennung.

**Bewertung:** „Handshake“ lässt sich hier ohne Bedeutungsverlust durch den bereits im Kapitel verwendeten deutschen
Begriff ersetzen.

**Vorschlag:** UDP benötigt keinen vorherigen Verbindungsaufbau und bietet selbst keine Garantie für Zustellung,
Reihenfolge oder Duplikaterkennung.

**A053 · Satz · [Zeile 199](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:199>) · Belassen**

> Zuverlässigkeit und Staukontrolle muss ein nutzendes Protokoll bei Bedarf oberhalb von UDP bereitstellen.

**Bewertung:** Der Satz beantwortet unmittelbar, wer die von UDP nicht bereitgestellten Funktionen übernimmt; „oberhalb
von UDP“ ordnet diese Verantwortung ein.

**A054 · Satz · [Zeile 200](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:200>) · Belassen**

> UDP verwendet die IP-Protokollnummer 17 und ist als STD 6 standardisiert.

**Bewertung:** Protokollnummer und Standardbezeichnung werden knapp zugeordnet; der Satz benötigt keine längere
Hinführung.

**A055 · Satz · [Zeile 201](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:201>) · Vereinfachen, optional**

> Bemerkenswert ist, dass RFC 768 seit seiner Veröffentlichung im August 1980 über 45 Jahre hinweg keine formelle
> Aktualisierung erfahren hat.

**Bewertung:** „Bemerkenswert ist“ bewertet die Tatsache, und „eine Aktualisierung erfahren“ ist schwerer als das
direkte Verb.

**Vorschlag:** RFC 768 wurde seit seiner Veröffentlichung im August 1980 über 45 Jahre hinweg nicht formell
aktualisiert.

**A056 · Satz · [Zeile 202](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:202>) · Belassen**

> Erst RFC 9868 trägt den Header-Eintrag Updates: 768 und erweitert damit den ursprünglichen UDP-Standard erstmalig
> direkt.

**Bewertung:** Der konkrete Header-Eintrag erklärt, was mit einer formellen Aktualisierung gemeint ist und warum RFC
9868 hier eingeordnet wird.

**A057 · Satz · [Zeile 205](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:205>) · Vereinfachen, optional**

> Historisch geht UDP auf die Aufspaltung des ursprünglichen Transmission Control Program zurück, das Cerf, Dalal und
> Sunshine Ende 1974 noch als monolithische Einheit aus Netzwerk- und Transportfunktionen beschrieben.

**Bewertung:** „Monolithische Einheit“ ist ein zusätzlicher abstrakter Begriff; die gemeinsame Behandlung beider
Funktionen lässt sich direkt ausdrücken.

**Vorschlag:** UDP geht auf die Aufspaltung des ursprünglichen Transmission Control Program zurück, in dem Cerf, Dalal
und Sunshine Ende 1974 Netzwerk- und Transportfunktionen noch gemeinsam beschrieben.

**A058 · Satz · [Zeile 207](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:207>) · Vereinfachen, Klarheit**

> Mit deren Trennung in IP und TCP entstand Raum für eine schlanke, transaktionsorientierte Alternative ohne den
> Overhead von TCP.

**Bewertung:** „Deren“ und „Alternative“ verlangen Rückbezüge auf den vorigen Satz; „schlank“ und „Overhead“ umschreiben
den gemeinten Zusatzaufwand.

**Vorschlag:** Die Trennung in IP und TCP schuf Raum für UDP als transaktionsorientierte Alternative ohne den
Zusatzaufwand von TCP.

**A059 · Satz · [Zeile 208](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:208>) · Vereinfachen, optional**

> Der UDP-Kern blieb über die folgenden Jahrzehnte unverändert, und Begleitdokumente wie die Einsatzrichtlinien von RFC
> 8085 klärten Randfragen, ohne den Standard formell zu ändern.

**Bewertung:** Der unveränderte Kern wiederholt die vorherige historische Einordnung; „Randfragen“ benennt den Beitrag
des genannten Dokuments nur vage.

**Vorschlag:** Begleitdokumente wie RFC 8085 geben Einsatzrichtlinien für UDP vor, ohne den Standard formell zu ändern.

### 2.2.1 Protokollstruktur

**A060 · Satz · [Zeile 215](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:215>) · Belassen**

> Ein UDP-Datagramm besteht aus einem Header mit fester Länge von 8 Byte und den darauf folgenden Nutzdaten; den Aufbau
> des Headers zeigt Abbildung 2.3.

**Bewertung:** Die Definition erklärt die Reihenfolge der Bereiche und verweist direkt auf das dazugehörige Bild; das
Semikolon verbindet zusammengehörige Informationen.

**A061 · Definition/Beschriftung · [Zeile 237](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:237>) · Belassen**

> Der UDP-Header nach RFC 768

**Bewertung:** Die nominale Bildunterschrift nennt genau den gezeigten Header und seine Quelle.

**A062 · Satz · [Zeile 241](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:241>) · Vereinfachen, optional**

> Aus Abbildung 2.3 geht hervor, dass der gesamte Header aus genau vier Feldern zu je 16 Bit besteht; unter ihnen das
> Längenfeld, für das Abschnitt 2.1 mit Gleichung 2.2 bereits die Obergrenze aufgestellt hat.

**Bewertung:** Der lange Rückverweis auf eine frühere Formel unterbricht die Einführung der vier Felder; deren
Einzelbeschreibung folgt ohnehin unmittelbar.

**Vorschlag:** Der UDP-Header besteht aus vier Feldern zu je 16 Bit (Abbildung 2.3).

**A063 · Definition/Beschriftung · [Zeile 246](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:246>) · Belassen**

> Source Port: Die Portnummer des sendenden Prozesses.

**Bewertung:** Die nominale Felddefinition ordnet den Feldnamen direkt dem sendenden Prozess zu.

**A064 · Satz · [Zeile 246](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:246>) · Belassen**

> Dieses Feld ist optional; wird es nicht benötigt, wird es auf null gesetzt.

**Bewertung:** Die Bedingung und der dann verwendete Feldwert stehen unmittelbar zusammen; die folgende Fußnote
beantwortet, wann diese Bedingung erfüllt sein kann.

**A065 · Fußnotensatz · [Zeile 247](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:247>) · Belassen**

> Dies ist etwa möglich, wenn weder Antworten noch eine Zuordnung des Senders über den Quellport nötig sind; RFC 8085
> rät jedoch von Quellport 0 ab.

**Bewertung:** Die Fußnote beantwortet die konkrete Frage nach einem unbenötigten Quellport und stellt die zugehörige
Empfehlung direkt daneben.

**A066 · Satz · [Zeile 249](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:249>) · Vereinfachen, Klarheit**

> In der Praxis nutzen Anwendungen den Source Port zur Identifikation des Absenders, damit der Empfänger Antworten an
> den korrekten Port zurücksenden kann.

**Bewertung:** „Anwendungen“ und „der Empfänger“ erscheinen wie zwei getrennte handelnde Stellen; der empfangenden
Anwendung lässt sich der gesamte Vorgang zuordnen.

**Vorschlag:** Die empfangende Anwendung nutzt den Source Port, um den Absender zuzuordnen und Antworten an dessen Port
zu senden.

**A067 · Definition/Beschriftung · [Zeile 252](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:252>) · Belassen**

> Destination Port: Die Portnummer des Zielprozesses auf dem empfangenden Host.

**Bewertung:** Die nominale Felddefinition nennt Zielprozess und empfangenden Host, also genau die nötige Zuordnung.

**A068 · Satz · [Zeile 252](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:252>) · Vereinfachen, Klarheit**

> Zusammen mit der IP-Zieladresse ermöglicht dieses Feld die Demultiplexierung eingehender Datagramme an die korrekte
> Anwendung.

**Bewertung:** Die Funktion ist für die Arbeit wichtig, der zusätzliche Begriff „Demultiplexierung“ wird hier aber nicht
benötigt. Die aktive Zuordnung beantwortet deine konkrete frühere Frage nach Bedeutung und Nutzen.

**Vorschlag:** Anhand von IP-Zieladresse und Zielport ordnet der Empfänger eingehende Datagramme der richtigen Anwendung
zu.

**A069 · Definition/Beschriftung · [Zeile 256](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:256>) · Belassen**

> Length: Die Gesamtlänge des UDP-Datagramms in Byte, bestehend aus Header und Nutzdaten.

**Bewertung:** Die nominale Definition nennt Einheit und Umfang ausdrücklich; besonders „Header und Nutzdaten“
verhindert eine Verwechslung mit der reinen Nutzdatenlänge.

**A070 · Satz · [Zeile 257](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:257>) · Belassen**

> Der Minimalwert beträgt 8, was einem Datagramm ohne Nutzdaten entspricht.

**Bewertung:** Das Zahlenbeispiel erklärt den Minimalwert durch den bereits eingeführten 8-Byte-Header.

**A071 · Satz · [Zeile 257](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:257>) · Belassen**

> Da das Feld 16 Bit breit ist, ergibt sich eine theoretische Maximalgröße von 65 535 Byte.

**Bewertung:** Ursache und Grenze werden direkt verbunden; „theoretisch“ bewahrt die zuvor erläuterte Unterscheidung zur
IP-Obergrenze.

**A072 · Satz · [Zeile 260](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:260>) · Belassen**

> Checksum: Eine Prüfsumme zur Fehlererkennung über einen Pseudo-Header, den UDP-Header und die Nutzdaten; ihr Verfahren
> und ihre Sonderwerte erläutert der folgende Absatz.

**Bewertung:** Die vollständige Listenpassage nennt den Prüfbereich und verweist gezielt auf die unmittelbar folgende
Erklärung; sie wird wegen des Semikolons nicht in Bruchstücke zerlegt.

**A073 · Satz · [Zeile 265](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:265>) · Belassen**

> Die Prüfsumme dient der Fehlererkennung: Mit ihr erkennt der Empfänger, ob einzelne Bits des Datagramms auf dem Weg
> verändert wurden.

**Bewertung:** Nach der knappen Felddefinition wird der Zweck anhand veränderter Bits konkret erklärt; das beantwortet
die Frage nach dem Nutzen der Rechnung.

**A074 · Satz · [Zeile 266](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:266>) · Belassen**

> Diese Prüfung auf der Transportschicht ist nötig, weil nicht jede Teilstrecke eines Pfades eigene Fehlererkennung
> bietet und Bits auch im Speicher eines Routers kippen können.

**Bewertung:** Die beiden konkreten Fehlerorte beantworten, warum eine Prüfung der Transportschicht trotz vorhandener
Netztechnik gebraucht wird.

**A075 · Satz · [Zeile 268](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:268>) · Belassen**

> Der Feldwert null bedeutet: keine UDP-Prüfsumme.

**Bewertung:** Feldwert und Bedeutung sind ohne Umweg zugeordnet; die kurze Form ist für den anschließenden Sonderfall
hilfreich.

**A076 · Fußnotensatz · [Zeile 268](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:268>) · Belassen**

> Manche Anwendungen verzichten auf die UDP-Prüfsumme, um Rechenaufwand für ihre Berechnung und Prüfung zu sparen.

**Bewertung:** Die Fußnote beantwortet ausschließlich die naheliegende Warum-Frage zum Verzicht und führt keine weitere
Mechanik ein.

**A077 · Satz · [Zeile 271](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:271>) · Vereinfachen, Klarheit**

> Für die Berechnung summiert der Sender Pseudo-Header, UDP-Header und Nutzdaten als 16-Bit-Wörter im Einerkomplement
> auf (ein Übertrag wird am niederwertigen Ende wieder hinzugezählt); das invertierte Ergebnis bildet den Feldwert.

**Bewertung:** Der Satz verbindet Eingabedaten, Einerkomplementaddition, Übertrag und Invertierung. Die Rechenfolge ist
richtig, aber angesichts deiner wiederholten Fragen zur Prüfsumme leichter in einzelnen Schritten zu lesen.

**Vorschlag:** Der Sender berechnet die Prüfsumme aus den 16-Bit-Wörtern von Pseudo-Header, UDP-Header und Nutzdaten. Er
addiert sie im Einerkomplement und zählt einen Übertrag am niederwertigen Ende wieder hinzu. Das invertierte Ergebnis
trägt er in das Prüfsummenfeld ein.

**A078 · Satz · [Zeile 273](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:273>) · Belassen**

> Der Empfänger summiert dieselben Wörter einschließlich des Prüfsummenfelds und erwartet lauter Einsen, also 0xFFFF;
> jedes andere Ergebnis zeigt einen Übertragungsfehler an.

**Bewertung:** Der Empfänger ist als handelnde Stelle benannt, und das erwartete Prüfergebnis wird sowohl in Worten als
auch hexadezimal angegeben.

**A079 · Satz · [Zeile 277](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:277>) · Vereinfachen, optional**

> Dabei hilft eine Eigenheit des Einerkomplements: Es kennt zwei Darstellungen der Null, 0x0000 und 0xFFFF.

**Bewertung:** „Dabei hilft eine Eigenheit“ ist eine erzählerische Einleitung; die beiden Darstellungen lassen sich
unmittelbar nennen.

**Vorschlag:** Das Einerkomplement kennt zwei Darstellungen der Null: 0x0000 und 0xFFFF.

**A080 · Satz · [Zeile 278](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:278>) · Vereinfachen, Klarheit**

> Diese Doppelrolle nutzt UDP für die Sonderwerte des Feldes: eine übertragene 0x0000 bedeutet, dass der Sender keine
> berechnet hat.

**Bewertung:** „Doppelrolle“ bezeichnet die zwei Darstellungen nicht eindeutig, und bei „keine berechnet“ fehlt das
Bezugswort Prüfsumme.

**Vorschlag:** Eine übertragene 0x0000 bedeutet, dass der Sender keine Prüfsumme berechnet hat.

**A081 · Satz · [Zeile 279](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:279>) · Belassen**

> Ergibt die Berechnung selbst den Wert null, wird stattdessen 0xFFFF übertragen.

**Bewertung:** „Die Berechnung selbst“ grenzt den berechneten Nullwert klar vom ungenutzten Feld des vorigen Satzes ab.

**A082 · Satz · [Zeile 281](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:281>) · Vereinfachen, Klarheit**

> Dadurch bleibt im Einerkomplement die Zahl Null erhalten, und der Sonderwert bleibt eindeutig.

**Bewertung:** „Die Zahl Null bleibt erhalten“ erklärt die praktische Bedeutung des Sonderwerts nur abstrakt. Die
Unterscheidung durch den Empfänger beantwortet deutlicher, wofür die zwei Darstellungen gebraucht werden.

**Vorschlag:** Der Empfänger kann dadurch eine berechnete Prüfsumme mit dem Ergebnis null von einer ungenutzten
Prüfsumme unterscheiden.

**A083 · Satz · [Zeile 282](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:282>) · Vereinfachen, optional**

> Dabei ist zu beachten, dass UDP Fehler nur erkennen und nicht beheben kann; ein beschädigtes Datagramm wird
> typischerweise verworfen.

**Bewertung:** „Dabei ist zu beachten, dass“ trägt nichts zur Erklärung bei; die Grenze der Prüfsumme kann direkt als
UDP-Eigenschaft formuliert werden.

**Vorschlag:** UDP kann Fehler nur erkennen und nicht beheben; ein beschädigtes Datagramm wird typischerweise verworfen.

**A084 · Satz · [Zeile 286](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:286>) · Belassen**

> Der Pseudo-Header bezieht ausgewählte IP-Angaben in die UDP-Prüfsumme ein.

**Bewertung:** Die erste Aussage erklärt direkt, wozu dieser zusätzliche Begriff eingeführt wird.

**A085 · Satz · [Zeile 286](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:286>) · Belassen**

> So können unbeabsichtigte Änderungen an IP-Adressen auffallen, selbst wenn UDP-Header und Nutzdaten unverändert sind.

**Bewertung:** Das konkrete Fehlerbeispiel beantwortet, warum auch IP-Angaben in die UDP-Prüfung eingehen.

**A086 · Satz · [Zeile 288](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:288>) · Belassen**

> Die UDP-Implementierung des Senders bezieht den Pseudo-Header zusammen mit dem UDP-Header und den Nutzdaten in die
> Berechnung ein und trägt das Ergebnis in das UDP-Prüfsummenfeld ein.

**Bewertung:** Der Satz beantwortet ausdrücklich, welche Komponente rechnet und wo sie das Ergebnis ablegt; diese
Rollenklärung darf trotz ähnlicher früherer Rechenschritte stehen bleiben.

**A087 · Satz · [Zeile 289](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:289>) · Belassen**

> Die UDP-Implementierung des Empfängers bildet den Pseudo-Header aus den empfangenen Angaben und verwendet ihn für die
> Prüfung einer UDP-Prüfsumme ungleich null.

**Bewertung:** Die Empfängerseite wird parallel zur Senderseite erklärt; Ausgangsdaten und Bedingung der Prüfung sind
ausdrücklich genannt.

**A088 · Satz · [Zeile 291](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:291>) · Belassen**

> Der Pseudo-Header wird nicht als eigener Header übertragen; seine Werte gehen nur in die Rechnung ein.

**Bewertung:** Der Satz verhindert die konkrete Fehlvorstellung eines zusätzlich übertragenen Headers und erläutert
zugleich dessen tatsächliche Verwendung.

**A089 · Satz · [Zeile 292](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:292>) · Belassen**

> Seinen Aufbau zeigt Abbildung 2.4.

**Bewertung:** Der kurze Verweis führt direkt zu der noch fehlenden Übersicht der verwendeten Werte.

**A090 · Definition/Beschriftung · [Zeile 315](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:315>) · Belassen**

> Der Pseudo-Header der UDP-Prüfsumme für IPv4

**Bewertung:** Die nominale Bildunterschrift benennt Prüfsumme und IP-Version; diese Einschränkung ist für die Abbildung
aussagekräftig.

**A091 · Satz · [Zeile 319](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:319>) · Belassen**

> Der Pseudo-Header besteht aus beiden IP-Adressen, einem Nullbyte, Protocol und der wiederholten UDP Length.

**Bewertung:** Die vollständige Feldliste erklärt das Bild in Worten und kennzeichnet die UDP-Länge ausdrücklich als
erneut verwendeten Wert.

**A092 · Satz · [Zeile 320](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:320>) · Belassen**

> Sender und Empfänger verwenden dafür die Werte aus den jeweiligen IP- und UDP-Headern.

**Bewertung:** Der Satz beantwortet die Herkunft der Werte und verdeutlicht, dass jede Seite mit ihren eigenen
Headerangaben rechnet.

**A093 · Satz · [Zeile 321](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:321>) · Vereinfachen, Klarheit**

> Ohne Umschreibung sind die Werte an beiden Enden gleich; eine NAT kann Adressen oder Ports samt UDP-Prüfsumme
> anpassen.

**Bewertung:** „Samt UDP-Prüfsumme anpassen“ erklärt nicht, warum die Adress- oder Portänderung die Prüfsumme betrifft.
Deine frühere Frage zu NAT und Prüfsumme verlangt genau diese Verbindung.

**Vorschlag:** Ohne Änderungen an den Headern verwenden Sender und Empfänger dieselben Werte. Eine NAT kann Adressen
oder Ports umschreiben und die UDP-Prüfsumme entsprechend anpassen, weil diese Felder in deren Berechnung eingehen.

**A094 · Satz · [Zeile 322](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:322>) · Vereinfachen, Klarheit**

> Das Nullbyte ergänzt das 8-Bit-Protokollfeld zu einem 16-Bit-Wort, wie ein Nulloktett Nutzdaten ungerader Länge für
> die Rechnung auffüllt.

**Bewertung:** Der Vergleich verbindet das feste Nullbyte des Pseudo-Headers mit einem anderen Auffüllvorgang; getrennte
Aussagen halten beide Orte auseinander.

**Vorschlag:** Das Nullbyte ergänzt das 8-Bit-Protokollfeld zu einem 16-Bit-Wort. Auch Nutzdaten ungerader Länge werden
für die Prüfsummenrechnung mit einem Nulloktett aufgefüllt.

**A095 · Satz · [Zeile 324](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:324>) · Belassen**

> Ein veränderliches Feld wie Time to Live wäre ungeeignet, weil Sender und Empfänger dann verschiedene Summen bildeten
> (Abschnitt 2.1).

**Bewertung:** Der konkrete Gegenfall erklärt, warum der Pseudo-Header nur bestimmte IP-Angaben enthält; der Vergleich
liefert hier eine klare Begründung.

### 2.2.2 Eigenschaften

**A096 · Satz · [Zeile 332](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:332>) · Belassen**

> UDP ist nachrichtenorientiert: Jede Sendeoperation erzeugt ein Datagramm, das der Empfänger als Einheit entgegennimmt.

**Bewertung:** Der Fachbegriff wird unmittelbar über Sendeoperation und Empfang erklärt; es bleibt keine abstrakte
Definition stehen.

**A097 · Satz · [Zeile 333](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:333>) · Belassen**

> TCP stellt dagegen einen Bytestrom bereit, segmentiert ihn selbst und überlässt der Anwendung die Kennzeichnung von
> Nachrichtengrenzen.

**Bewertung:** Der Vergleich dient hier genau der Erklärung von Nachrichtengrenzen und benennt, welche Aufgabe bei TCP
bei der Anwendung liegt.

**A098 · Satz · [Zeile 334](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:334>) · Belassen**

> UDP nach RFC 768 hält zudem keine Sequenznummern, Fenstergrößen oder Zeitgeber je Kommunikationsbeziehung vor.

**Bewertung:** Die konkreten Beispiele erklären den geringen Protokollzustand; die Einschränkung auf RFC 768 bereitet
die folgende FRAG-Ausnahme vor.

**A099 · Satz · [Zeile 335](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:335>) · Belassen**

> Nur die Reassemblierung von FRAG-Datagrammen bildet in RFC 9868 eine begrenzte Ausnahme.

**Bewertung:** Die kurze Ausnahme ist durch die zuvor erklärte Zusammensetzung von Fragmenten verständlich und
verhindert eine pauschale Aussage zur Zustandslosigkeit.

**A100 · Satz · [Zeile 338](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:338>) · Belassen**

> Da kein Verbindungsaufbau nötig ist, kann die erste Nachricht sofort gesendet werden.

**Bewertung:** Der Satz verbindet eine Protokolleigenschaft mit ihrer konkreten Auswirkung auf den ersten Versand.

**A101 · Satz · [Zeile 339](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:339>) · Belassen**

> UDP garantiert weder Zustellung noch Reihenfolge und wiederholt verlorene Datagramme nicht.

**Bewertung:** Die erneute Nennung ist hier funktional: Sie liefert unmittelbar die Voraussetzung für die folgende
Erklärung des Verhaltens nach einem Verlust.

**A102 · Satz · [Zeile 340](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:340>) · Belassen**

> Später eintreffende Datagramme werden auf UDP-Ebene deshalb nicht wegen eines Verlusts zurückgehalten; dort entsteht
> kein Head-of-Line-Blocking wie bei einem gesicherten Bytestrom.

**Bewertung:** Das Verhalten wird zuerst in deutschen Worten beschrieben und danach benannt; der Vergleich erklärt die
Folge fehlender Wiederholungen und Reihenfolgegarantien.

**A103 · Satz · [Zeile 342](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:342>) · Belassen**

> Benötigte Zuverlässigkeit oder Reihenfolge muss die Anwendung selbst herstellen.

**Bewertung:** Der Satz schließt den Absatz mit einer klaren Verantwortungszuordnung ab; die Wiederaufnahme der
Einleitung ist hier inhaltlich begründet.

**A104 · Satz · [Zeile 345](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:345>) · Belassen**

> Diese Eigenschaften eignen sich für latenzempfindliche oder verlusttolerante Anwendungen.

**Bewertung:** Die abschließende Einordnung nennt zwei konkrete Anforderungsarten, statt eine allgemeine Wertung wie
„effizient“ oder „leistungsfähig“ zu verwenden.

### 2.3 Die Surplus Area

**B001 · Satz · [Zeile 350](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:350>) · Belassen**

> Der UDP-Header bietet keinen Platz für zusätzliche Optionsfelder.

**Bewertung:** Der Satz nennt unmittelbar die räumliche Beschränkung des UDP-Headers.

**B002 · Satz · [Zeile 350](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:350>) · Belassen**

> Zusätze innerhalb der UDP-Nutzdaten würden auch an Anwendungen weitergegeben, die keine Optionen unterstützen.

**Bewertung:** Der Satz erklärt konkret, weshalb Optionen innerhalb der Nutzdaten auch unvorbereitete Anwendungen
erreichen würden.

**B003 · Satz · [Zeile 351](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:351>) · Belassen**

> RFC 9868 legt die Optionen deshalb hinter die UDP-Nutzdaten in die Surplus Area.

**Bewertung:** Der Satz verbindet die zuvor genannte Beschränkung mit der festgelegten Position der Optionen.

### 2.3.1 Lage und Kompatibilität

**B004 · Satz · [Zeile 357](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:357>) · Belassen**

> UDP Length umfasst nur den UDP-Header und die UDP-Nutzdaten.

**Bewertung:** Der Satz nennt beide Bestandteile von UDP Length ausdrücklich und knapp.

**B005 · Satz · [Zeile 357](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:357>) · Vereinfachen, Klarheit**

> Die Längenangaben des IP-Headers können einen größeren Transportbereich ausweisen (Abschnitt 2.1).

**Bewertung:** Transportbereich ausweisen nennt weder den Vergleichswert noch anschaulich, worin der zusätzliche Platz
besteht.

**Vorschlag:** Die Längenangaben im IP-Header können für UDP mehr Platz angeben, als UDP Length umfasst (Abschnitt 2.1).

**B006 · Satz · [Zeile 358](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:358>) · Vereinfachen, Klarheit**

> RFC 9868 nennt die gesamte Nutzlast hinter dem IP-Header IP Transport Payload, in dieser Arbeit kurz IP-Nutzlast, und
> den Teil zwischen dem Ende der UDP-Nutzdaten und dem Ende des IP-Datagramms Surplus Area; dort liegen die UDP Options.

**Bewertung:** Ein Satz führt zwei Bereiche, eine englische Benennung und die Kurzbezeichnung der Arbeit ein; die zweite
Definition ist erst nach einem langen Einschub erreicht.

**Vorschlag:** Die gesamte Nutzlast hinter dem IP-Header heißt in RFC 9868 IP Transport Payload, in dieser Arbeit kurz
IP-Nutzlast. Der Teil hinter den UDP-Nutzdaten bis zum Ende des IP-Datagramms heißt Surplus Area. Dort liegen die UDP
Options.

**B007 · Satz · [Zeile 360](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:360>) · Belassen**

> Die Lage beider Bereiche zeigt Abbildung 2.5 an einem Beispieldatagramm mit Total Length 60, IHL 5 und UDP Length 32:

**Bewertung:** Die Abbildungsankündigung nennt die drei konkreten Werte des folgenden Beispiels.

**B008 · Definition/Beschriftung · [Zeile 390](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:390>) · Belassen**

> IP Transport Payload und Surplus Area eines Datagramms mit Total Length 60

**Bewertung:** Die vollständige nominale Bildunterschrift benennt beide gezeigten Bereiche und das Beispieldatagramm.

**B009 · Satz · [Zeile 395](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:395>) · Vereinfachen, optional**

> Abbildung 2.5 zeigt drei Grenzen ab Byte 0 des IP-Datagramms: Die IP Transport Payload beginnt nach dem IP-Header, UDP
> Length deckt von dort nur UDP-Header und Nutzdaten ab, und die Surplus Area reicht bis zum IP-Datagrammende.

**Bewertung:** Die einleitende Zählung von drei Grenzen ist für die unmittelbar anschließende Beschreibung der Bereiche
entbehrlich.

**Vorschlag:** In Abbildung 2.5 beginnt die IP Transport Payload nach dem IP-Header. UDP Length umfasst darin UDP-Header
und Nutzdaten; die Surplus Area reicht bis zum Ende des IP-Datagramms.

**B010 · Satz · [Zeile 397](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:397>) · Vereinfachen, Klarheit**

> Im Beispiel bleiben von 60-20=40 Byte IP Transport Payload nach UDP Length =32 genau 8 Byte.

**Bewertung:** Nach UDP Length kann eine Position oder einen Rechenschritt meinen; der Satz sollte den Abzug und den
verbleibenden Bereich nennen.

**Vorschlag:** Im Beispiel bleiben von 60 - 20 = 40 Byte IP Transport Payload nach Abzug von UDP Length = 32 genau 8
Byte Surplus Area.

**B011 · Satz · [Zeile 398](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:398>) · Belassen**

> Allgemein gilt Surplus-Länge = Total Length - IP-Headerlänge - UDP Length.

**Bewertung:** Die kurze Einleitung und die Formel nennen unmittelbar, wie die Surplus-Länge berechnet wird.

**B012 · Satz · [Zeile 403](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:403>) · Vereinfachen, Klarheit**

> Die Obergrenze aus Gleichung 2.2 verhindert negative Werte; bei Überschreitung ist das Datagramm ungültig und wird
> still verworfen.

**Bewertung:** Bei Überschreitung lässt offen, welcher Wert die Grenze überschreitet; das Passiv verdeckt zudem die
Handlung des Empfängers.

**Vorschlag:** Eine negative Surplus-Länge bedeutet, dass UDP Length die Obergrenze aus Gleichung 2.2 überschreitet. Der
Empfänger verwirft ein solches Datagramm still als ungültig.

**B013 · Satz · [Zeile 404](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:404>) · Belassen**

> Ohne Surplus Area ist die Differenz null.

**Bewertung:** Die Aussage ist kurz; die Differenz bezieht sich eindeutig auf die unmittelbar vorangehende Formel.

**B014 · Satz · [Zeile 405](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:405>) · Belassen**

> RFC 768 verlangt diese Gleichheit jedoch nicht; RFC 9868 nutzt die seit 1980 bestehende Freiheit.

**Bewertung:** Gleichheit und Differenz sind im direkten Absatzkontext eindeutig; der Satz begründet den zusätzlichen
Platz.

**B015 · Satz · [Zeile 408](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:408>) · Belassen**

> Ein Altempfänger verarbeitet gewöhnlich nur die durch UDP Length begrenzten Nutzdaten und überliest den Rest.

**Bewertung:** Altempfänger, verarbeiteter Bereich und überlesener Rest sind eindeutig benannt.

**B016 · Satz · [Zeile 409](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:409>) · Vereinfachen, optional**

> RFC 9868 dokumentiert neben diesem Verhalten getesteter Altempfänger auch Abweichungen: Ein eingebettetes Gerät
> reichte das ganze IP-Datagramm weiter, ein Erkennungssystem meldete die Differenz als Angriff.

**Bewertung:** Neben diesem Verhalten getesteter Altempfänger auch Abweichungen ist eine verschachtelte Einleitung vor
zwei bereits konkreten Beispielen.

**Vorschlag:** RFC 9868 nennt auch abweichendes Verhalten: Ein eingebettetes Gerät reichte das ganze IP-Datagramm
weiter, ein Erkennungssystem meldete die Differenz als Angriff.

**B017 · Satz · [Zeile 411](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:411>) · Belassen**

> Die Erweiterung ist daher für Endsysteme typischerweise, nicht ausnahmslos, abwärtskompatibel; reale Pfade untersucht
> Kapitel 6.

**Bewertung:** Der Satz hält die Einschränkung der Kompatibilität ausdrücklich fest und verweist knapp auf die
Pfadmessungen.

**B018 · Satz · [Zeile 412](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:412>) · Belassen**

> Für IP bleibt die Surplus Area gewöhnliche IP-Nutzlast innerhalb von Total Length; neue IP-Felder oder eine geänderte
> IPv4-Verarbeitung entstehen nicht.

**Bewertung:** Der Satz erklärt konkret, was die Surplus Area für IP bedeutet und welche IP-Eigenschaften gleich
bleiben.

**B019 · Satz · [Zeile 416](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:416>) · Belassen**

> Die Surplus Area darf an jedem gültigen Byte-Offset, auch einem ungeraden, beginnen.

**Bewertung:** Die Regel nennt den zulässigen Beginn und schließt ungerade Positionen ausdrücklich ein.

**B020 · Satz · [Zeile 416](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:416>) · Streichen, optional**

> Das Ausrichtungsproblem wird in ihr gelöst (Abschnitt 2.3.2).

**Bewertung:** Die abstrakte Vorankündigung eines Ausrichtungsproblems erklärt weder Ursache noch Lösung; beides folgt
konkret in 2.3.2.

**Vorschlag:** Satz entfernen; die Begründung und etwaige Nachbarsätze oben beachten.

**B021 · Satz · [Zeile 417](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:417>) · Belassen**

> UDP Length gibt weiterhin die Gesamtlänge von UDP-Header und UDP-Nutzdaten an.

**Bewertung:** Die kürzlich geklärte Bedeutung von UDP Length ist direkt und verständlich formuliert.

**B022 · Satz · [Zeile 418](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:418>) · Belassen**

> Der Empfänger kann damit zugleich den Beginn einer vorhandenen Surplus Area bestimmen: Sie beginnt unmittelbar hinter
> diesem Bereich.

**Bewertung:** Der Empfänger und der von ihm bestimmte Beginn sind klar; dieser Bereich verweist auf UDP-Header und
Nutzdaten im Vorsatz.

### 2.3.2 Aufbau und Ausrichtung

**B023 · Satz · [Zeile 427](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:427>) · Belassen**

> Trägt die Surplus Area Optionen, ist sie vollständig strukturiert; ungedeutete Restbytes gibt es dann nicht.

**Bewertung:** Die beiden Satzteile erläutern dieselbe Eigenschaft: Der Aufbau weist den vorhandenen Bytes eine Struktur
zu.

**B024 · Satz · [Zeile 428](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:428>) · Vereinfachen, Klarheit**

> Sie beginnt mit der Option Checksum (OCS), einem 2 Byte großen Prüfsummenfeld an der ersten 2-Byte-Grenze der Area,
> gemessen am Beginn des IP-Datagramms.

**Bewertung:** Die lange Apposition verbindet Feldname, Größe, Ausrichtung und Bezugspunkt; gemessen am Beginn hat dabei
keinen eindeutigen grammatischen Bezug.

**Vorschlag:** An der ersten 2-Byte-Grenze der Surplus Area steht das 2 Byte große Prüfsummenfeld Option Checksum (OCS).
Die Bytepositionen werden ab dem Beginn des IP-Datagramms gezählt.

**B025 · Satz · [Zeile 429](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:429>) · Belassen**

> Beginnt die Surplus Area an einem ungeraden Offset, stellt genau ein Nullbyte vor dem OCS diese Ausrichtung her (das
> Pad).

**Bewertung:** Bedingung, Position und Zweck des einzelnen Nullbytes stehen in einem klaren Zusammenhang.

**B026 · Satz · [Zeile 430](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:430>) · Belassen**

> Hinter dem OCS folgt die Optionsliste im TLV-Format (Type-Length-Value, Abschnitt 2.3.4); bei gewöhnlichen Datagrammen
> läuft sie bis zum Ende der Surplus Area oder endet vorzeitig mit EOL, worauf nur noch Nullbytes folgen.

**Bewertung:** Der Satz beschreibt den Aufbau in seiner räumlichen Reihenfolge; EOL und TLV werden durch den Verweis
weiter erklärt.

**B027 · Satz · [Zeile 433](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:433>) · Belassen**

> Bei UDP-Fragmenten folgen hinter dem Optionsbereich noch die Fragmentdaten (Abschnitt 2.3.5).

**Bewertung:** Die gerade vorgenommene Klarstellung benennt den Optionsbereich und die nachfolgenden Fragmentdaten
eindeutig.

**B028 · Satz · [Zeile 435](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:435>) · Vereinfachen, optional**

> Diese Anatomie zeigt Abbildung 2.6 an einem Datagramm mit 5 Byte Nutzdaten und einer einzelnen Option:

**Bewertung:** Anatomie ist eine unnötige bildhafte Benennung für den bereits beschriebenen Aufbau.

**Vorschlag:** Diesen Aufbau zeigt Abbildung 2.6 an einem Datagramm mit 5 Byte Nutzdaten und einer einzelnen Option:

**B029 · Definition/Beschriftung · [Zeile 493](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:493>) · Vereinfachen, optional**

> Anatomie eines Datagramms mit UDP Options

**Bewertung:** Die nominale Bildunterschrift kann denselben Inhalt ohne die Metapher Anatomie benennen.

**Vorschlag:** Aufbau eines Datagramms mit UDP Options

**B030 · Satz · [Zeile 497](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:497>) · Vereinfachen, optional**

> Aus Abbildung 2.6 geht hervor, wie die Bausteine ineinandergreifen: UDP Length = 8 + 5 = 13 lässt die Surplus Area bei
> Byte 20 + 13 = 33 beginnen.

**Bewertung:** Wie die Bausteine ineinandergreifen kündigt die Erklärung nur an; die Zahlen beschreiben den Zusammenhang
bereits unmittelbar.

**Vorschlag:** In Abbildung 2.6 beträgt UDP Length 8 + 5 = 13 Byte. Die Surplus Area beginnt deshalb bei Byte 20 + 13 =
33.

**B031 · Satz · [Zeile 498](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:498>) · Belassen**

> Dieser Offset ist ungerade, also rückt ein Pad-Byte das OCS auf die 2-Byte-Grenze bei Byte 34, und die erste Option
> beginnt bei Byte 36.

**Bewertung:** Der Satz führt das Zahlenbeispiel mit nachvollziehbarer Ursache und den beiden Folgepositionen fort.

**B032 · Satz · [Zeile 500](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:500>) · Belassen**

> Die unterste Ebene der Abbildung unterscheidet die Prüfbereiche bei verwendeten Prüfsummen: Die UDP-Prüfsumme erfasst
> den UDP-Header und die Nutzdaten; zusätzlich geht der Pseudo-Header in ihre Berechnung ein (Abschnitt 2.2.1).

**Bewertung:** Der Satz kennzeichnet verwendete Prüfsummen und trennt den sichtbaren UDP-Bereich vom zusätzlich
einbezogenen Pseudo-Header.

**B033 · Satz · [Zeile 502](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:502>) · Belassen**

> Das OCS prüft die Surplus Area ab dem OCS-Feld.

**Bewertung:** Der Anfang des OCS-Prüfbereichs ist kurz und eindeutig benannt.

**B034 · Satz · [Zeile 503](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:503>) · Belassen**

> Ein davorliegendes Pad-Byte prüft der Empfänger gesondert auf null.

**Bewertung:** Der Empfänger, das zu prüfende Byte und der erforderliche Wert sind ausdrücklich benannt.

**B035 · Satz · [Zeile 505](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:505>) · Vereinfachen, optional**

> Für diese Stelle formuliert RFC 9868 verbindliche Regeln: Der Sender darf Optionen an jedem gültigen UDP-Length-Offset
> beginnen lassen, und Ausrichtungsbytes vor dem OCS müssen null sein.

**Bewertung:** Für diese Stelle formuliert verbindliche Regeln ist eine verzichtbare Einleitung vor der konkreten
Senderregel.

**Vorschlag:** Der Sender darf Optionen an jedem gültigen UDP-Length-Offset beginnen lassen. Ausrichtungsbytes vor dem
OCS müssen null sein.

**B036 · Satz · [Zeile 507](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:507>) · Vereinfachen, Klarheit**

> Findet der Empfänger dort einen anderen Wert, greift zum ersten Mal eine Grundregel, die alle weiteren Prüfungen
> dieses Abschnitts teilen: Im Standardfall kostet ein Fehler in der Surplus Area nur die Optionen.

**Bewertung:** Die allgemeine Grundregel ist für die späteren Rückverweise nötig und soll erhalten bleiben. Unnötig sind
die Ankündigung ihres erstmaligen Auftretens und die bildhafte Wendung „kostet... nur die Optionen“. Zusammen mit B037
lesen.

**Vorschlag:** Für Fehler in der Surplus Area gilt im Standardfall: Der Empfänger verwirft die Optionsliste still und
stellt die Nutzdaten trotzdem zu.

**B037 · Satz · [Zeile 509](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:509>) · Vereinfachen, Klarheit**

> Der Empfänger verwirft die Optionsliste still und stellt die Nutzdaten trotzdem zu, wie es auch ein Altempfänger täte.

**Bewertung:** Die Pad-Bedingung wird als konkreter Anwendungsfall an die allgemeine Regel in B036 angeschlossen. So
bleiben Regel, Fehlerbedingung und Vergleich mit dem Altempfänger erhalten. Nur gemeinsam mit B036 anwenden.

**Vorschlag:** Das gilt auch bei einem Ausrichtungsbyte ungleich null und entspricht dem Verhalten eines Altempfängers.

**B038 · Satz · [Zeile 510](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:510>) · Belassen**

> Dieser Standardfall setzt ein gültiges Datagramm voraus.

**Bewertung:** Der Satz nennt die Voraussetzung des Standardfalls ausdrücklich; die nächsten Sätze erklären sie.

**B039 · Satz · [Zeile 511](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:511>) · Belassen**

> Eine ungültige UDP Length oder eine fehlgeschlagene UDP-Prüfsumme führt zum Verwerfen des ganzen Datagramms, noch
> bevor Optionen betrachtet werden.

**Bewertung:** Die beiden Fehlerfälle und das Verwerfen vor der Optionsprüfung sind klar; der Empfänger ergibt sich aus
dem Absatz.

**B040 · Satz · [Zeile 512](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:512>) · Belassen**

> Eine zulässig ungenutzte Prüfsumme (Abschnitt 2.2.1) ist dagegen kein Fehler.

**Bewertung:** Der Satz grenzt eine zulässig ungenutzte Prüfsumme eindeutig vom Fehlerfall ab und verweist auf die
Erklärung.

**B041 · Satz · [Zeile 514](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:514>) · Belassen**

> Außerdem darf die Anwendung kein strengeres Verhalten angefordert haben.

**Bewertung:** Die zusätzliche Bedingung und die dafür verantwortliche Anwendung sind eindeutig benannt.

**B042 · Satz · [Zeile 514](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:514>) · Belassen**

> FRAG und UNSAFE sind von dieser vereinfachten Regel ausgenommen; ihre Sonderfälle behandelt Abschnitt 2.3.5.

**Bewertung:** Die gerade präzisierte Ausnahme nennt FRAG und UNSAFE ausdrücklich und führt zur zuständigen Erklärung.

**B043 · Satz · [Zeile 517](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:517>) · Vereinfachen, optional**

> Die 2-Byte-Ausrichtung selbst begründet der RFC pragmatisch: Das OCS wird, wie der nächste Unterabschnitt zeigt, über
> 16-Bit-Wörter berechnet, und die Ausrichtung erspart dieser Rechnung das Vertauschen von Bytes.

**Bewertung:** Pragmatisch und der Einschub zum nächsten Unterabschnitt unterbrechen die bereits konkrete Begründung der
Ausrichtung.

**Vorschlag:** Das OCS wird aus 16-Bit-Wörtern berechnet; die 2-Byte-Ausrichtung vermeidet dabei das Vertauschen von
Bytes.

**B044 · Satz · [Zeile 521](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:521>) · Vereinfachen, Klarheit**

> Ob ein Pad-Byte nötig ist, entscheidet allein die Parität des Startoffsets; es gibt nur zwei Fälle, kein Pad oder
> genau eines.

**Bewertung:** Parität ist ein unnötiger zusätzlicher Fachbegriff für die hier benötigte Entscheidung zwischen gerade
und ungerade.

**Vorschlag:** Bei einem geraden Startoffset ist kein Pad-Byte nötig, bei einem ungeraden genau eines.

**B045 · Satz · [Zeile 522](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:522>) · Belassen**

> Den Unterschied zeigt Abbildung 2.7 an zwei sonst gleichen Datagrammen, deren Nutzdaten sich um ein einziges Byte
> unterscheiden:

**Bewertung:** Der Satz erklärt konkret den einzigen Unterschied zwischen den beiden folgenden Beispielen.

**B046 · Definition/Beschriftung · [Zeile 553](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:553>) · Vereinfachen, Klarheit**

> Paritätsentscheid für das Pad-Byte vor dem OCS

**Bewertung:** Die nominale Bildunterschrift verwendet mit Paritätsentscheid einen abstrakten Begriff, obwohl die
Abbildung zwei einfache Fälle zeigt.

**Vorschlag:** Pad-Byte bei geradem und ungeradem Startoffset

**B047 · Satz · [Zeile 557](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:557>) · Vereinfachen, Klarheit**

> Aus Abbildung 2.7 geht hervor, dass bereits ein einziges Nutzdatenbyte über das Pad entscheidet: Bei einem IP-Header
> ohne Optionen liegt der Startoffset bei 20 + UDP Length, sodass allein die Parität von UDP Length den Ausschlag gibt.

**Bewertung:** Parität und den Ausschlag geben verdecken die einfache Entscheidung zwischen geradem und ungeradem
Offset; die Formeleinordnung soll bleiben.

**Vorschlag:** Bei einem IP-Header ohne Optionen beginnt die Surplus Area bei Byte 20 + UDP Length. Durch ein
zusätzliches Nutzdatenbyte wird aus einer geraden UDP Length eine ungerade oder umgekehrt. Dadurch ändert sich, ob ein
Pad-Byte nötig ist (Abbildung 2.7).

**B048 · Satz · [Zeile 559](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:559>) · Belassen**

> An der Größe der Surplus Area hängt zugleich, ob sie überhaupt Optionen trägt: Nötig sind mindestens 2 Byte bei
> geradem und 3 Byte bei ungeradem Start, damit das ausgerichtete OCS vollständig hineinpasst.

**Bewertung:** Die benötigten Größen, die Unterscheidung nach Startposition und der Zweck sind ausdrücklich angegeben.

**B049 · Satz · [Zeile 561](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:561>) · Vereinfachen, optional**

> Ein kleinerer Überschuss enthält schlicht keine Optionen und ist kein Fehlerfall; passt genau das OCS hinein und sonst
> nichts, ist die Optionsliste leer und das Datagramm ebenfalls gültig.

**Bewertung:** Zwei unterschiedliche Größenfälle stehen in einem Satz; sie lassen sich ohne inhaltliche Änderung
getrennt lesen. Schlicht ist entbehrlich.

**Vorschlag:** Ein kleinerer Überschuss enthält keine Optionen, ist aber kein Fehlerfall. Passt genau das OCS hinein und
sonst nichts, ist die Optionsliste leer und das Datagramm ebenfalls gültig.

**B050 · Satz · [Zeile 563](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:563>) · Vereinfachen, optional**

> Nutzdaten braucht es dagegen keine: Auch ein Datagramm mit UDP Length 8, also leerem Nutzdatenteil, kann Optionen
> tragen; davon macht später die FRAG-Option Gebrauch, deren Fragmente ihre Daten vollständig in der Surplus Area
> transportieren.

**Bewertung:** Die vorangestellte Verneinung und davon macht später Gebrauch verzögern die konkrete Aussage zum leeren
Nutzdatenteil.

**Vorschlag:** Auch ein Datagramm mit UDP Length 8 und damit ohne UDP-Nutzdaten kann Optionen tragen. Die FRAG-Option
nutzt dies: Ihre Fragmente transportieren ihre Daten vollständig in der Surplus Area.

### 2.3.3 OCS und Fehlerbehandlung

**B051 · Satz · [Zeile 570](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:570>) · Belassen**

> Das OCS selbst ist eine gewöhnliche Internet-Prüfsumme mit derselben Einerkomplementarithmetik, die Abschnitt 2.2.1
> für die UDP-Prüfsumme beschreibt.

**Bewertung:** Der Vergleich erklärt die wiederverwendete Prüfsummenarithmetik; er führt kein weiteres Protokoll ein.

**B052 · Satz · [Zeile 571](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:571>) · Streichen, optional**

> Zwei Eigenheiten unterscheiden die beiden.

**Bewertung:** Der Satz kündigt nur die folgende Erklärung an. Bei Streichung entfallen Erstens und Zweitens wie in B053
und B054 vorgeschlagen.

**Vorschlag:** Satz entfernen; die Begründung und etwaige Nachbarsätze oben beachten.

**B053 · Satz · [Zeile 572](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:572>) · Vereinfachen, Klarheit**

> Erstens schützt das OCS genau den Bereich, den die UDP-Prüfsumme ausspart: Die Summe läuft ab dem ausgerichteten
> OCS-Feld über den Rest der Surplus Area, wobei das OCS-Feld selbst als null gilt; das Pad davor wird getrennt auf null
> geprüft und ist so mitgeschützt.

**Bewertung:** Der Satz mischt erneut den Schutzbereich, die Rechenschritte des Senders und die getrennte
Empfangsprüfung des Pads. Die Handlungsträger sollten ausdrücklich getrennt werden.

**Vorschlag:** Der Sender summiert die Wörter ab dem ausgerichteten OCS-Feld bis zum Ende der Surplus Area. Das OCS-Feld
behandelt er dabei als null. Der Empfänger prüft das Pad davor getrennt auf null.

**B054 · Satz · [Zeile 574](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:574>) · Vereinfachen, optional**

> Zweitens geht zusätzlich die Länge der gesamten Surplus Area einschließlich des Pads als vorzeichenloser
> 16-Bit-Summand in die Rechnung ein, obwohl dieser Wert in keinem eigenen Feld des Pakets steht.

**Bewertung:** Die Rechnung und das Fehlen eines eigenen Paketfelds sind leichter getrennt lesbar; Zweitens entfällt
zusammen mit B052. Der technische 16-Bit-Wert bleibt erhalten.

**Vorschlag:** Zusätzlich addiert der Sender die Länge der gesamten Surplus Area einschließlich des Pads als
vorzeichenlosen 16-Bit-Wert. Dieser Wert steht in keinem eigenen Feld des Pakets.

**B055 · Satz · [Zeile 576](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:576>) · Vereinfachen, Klarheit**

> Das folgt demselben Gedanken wie der Pseudo-Header aus Abschnitt 2.2.1: Wie die UDP-Prüfsumme dort die UDP Length
> einbezieht, bezieht das OCS die Surplus-Länge ein, und beide Seiten können diesen Summanden unabhängig voneinander aus
> den Längenfeldern ableiten.

**Bewertung:** Derselbe Gedanke, beide Seiten und diesen Summanden verlangen mehrere gedankliche Rückbezüge zwischen
zwei Prüfsummen. Wichtig ist hier, wie Sender und Empfänger an die Surplus-Länge gelangen; der Vergleich wiederholt
bereits erklärte Längenbeiträge.

**Vorschlag:** Sender und Empfänger können die Surplus-Länge unabhängig voneinander aus den Längenfeldern ableiten.

**B056 · Satz · [Zeile 579](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:579>) · Belassen**

> Der Sender trägt das invertierte Ergebnis in das Feld ein.

**Bewertung:** Der Sender, seine Handlung und das einzutragende Ergebnis sind ausdrücklich benannt.

**B057 · Satz · [Zeile 580](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:580>) · Belassen**

> Abschnitt 9 verlangt ein OCS ungleich null, sobald die UDP-Prüfsumme ungleich null ist, und kennzeichnet ein
> ungenutztes OCS mit null.

**Bewertung:** Die Bedingung für ein OCS ungleich null und die Bedeutung des Nullwerts sind klar voneinander
unterscheidbar.

**B058 · Satz · [Zeile 581](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:581>) · Vereinfachen, Klarheit**

> Eine ausdrückliche Senderegel für eine errechnete Null enthält der Abschnitt nicht; weil der Nullwert die unbenutzte
> Form kennzeichnet, bleibt für ein verwendetes OCS im Einerkomplement nur die Abbildung auf 0xFFFF, analog zur
> UDP-Prüfsumme.

**Bewertung:** Errechnete Null, Nullwert und unbenutzte Form sind in einer langen Begründung ineinander geschoben. Die
Unterscheidung von berechnetem Ergebnis und übertragenem Wert sollte ausdrücklich sichtbar sein.

**Vorschlag:** Abschnitt 9 enthält keine ausdrückliche Senderegel für den Fall, dass die Berechnung null ergibt. Der
Wert 0x0000 kennzeichnet ein ungenutztes OCS. Für ein verwendetes OCS trägt der Sender eine berechnete Null deshalb als
0xFFFF ein, wie bei der UDP-Prüfsumme.

**B059 · Satz · [Zeile 584](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:584>) · Belassen**

> Der Empfänger summiert die Wörter der Surplus Area einschließlich des OCS-Felds sowie den Längensummanden und erwartet
> wie in Abschnitt 2.2.1 lauter Einsen, also 0xFFFF.

**Bewertung:** Der Empfänger, die zu addierenden Werte und das erwartete Ergebnis sind konkret benannt.

**B060 · Satz · [Zeile 588](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:588>) · Vereinfachen, optional**

> Tabelle 2.1 führt diese Rechnung an einem bewusst kleinen Beispiel vollständig vor.

**Bewertung:** Bewusst und vollständig bewerten die Darstellung, ohne dem Leser zusätzliche Information über die
Rechnung zu geben.

**Vorschlag:** Tabelle 2.1 zeigt die Berechnung an einem kleinen Beispiel.

**B061 · Definition/Beschriftung · [Zeile 592](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:592>) · Belassen**

> OCS-Rechnung einer 6-Byte-Surplus-Area bei geradem Startoffset

**Bewertung:** Die vollständige nominale Tabellenunterschrift nennt Rechengegenstand, Größe und Startbedingung.

**B062 · Satz · [Zeile 609](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:609>) · Belassen**

> Die Optionswörter stehen für zwei NOP, ein EOL und ein Nullbyte.

**Bewertung:** Die vier Beispielbytes werden unmittelbar den zuvor eingeführten Optionen beziehungsweise der Nullfüllung
zugeordnet.

**B063 · Satz · [Zeile 609](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:609>) · Belassen**

> Die zwei NOP dienen nur der Rechnung; als Füllung vor EOL rät RFC 9868 von ihnen ab.

**Bewertung:** Der Satz erklärt konkret den didaktischen Zweck der NOPs und die Einschränkung für reguläre Verwendung.

**B064 · Satz · [Zeile 610](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:610>) · Belassen**

> Ein regulärer Sender schriebe EOL unmittelbar hinter das OCS.

**Bewertung:** Der kurze Satz sagt eindeutig, welchen Wert ein regulärer Sender stattdessen einsetzen würde.

**B065 · Satz · [Zeile 613](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:613>) · Vereinfachen, optional**

> Diese Bauart hat einen praktischen Hintergrund: Manche fehlerhafte Middleboxes berechnen die UDP-Prüfsumme über die
> gesamte IP-Nutzlast statt nur bis UDP Length und verwenden auch im Pseudo-Header diese größere Länge.

**Bewertung:** Nur die allgemeine Einleitung Diese Bauart hat einen praktischen Hintergrund entfällt. Die gerade
ergänzte Voraussetzung zur Pseudo-Header-Länge ist klar und bleibt vollständig erhalten.

**Vorschlag:** Manche fehlerhafte Middleboxes berechnen die UDP-Prüfsumme über die gesamte IP-Nutzlast statt nur bis UDP
Length und verwenden auch im Pseudo-Header diese größere Länge.

**B066 · Satz · [Zeile 615](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:615>) · Belassen**

> Weil das OCS über die Surplus Area und deren Länge gebildet und anschließend invertiert wird, neutralisiert es den
> Beitrag der fälschlich einbezogenen Surplus Area und den Längenzuschlag im Pseudo-Header.

**Bewertung:** Die gerade ergänzte Erklärung nennt beide zu kompensierenden Beiträge; der Folgesatz erklärt das
Ergebnis.

**B067 · Satz · [Zeile 617](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:617>) · Belassen**

> Mit gültigem OCS fällt die UDP-Prüfsumme deshalb genauso aus wie bei korrekter Berechnung.

**Bewertung:** Der Satz nennt kurz die Folge der zuvor beschriebenen Kompensation.

**B068 · Satz · [Zeile 619](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:619>) · Vereinfachen, optional**

> In erster Linie dient das OCS ohnehin dem Erkennen zufälliger Fehler und anderweitiger, nicht standardkonformer
> Nutzungen der Surplus Area; ein Schutz gegen gezielte Angriffe ist es ausdrücklich nicht.

**Bewertung:** Ohnehin wertet den vorigen Absatz ab; der dichte Nominalstil Erkennen anderweitiger Nutzungen lässt sich
direkt ausdrücken.

**Vorschlag:** Das OCS dient vor allem dazu, zufällige Fehler und nicht standardkonforme Nutzungen der Surplus Area zu
erkennen. Es schützt nicht gegen gezielte Angriffe.

**B069 · Satz · [Zeile 621](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:621>) · Vereinfachen, Klarheit**

> Wie die UDP-Prüfsumme ist das OCS zudem bedingt abschaltbar: Der Wert 0x0000 bedeutet ungenutzt, zulässig ist das nur,
> wenn auch die UDP-Prüfsumme null ist, und Implementierungen müssen standardmäßig ein echtes OCS setzen.

**Bewertung:** Bedingt abschaltbar und echtes OCS sind unbestimmter als die bereits bekannten Nullwerte. Drei
unterschiedliche Regeln sollten getrennt erkennbar sein.

**Vorschlag:** Ein OCS-Wert von 0x0000 bedeutet, dass das OCS nicht verwendet wird. Das ist nur zulässig, wenn auch die
UDP-Prüfsumme null ist. Implementierungen müssen standardmäßig ein OCS ungleich null setzen.

**B070 · Satz · [Zeile 624](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:624>) · Belassen**

> Schlägt die Prüfung beim Empfänger fehl, gilt die Grundregel aus Abschnitt 2.3.2: Optionen still verwerfen, Nutzdaten
> bei bestandener oder zulässig ungenutzter UDP-Prüfsumme dennoch zustellen.

**Bewertung:** Bedingung und Empfangsentscheidung sind klar; der Rückverweis erhält die bereits erläuterten Ausnahmen.

### 2.3.4 TLV-Format und Empfangsentscheidung

**B071 · Satz · [Zeile 631](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:631>) · Vereinfachen, Klarheit**

> Die Optionen hinter dem OCS folgen dem TLV-Muster, dessen Syntax RFC 9868 bewusst an TCP anlehnt: Ein 1 Byte großes
> Feld Kind, benannt nach dem TCP-Vorbild, identifiziert die Option; das 1 Byte große Feld Length zählt die Gesamtlänge
> der Option einschließlich Kind und Length selbst; dahinter kann ein Wert folgen.

**Bewertung:** Der Satz enthält die gesamte Feldbeschreibung und zweimal einen Hinweis auf TCP. Die Benennungsgeschichte
hilft bei der Frage nach Aufbau und Funktion nicht und unterbricht die Zuordnung von Feld und Zweck.

**Vorschlag:** Die Optionen hinter dem OCS folgen dem TLV-Format. Das 1 Byte große Feld Kind identifiziert die Option.
Das 1 Byte große Feld Length gibt die Gesamtlänge einschließlich Kind und Length an. Dahinter kann ein Wert folgen.

**B072 · Satz · [Zeile 635](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:635>) · Vereinfachen, Klarheit**

> Für die Größe des Werts ist das nur scheinbar eine enge Grenze: Im Standardformat fasst eine Option höchstens 254 Byte
> einschließlich Kind und Length; größere Optionen weichen auf ein erweitertes Format aus, in dem der Wert 255 im
> Length-Feld ein zusätzliches 16-Bit-Längenfeld ankündigt.

**Bewertung:** Für die Größe des Werts lenkt auf den Value-Teil, obwohl anschließend die Gesamtlänge der Option erklärt
wird. Die vermeintliche Grenze ist eine unnötige rhetorische Einleitung.

**Vorschlag:** Im Standardformat ist die gesamte Option einschließlich Kind und Length höchstens 254 Byte lang. Größere
Optionen verwenden ein erweitertes Format: Der Wert 255 im Length-Feld kündigt ein zusätzliches 16-Bit-Längenfeld an.

**B073 · Satz · [Zeile 638](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:638>) · Belassen**

> Damit sind je Option höchstens 65535 Byte einschließlich der Headerfelder kodierbar.

**Bewertung:** Der Satz benennt die kodierbare Gesamtlänge ausdrücklich einschließlich der Headerfelder.

**B074 · Satz · [Zeile 639](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:639>) · Vereinfachen, Klarheit**

> Eine zusätzliche Gesamtgrenze für den Optionsraum kennt RFC 9868 dagegen bewusst nicht: Wie das Entwurfsprinzip der
> fehlenden Längengrenze in Abschnitt 2.3.5 festhält, gilt allein die Grenze des UDP-Pakets selbst; bei einem nicht
> fragmentierten Datagramm begrenzt somit der im IP-Datagramm verfügbare Platz, wie viele Optionen es trägt.

**Bewertung:** Der eingeschobene Verweis auf ein Entwurfsprinzip unterbricht den Zusammenhang zwischen fehlender
Zusatzgrenze und tatsächlich verfügbarem Platz.

**Vorschlag:** RFC 9868 setzt keine zusätzliche Gesamtgrenze für den Optionsraum; maßgeblich ist die Grenze des
UDP-Pakets selbst (Abschnitt 2.3.5). Bei einem nicht fragmentierten Datagramm begrenzt der im IP-Datagramm verfügbare
Platz, wie viele Optionen es trägt.

**B075 · Satz · [Zeile 642](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:642>) · Vereinfachen, Klarheit**

> Die beiden Ein-Byte-Codes besitzen als einzige Ausnahmen kein Längenfeld: NOP (No Operation, Kind 1) dient mit
> impliziter Länge eins der Ausrichtung zwischen Optionen und darf sich dafür wiederholen.

**Bewertung:** Die beiden Ein-Byte-Codes nennt die zwei Ausnahmen noch nicht; implizite Länge erschwert die einfache
Aussage, dass NOP aus einem Byte besteht.

**Vorschlag:** Nur NOP und EOL besitzen kein Längenfeld. NOP (No Operation, Kind 1) ist ein Byte lang und dient der
Ausrichtung zwischen Optionen. Dafür darf NOP mehrfach vorkommen.

**B076 · Satz · [Zeile 644](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:644>) · Belassen**

> EOL (End of Option List, Kind 0) beendet die Liste vorzeitig; die Bytes dahinter muss der Sender bis zum Ende der
> Surplus Area beziehungsweise des Optionsbereichs eines UDP-Fragments auf null setzen.

**Bewertung:** EOL, Senderhandlung und beide räumlichen Grenzen sind konkret benannt; die Fragmentausnahme muss erhalten
bleiben.

**B077 · Satz · [Zeile 647](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:647>) · Belassen**

> Der Empfänger darf diese Nullfüllung prüfen, muss es aber nicht; findet er dabei ein Byte ungleich null, verwirft er
> nach der Grundregel aus Abschnitt 2.3.2 die gesamte Optionsliste still.

**Bewertung:** Der Satz unterscheidet klar zwischen freiwilliger Prüfung und verpflichtender Reaktion auf einen
erkannten Fehler.

**B078 · Satz · [Zeile 649](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:649>) · Streichen, optional**

> Variable Optionslängen und künftige Erweiterungen sind damit im Format selbst angelegt.

**Bewertung:** Der abstrakte Abschlusssatz wiederholt nur die zuvor erklärten variablen Längen und Erweiterungen.

**Vorschlag:** Satz entfernen; die Begründung und etwaige Nachbarsätze oben beachten.

**B079 · Satz · [Zeile 652](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:652>) · Vereinfachen, optional**

> Für die Anzahl der Optionen gilt dasselbe Bild wie für ihre Länge: Eine feste Obergrenze gibt es nicht; ohne
> vorzeitiges EOL endet die Liste erst am Ende der Surplus Area.

**Bewertung:** Gilt dasselbe Bild wie für ihre Länge ist eine unnötige Vergleichseinleitung; die Aussage zur Anzahl kann
unmittelbar beginnen.

**Vorschlag:** Für die Anzahl der Optionen gibt es keine feste Obergrenze; ohne vorzeitiges EOL endet die Liste erst am
Ende der Surplus Area.

**B080 · Satz · [Zeile 653](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:653>) · Streichen, optional**

> Begrenzend wirken stattdessen zwei Regelgruppen.

**Bewertung:** Der Satz kündigt nur zwei Regelgruppen an. Die Regeln selbst folgen unmittelbar; Erstens und Zweitens
entfallen entsprechend B081 und B082.

**Vorschlag:** Satz entfernen; die Begründung und etwaige Nachbarsätze oben beachten.

**B081 · Satz · [Zeile 654](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:654>) · Vereinfachen, Klarheit**

> Erstens die Wiederholungsregeln: Außer FRAG, NOP und den Experimentaloptionen soll jede Option höchstens einmal je
> Datagramm vorkommen, ein Empfänger wertet von einer solchen Option ohnehin nur die erste Instanz, und ein mehrfaches
> FRAG macht die gesamte Optionsliste ungültig; NOP wiederum soll höchstens siebenmal in Folge stehen und nicht als
> Ersatz für EOL samt Nullfüllung dienen.

**Bewertung:** Ein Satz enthält vier unterschiedliche Wiederholungsregeln, mehrere Ausnahmen und zwei Normstellen. Die
Senderempfehlung, das Empfangsverhalten und die Sonderfälle sollten einzeln lesbar sein.

**Vorschlag:** Außer FRAG, NOP und den Experimentaloptionen soll jede Option höchstens einmal je Datagramm vorkommen.
Wiederholt sich eine der übrigen Optionen, wertet der Empfänger nur ihr erstes Vorkommen aus. Mehrfaches FRAG macht die
gesamte Optionsliste ungültig. NOP soll höchstens siebenmal in Folge stehen und nicht als Ersatz für EOL samt
Nullfüllung dienen.

**B082 · Satz · [Zeile 660](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:660>) · Vereinfachen, optional**

> Zweitens die Vollständigkeitsregel: Jede Option muss ganz in die Surplus Area passen.

**Bewertung:** Der Name Vollständigkeitsregel wiederholt die anschließende klare Anforderung; Zweitens entfällt mit
B080.

**Vorschlag:** Jede Option muss vollständig in die Surplus Area passen.

**B083 · Satz · [Zeile 660](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:660>) · Vereinfachen, Klarheit**

> Meldet ein Length-Feld eine Länge über deren Ende hinaus, gilt die gesamte Surplus Area als fehlerhaft, und der
> Empfänger verwirft still alle Optionen, nicht nur die angeschnittene; das verifizierte Erratum EID 8834 bestätigt
> diese Regel gegen eine ältere, weichere Formulierung in Abschnitt 14.

**Bewertung:** Fehlererkennung, Verwerfen der gesamten Liste und Geschichte der Normkorrektur stehen in einem langen
Satz; deren Ende und diese Regel verlangen zusätzliche Rückbezüge.

**Vorschlag:** Reicht eine Option laut ihrem Length-Feld über das Ende der Surplus Area hinaus, gilt die gesamte Surplus
Area als fehlerhaft. Der Empfänger verwirft dann still alle Optionen. Das verifizierte Erratum EID 8834 bestätigt diese
Regel und korrigiert die ältere Formulierung in Abschnitt 14.

**B084 · Satz · [Zeile 664](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:664>) · Vereinfachen, optional**

> Im Regelfall entsteht diese Lage nicht, denn der Sender muss die Surplus Area von vornherein so bemessen, dass das OCS
> und alle Optionen vollständig hineinpassen.

**Bewertung:** Im Regelfall entsteht diese Lage nicht ist eine abstrakte Vorbemerkung; die konkrete Senderpflicht
erklärt bereits, wie der Fehler vermieden wird.

**Vorschlag:** Der Sender muss in der Surplus Area von vornherein genügend Platz für das OCS und alle Optionen vorsehen.

**B085 · Satz · [Zeile 667](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:667>) · Streichen, optional**

> Damit sind die Prüfschritte des Standardpfads beisammen.

**Bewertung:** Der Satz meldet nur einen Zwischenstand der Darstellung. Die Abbildung kann unmittelbar angekündigt
werden; B086 übernimmt den ausdrücklichen Bezug.

**Vorschlag:** Satz entfernen; die Begründung und etwaige Nachbarsätze oben beachten.

**B086 · Satz · [Zeile 667](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:667>) · Vereinfachen, optional**

> Abbildung 2.8 ordnet sie in der Reihenfolge, in der ein optionsfähiger Empfänger sie durchläuft, und stellt ihnen die
> vorgelagerte Prüfung des Datagramms selbst voran:

**Bewertung:** Ordnet sie und stellt ihnen voran beschreibt die Präsentation umständlich; ohne B085 braucht sie außerdem
einen ausdrücklichen Bezug.

**Vorschlag:** Abbildung 2.8 zeigt, in welcher Reihenfolge ein optionsfähiger Empfänger das Datagramm und die Surplus
Area prüft:

**B087 · Definition/Beschriftung · [Zeile 713](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:713>) · Belassen**

> Empfangsentscheidung für die Surplus Area im Standardfall

**Bewertung:** Die vollständige nominale Bildunterschrift nennt Entscheidungsgegenstand und Geltungsbereich.

**B088 · Satz · [Zeile 717](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:717>) · Vereinfachen, Klarheit**

> Aus Abbildung 2.8 geht hervor, dass nur die vorgelagerte Prüfung des Datagramms selbst Nutzdaten kosten kann: Eine
> ungültige UDP Length oder eine falsche UDP-Prüfsumme verwirft das ganze Datagramm.

**Bewertung:** Im Original erscheint eine ungültige Länge oder Prüfsumme als Handelnde: Sie „verwirft“ das Datagramm.
Tatsächlich verwirft es der Empfänger. Die Ersatzfassung benennt ihn und erhält die Beschränkung auf den Standardfall.

**Vorschlag:** Im Standardfall können die Nutzdaten nur bei der vorgelagerten Prüfung des Datagramms verworfen werden.
Der Empfänger verwirft das ganze Datagramm, wenn UDP Length ungültig ist oder die UDP-Prüfsumme fehlschlägt.

**B089 · Satz · [Zeile 719](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:719>) · Vereinfachen, Klarheit**

> Alle Prüfungen der Surplus Area treffen dagegen höchstens die Optionen: Die beiden Größenfragen führen auf den
> harmlosen Ausgang links, die drei Prüfungen dahinter auf den Fehlerausgang rechts; genau das ist die Grundregel aus
> Abschnitt 2.3.2 im Bild.

**Bewertung:** Größenfragen, harmloser Ausgang und Fehlerausgang erklären nur die Lage im Bild. Der Leser muss selbst
zurückverfolgen, was der Empfänger prüft und ausliefert.

**Vorschlag:** Ist keine Surplus Area vorhanden oder passt das ausgerichtete OCS nicht hinein, werden die Nutzdaten ohne
Optionen zugestellt. Stellt der Empfänger bei den Prüfungen von Pad, OCS oder der Optionsliste einen Fehler fest,
verwirft er im Standardfall nur die Optionen und stellt die Nutzdaten trotzdem zu (Abschnitt 2.3.2).

**B090 · Satz · [Zeile 721](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:721>) · Vereinfachen, Klarheit**

> Bei der Auswertung selbst wird einzeln ignoriert, was nur lokal stört: eine unbekannte SAFE-Option ebenso wie spätere
> Instanzen einer gewöhnlichen wiederholten Option.

**Bewertung:** Was nur lokal stört nennt keine konkrete Regel; das Passiv und Instanzen erschweren außerdem die
Zuordnung der Empfangshandlung.

**Vorschlag:** Der Empfänger ignoriert unbekannte SAFE-Optionen einzeln. Bei wiederholten Optionen wertet er nur das
erste Vorkommen aus; ausgenommen sind FRAG, NOP und die Experimentaloptionen.

**B091 · Satz · [Zeile 723](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:723>) · Vereinfachen, Klarheit**

> Die ganze Liste ist bei den strukturellen Längenfehlern aus dem vorigen Absatz und bei mehrfachem FRAG ungültig;
> daneben darf der Empfänger sie verwerfen, wenn verpflichtend zu unterstützende Optionen (im RFC must-support,
> ausgenommen NOP und EOL) nicht vor den übrigen SAFE-Optionen stehen, und er muss es, wenn seine freiwillige
> Nullfüllungsprüfung hinter EOL ein Byte ungleich null findet.

**Bewertung:** Die Formulierung verbindet drei verschiedene Ablehnungsgründe und wechselt innerhalb desselben Satzes von
darf zu muss. Die Bezüge sie und es erschweren die Unterscheidung dieser Regeln.

**Vorschlag:** Strukturelle Längenfehler und mehrfaches FRAG machen die ganze Optionsliste ungültig. Stehen
verpflichtend zu unterstützende Optionen (im RFC must-support, ausgenommen NOP und EOL) nicht vor den übrigen
SAFE-Optionen, darf der Empfänger alle Optionen verwerfen. Prüft er freiwillig die Nullfüllung hinter EOL und findet
dabei ein Byte ungleich null, muss er alle Optionen verwerfen.

**B092 · Satz · [Zeile 728](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:728>) · Belassen**

> Die gestrichelte Randnotiz markiert die Sonderwege: Ein UDP-Fragment wird erst gepuffert und nach der Reassemblierung
> zugestellt; UNSAFE-Optionen und strengere, von der Anwendung angeforderte Empfangsregeln behandelt der folgende
> Unterabschnitt.

**Bewertung:** Die Randnotiz verbindet das Diagramm mit den Sonderfällen; Puffern, Reassemblierung und der nächste
Unterabschnitt sind klar zugeordnet.

### 2.3.5 Entwurfsprinzipien und Optionsklassen

**C001 · Satz · [Zeile 736](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:736>) · Vereinfachen, Klarheit**

> Wie dieser Bereich genutzt werden darf, bindet RFC 9868 an sechs Entwurfsprinzipien, die ein gemeinsames Ziel haben:
> UDP soll durch die Optionen seinen Charakter nicht verlieren:

**Bewertung:** Die vorangestellte indirekte Frage und die Wendung seinen Charakter nicht verlieren verschleiern die
Aussage; sechs Prinzipien als Subjekt machen den Einstieg direkt.

**Vorschlag:** RFC 9868 legt sechs Entwurfsprinzipien für UDP Options fest, damit UDP seine bisherigen Eigenschaften
behält:

**C002 · Satz · [Zeile 740](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:740>) · Belassen**

> Zustandslos: Nötiger Zustand gehört in die Anwendung oder in eine Bibliothek, die in ihrem Auftrag arbeitet.

**Bewertung:** Anwendung und beauftragte Bibliothek sind klar als zuständige Stellen genannt. Der Begriff Zustand gehört
zum hier erläuterten Prinzip.

**C003 · Satz · [Zeile 741](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:741>) · Belassen**

> Die einzige, ausdrücklich begrenzte Ausnahme ist die Zusammenführung von Fragmenten.

**Bewertung:** Nennt die Ausnahme unmittelbar nach der Grundregel und ohne unklaren Rückverweis.

**C004 · Satz · [Zeile 743](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:743>) · Belassen**

> Unidirektional: Die UDP-Schicht erzeugt nie von sich aus eine Antwort auf eine Option; ob und wann geantwortet wird,
> entscheidet die Anwendung oder eine Schicht beziehungsweise Bibliothek in ihrem Auftrag.

**Bewertung:** Trotz des Semikolons ist die Zuständigkeit eindeutig: Die UDP-Schicht antwortet nicht selbst; Anwendung
oder beauftragte Schicht entscheiden.

**C005 · Satz · [Zeile 745](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:745>) · Belassen**

> Verfahren, die auf Antworten angewiesen sind, verlagert der RFC in eigene Dokumente.

**Bewertung:** Der Satz sagt knapp, wo antwortabhängige Verfahren geregelt werden.

**C006 · Satz · [Zeile 745](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:745>) · Vereinfachen, Klarheit**

> Als Einordnung dieser Arbeit, nicht als Begründung des RFC: Diese Zurückhaltung verhindert, dass schon der
> Grundmechanismus mit gefälschter Absenderadresse als Reflektor missbraucht wird; ein ausdrücklich aktiviertes
> Antwortverfahren muss diesen Missbrauch selbst abwehren, etwa durch die Ratenbegrenzung, die RFC 9869 für eigens als
> Antwort erzeugte Datagramme vorschreibt.

**Bewertung:** Der Satz verbindet die Herkunft der Bewertung, den Angriff und die Abwehr in einer langen Kette.
Grundmechanismus, Zurückhaltung und Reflektor bleiben dabei abstrakt. Die Herkunft der Sicherheitsbewertung muss
ausdrücklich erhalten bleiben.

**Vorschlag:** Die folgende Sicherheitsbewertung stammt aus dieser Arbeit: Ohne automatische Antworten kann der
Grundmechanismus nicht dazu missbraucht werden, Antworten an gefälschte Absenderadressen zu senden. Ein ausdrücklich
aktiviertes Antwortverfahren muss diesen Missbrauch selbst abwehren. RFC 9869 schreibt beispielsweise vor, die Zahl
eigens erzeugter Antwortdatagramme pro Zeit zu begrenzen.

**C007 · Satz · [Zeile 751](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:751>) · Belassen**

> Keine eigene Längengrenze: Für den Optionsraum gilt allein die Grenze des UDP-Pakets selbst; bei einem nicht
> fragmentierten Paket ist das der im IP-Datagramm verfügbare Platz.

**Bewertung:** Die Erläuterung nach dem Semikolon konkretisiert die abstrakte Längengrenze durch den verfügbaren Platz
im IP-Datagramm.

**C008 · Satz · [Zeile 752](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:752>) · Vereinfachen, optional**

> Feste Grenzen werden erfahrungsgemäß überschritten; der RFC verweist auf die Erfahrung mit TCP-Optionen (40 Byte
> Optionsraum ) und IPv4-Adressen (32 Bit ).

**Bewertung:** Erfahrungsgemäß und Erfahrung wiederholen sich. Die Beispiele lassen sich direkt mit der Aussage zu
festen Grenzen verbinden.

**Vorschlag:** Der RFC nennt TCP-Optionen (40 Byte Optionsraum ) und IPv4-Adressen (32 Bit ) als Beispiele für feste
Grenzen, die sich später als zu eng erwiesen haben.

**C009 · Satz · [Zeile 754](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:754>) · Belassen**

> Grenzen darf eine Implementierung setzen, nicht die Spezifikation.

**Bewertung:** Der kurze Satz unterscheidet klar zwischen einer Grenze der Implementierung und einer Grenze der
Spezifikation.

**C010 · Satz · [Zeile 757](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:757>) · Belassen**

> Kein Protokollersatz: Optionen liefern Funktionen für den eigenen Verkehr einer Anwendung; sie sollen NTP, ICMP
> (insbesondere Echo) und Netzwerk-Testgeräte weder ersetzen noch nachbauen.

**Bewertung:** Funktion und Abgrenzung der Optionen stehen in einem klaren Zusammenhang; die Beispiele konkretisieren
Protokollersatz.

**C011 · Satz · [Zeile 760](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:760>) · Belassen**

> Rahmenwerk statt Protokoll: RFC 9868 definiert Optionsformate auch dann, wenn sie noch kein vollständiges Verfahren
> ergeben; die Nutzung regeln andere Dokumente.

**Bewertung:** Die Gegenüberstellung von Optionsformat und vollständigem Verfahren ist direkt formuliert.

**C012 · Satz · [Zeile 761](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:761>) · Vereinfachen, Klarheit**

> Für REQ/RES übernimmt das RFC 9869, für TIME bleibt sie bewusst offen.

**Bewertung:** Das und sie beziehen sich auf verschiedene Satzteile des vorigen Satzes. Die Nutzung der beiden Optionen
kann ausdrücklich genannt werden.

**Vorschlag:** Die Nutzung von REQ/RES regelt RFC 9869; wie TIME genutzt wird, bleibt bewusst offen.

**C013 · Satz · [Zeile 762](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:762>) · Streichen, optional**

> Das entspricht dem Muster von TCP, dessen Basisnorm den Optionsmechanismus festlegt, während einzelne Optionen in
> eigenen Dokumenten folgten.

**Bewertung:** Der TCP-Vergleich wiederholt die Trennung von Optionsformat und Verfahren nach dem bereits konkreten
REQ/RES-Beispiel. Für die anschließende Unterscheidung von SAFE und UNSAFE ist er nicht nötig.

**Vorschlag:** Satz entfernen; die Begründung und etwaige Nachbarsätze oben beachten.

**C014 · Satz · [Zeile 765](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:765>) · Belassen**

> Voreinstellung wie beim Altempfänger: Empfangene Pakete werden standardmäßig auch dann zugestellt, wenn Prüfsummen-,
> Authentifizierungs- oder Entschlüsselungsprüfungen der Optionen scheitern; einzige Ausnahme sind UDP-Fragmente.

**Bewertung:** Die Grundregel, die drei Arten fehlgeschlagener Prüfung und die Ausnahme sind trotz der Satzlänge klar
zuzuordnen.

**C015 · Satz · [Zeile 767](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:767>) · Belassen**

> Strengeres Verhalten muss die Anwendung ausdrücklich anfordern.

**Bewertung:** Anwendung, Handlung und notwendige ausdrückliche Anforderung sind eindeutig.

**C016 · Satz · [Zeile 768](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:768>) · Streichen, optional**

> Optionen sind ein Angebot, kein Filter.

**Bewertung:** Die Metapher Angebot statt Filter wiederholt die beiden vorigen Sätze und erklärt kein zusätzliches
Verhalten.

**Vorschlag:** Satz entfernen; die Begründung und etwaige Nachbarsätze oben beachten.

**C017 · Satz · [Zeile 771](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:771>) · Streichen, optional**

> Der gemeinsame Nenner der sechs Prinzipien: RFC 9868 legt die Optionsformate und ihre Grundverarbeitung fest, aber
> kein vollständiges Anwendungsprotokoll.

**Bewertung:** Die Zusammenfassung wiederholt den Listenpunkt Rahmenwerk statt Protokoll nahezu vollständig.

**Vorschlag:** Satz entfernen; die Begründung und etwaige Nachbarsätze oben beachten.

**C018 · Satz · [Zeile 772](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:772>) · Belassen**

> UDP bleibt ein minimales Transportprotokoll, und jede zusätzliche Fähigkeit wird von der Anwendung ausdrücklich
> aktiviert.

**Bewertung:** Der Satz verbindet die minimale Transportfunktion mit der ausdrücklichen Aktivierung zusätzlicher
Fähigkeiten. Diese allgemeine Aussage steht so nicht vollständig in den vorigen Einzelprinzipien und erklärt den Umgang
der Anwendung mit den Optionen.

**C019 · Satz · [Zeile 775](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:775>) · Vereinfachen, Klarheit**

> An das letzte Prinzip knüpft die zentrale Zweiteilung der Optionen an, und sie folgt unmittelbar aus der
> Abwärtskompatibilität: Weil ein Altempfänger die Surplus Area überliest, muss jede Option damit rechnen, ignoriert zu
> werden.

**Bewertung:** Anknüpfen, zentrale Zweiteilung und damit rechnen sind abstrakte beziehungsweise vermenschlichende
Wendungen. Der Altempfänger und sein Verhalten können den Übergang direkt erklären.

**Vorschlag:** Ein Altempfänger überliest die Surplus Area und ignoriert damit die Optionen. Deshalb unterscheidet RFC
9868 zwischen SAFE- und UNSAFE-Optionen.

**C020 · Satz · [Zeile 777](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:777>) · Belassen**

> SAFE-Optionen (Kind 0 bis 191) sind genau dafür entworfen: Ein Empfänger, der sie nicht versteht, ignoriert sie, ohne
> dass sich die Bedeutung der Nutzdaten ändert.

**Bewertung:** Der Satz benennt Empfänger, Bedingung, Handlung und Folge. Genau dafür verweist nachvollziehbar auf das
Ignorieren im vorigen Satz.

**C021 · Satz · [Zeile 778](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:778>) · Belassen**

> In diese Klasse gehören die Ein-Byte-Codes NOP und EOL ebenso wie FRAG.

**Bewertung:** Die Beispiele gehören eindeutig zur direkt zuvor eingeführten SAFE-Klasse.

**C022 · Satz · [Zeile 781](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:781>) · Belassen**

> UNSAFE-Optionen (Kind 192 bis 255) können dagegen die Nutzdaten verändern oder eine Änderung ihrer Deutung
> signalisieren, etwa durch Kompression oder Verschlüsselung; ein Empfänger, der die Option nicht versteht, würde die
> Nutzdaten falsch deuten.

**Bewertung:** Kompression und Verschlüsselung machen die Aussage anschaulich; der zweite Teilsatz erklärt unmittelbar
die Folge für einen Empfänger ohne Unterstützung.

**C023 · Satz · [Zeile 783](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:783>) · Vereinfachen, Klarheit**

> RFC 9868 löst das mit einer Transportbeschränkung: UNSAFE-Optionen dürfen nur in UDP-Fragmenten auftreten, deren
> regulärer Nutzdatenteil leer ist; die transportierten Daten liegen im Fragmentdatenbereich der Surplus Area hinter der
> Optionsliste.

**Bewertung:** Transportbeschränkung benennt die Regel nur abstrakt. Drei Aussagen über zulässigen Ort, leeren
Nutzdatenteil und tatsächlichen Datenbereich stehen hintereinander.

**Vorschlag:** UNSAFE-Optionen dürfen nach RFC 9868 nur in UDP-Fragmenten auftreten. Deren regulärer Nutzdatenteil ist
leer; die transportierten Daten liegen im Fragmentdatenbereich der Surplus Area hinter der Optionsliste.

**C024 · Satz · [Zeile 786](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:786>) · Belassen**

> Ein Altempfänger sieht dann nur ein leeres Datagramm und verwirft die Daten still, statt sie falsch zu deuten.

**Bewertung:** Beschreibt direkt, was der Altempfänger sieht und warum dadurch keine falsche Deutung erfolgt.

**C025 · Satz · [Zeile 787](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:787>) · Vereinfachen, Klarheit**

> Ein optionsfähiger Empfänger, der eine UNSAFE-Option nicht unterstützt, muss die reassemblierten Nutzdaten ebenso
> still verwerfen, und dasselbe gilt, wenn eine UNSAFE-Option außerhalb eines Fragment- oder Reassemblierungskontexts
> erscheint; zugestellt wird in beiden Fällen höchstens ein leeres Datagramm.

**Bewertung:** Zwei Verwerfungsbedingungen und die gemeinsame Zustellungsfolge stecken in einer Satzkette. Die Trennung
macht die Bedingungen leichter unterscheidbar, ohne ihren Inhalt zu ändern.

**Vorschlag:** Unterstützt ein optionsfähiger Empfänger eine UNSAFE-Option nicht, muss er die reassemblierten Nutzdaten
ebenfalls still verwerfen. Dasselbe gilt, wenn eine UNSAFE-Option außerhalb eines Fragment- oder
Reassemblierungskontexts erscheint. In beiden Fällen wird höchstens ein leeres Datagramm zugestellt.

**C026 · Satz · [Zeile 791](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:791>) · Belassen**

> Den Maßstab für die Einzelbewertung führt Abschnitt 4.2 ein; den Soll-Ist-Abgleich enthält Abschnitt 6.3.

**Bewertung:** Die beiden Verweise haben unterschiedliche und ausdrücklich genannte Zwecke: Bewertungsmaßstab und
Soll-Ist-Abgleich.

**C027 · Satz · [Zeile 792](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:792>) · Belassen**

> Die Umsetzung der Optionen beschreibt Kapitel 5.

**Bewertung:** Kurzer, eindeutiger Verweis auf die Umsetzung.

**C028 · Satz · [Zeile 795](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:795>) · Streichen, optional**

> Zwei Folgen dieser Prinzipien verdienen eine eigene Erwähnung.

**Bewertung:** Kündigt nur die folgenden Aussagen an und bewertet ihre Erwähnung, ohne selbst Inhalt beizutragen.

**Vorschlag:** Satz entfernen; die Begründung und etwaige Nachbarsätze oben beachten.

**C029 · Satz · [Zeile 795](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:795>) · Vereinfachen, optional**

> Erstens verteilt die FRAG-Option ein logisches Anwendungsdatagramm (im RFC user datagram) künftig gegebenenfalls auf
> mehrere IP-Datagramme.

**Bewertung:** Erstens hängt an der entbehrlichen Ankündigung; künftig gegebenenfalls ist unnötig umständlich. Kann
drückt dieselbe Möglichkeit direkt aus.

**Vorschlag:** Die FRAG-Option kann ein logisches Anwendungsdatagramm (im RFC user datagram) auf mehrere IP-Datagramme
verteilen.

**C030 · Satz · [Zeile 797](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:797>) · Vereinfachen, optional**

> Zweitens nimmt der RFC einen ausdrücklich benannten Unterschied in Kauf: Ein Altempfänger sieht jedes UDP-Fragment als
> leeres Datagramm, ein optionsfähiger Empfänger das reassemblierte Datagramm mit Inhalt.

**Bewertung:** Die Einleitung mit zweitens und nimmt in Kauf verzögert den konkreten Empfängervergleich. Beide
Empfängersichten können zuerst stehen.

**Vorschlag:** Ein Altempfänger sieht jedes UDP-Fragment als leeres Datagramm, ein optionsfähiger Empfänger das
reassemblierte Datagramm mit Inhalt. Der RFC nimmt diesen Unterschied ausdrücklich in Kauf.

**C031 · Satz · [Zeile 799](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:799>) · Vereinfachen, Klarheit**

> Diese Zählungen gleicht der RFC nicht an, weil leere Datagramme als Lebenszeichen ohnehin unzuverlässig sind.

**Bewertung:** Diese Zählungen nennt nicht, was gezählt wird; der vorangehende Satz enthält selbst keine Zählung.

**Vorschlag:** Der RFC gleicht die unterschiedliche Anzahl zugestellter Datagramme nicht an, weil leere Datagramme als
Lebenszeichen unzuverlässig sind.

### 2.4 Betriebssystem und Netzpfad

**C032 · Satz · [Zeile 805](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:805>) · Vereinfachen, optional**

> Ob ein Datagramm mit Surplus Area sein Ziel erreicht, entscheidet sich an zwei Stellen außerhalb des Protokolls: im
> Betriebssystem der beiden Endpunkte und auf dem Netzpfad dazwischen.

**Bewertung:** Entscheidet sich an zwei Stellen außerhalb des Protokolls lässt die handelnden Systeme erst spät
erkennen. Die genannten Systeme können das Subjekt bilden.

**Vorschlag:** Die Betriebssysteme der Endpunkte und die Geräte auf dem Netzpfad bestimmen mit, ob ein Datagramm mit
Surplus Area sein Ziel erreicht.

**C033 · Satz · [Zeile 806](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:806>) · Belassen**

> Betrachtet wird dabei durchgehend der Linux-Netzwerkstapel für IPv4, auf dem die Referenzimplementierung dieser Arbeit
> läuft; andere Betriebssysteme und IPv6 bleiben ausgeklammert.

**Bewertung:** Die Beschränkung auf Linux und IPv4 ist konkret und durch die verwendete Referenzimplementierung
begründet.

**C034 · Satz · [Zeile 808](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:808>) · Streichen, optional**

> Dieser Abschnitt stellt zunächst die zwei Socket-Sichten vor, mit denen der Kernel UDP-Verkehr an Anwendungen
> übergibt, und anschließend die Akteure des Pfades; am Ende fügt Abbildung 2.11 beides zu einem Gesamtbild zusammen.

**Bewertung:** Reine Ablaufankündigung. Die Absatzüberschriften und die späteren Abbildungsverweise leisten dieselbe
Orientierung.

**Vorschlag:** Satz entfernen; die Begründung und etwaige Nachbarsätze oben beachten.

**C035 · Satz · [Zeile 810](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:810>) · Streichen, optional**

> Allgemeine Netzwerkgrundlagen bleiben bewusst ausgespart: Es geht genau um die Kette, die die Messpfade dieser Arbeit
> tatsächlich durchlaufen.

**Bewertung:** Erklärt hauptsächlich, was der Abschnitt nicht behandelt. Der relevante Umfang ist bereits im
Linux-/IPv4-Satz genannt und wird danach konkret gezeigt.

**Vorschlag:** Satz entfernen; die Begründung und etwaige Nachbarsätze oben beachten.

**C036 · Satz · [Zeile 815](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:815>) · Streichen, optional**

> Beim gewöhnlichen UDP-Socket übernimmt der Kernel die Protokollarbeit.

**Bewertung:** Protokollarbeit kündigt nur die konkreten Tätigkeiten im Folgesatz an. Der Ersatz für Zeile 815 nennt den
Kernel ausdrücklich und erhält damit den Bezug.

**Vorschlag:** Satz entfernen; die Begründung und etwaige Nachbarsätze oben beachten.

**C037 · Satz · [Zeile 815](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:815>) · Vereinfachen, Klarheit**

> Empfangsseitig prüft er Länge und Prüfsumme, demultiplexiert nach Adresse, Port und Socketmerkmalen und liefert nur
> die Nutzdaten bis UDP Length.

**Bewertung:** „Demultiplexiert“ benennt die Funktion ohne Erklärung. Die Ersatzfassung erklärt die Zuordnung und nennt
den gewöhnlichen UDP-Socket ausdrücklich, damit der Zusammenhang auch bei Wegfall von C036 erhalten bleibt.

**Vorschlag:** Bei einem gewöhnlichen UDP-Socket prüft der Kernel beim Empfang Länge und Prüfsumme. Anhand von Adresse,
Port und Socketmerkmalen ordnet er das Datagramm einem Socket zu. Er liefert nur die Nutzdaten bis UDP Length.

**C038 · Satz · [Zeile 817](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:817>) · Belassen**

> Damit entspricht diese Sicht dem Altempfänger aus Abschnitt 2.3; getestete Altempfänger schneiden die Surplus Area ab.

**Bewertung:** Der Rückbezug auf den Altempfänger verbindet die Socket-Eigenschaft mit dem bereits eingeführten Modell
und benennt das Abschneiden konkret.

**C039 · Satz · [Zeile 819](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:819>) · Belassen**

> Sendeseitig baut der Kernel beide Header und lässt hinter den Nutzdaten keinen Raum.

**Bewertung:** Der Kernel ist als Akteur genannt; Headerbau und fehlender Raum erklären unmittelbar die Grenze des
UDP-Sockets.

**C040 · Satz · [Zeile 820](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:820>) · Belassen**

> Ein UDP-Socket kann die Surplus Area daher weder lesen noch erzeugen.

**Bewertung:** Eine kurze und klare Schlussfolgerung aus Sende- und Empfangsverhalten.

**C041 · Satz · [Zeile 822](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:822>) · Vereinfachen, Klarheit**

> Der normale Kernelweg führt sendeseitig von write() über die Socket- und UDP-Schicht zur IP-Schicht, empfangsseitig
> entsprechend zurück zu read(); ausgeliefert wird erst nach der UDP-Prüfsumme.

**Bewertung:** Nach der UDP-Prüfsumme lässt die eigentliche Handlung Prüfung aus. Außerdem wechseln Sende- und
Empfangsrichtung innerhalb eines Satzes.

**Vorschlag:** Beim Senden führt der Weg von write() über die Socket- und UDP-Schicht zur IP-Schicht. Beim Empfang
verläuft er entsprechend zurück zu read(); die Anwendung erhält die Nutzdaten erst nach der Prüfung der UDP-Prüfsumme.

**C042 · Satz · [Zeile 824](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:824>) · Streichen, optional**

> Diese Folge berichtigt zwei Beschriftungen der Vorlage (dort Abbildung 5): Auf der Socket-Schicht stehen
> sock_sendmsg() und sock_recvmsg(), und der UDP-Sendepfad übergibt an ip_send_skb() statt ip_queue_xmit().

**Bewertung:** Der Satz behandelt die Überarbeitung einer fremden Vorlage statt die Funktionsweise des eigenen Empfangs-
und Sendepfads. Die Funktionsnamen sind für den hier erklärten Unterschied zwischen UDP-Socket und Raw Socket nicht
nötig. Die Quellenbelege an der Darstellung bleiben erhalten.

**Vorschlag:** Satz entfernen; die Begründung und etwaige Nachbarsätze oben beachten.

**C043 · Satz · [Zeile 828](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:828>) · Vereinfachen, Klarheit**

> Wer beides will, braucht die zweite Sicht: den Raw Socket, den Linux nur Prozessen mit der Berechtigung CAP_NET_RAW
> öffnet.

**Bewertung:** Wer beides will verweist über den dazwischenliegenden Funktionsabsatz hinweg auf Lesen und Erzeugen der
Surplus Area. Die beiden Aufgaben sollten ausdrücklich genannt werden.

**Vorschlag:** Zum Lesen und Erzeugen der Surplus Area ist ein Raw Socket nötig. Linux öffnet ihn nur Prozessen mit der
Berechtigung CAP_NET_RAW.

**C044 · Satz · [Zeile 829](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:829>) · Vereinfachen, optional**

> Er zweigt auf der IP-Schicht ab: Der Sender speist dort ein selbst gebautes Datagramm ein, der Empfänger erhält vor
> dem UDP-Pfad eine Kopie; die folgenden Abbildungen trennen beide Richtungen.

**Bewertung:** Die Richtungen sind konkret beschrieben, aber der abschließende Hinweis auf die folgenden Abbildungen ist
entbehrlich. Der Raw Socket kann ausdrücklich als Bezug genannt werden.

**Vorschlag:** Der Raw Socket setzt auf der IP-Schicht an: Der Sender übergibt dort ein selbst gebautes Datagramm, der
Empfänger erhält vor dem UDP-Pfad eine Kopie.

**C045 · Satz · [Zeile 831](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:831>) · Vereinfachen, Klarheit**

> Er arbeitet unterhalb von UDP direkt mit IP-Datagrammen: Die Anwendung schreibt den UDP-Header selbst, und die
> IP-Längenangabe bemisst der Kernel an der übergebenen Pufferlänge statt am UDP-Datagramm; alles, was die Anwendung
> hinter das UDP-Datagramm in den Puffer legt, wird so zur Surplus Area.

**Bewertung:** Der Zusammenhang von Pufferlänge, IP-Länge und Surplus Area wird durch eine lange Satzkette verdeckt. Die
Schritte lassen sich den Akteuren einzeln zuordnen.

**Vorschlag:** Ein Raw Socket arbeitet direkt mit IP-Datagrammen. Die Anwendung schreibt den UDP-Header selbst. Der
Kernel richtet die IP-Längenangabe nach dem übergebenen Puffer und nicht nach der UDP-Länge. Bytes, die in diesem Puffer
hinter dem UDP-Datagramm liegen, werden dadurch zur Surplus Area.

**C046 · Satz · [Zeile 834](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:834>) · Vereinfachen, optional**

> Mit der Socket-Option IP_HDRINCL baut sie darüber hinaus den IP-Header selbst, statt ihn vom Kernel erzeugen zu
> lassen; diesen Weg nutzt die Referenzimplementierung, die damit das vollständige Datagramm selbst baut (Abschnitt
> 4.4).

**Bewertung:** Selbst bauen wird innerhalb des Satzes wiederholt. Die Socket-Option und die Entscheidung der
Referenzimplementierung können getrennt stehen.

**Vorschlag:** Mit der Socket-Option IP_HDRINCL baut die Anwendung auch den IP-Header selbst. Die
Referenzimplementierung nutzt diesen Weg und erzeugt damit das vollständige Datagramm (Abschnitt 4.4).

**C047 · Satz · [Zeile 837](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:837>) · Vereinfachen, optional**

> Die vertauschten Rollen beider Sendewege zeigt Abbildung 2.9:

**Bewertung:** Vertauschte Rollen ist bildhaft; gemeint ist die Zuständigkeit von Anwendung und Kernel.

**Vorschlag:** Die Arbeitsteilung zwischen Anwendung und Kernel zeigt Abbildung 2.9:

**C048 · Definition/Beschriftung · [Zeile 857](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:857>) · Belassen**

> Die zwei Sendepfade durch den Linux-Kernel

**Bewertung:** Kurze nominale Bildunterschrift mit eindeutigem Gegenstand; zusätzliche Prüfeinheit, kein vollständiger
Satz.

**C049 · Satz · [Zeile 861](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:861>) · Streichen, optional**

> Aus Abbildung 2.9 geht hervor, dass die Arbeitsteilung kippt: Am UDP-Socket baut der Kernel beide Header und bemisst
> die Längen bündig, am Raw Socket liefert die Anwendung das fertige Datagramm ab, und nur auf dem Raw-Socket-Weg
> entsteht hinter den Nutzdaten Platz für eine Surplus Area.

**Bewertung:** Wiederholt die zuvor erklärten und unmittelbar in der Abbildung sichtbaren Sendeaufgaben. Arbeitsteilung
kippt und Längen bündig sind zudem unnötig bildhaft. Der folgende Satz zu gemeinsamen Stationen bleibt als neue Aussage
erhalten.

**Vorschlag:** Satz entfernen; die Begründung und etwaige Nachbarsätze oben beachten.

**C050 · Satz · [Zeile 863](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:863>) · Belassen**

> Der Unterbau bleibt derselbe: Beide Wege münden in die IP-Schicht mit ihren netfilter-Stationen und enden an der
> Netzwerkkarte.

**Bewertung:** Der gemeinsame weitere Weg ist eine eigene, klare Aussage. Der kurze Vergleich Unterbau wird nach dem
Doppelpunkt unmittelbar konkretisiert.

**C051 · Satz · [Zeile 867](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:867>) · Streichen, optional**

> Ganz entlässt der Kernel den Raw-Sender allerdings nicht aus seiner Obhut, und diese Restarbeit prägt den Sendepfad
> der Implementierung.

**Bewertung:** Obhut und Restarbeit sind blumige Ankündigungen; der nächste Satz nennt die verbliebenen Kernelaufgaben
direkt.

**Vorschlag:** Satz entfernen; die Begründung und etwaige Nachbarsätze oben beachten.

**C052 · Satz · [Zeile 868](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:868>) · Vereinfachen, Klarheit**

> Routing, Nachbarauflösung und Link-Schicht bleiben Kernelsache, und im übergebenen IP-Header trägt der Kernel Total
> Length und die IP-Header-Prüfsumme stets selbst ein; UDP-Header und Surplus Area lässt er selbst dagegen unangetastet,
> die netfilter-Stationen dieses Wegs können das Datagramm gleichwohl noch verwerfen oder verändern.

**Bewertung:** Kernelaufgaben, zwei automatische Headerwerte, unveränderte UDP-Daten und mögliche Filtereingriffe stehen
in einer Satzkette. Kurze Sätze trennen die Zuständigkeiten; der netfilter-Vorbehalt bleibt erhalten.

**Vorschlag:** Der Kernel übernimmt Routing, Nachbarauflösung und Link-Schicht. Im übergebenen IP-Header trägt er Total
Length und die IP-Header-Prüfsumme stets selbst ein. UDP-Header und Surplus Area lässt er unangetastet; die
netfilter-Stationen dieses Wegs können das Datagramm jedoch noch verwerfen oder verändern.

**C053 · Satz · [Zeile 872](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:872>) · Belassen**

> Zugleich fragmentiert dieser Pfad nicht: Mit IP_HDRINCL ist ein Datagramm auf die MTU des Interfaces begrenzt, ein
> größerer Sendeaufruf schlägt fehl.

**Bewertung:** Nennt die Socket-Einstellung, die konkrete Grenze und die Folge eines zu großen Sendeaufrufs.

**C054 · Satz · [Zeile 873](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:873>) · Vereinfachen, optional**

> Für RFC 9868 ist das kein Verlust: IP-Fragmentierung sollen UDP-Anwendungen ohnehin vermeiden (Abschnitt 2.1), und für
> große Datagramme stellt der RFC stattdessen die FRAG-Option auf Transportebene bereit.

**Bewertung:** Kein Verlust ist eine wertende Einleitung. Empfehlung und Ausweg sind auch ohne diese Bewertung
verständlich.

**Vorschlag:** UDP-Anwendungen sollen IP-Fragmentierung ohnehin vermeiden (Abschnitt 2.1). Für große Datagramme stellt
RFC 9868 die FRAG-Option auf Transportebene bereit.

**C055 · Satz · [Zeile 878](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:878>) · Vereinfachen, optional**

> Beim Empfang entscheidet sich, an welcher Stelle ein Datagramm geprüft wird; den Weg vom Draht zu den beiden Sichten
> zeichnet Abbildung 2.10 nach:

**Bewertung:** Der erste Teilsatz kündigt nur allgemein Prüfungen an; der Zweck der Abbildung lässt sich direkt
benennen.

**Vorschlag:** Abbildung 2.10 zeigt den Empfangsweg von der Netzwerkkarte zum UDP-Socket und zum Raw Socket:

**C056 · Definition/Beschriftung · [Zeile 901](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:901>) · Belassen**

> Der Empfangspfad durch den Linux-Kernel

**Bewertung:** Kurze nominale Bildunterschrift mit eindeutigem Gegenstand; zusätzliche Prüfeinheit, kein vollständiger
Satz.

**C057 · Satz · [Zeile 906](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:906>) · Belassen**

> Aus Abbildung 2.10 geht hervor, dass sich der Weg hinter dem Paketfilter gabelt: Der Raw Socket erhält eine Kopie des
> gesamten IP-Datagramms samt Surplus Area, und zwar vor den Prüfungen von Länge, Prüfsumme und Portzuordnung im
> regulären UDP-Empfangspfad.

**Bewertung:** Die Satzlänge ist hier kein eigener Mangel: Der Satz beschreibt den Ort der Aufteilung und die
entscheidende Reihenfolge. Der Zusatz regulärer UDP-Empfangspfad bleibt präzise und verständlich.

**C058 · Satz · [Zeile 909](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:909>) · Belassen**

> Den IP-Header hat die IP-Schicht zu diesem Zeitpunkt bereits geprüft, wie die Abbildung zeigt.

**Bewertung:** Die IP-Schicht ist klar als Akteur genannt; der Zeitpunkt bezieht sich eindeutig auf die Raw-Zustellung.

**C059 · Satz · [Zeile 910](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:910>) · Belassen**

> Sofern vorgeschaltete Filter es passieren lassen, kann ein Datagramm mit falscher UDP-Prüfsumme oder einer UDP Length,
> die über die IP-Nutzlast hinausweist, unverändert am Raw Socket ankommen.

**Bewertung:** Der Filtervorbehalt steht ausdrücklich vor der Aussage. Beide fehlerhaften UDP-Fälle und die mögliche
Raw-Zustellung sind verständlich; keine erneute fachliche Beanstandung.

**C060 · Satz · [Zeile 912](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:912>) · Vereinfachen, Klarheit**

> Die Prüfungen, die der Kernel dem UDP-Socket abnimmt, muss eine Raw-Empfangsschicht deshalb vollständig selbst
> ausführen, und zwar in der Reihenfolge, die RFC 9868 vorgibt: erst Mindestlänge und Längenkonsistenz des UDP-Headers,
> dann die UDP-Prüfsumme, erst danach Surplus-Ortung und OCS; wie die Implementierung das umsetzt, zeigt Kapitel 5.

**Bewertung:** Die nötigen Prüfhandlungen werden zuletzt als Nomen aufgezählt; Surplus-Ortung ist besonders abstrakt.
Tätigkeitsverben machen die Reihenfolge leichter nachvollziehbar, ohne sie zu ändern.

**Vorschlag:** Die Raw-Empfangsschicht muss diese UDP-Prüfungen selbst ausführen. RFC 9868 verlangt folgende
Reihenfolge: Zuerst prüft sie Mindestlänge und Längenkonsistenz des UDP-Headers, dann die UDP-Prüfsumme. Erst danach
bestimmt sie die Grenzen der Surplus Area und prüft das OCS. Wie die Implementierung das umsetzt, zeigt Kapitel 5.

**C061 · Satz · [Zeile 916](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:916>) · Streichen, optional**

> Zwei Arbeiten behält der Kernel dagegen auch hier.

**Bewertung:** Kündigt lediglich die beiden folgenden Kernelaufgaben an. Diese nennen ihren Akteur und ihre Wirkung
bereits selbst.

**Vorschlag:** Satz entfernen; die Begründung und etwaige Nachbarsätze oben beachten.

**C062 · Satz · [Zeile 916](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:916>) · Belassen**

> Die netfilter-Hooks bleiben beiden Sichten vorgeschaltet: Ein lokaler Paketfilter kann ein Datagramm verwerfen, bevor
> irgendeine Anwendung es sieht.

**Bewertung:** Der Satz erklärt die Folge der vorgeschalteten netfilter-Hooks unmittelbar am möglichen Verwerfen eines
Datagramms.

**C063 · Satz · [Zeile 918](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:918>) · Belassen**

> Und ankommende IP-Fragmente setzt die IP-Schicht bereits vor der Zustellung wieder zusammen, auch für Raw Sockets;
> eine Raw-Empfangsschicht muss die IPv4-Reassemblierung deshalb nicht nachbauen.

**Bewertung:** IP-Schicht, Reassemblierung vor Zustellung und die daraus folgende Entlastung der Raw-Empfangsschicht
sind klar verbunden.

**C064 · Satz · [Zeile 924](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:924>) · Belassen**

> Zwischen den Endpunkten kann das Datagramm auf Middleboxes treffen.

**Bewertung:** Kurzer Einstieg, der den anschließend erklärten Begriff Middleboxes einführt.

**C065 · Satz · [Zeile 924](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:924>) · Belassen**

> RFC 8085 nennt damit Zwischensysteme wie NATs und Firewalls, die zusätzliche Funktionen ausführen und typischerweise
> Zustand je Fluss führen.

**Bewertung:** Die Definition nennt konkrete Beispiele und beschreibt ihr gemeinsames Merkmal. Zustand und Fluss werden
im nachfolgenden NAT-Satz konkretisiert.

**C066 · Satz · [Zeile 926](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:926>) · Streichen, optional**

> Für die Interpretation der späteren Messungen genügt der Sammelbegriff nicht, denn die Akteure setzen an verschiedenen
> Stellen an und hinterlassen verschiedene Spuren.

**Bewertung:** Die Aussage über verschiedene Spuren kündigt die folgende Aufzählung nur abstrakt an. Die konkreten
Eingriffe zeigen den Unterschied bereits.

**Vorschlag:** Satz entfernen; die Begründung und etwaige Nachbarsätze oben beachten.

**C067 · Satz · [Zeile 928](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:928>) · Vereinfachen, Klarheit**

> Im Zugangsnetz ersetzt die NAT eines Heimrouters oder Hotspots Adressen und Ports und bindet jeden Fluss an einen
> Zustandseintrag mit Zeitschranke; ihre Provider-Variante Carrier-Grade NAT (CGNAT) teilt dieselben öffentlichen
> Adressen zusätzlich unter vielen Kunden auf.

**Bewertung:** Zustandseintrag mit Zeitschranke ist unnötig abstrakt. Die zeitlich begrenzte Speicherung der Zuordnung
erklärt dasselbe konkreter. Der Wechsel zur Provider-Variante erhält einen eigenen Satz.

**Vorschlag:** Im Zugangsnetz ersetzt die NAT eines Heimrouters oder Hotspots Adressen und Ports. Sie speichert die
Zuordnung für jeden Datenfluss für eine begrenzte Zeit. Die Provider-Variante Carrier-Grade NAT (CGNAT) verwendet
dieselben öffentlichen Adressen für viele Kunden.

**C068 · Satz · [Zeile 930](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:930>) · Vereinfachen, Klarheit**

> Firewalls verwerfen an Netzgrenzen und Endsystemen nach Regelwerk, etwa anhand von Ports und Protokollen.

**Bewertung:** Das Verb verwerfen hat kein ausdrücklich genanntes Objekt; Datagramme macht die Handlung vollständig.

**Vorschlag:** Firewalls verwerfen an Netzgrenzen und Endsystemen Datagramme nach Regelwerk, etwa anhand von Ports und
Protokollen.

**C069 · Satz · [Zeile 931](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:931>) · Vereinfachen, Klarheit**

> Leicht zu übersehen sind die letzten beiden Akteure: die Virtualisierungsschicht eines Testrechners, deren eigener
> Netz- und NAT-Stack Headerfelder auf erwartete Normwerte umschreiben kann, und das Transitnetz selbst, die AS-Kette
> zwischen den Zugangsnetzen, in der einzelne Netze filtern.

**Bewertung:** Leicht zu übersehen bewertet den Leserblick statt die Funktion zu erklären. Zwei sehr unterschiedliche
Eingriffsstellen stehen in einer langen Aufzählung; AS-Kette bleibt unaufgelöst.

**Vorschlag:** Auch der Netz- und NAT-Stack der Virtualisierungsschicht eines Testrechners kann Headerfelder auf
erwartete Werte umschreiben. Im Transitnetz, der Kette eigenständig verwalteter Netze (autonomer Systeme, AS) zwischen
den Zugangsnetzen, können einzelne Netze Datagramme filtern.

**C070 · Satz · [Zeile 936](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:936>) · Belassen**

> Ob ein einzelner Akteur UDP Options kennt, lässt sich von außen nicht feststellen.

**Bewertung:** Die Beobachtungsgrenze ist knapp und verständlich formuliert; Akteur ist durch die unmittelbar vorher
genannten Systeme konkret.

**C071 · Satz · [Zeile 936](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:936>) · Belassen**

> Unbekannte Zwischensysteme können eine Surplus Area unverändert weiterleiten, verändern, entfernen oder das gesamte
> Datagramm verwerfen.

**Bewertung:** Eine klare Aufzählung der vier möglichen Folgen ohne unnötige Einleitung.

**C072 · Satz · [Zeile 938](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:938>) · Belassen**

> Zustandsbehaftete NATs und Firewalls können dabei je Richtung und Messzeitpunkt unterschiedlich reagieren.

**Bewertung:** Benannte Systeme, wechselnde Bedingungen und mögliches Verhalten stehen in einem kurzen Satz.

**C073 · Satz · [Zeile 939](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:939>) · Belassen**

> Eine Kapselung, etwa in einen WireGuard-Tunnel, verbirgt das innere Datagramm vor den Akteuren zwischen den
> Tunnelendpunkten, die nur noch das äußere Tunnelpaket behandeln.

**Bewertung:** Erklärt anschaulich, was die Kapselung verbirgt und welche Pakete die Geräte auf dem restlichen Weg
behandeln.

**C074 · Satz · [Zeile 941](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:941>) · Belassen**

> Welche dieser Eingriffe auf den untersuchten Pfaden beobachtet wurden, bewertet Kapitel 6.

**Bewertung:** Ein knapper Verweis mit klarem Zweck: Bewertung der tatsächlich beobachteten Eingriffe.

**C075 · Satz · [Zeile 944](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:944>) · Streichen, optional**

> Diese Kette erklärt zugleich, warum RFC 9868 seine Optionen ausgerechnet in einem Bereich ablegt, den Altempfänger
> üblicherweise nicht lesen.

**Bewertung:** Wiederholt nur die bereits behandelte Platzierung der Optionen und kündigt die folgende Erklärung an;
ausgerechnet ist unnötig wertend.

**Vorschlag:** Satz entfernen; die Begründung und etwaige Nachbarsätze oben beachten.

**C076 · Satz · [Zeile 945](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:945>) · Vereinfachen, Klarheit**

> Weil Middleboxes bevorzugt durchlassen, was sie kennen, weichen Protokollerweiterungen in Bereiche aus, die Altsysteme
> nicht deuten; dieses Erstarren des Netzes unter seinen Zwischensystemen wird als Ossifikation bezeichnet.

**Bewertung:** Erstarren des Netzes ist eine Metapher und erklärt Ossifikation nicht konkret. Die Behinderung von
Protokolländerungen kann als Handlung der Middleboxes beschrieben werden.

**Vorschlag:** Middleboxes lassen bevorzugt bekannte Paketformate durch. Dadurch erschweren sie Änderungen an
Protokollen; das wird als Ossifikation bezeichnet. Protokollerweiterungen nutzen deshalb Bereiche, die Altsysteme nicht
deuten.

**C077 · Satz · [Zeile 947](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:947>) · Vereinfachen, Klarheit**

> Unsichtbar ist die Surplus Area allerdings nur für die Anwendungen an Altempfängern, und auch das nur in der Regel;
> für die Geräte auf dem Pfad bleibt sie ohne Verschlüsselung sichtbar, und RFC 9868 rechnet ausdrücklich mit deren
> Eingriffen: Fehlerhaft rechnende Middleboxes begründen Details der OCS-Berechnung (Abschnitt 2.3), und UDP-Relays
> können eine Surplus Area beim Weiterleiten vollständig abstreifen.

**Bewertung:** Anwendungssicht, Sichtbarkeit auf dem Pfad und zwei Eingriffsbeispiele werden mit mehreren
Einschränkungen in einem Satz verbunden. Getrennte Aussagen klären, wer die Surplus Area lesen oder verändern kann.

**Vorschlag:** Anwendungen an Altempfängern erhalten die Surplus Area in der Regel nicht. Geräte auf dem Netzpfad können
sie dagegen ohne Verschlüsselung lesen. RFC 9868 berücksichtigt bei der OCS-Berechnung auch Middleboxes, die
UDP-Prüfsummen falsch berechnen (Abschnitt 2.3). UDP-Relays können eine Surplus Area beim Weiterleiten vollständig
abstreifen.

**C078 · Satz · [Zeile 955](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:955>) · Vereinfachen, optional**

> Alle Stationen zusammen ordnet Abbildung 2.11 zu einem Messmodell des Weges von der sendenden Anwendung bis zu dem
> Raw-Empfänger, der die Surplus Area auswertet; je nach Pfad können einzelne Stationen fehlen oder zusammenfallen.

**Bewertung:** Die umgekehrte Wortstellung Alle Stationen zusammen ordnet verzögert das Subjekt. Der Abbildungsverweis
selbst ist sinnvoll und bleibt erhalten.

**Vorschlag:** Abbildung 2.11 ordnet alle Stationen zu einem Messmodell des Weges von der sendenden Anwendung bis zum
Raw-Empfänger, der die Surplus Area auswertet; je nach Pfad können einzelne Stationen fehlen oder zusammenfallen.

**C079 · Definition/Beschriftung · [Zeile 982](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:982>) · Belassen**

> Messmodell des Datagrammwegs

**Bewertung:** Kurze nominale Bildunterschrift mit eindeutigem Gegenstand; zusätzliche Prüfeinheit, kein vollständiger
Satz.

**C080 · Satz · [Zeile 986](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:986>) · Vereinfachen, Klarheit**

> Aus Abbildung 2.11 geht hervor, dass zwischen Socket-Schicht und Empfänger-Kernel bis zu vier Stationen liegen, die
> das Datagramm außerhalb der Endpunkte berühren: Sie greifen teils mit Zustand ein und sind von außen nicht direkt
> beobachtbar.

**Bewertung:** Datagramm berühren und mit Zustand eingreifen sagen nicht konkret, was die Stationen tun. Der Bezug
zwischen Zustand und Verarbeitung lässt sich ausdrücklich nennen.

**Vorschlag:** Abbildung 2.11 zeigt zwischen Socket-Schicht und Empfänger-Kernel bis zu vier Stationen außerhalb der
Endpunkte. Einige verarbeiten Datagramme abhängig von gespeichertem Zustand. Ihr Verhalten lässt sich von außen nicht
direkt beobachten.

**C081 · Satz · [Zeile 988](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:988>) · Vereinfachen, Klarheit**

> Für die Feldmessungen folgt daraus die Interpretationsregel dieser Arbeit: Geht ein optionsbehaftetes Datagramm
> verloren oder kommt es verändert an, ist der Befund zuerst dieser Kette zuzuordnen, bevor er der Implementierung oder
> dem Standard angelastet wird.

**Bewertung:** Interpretationsregel und dieser Kette zuzuordnen bleiben abstrakt; angelastet ist wertend. Der Satz soll
den Untersuchungsschritt direkt nennen.

**Vorschlag:** Geht ein optionsbehaftetes Datagramm verloren oder kommt es verändert an, untersucht diese Arbeit
zunächst mögliche Ursachen auf dem Datagrammweg, bevor sie einen Fehler der Implementierung oder des Standards annimmt.

**C082 · Satz · [Zeile 990](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:990>) · Vereinfachen, Klarheit**

> Messpunkte an beiden Enden grenzen ihn dabei auf ein Intervall der Kette ein; welches Gerät eingreift, bleibt ohne
> zusätzliche Messpunkte oder unabhängige Evidenz offen (Kapitel 6).

**Bewertung:** Ihn kann auf Befund oder Fehler bezogen werden; Intervall der Kette ist für einen räumlichen
Netzabschnitt unnötig abstrakt.

**Vorschlag:** Mit Messpunkten an beiden Enden lässt sich eingrenzen, in welchem Abschnitt des Weges ein Verlust oder
eine Veränderung auftritt. Welches Gerät eingreift, bleibt ohne zusätzliche Messpunkte oder unabhängige Evidenz offen
(Kapitel 6).

**C083 · Satz · [Zeile 994](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:994>) · Vereinfachen, Klarheit**

> Wireshark und tshark 4.6 dekodieren RFC 9868 nicht; die Kampagnen benötigen deshalb einen eigenen Prüfer für
> PCAP-Dateien (Abschnitt 4.4.3), und der fehlende Dissektor zeigt zugleich die geringe bisherige Werkzeugunterstützung.

**Bewertung:** Dekodieren RFC benennt das Dokument statt die auszuwertenden Optionen; Dissektor wird ohne Erklärung
eingeführt. Drei Aussagen können mit bekannten Begriffen getrennt werden.

**Vorschlag:** Wireshark und tshark 4.6 dekodieren UDP Options nach RFC 9868 nicht. Die Kampagnen benötigen deshalb
einen eigenen Prüfer für PCAP-Dateien (Abschnitt 4.4.3). Die fehlende Dekodierung zeigt zugleich die geringe bisherige
Unterstützung von UDP Options durch Analysewerkzeuge.

**C084 · Satz · [Zeile 998](</Users/ab/Library/Mobile Documents/com~apple~CloudDocs/cs/master/hagen/thesis/mcs-thesis-docs/thesis/chapters/02_grundlagen.tex:998>) · Belassen**

> Die Auswertungsmethode folgt in Kapitel 3.

**Bewertung:** Kurzer und eindeutiger Übergang zur Auswertungsmethode im folgenden Kapitel.

## Prüfung des Umfangs

Alle Fließtextsätze, Fußnotensätze, Felddefinitionen und Bild-/Tabellenunterschriften wurden in Quellreihenfolge erfasst
und am Absatzkontext geprüft. Der Abgleich des erfassten Wortlauts mit dem Quelltext ergab keine fehlende Satzpassage.
Überschriften, Zeichenanweisungen und numerische Tabellenzellen sind nicht Bestandteil der Satzliste.

Quellstand von `02_grundlagen.tex`, SHA-256: `fa182b032d03d98979a94db353be61bb404dee508e72fcdca2449a7a6169fe4f`.

Kapiteltext, Bibliografie und PDF wurden für diese Sprachprüfung nicht verändert.
