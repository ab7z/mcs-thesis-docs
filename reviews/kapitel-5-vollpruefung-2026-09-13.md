# Kapitel 5: Vollprüfung durch Workflow, Einarbeitung und Codex-Review vom 13. September 2026

## Auftrag und Ablauf

Auftrag von GreenCodeDoesntSmell: Kapitel 5 (`thesis/chapters/05_entwurf_implementierung.tex`, Stand vom
13.09.2026, 688 Zeilen) vollständig prüfen, Satz für Satz und im Zusammenhang der ganzen Arbeit, nach den 24 Kriterien
aus AGENTS.md (Abschnitt "Kapitelprüfung und Freigabe"), mit denselben Mitteln wie bei Kapitel 4: ein Workflow mit
drei Sonnet-5-, zwei Opus-5-Lanes und Fable 5.1 als Adjudikator, danach Einarbeitung durch Claude (Orchestrator) mit
eigener Verifikation jeder Ersetzung, Neubau und Prüfung der PDF, abschließend ein Review durch Codex (gpt-6-astra,
Effort ultra, read-only) mit neutralem Auftrag ohne Hinweis auf die Befunde oder die Änderungen.

Zusätzliche Vorgaben des Autors: einfache Sprache bei korrekter Fachterminologie, leichte Lesbarkeit des ganzen
Kapitels, keine Wortungetüme, keine Gedankenstriche, Kapitel 5 darf nicht länger werden.

Workflow `wf_f86720ef-fda` (54 Minuten, 6/6 Berichte, 347 Werkzeugaufrufe, 1,66 Mio. Token):

| Lane | Modell | Aufgabe | Befunde | bestätigte Aussagen |
|------|--------|---------|---------|---------------------|
| S1 | Sonnet 5 | Implementierungsaussagen am Code (Stand vom 03.09.2026) | 0 | 39 |
| S2 | Sonnet 5 | Norm, Belege, Verbindlichkeit (RFC 9868 mit Zeilennummern, RFC 768, Bib) | 5 | 16 |
| S3 | Sonnet 5 | Verweise, Begriffe, PDF, Silbentrennung, Form | 9 | 12 |
| O1 | Opus 5 | adversariale Vollprüfung Satz für Satz, Zahlen nachgerechnet | 13 | 58 |
| O2 | Opus 5 | Lesbarkeit und Zusammenhang aus Lesersicht, mit Ersatzvorschlägen | 48 | 17 |
| F | Fable 5.1 | Adjudikation mit eigener Quellenprüfung, alt/neu-Ersetzungen | 54 Ersetzungen, 4 Ablehnungen | |

Alle Lanes arbeiteten nur lesend (kein make, kein cargo, kein git mit Schreibwirkung). Der vollständige
Workflow-Ausgang liegt in der Sitzungsablage (`tasks/wf-k5-result.json`); dieser Bericht fasst ihn zusammen.

## Urteil des Adjudikators

Fable: **mit Auflagen**. Keine Lane und auch der Adjudikator fanden eine falsche Sachaussage; alle Zahlen (OCS
0x09C4 plus 0x0009 ergibt 0xF632, Probe 0xFFFF; 40/11/9/31; 48/17/11/37; 1472/1460/1458/2918/2926/1468; CRC32c
0xE3069283; Vorversuch 97/69/28/4/42) und alle Implementierungsaussagen sind am Code (Stand vom 03.09.2026) und an RFC
9868 mit Zeilennummern belegt. Vier Pflichtpunkte standen der Freigabe entgegen:

1. A1: Trennung "Pflichtop-/tionen" auf gedruckter Seite 49 verstößt gegen die verbindliche Trennregel.
2. A2: "Manifestdatei" statt des thesisweit festgelegten Begriffs "Sendemanifest" (K3, K4, K6).
3. A3: "Pflichtkern" statt "Pflichtoptionen" (einzige Fundstelle in der Thesis).
4. A4: "Passt der gesamte Rest in ein terminales Fragment, verwendet dieses Frag.Offset null" ist mehrdeutig und in
   der naheliegenden Lesart falsch; Offset null gilt nur, wenn das ganze Datagramm in ein einziges Fragment passt
   (src/frag/split.rs Z. 163-170 und 227-228; RFC 9868 Z. 1099-1101).

Dazu außerhalb des Kapitels A25: Das Abkürzungsverzeichnis löste EOL als "End of List" auf; RFC 9868 (Z. 637, 812)
und Kapitel 5 schreiben "End of Options List".

Die weiteren 49 Ersetzungen (24 Empfehlungen, 25 optionale) betreffen fehlende Belege, verrutschte Abschnittsangaben,
Begriffe, Bezüge, Metaphern, Anglizismen, Wortungetüme und Abbildungstexte.

## 24 Kriterien nach der Adjudikation

Eigene Prüfung des Orchestrators zusätzlich zu den Lanes: Beispielwerte (OCS, CRC32c, Längen) in Python nachgerechnet;
unsafe-Blöcke (send.rs:131, recv.rs:169), Uhr nur in api und socket (Instant::now in frag und recv nur unter
cfg(test)), /dev/urandom vier Bytes, Kennungsgenerator, Duplikatregel, Frist 120 s, Aufruferpflicht des Caches und
alle von Fable zitierten RFC-Zeilen am Quelltext gelesen.

1. Fachliche Richtigkeit: geprüft. Keine falsche Sachaussage; A4 beseitigt eine falsche Lesart, der Codex-Review
   präzisierte RDOS, Absenderfilter und Empfangsfrist.
2. Quellen und Belege: geprüft. Fehlende oder verrutschte Belege ergänzt (A7, A8, A9, A10, A23); S2-4 abgelehnt.
3. Verbindlichkeit: geprüft. MUST ("verlangt", Z. 619-621), SHOULD ("empfiehlt nur", Z. 1149, 2182) und MAY
   (Duplikate Z. 1134-1138, EOL-Nullfüllung) bleiben erhalten; die NOP/EOL-Ausnahme der Reihenfolge steht jetzt auch
   in 5.2.
4. Persönlicher Schreibstil: geprüft. Metaphern (roter Faden, ansetzen), Anglizismen (Splitter, Budget) und
   Wortungetüme (Mindestlängenprüfungen, Betriebssystemkontakt, Produktionsquelltext, Fragmentidentifikation) ersetzt.
5. Einzelne Sätze: geprüft. Unklare Bezüge ("diese eigene Prüfung", "Fehlt sie", "ihrer Art", "der gesamte Rest")
   und Zeugmen ("erfasste ... keinen Vergleich", "überspringt ... Ports") behoben.
6. Zweck und Ursache: geprüft. Zweckangaben vorhanden; im Warnzähler-Absatz ergänzt ("nur eine Warnung").
7. Zusammenhang: geprüft. Einleitung, Schluss und Nachbarkapitel abgeglichen (A6 zu 02:833-835, A29 zu 03:128-130,
   A46 zu 06:924-926, A24 in Kapitel 1, K6-Verweis auf das Beispieldatagramm).
8. Relevanz und Wiederholungen: geprüft. Wiederholung des Generator-Startwerts, doppelte Duplikatbedingung,
   Vorbemerkung "Wichtig ist die Aufgabenteilung" und der Kennung-Zusatz gestrichen.
9. Begriffe: geprüft. Sendemanifest, Pflichtoptionen, Kennung, Fragmentsatz, Surplus Area, Empfangspfad, Füllbyte,
   UDP Length vereinheitlicht; EXP beim ersten Auftreten aufgelöst.
10. Fußnoten: nicht anwendbar (Kapitel 5 enthält keine Fußnote).
11. Ziel und Umfang: geprüft. Linux, IPv4, Raw Sockets und acht Pflichtoptionen erhalten; IPv6 kommt nicht vor;
    Ankündigung in Kapitel 1 an die Gliederung nach Datenpfaden angepasst.
12. Ergebniszuordnung: geprüft. Vorversuch als Pilot ausgewiesen, Zahlen an docs/plan/steps/00b-spike.md belegt,
    Beobachtungsgrenze im Text.
13. IPv4, MTU und Fragmentierung: geprüft. Header 20/8, MTU 1500, Kapazitäten und Offsets nachgerechnet, Kernel
    fragmentiert bei IP_HDRINCL nicht (raw(7)).
14. UDP und Prüfsummen: geprüft. OCS-Beispiel, Nullregeln (RFC 768, RFC 9868 Sec. 9), Prüfreihenfolge.
15. Surplus Area und Optionen: geprüft. Pad, OCS mit Längensummand, TLV, EOL/NOP, SAFE/UNSAFE, doppeltes FRAG,
    Unter- und Überlauf, erweitertes Längenformat, Erratum 8834.
16. Betriebssystem und Netzpfad: geprüft. raw(7)-Feldtabelle gegen 05:228 (A6), CAP_NET_RAW, EMSGSIZE, ICMP-Senke.
17. Messbedingungen: geprüft. Einziger Messbezug ist der Vorversuch (veth, ein Linux-Host, MTU 1500).
18. Methodik: geprüft. Norm und eigene Entscheidung getrennt (A23; erweitertes Längenformat, 64er-Grenze,
    Filtered/Dropped als eigene Regeln markiert).
19. Aussagekraft der Nachweise: geprüft. Einschränkungen ("nur teilweise", "keine vollständige Unterstützung",
    "nicht vollständig verglichen") bleiben erhalten.
20. Entwicklungs- und Prüfablauf: geprüft. "Frühe" gegen "heutige" Fassung der Empfangsschleife durch die Korrekturen
    vom 11.08. und 14.08.2026 im Repository der Implementierung belegt.
21. Abbildungen, Tabellen und Verweise: geprüft. Abbildungszahlen und Annotationen gegen Text und Code; Caption
    5.4 mit Tausenderpunkt; Ankündigung 01:166-167 und K6-Verweise 06:346 (Prüfszenarien-Set) und 06:771 korrigiert.
22. PDF-Lesbarkeit: geprüft. Abbildungen 5.1 bis 5.3 bei ihrer Erklärung, 5.4 auf eigener Seite, Listing ungeteilt;
    Seitenaufteilung nach der Einarbeitung unverändert (Kapitel 5 gedruckt S. 44 bis 55).
23. Silbentrennung: geprüft. Alle Zeilenendtrennungen der gedruckten Seiten 44 bis 55 nach dem Neubau bewertet;
    fünf Trennhilfen gesetzt (siehe unten); nach dem Codex-Review erneut geprüft.
24. Abschlusskontrolle: geprüft. Fünfmal neu gebaut, keine Overfull- oder Underfull-Boxen, keine undefinierten
    Referenzen, 95 Seiten; Diff auf Bedeutungsänderungen gelesen.

## Eingearbeitete Änderungen

Alle 54 Ersetzungen von Fable wurden am Quelltext geprüft; 52 wurden unverändert übernommen, eine (A45) in
korrigierter Form, eine (A11) über die Trennhilfen. Dazu kommen vier eigene Änderungen.

Pflicht (A1 bis A4, A25):

- A1 (05:395-398): Trennhilfe `Pflicht\-optionen`; "meldefähig" beim ersten Auftreten erklärt
  ("alle außer EOL, NOP und FRAG"; api/mod.rs is_required_reportable_kind: APC, MDS, MRDS, REQ, RES).
- A2 (05:105): "Manifestdatei" durch "das Sendemanifest" ersetzt.
- A3 (05:416): "Der Pflichtkern umfasst" durch "Die Pflichtoptionen umfassen" ersetzt.
- A4 (05:454-457): "Passt das ganze Datagramm in ein einziges terminales Fragment, trägt dieses Frag.Offset null";
  "Splitter" durch "Beim Zerlegen prüft die Bibliothek" ersetzt.
- A25 (main.tex:248): Abkürzungsverzeichnis "End of Options List".

Belege und Verbindlichkeit:

- A7 (05:611-613): Duplikatregel mit Handelndem und Beleg Sec. 11.4 (MAY, Z. 1134-1138); "Den OCS-Befund der
  Fragmente führt die Bibliothek davon getrennt zusammen."
- A8 (05:616-617): Zusammenführung der Berichte mit Belegen Sec. 11.5 bis 11.7 und Sec. 15 (Z. 1781-1782);
  Fehlschlagregel gilt für jede meldefähige Optionsart, nicht nur für REQ/RES.
- A9 (05:625): Beleg für unbekannte SAFE- und UNSAFE-Optionen um Sec. 10 ergänzt (Z. 713-714, 741-743).
- A10 (05:673-676): Voreinstellungen mit Sec. 11.4 und 11.6 belegt; Sec. 25.4 an die Empfehlung zur Begrenzung
  verschoben (dort steht keine Zahl).
- A23 (05:205-206): Beleg Sec. 10 an die Normaussage (Pflichtoptionen vor SAFE-Optionen); die feste Reihenfolge
  darunter ist als Entwurfsentscheidung erkennbar.
- A6 (05:228-229): Kernelverhalten bei IP_HDRINCL nach raw(7): Gesamtlänge und Kopfprüfsumme trägt der Kernel
  stets selbst ein, die leere Identification füllt er; "ergänzt nur" gestrichen.
- A18 (05:645-646): "vollständige Option" gestrichen (der Parser prüft die Untergrenze 255 vor der Überlaufprüfung).

Begriffe und Bezüge:

- A12, A13 (05:459-463, 575): Generator-Absatz gekürzt (Startwert und /dev/urandom stehen in 5.1), Begriffe
  Kennung/Identifikation/Fragmentidentifikation auf "Kennung" gezogen; "Identification" bleibt der Feldname.
- A14 (05:422-424): EXP als Experimentaloption aufgelöst; "Nur für TIME und EXP prüft der Parser eine Mindestlänge".
- A19, A20, A22 (05:340, 387, 370): Bezüge "diese eigene Prüfung", "Fehlt sie", "ihrer Art" ersetzt.
- A21 (05:403): "überspringt ... Datagramme mit unlesbarem Header, eigenem Absender oder nicht passenden Ports"
  (socket/recv.rs filter_datagram).
- A27 (05:393-394): Peer "fasst Senden und Empfangen zusammen" und wird "erzeugt", nicht "gebunden".
- A32, A33, A34, A35, A48, A51, A52, A53: Fragmentsatz statt Fragmentgruppe, Surplus Area statt Überschuss,
  Empfangspfad statt Empfangspipeline, UDP Length statt UDP-Länge, Füllbyte statt Nullbyte, "Verwerfen" statt
  "Verwerfungsweg".
- A46 (05:664-666): Richtung des Cache-Vertrags korrigiert: das Modul frag dokumentiert eine Aufruferpflicht (ein
  Cache je UDP-Vierertupel), die Peer nur teilweise erfüllt (reassembly.rs Z. 16-20, wie 06:924-926).
- A45 (05:662), in korrigierter Form: "Der ReassemblyCache ist der einzige Empfangszustand, der über ein Datagramm
  hinaus erhalten bleibt." Fables Fassung ("einzige Protokollzustand") hätte den Kennungsgenerator übergangen, der
  sendeseitig ebenfalls Zustand über Datagramme hinweg hält.

Lesbarkeit und Kürzungen:

- A5, A16, A29, A41: Splitter, roter Faden, ansetzen, Budget ersetzt; Schlusssatz nennt jetzt die Doppelrolle aus
  Kapitel 3 (Prüfgegenstand für FF1, Messmittel für FF2).
- A15, A31: Betriebssystemkontakt und Produktionsquelltext vereinfacht.
- A17 (05:668-671): Warnzähler-Absatz mit gemeinsamem Punkt ("nur eine Warnung", "derselben Warnung"), eine Zeile
  kürzer.
- A28, A36, A37, A38, A39, A43, A44, A47, A49, A50: Handelnde genannt, Zeugmen aufgelöst, Vorbemerkung und
  widersprüchlich wirkender Zusatz gestrichen, "hier" durch "in dieser Implementierung" ersetzt.
- A30: Einleitung nennt die Reihenfolge wie die Überschrift von 5.4 (FRAG, weitere Pflichtoptionen, Grenzen).
- A40, A42, A54: Annotationen in Abbildung 5.4 (Abzug des UDP-Headers erklärt, Ordnung nach Position), Caption
  mit "2.918".

Andere Kapitel:

- A24 (01:166-167): Ankündigung "komponentenweise" durch "entlang ihrer Datenpfade" ersetzt.
- A26 (02:632): "End of Option List" durch "End of Options List" ersetzt.
- Eigene Änderung (06:770-771): "am Beispieldatagramm aus Kapitel 5" traf nicht zu (fig:eval-paketformen zeigt
  pad-odd mit 42 Byte, Kapitel 5 rechnet 40 und 48 Byte vor); jetzt "an einem Datagramm mit den Nutzdaten odd wie
  im Leitbeispiel aus Kapitel 5" (Befund S3-9, von Fable als offen gemeldet).

Trennhilfen nach dem ersten Neubau: `Pflicht\-optionen` (A1), `options\-tragenden`, `Fragment\-optionen`,
`Sonder\-fall` (Trennung über den Seitenwechsel 53/54), `Options\-bereichs` (A11). Die früheren Fehltrennungen
"Min-destlängenprüfungen", "Emp-fangsseitig", "Data-grammgrenzen" und "Frag-mentidentifikation" verschwanden mit
den Textänderungen A14, A45 und A12.

## Abgelehnte Befunde

- S2-4 ("verlangt" beim erweiterten Längenformat sei zu stark): RFC 9868 Z. 619-621 schreibt das Standardformat
  für Längen bis 254 als MUST vor; "verlangt" ist richtig.
- O1-13 (Linux-Vermerk am Vorversuch): Die Linux-Grenze ist thesisweit festgelegt; ein Vermerk nur an diesem Satz
  erzeugte eine neue Inkonsistenz.
- O2-14 (Verweis 04:57): Das Ziel enthält den angekündigten Inhalt; kein Mangel nach Kriterium 21.
- O2-18 ("auf die Leitung"): eingebürgerter Netzbegriff, in Kapitel 6 ebenso verwendet.

## Offene Punkte für den Autor

- Abkürzungsverzeichnis: erledigt, siehe Nachtrag 1 und Nachtrag 3 (jetzt 24 Einträge für Kürzel, die der Text
  nicht auflöst).
- Bib-Eintrag man7raw: Die zitierte Fassung 6.18 auf git.kernel.org antwortet mit HTTP 403 (Bot-Sperre; zwei Lanes
  und der Adjudikator prüften den Wortlaut über man7.org). URL-Wechsel ist Autorenentscheidung; urldate bleibt gültig.
- Zweigliedrige Wörter mit 20 bis 23 Buchstaben blieben stehen (Richtlinienentscheidung, Richtlinienauswertung,
  Protokollverarbeitung, Fragmentierungsoption, Anwendungsrichtlinie, Überlappungsprüfungen, Reassemblierungssatzes).
- Nichts im Repository der Implementierung zu ändern; der Cache-Kommentar (reassembly.rs Z. 16-20) und Kapitel 6
  sagen dasselbe wie A46.
- CSV-Kennung 226 (RFC 25.2): erledigt, siehe Nachtrag.

## Bau, PDF und Silbentrennung

Fünf Neubauten mit `make -C thesis pdf` (pdflatex, biber, makeglossaries, zweimal pdflatex; zwei nach dem
Workflow, drei nach dem Codex-Review): keine Overfull- oder
Underfull-Boxen, keine undefinierten oder mehrfachen Referenzen, 95 Seiten. Kapitel 5 steht unverändert auf den
gedruckten Seiten 44 bis 55 (physisch 50 bis 61), Kapitel 6 beginnt auf Seite 56, Literaturverzeichnis Seite 85,
Erklärung Seite 89. Die Zeilenzahl je Seite blieb bis auf phys. 57 (+2) und 61 (+1) gleich; Abbildung 5.4 bleibt
allein auf Seite 52, das Listing ungeteilt auf Seite 53. Die gerenderten Seiten 44, 52 und 55 wurden als Bild
kontrolliert (Legende, Annotationen, Kapitelende). Alle Zeilenendtrennungen der Seiten 44 bis 55 liegen nach dem
zweiten Neubau an Wortfugen oder an regulären Silbengrenzen einfacher Wörter.

## Codex-Review (gpt-6-astra, Effort ultra, read-only)

Auftrag (Sitzungsablage `codex-review-k5/prompt.md`): vollständige Prüfung von Kapitel 5 im aktuellen Arbeitsbaum
nach den 24 Kriterien und den Autorenvorgaben, Satz für Satz und im Zusammenhang der Kapitel 1 bis 7; ohne Diff,
ohne Nennung der Workflow-Befunde oder der Änderungen ("Die Änderungshistorie ist nicht Prüfgegenstand"). Lauf 18:20
bis 18:33 Uhr, Exit 0, keine Datei in beiden Repositorys verändert (git status geprüft). Wortlaut:
`reviews/kapitel-5-codex-review-2026-09-13.md`.

Urteil: **Freigabe mit Auflagen**. Architektur, Rechenbeispiele, Empfangsverarbeitung und Betriebsgrenzen stimmen mit
RFC und Code überein (MDS 1.472/40 Byte/0xF632, APC 0xE3069283, FRAG 1.460 + 1.458 mit Offsets 8 und 1468 und
RDOS 2926 ausdrücklich bestätigt). Fünf abgaberelevante und drei optionale Befunde; Kriterien 17 und 20 "offen".
Alle Befunde habe ich vor der Übernahme selbst geprüft:

1. Optionsreihenfolge in 5.2 (05:204-206) ohne die Ausnahme für NOP und EOL, die 5.4 nennt: bestätigt an RFC 9868
   Z. 793-796. Übernommen als "die Pflichtoptionen außer EOL und NOP".
2. Absenderfilter und Empfangsfrist (05:400-411) waren als fest beschrieben: bestätigt, Peer bindet den Empfänger
   ohne eigene Quelladresse (api/mod.rs Z. 279) und ohne Frist (PeerConfig::new, read_timeout None); udpopt-recv
   bietet beides als Option. Übernommen in kürzerer Form: "auf Anforderung auch Datagramme vom eigenen Absender";
   "Eine gesetzte Empfangsfrist gilt für die ganze Schleife; ohne Frist wartet sie unbegrenzt".
3. RDOS (05:435-436) zeigt auf den Beginn der Surplus Area, nicht der Datagrammoptionen: bestätigt an RFC 9868
   Z. 1041-1046. Übernommen.
4. 06:346-347 verwies für das "goldene Prüfszenarien-Set" auf Kapitel 5, das es nicht beschreibt: bestätigt.
   Übernommen als Verweis auf die Wire-Prüfung in \secref{subsec:pruefmittel}; Kapitel 5 blieb unverändert.
5. Wortregel: übernommen "Byte Nutzdaten" statt "Nutzdatenbytes" (sechsmal), "mit dem höchstwertigen Byte zuerst"
   statt "in Netzwerkbytefolge", "Position innerhalb der Nutzdaten" in Abbildung 5.4 (b). Nicht übernommen:
   "Netz-Systemaufrufe" (Bindestrich-Kompositum, verständlich), "Nutzdatenprüfsumme" (Kapitel 1 verwendet denselben
   Begriff) und "IP-Headerprüfsumme" (thesisweit, auch in AGENTS.md Kriterium 14); Einheitlichkeit geht vor.
6. Optional, übernommen: Surplus-Rechnung "Sie beginnt im Beispiel bei Byte 37 ($20 + 17$) und umfasst
   $48 - 37 = 11$ Byte"; MRDS-Absatz ohne mehrdeutiges "sie" (mit "Empfangene" erhalten); Duplikatregel benennt
   \texttt{Peer} und \texttt{build\_outgoing\_datagrams} (validate_send_options wird in api/mod.rs Z. 369 von
   build_outgoing_datagrams aufgerufen; das tiefere build_datagram lässt Duplikate zu), statt nur "Peer" wie von Codex
   vorgeschlagen.

Grenzen laut Codex, die bleiben: Für den Vorversuch (05:340-349) existiert kein Rohprotokoll des damaligen Laufs in
den Messarchiven; die Zahlen sind am Fallgenerator (examples/support/common.rs) und an docs/plan/steps/00b-spike.md
nachvollziehbar, der Text weist sie als Vorversuch aus (Kriterium 17). Das Verhalten der "frühen Fassung" der
Empfangsschleife prüfte Codex nicht an der Historie; die Fable-Lane belegte es an den Korrekturen vom 11.08. und
14.08.2026 (Kriterium 20). Beides erfordert keine Textänderung.

Nach diesen Änderungen dreimal neu gebaut (Builds 3 bis 5): keine Warnungen, 95 Seiten, Kapitelanfänge unverändert
(Kapitel 5 Seite 44, Kapitel 6 Seite 56, Kapitel 7 Seite 83, Literatur 85, Erklärung 89); alle Zeilenendtrennungen der
Seiten 44 bis 55 erneut kontrolliert (auch über Seitenwechsel: "options-tragenden", "Sonder-fall"). Kein weiterer
Codex-Lauf; die Änderungen dieser Runde sind klein und an den Quellen belegt.

## Nachtrag: Abkürzungsverzeichnis und CSV-Kennung 226 (Autorenanweisung vom 13.09.2026)

Abkürzungsverzeichnis (thesis/main.tex): Der Text löst OCS (Kapitel 1 und 2) sowie EOL, NOP, APC, FRAG, MDS und MRDS
(Kapitel 5, 5.4) selbst auf; diese sieben Einträge sind gestrichen. DTLS und PMTU kommen in keinem Kapitel vor und
sind ebenfalls gestrichen. Es bleiben TIME, AUTH und PCAP, die der Text nirgends ausschreibt. Kein \gls-Aufruf war
betroffen (die Kapitel verwenden keine). Vorspann und Seitenzahlen unverändert (Kapitel 1 weiter auf phys. Seite 7).

CSV-Kennung 226 (RFC 9868, Abschnitt 25.2, Z. 2113-2116): Das SHOULD, empfangene Optionen in einer von der
Paketreihenfolge unabhängigen Ordnung zurückzugeben, gilt für "Implementations concerned with the potential use of
UDP Options as a covert channel". Die bisherige Begründung band es an das nicht gewählte MAY; das trägt nicht (Befund
Codex, Kapitel-4-Runde). Die Bibliothek gibt Optionen in Paketreihenfolge zurück (src/recv/pipeline.rs, kein
Umordnen im Code; die Selbstauskunft in docs/requirements.md Z. 226 "optional" hat keinen Codebeleg). Entscheidung:
Die Kategorie "nicht anwendbar" bleibt, weil die Bedingung des RFC (Bedenken wegen verdeckter Kanäle) nicht zum
Umfang der Arbeit gehört; diese Umfangsfestlegung fehlte bisher und steht jetzt ausdrücklich in 1.4
("Ein Schutz gegen verdeckte Kanäle über UDP-Optionen ist kein Ziel dieser Arbeit"). Geändert: Generator
thesis/tikz/gen/ff1-kategorien.py (Kommentar und Zeile 226: Beleg "kein Schutzziel gegen verdeckte Kanaele;
Empfangsausgabe in Paketreihenfolge", Prüfnotiz 2026-09-13), CSV per Generator neu geschrieben (nur Zeile 226
geändert, Asserts 67 Zeilen, 50/7/0/10 und 57/0/0/10 bestanden, Summen und Abbildungen unverändert), Kapitel 6
Abschnitt 6.3 (Satz zu Zeile 226 mit Verweis auf 1.4), thesis/insights-inbox.md (Punkt abgehakt). Zeile 225
(DoS-SHOULD, anwendbar, teilweise) bleibt davon unberührt, weil die Bibliothek dort Grenzen umsetzt.

Build 6: keine Warnungen, 95 Seiten, alle Kapitelanfänge unverändert; Trennungen auf den geänderten Seiten (phys. 10,
11, 86) geprüft.

## Nachtrag 2: Keine Commit-Kennungen im Thesistext (Autorenanweisung vom 13.09.2026)

Neues Kriterium 25 in AGENTS.md ("Versionsangaben"): keine Commit-Hashes, Kurzkennungen, Branch- oder Tag-Namen im
Thesistext, auch nicht in Fußnoten, Tabellen, Beschriftungen und Links; Stände über Datum, Bezeichnung des Laufs oder
die abgegebene Fassung benennen; Repository-Links ohne Commit-Bezug. Damit entfällt die Abhängigkeit der CSV-Fußnote
vom Commit.

Umgesetzt in den bereits geprüften Kapiteln:

- 04_analyse.tex Z. 67-69 (Fußnote zur Einzelzuordnung): Link auf das Repository ohne Commit-Pfad, "Stand der
  abgegebenen Fassung" statt der alten Commit-Angabe. Dazu eine vorbestehende Zeile mit 126 Zeichen (Z. 223-231)
  umbrochen; nur Quelltext-Umbruch, keine Textänderung.
- 03_methodik.tex Z. 250 (Fußnote zu den Arbeitsvorgaben): "Stand vom 14. August 2026" statt der alten Commit-Angabe
  (Datum des Commits im Repository der Implementierung).

Noch offen, weil Kapitel 6 seine eigene Runde bekommt und die Tabellenlogik betroffen ist:

- 06_evaluation.tex Z. 53-73: Tabelle tab:eval-messlaeufe, Spalte "Stand" mit sieben Kurzkennungen.
- 06_evaluation.tex Z. 91-96: Fußnote mit Erklärung der Kurzkennungen und der vollen Revision des Auswertungsstands.
- 06_evaluation.tex Z. 98-103: Zuordnung des Pilotstands zu SHA-256-Werten, "Der Commit war ... kein Vorfahr des
  Hauptzweigs", "alle Aussagen über Quelltext und Tests" auf den Auswertungsstand.
- 06_evaluation.tex Z. 111: "Versioniert sind die Archive seit der Revision ..." mit voller Kennung.
- 06_evaluation.tex Z. 997: Fußnote mit zwei Commit-Kennungen; Z. 1116: "mit Commit ... drei Tage später".

Vorschlag für die Kapitel-6-Runde: Spalte "Stand" durch das Datum des Binärstands ersetzen, die Zuordnung zu den
Archiven in thesis/evidence/README.md belassen (dort dürfen Kennungen stehen), Fußnoten auf Datum umstellen.

Build 7 (nach den Fußnoten): keine Warnungen, 95 Seiten, alle Kapitelanfänge unverändert.

## Nachtrag 3: Unabhängige Schlussprüfung durch Fable 5.1 und Codex (Autorenanweisung vom 13.09.2026)

Auftrag an beide, wortgleich und neutral: Kapitel 5 vollständig sowie die Stellen dieser Runde in Kapitel 1, 2,
3, 4 und 6, im Abkürzungsverzeichnis und in CSV-Zeile 226 nach allen 25 Kriterien prüfen; nur lesend; Berichte
unter reviews/, Lernnotizen und Inbox nicht lesen; Änderungshistorie kein Prüfgegenstand.

Codex (gpt-6-astra, ultra): Abbruch nach sechs Minuten mit "You've hit your usage limit ... try again at
Sep 19th, 2026 10:14 AM" (Exit 1, keine Ausgabe). Der Auftrag liegt in der Sitzungsablage
(`schlusspruefung-k5/prompt.md`) und kann unverändert wiederholt werden.

Fable 5.1 (Workflow wf_c888e12e-7c4, 27 Minuten, 73 Werkzeugaufrufe, 27 bestätigte Aussagen): Kapitel 5
**abgabereif**, kein abgaberelevanter Befund; die geprüften Stellen **mit Auflagen** wegen des
Abkürzungsverzeichnisses. Entscheidungen zu den neun Befunden, jeweils nach eigener Prüfung:

- B1 (abgaberelevant, Abkürzungsverzeichnis): Das Verzeichnis führte nur TIME, AUTH und PCAP, obwohl der Text
  API, ICMP, TCP, UCMP, UENC, UEXP, EID, CRC32c, JSON, AWS, GCP, NTP, DNS, HTTP, STUN, KVM, XDP, CVE und NSA nirgends
  auflöst (eigener Scan des PDF-Texts bestätigt; TTL kommt hinzu, Kapitel 2 schreibt nur "Time to Live" ohne
  Kürzel). Übernommen: 21 Einträge ergänzt, jetzt 24. Sieben Randfälle bewusst weggelassen (GC, STD, PR, PTR,
  SHA-256, VM, TUN/TAP): Namen oder aus dem Kontext verständlich; mit ihnen wäre das Verzeichnis auf eine zweite
  Seite gewachsen (96 Seiten, alle physischen Seiten verschoben).
- B2 (abgaberelevant nach Kriterium 25, Kapitel 6): Commit-Kennungen in Tabelle 6.1, zwei Fußnoten und
  Fließtext. Bleibt nach Autorenentscheidung für die Kapitel-6-Runde. Fables Datumszuordnung wurde am Git-Log
  bestätigt: Auswertungsstand 18.08.2026; Messstände 10.08., 11.08., 13.08., 15.08. (09:49 und 19:54) und
  16.08.; Empfängerkorrekturen 11.08. und 14.08.; Archivversionierung im Thesis-Repository 25.08.2026.
- B3 (optional): Die Ordnungsregel stand wortgleich in 5.2 und 5.4. Übernommen: 5.4 verweist auf 5.2.
- B4 (optional): "einziger Empfangszustand" übergeht die globalen Warnzähler. Übernommen: "einzige
  Empfangszustand mit Protokollwirkung".
- B5 (optional, Kriterium 21): 06:839-841 sprach von einer "aus Kapitel 5 übergebenen Frage", die Kapitel 5 nicht
  stellte. Übernommen: Schlusssatz in 5.3 ("Ob diese Zusammenfassung für die Messkampagnen ausreicht, klärt
  Abschnitt 6.3") und in Kapitel 6 "zusammengefasste Meldung 'kein Datagramm'" statt "zusammengefasste
  Empfangsberichte".
- B6 (optional): 06:766-768 lud zum Vergleich 40 gegen 42 Byte ein. Übernommen in kurzer Form: "hier mit REQ statt
  MDS (42 statt 40 Byte)"; pad-odd trägt REQ (scripts/wire-check.py Z. 248 und 272).
- B7 (optional, Kriterium 1): "die Empfangsausgabe folgt der Paketreihenfolge" war für zusammengesetzte
  Fragmentsätze zu pauschal; merge_fragment_options stellt die zusammengeführten Fragmentoptionen in fester
  Reihenfolge davor (src/recv/pipeline.rs, src/frag/reassembly.rs to_raw_options). Übernommen: "bei gewöhnlichen
  Datagrammen" in 6.3, im Generator und in CSV-Zeile 226 (neu erzeugt, Asserts bestanden). Die Einstufung "nicht
  anwendbar" hängt am fehlenden Schutzziel und bleibt.
- B8 (optional, Kriterium 22): Fußnote 03:250 brach "docs/requirements." / "md" um. Übernommen mit \mbox und
  \raggedright (wie die Fußnote in Kapitel 4; ohne \raggedright entstand eine Underfull-Box).
- B9 (optional): Kurzkennung des Auswertungsstands im CSV-Kopf und im Generator-Docstring. Datendatei, kein Thesistext;
  zusammen mit B2 in der Kapitel-6-Runde auf ein Datum umstellen.

Von Fable nicht prüfbar (keine Textänderung nötig): Rohprotokoll des Vorversuchs (nur Fallgenerator und
Schrittdokument), Vorstufe vom 14.08. unversiegelt, raw(7) 6.18 mit HTTP 403 (6.19 inhaltsgleich), ICMP-Begründung
des Hilfs-Sockets nur am Codekommentar, keine Test- oder Messläufe, Kapitel 6 nur an den beauftragten Zeilen.

Builds 8 bis 10: Build 8 zeigte, dass 31 Einträge das Verzeichnis auf zwei Seiten treiben (96 Seiten); nach der
Kürzung auf 24 Einträge und der Fußnotenkorrektur ist Build 10 warnungsfrei, 95 Seiten, alle Kapitelanfänge
unverändert, Kapitel 6 seitenidentisch, Kapitel 5 auf den gedruckten Seiten 44 bis 55 mit korrekten Trennungen.

## Identifikation des ausgelieferten Standes

Ausgangsstand: Thesis vom 13.09.2026 (Arbeitsbaum sauber), Implementierung vom 03.09.2026 (nur gelesen). Endstand
(uncommitted, nach Build 10):

- thesis/chapters/05_entwurf_implementierung.tex:
  `40e3282bc0fa12b320cd6dc16d89b6ca1e5881bf7146c17a03c032f03974e968`
- thesis/chapters/06_evaluation.tex:
  `9eec5ae981c1be54678a5721e6508df928ed59aa09d90bf063b37f0495289bcb`
- thesis/main.pdf (95 Seiten):
  `56538468ec7fe5756de46cb4bcc4ace5be1171e1d33afe0c47a8b5b9e9d58655`
- thesis/chapters/04_analyse.tex:
  `312b0e7f88dd45d4c4239b7f4fd49baf4dbfe4c92dc7f90f535dd1330e97c53a`
- thesis/main.tex:
  `c75d1bc989ec54a514be0346f0bf4846b02856ad06fb09d5352a3d5323a96363`
- thesis/daten/konformitaet-kategorien.csv:
  `22a448762f112343a69e78b2b6f830c965c0a27fc9112798df0b4f80242414b4`

Weitere geänderte Dateien: thesis/chapters/01_einleitung.tex (A24, Umfangsfestlegung 1.4),
thesis/chapters/02_grundlagen.tex (A26), thesis/chapters/03_methodik.tex (Fußnote ohne Commit),
thesis/main.tex (A25, Abkürzungsverzeichnis), thesis/tikz/gen/ff1-kategorien.py (Zeile 226), AGENTS.md
(Kriterium 25). Neue Dateien: dieser Bericht und
`reviews/kapitel-5-codex-review-2026-09-13.md`.
