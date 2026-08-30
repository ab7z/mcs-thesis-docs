# Messartefakte

Stand 2026-08-26: Die elf Archive in diesem Verzeichnis sind die versiegelte Evidenz zu den
FF1- und FF2-Messungen der Arbeit. Die Thesis auf `main` (1f17af3) beantwortet beide
Forschungsfragen im geprüften Umfang (Paar, Richtung, Messfenster). Die älteren
Einleitungsabsätze einzelner Archive beschreiben den Beitrag *dieses* Datensatzes zum Zeitpunkt
der Versiegelung; sie sind keine aktuelle Gesamtwertung von FF2.

## Bidirektionale Kampagne vom 11. August 2026

- Kampagnenkennung: `bidir-campaign-20260811`
- Quellstand der Messung: `7b11140a91ec730bf5d8351e7b00653d41f3c255`
- Ursprünglicher Pfad:
  `../udp-transport-options/target/bidir-campaign-20260811/`
- Archiv: `bidir-campaign-20260811.tar.zst`
- Archivgröße: 44132 Byte
- Archiveinträge einschließlich Verzeichnissen: 84
- Durch das interne Manifest erfasste Dateien: 76
- SHA-256 des Archivs:
  `c327163d80aebb627d68e56a0df50840055126649abb20df390c30f6f76f8398`
- SHA-256 des enthaltenen Manifests `SHA256SUMS`:
  `71b33b5efb48f3ceddec0b4d239b24de057d1bbcaea90a6ac089560523fdcf90`

Das Archiv enthält den Kampagnenplan, die Sende- und Empfangsskripte, PCAP-Dateien von drei
Erfassungsstellen (Gast `enp2s0`, Mac `en0`, Hetzner `eth0`), Empfänger-JSONL, Sendemanifeste,
Konsolenprotokolle, die Auswertung und die wiederhergestellten Prüferberichte. Es enthält keine
Zugangsdaten; eine Prüfung aller Nicht-Cache-Dateien auf Schlüssel, Token und Passwörter fand
keine Treffer. Ausgeschlossen sind nur Python-Cachedateien.

Die 76 erfassten Dateien setzen sich zusammen aus den 68 ursprünglichen Kampagnendateien und
acht nachträglich gesicherten Verifikationsdateien unter `verification/`. Die eigenständigen
Berichte der drei Prüfer lagen nicht in der Kampagnenablage, sondern nur im flüchtigen
Arbeitsverzeichnis der damaligen Sitzung. Sie wurden von dort wiederhergestellt; die
Ursprungsdatei liegt als `verification/verifier-panel-result.json` bei, sodass die Wiedergabe
prüfbar ist. Herkunft und verbleibende Grenzen stehen in `verification/README.md`.

Vor der Archivierung wurde ein Zählfehler berichtigt und als Erratum erhalten: Richtung A enthält
18 unterschiedliche FULL-Kontrollen, nicht 15. Siehe `analysis/verdicts.md`, Abschnitt "Errata".

Die Kampagne belegt zwei richtungsabhängige Ergebnisse:

1. Richtung `achim -> mcs`: VMware NAT oder macOS VMnet entfernt die Surplus Area bereits lokal
   und schreibt die IPv4-Gesamtlänge auf `IPv4 IHL + UDP Length` um. Der Server sieht die
   Optionen nie.
2. Richtung `mcs -> achim`: Die getestete RFC-9868-Paketklasse geht vollständig verloren
   (0 von 6), während gleich große Kontrollpakete auf demselben Fluss ankommen (15 von 15). Der
   Verlust ist auf den Bereich zwischen Hetzner `eth0` und Mac `en0` eingegrenzt. Das Gerät ist
   aus zwei Erfassungsstellen nicht bestimmbar.

Der Datensatz ist ein bidirektionaler externer Beitrag zu FF2. Er vervollständigt FF2 nicht.

Prüfung im Verzeichnis `thesis/evidence`:

```sh
shasum -a 256 -c bidir-campaign-20260811.tar.zst.sha256
zstd -t bidir-campaign-20260811.tar.zst
zstd -dc bidir-campaign-20260811.tar.zst | tar -tf - > /dev/null
```

Die dritte Zeile entpackt ausdrücklich mit `zstd`. Ein direktes
`tar -tf <archiv>.tar.zst > /dev/null` ist nicht zuverlässig: `bsdtar` auf macOS startet `zstd`
dabei als Kindprozess und meldet bei diesem Archiv `Child process exited with status 1`.

Nach dem Entpacken kann das interne Manifest aus dem Kampagnenverzeichnis geprüft werden:

```sh
zstd -dc bidir-campaign-20260811.tar.zst | tar -x
cd bidir-campaign-20260811 && shasum -a 256 -c SHA256SUMS
```

## Externe Pfadkampagne vom 10. August 2026

- Kampagnenkennung: `20260810T200118Z`
- Quellstand: `7b11140a91ec730bf5d8351e7b00653d41f3c255`
- Messzeitraum: `2026-08-10T20:01:18Z` bis `2026-08-10T22:24:22Z`
- Abschluss der Dokumentation: `2026-08-10T22:35:56Z`
- Ursprünglicher Pfad:
  `../udp-transport-options/target/external-campaign/20260810T200118Z/`
- Archiv: `external-campaign-20260810T200118Z.tar.zst`
- Archivgröße: 365385 Byte
- Archiveinträge einschließlich Verzeichnissen: 1509
- Durch das interne Manifest erfasste Dateien: 1330
- SHA-256 des Archivs:
  `d59c0b86407622ba957586272573a0258c77d5bc271da9b8cba42eb72650c516`
- SHA-256 des enthaltenen Manifests `SHA256SUMS`:
  `e3adda5a170cb4426a8352a938ae7550a5a369890ca4685f460381a876fc87a0`

Das Archiv enthält PCAP-Dateien, Manifeste, Befehlsprotokolle, Zustandsaufnahmen, Webquellen,
Auswertungen, Fehlversuche, Bereinigungsnachweise und die veröffentlichte Wissenssicherung.
Kurzlebige private WireGuard-Schlüssel sind nicht enthalten.

Die Kampagne belegt drei getrennte Ergebnisse:

1. Der VMware-NAT-Pfad zusammen mit macOS VMnet normalisierte das frühere IPv4-Paket exakt auf
   `IPv4 IHL + UDP Length`. Die Daten trennen `vmnet-natd` nicht von der Apple-VMnet-API.
2. Je ein direkt gebridgtes IPv4- und IPv6-Paket mit Surplus Area war bis `en0` intakt, wurde aber
   nicht auf Hetzner `eth0` beobachtet. Dieser kleine Stichprobenumfang identifiziert keinen Betreiber.
3. Ein kurzlebiger WireGuard-Tunnel lieferte das innere IPv4-Paket nach der Entkapselung mit denselben
   26 Surplus-Bytes und gültiger OCS an Hetzner `wg-uoe`. Dies belegt keinen nativen öffentlichen Durchgang.

Der Datensatz ist ein erster externer Beitrag zu FF2. Er vervollständigt FF2 nicht.

Prüfung im Verzeichnis `thesis/evidence`:

```sh
sha256sum -c external-campaign-20260810T200118Z.tar.zst.sha256
zstd -t external-campaign-20260810T200118Z.tar.zst
tar -tf external-campaign-20260810T200118Z.tar.zst > /dev/null
```

Nach dem Entpacken kann das interne Manifest aus dem Kampagnenverzeichnis geprüft werden:

```sh
sha256sum -c SHA256SUMS
```

## Helsinki-Kampagnen vom 15. August 2026

- Kampagnenkennung: `hel-kampagne-20260815`
- Quellstand der Messung: Kampagnen-Binaries bitidentisch `d7187eb` auf allen drei Endpunkten
  (mcs, helsinki, 1blue); Treiber ab Commit `d3e22db`, `pair-campaign.sh` und `pair-pilot.sh` aus
  `8627860`, `checksumgate-cell.sh` aus `74bc65a`
- Ursprünglicher Pfad: `../udp-transport-options/target/` mit den sechs Kampagnen-Stamps
  `p0/p1/p2-campaign-20260815T205110Z-mcs-hel` und `p0/p1/p2-campaign-20260815T214507Z-hel-1blu`
- Enthaltene Stamps: die sechs Kampagnen-Stamps sowie drei Checksumgate-Stamps
  (`checksumgate-20260815T213446Z-mcs-hel` als Erstlauf ohne Captures, inhaltlich identisch,
  `checksumgate-20260815T221328Z-mcs-hel`, `checksumgate-20260815T221511Z-hel-1blu`)
- Archivgröße: 1086099 Byte; entpackt 60764160 Byte
- Archiveinträge einschließlich Verzeichnissen: 1050
- SHA-256 des Archivs:
  `1545f30a5f2d1c97d0a55d657c7615f035fecb0fd6c7841a0944ce9ecf5bb063`

Provenienz der Prüfsummendatei: `hel-kampagne-20260815.tar.zst.sha256` wurde am 2026-08-25
nachträglich angelegt. Der Referenzwert war am 2026-08-16, dem Erstellungszeitpunkt des Archivs,
in der internen Ergebnisdatei der Kampagne (`lernnotizen/hel-kampagne/hel-ergebnisse.md`,
Zeilen 10 bis 12) dokumentiert; die Neuberechnung am 2026-08-25 ergab bytegleich denselben Wert.
Anders als die beiden älteren Archive enthält dieses Archiv kein internes `SHA256SUMS`-Manifest.
Die Dateiintegrität stützt sich auf den Archiv-Hash und den zstd-Selbsttest; die Kampagnen-Stamps
enthalten Sende-Manifeste (`manifest.jsonl`) als fachliche Sollwerte je Szenario und Richtung.

Das Archiv belegt die Replikation der FF1-Suite auf den zwei neuen Cloud-Paaren mcs zu helsinki
und helsinki zu 1blue (je 18 Treiber-Szenarien in beiden Richtungen, alle mit Rückgabewert 0 und
ohne unerklärten Verlust; S-51 bleibt nach Entscheidung E1 gestrichen) sowie die enthaltenen
Checksumgate-Kreuzzellen. Der Datensatz erweitert die Realpfad-Basis von FF1 und FF2. Er
vervollständigt FF2 nicht.

Prüfung im Verzeichnis `thesis/evidence`:

```sh
shasum -a 256 -c hel-kampagne-20260815.tar.zst.sha256
zstd -t hel-kampagne-20260815.tar.zst
zstd -dc hel-kampagne-20260815.tar.zst | tar -tf - > /dev/null
```

## Nachversiegelung vom 25. August 2026

Nach der Autorenentscheidung vom 2026-08-25 (Testprogramm abgeschlossen, FF2-Entscheidungstor geschlossen,
bevorstehende Kündigung der Messserver) wurden die verbliebenen Messartefakte aus dem gitignorierten
target/-Verzeichnis des Implementierungsrepos und aus den privaten Kampagnenordnern in acht weitere Archive
versiegelt. Jedes Archiv wurde unmittelbar nach der Erstellung mit zstd geprüft und seine Prüfsummendatei
mit shasum -a 256 -c verifiziert. Die Eingabestände je Lauf stehen in den enthaltenen Dateien
meta-sender.txt und meta-receiver.txt beziehungsweise in den README- und Berichtsdateien der Archive. Die
Einstufung der einzelnen Läufe (Kampagne, vorregistrierte Messreihe, Pilot, Vorstufe) trifft Tabelle 6.1
der Arbeit; Läufe ohne beidseitige Captures oder Manifeste bleiben auch archiviert als Piloten oder
Messreihen gekennzeichnet und werden nicht mit Kampagnensummen verrechnet. Ausgeschlossen sind
Python-Cachedateien und Finder-Metadaten.

- `p0p1p2-kampagnen-1blu-mcs-20260814-15.tar.zst`: die 22 Kampagnen-Stamps der P0/P1/P2-Läufe auf dem Paar
  1blue und mcs vom 14./15.08. (12 p0, 5 p1, 5 p2, je mit PCAPs, Manifesten, Auswerterberichten);
  509680 Byte, entpackt 33280000 Byte, 607 Einträge; SHA-256
  `644955e5bf51d03dd353273a5606e7e2bc9150c723393ddc9a2e889e85566dad`.
- `p0p1p2-kampagnen-aws-20260816.tar.zst`: die neun Kampagnen-Stamps der transatlantischen FF1-Suiten
  (aws-mcs, aws-hel, aws-1blu, je p0/p1/p2) sowie die beiden NAT-Split-Smoke-Läufe; 1479690 Byte,
  entpackt 90951680 Byte, 1575 Einträge; SHA-256
  `d5f5a4d89eaa76f6ce872807461f26ec94bd9649f63ac91d2a202833e88c1d9a`.
- `piloten-und-nachtraege-20260810-15.tar.zst`: die drei Piloten vom 12./13.08. (pilot-1blu,
  pilot-bridged, pilot-mcs2mac), der external-smoke-Lauf vom 10.08. und der abgebrochene
  hel-1blu-Erstlauf `p0-campaign-20260815T213904Z-hel-1blu` (SSH-Drossel nach s31, Messdaten unversehrt);
  119325 Byte, entpackt 4505600 Byte, 214 Einträge; SHA-256
  `7753e4a3de331362a6b832b82ddfd74b2a4867b915dc5f170b374a2a7dcc0b70`.
- `ff2-hotspots-20260815.tar.zst`: die vorregistrierten Messreihen hotspot2, hotspot3 und hotspot4
  (Captures, JSONL, Responder- und tracepath-Protokolle, vmx-Backup); 55788 Byte, entpackt 1177600 Byte,
  39 Einträge; SHA-256 `b8a309942e69df9fda7aea86e9094acf37543678ac113b157440c229d809b30e`.
- `ff2-ttl-pfadanalyse-20260815.tar.zst`: die TTL-Pfadanalyse (bericht.md, ttl-report-alle-captures.md,
  traces, flusspinnte Traceroutes, sweep.pcap, Hotspot-TTL-Auswertung 10./11.08., die vier
  Vorregistrierungen, SHA256SUMS); 22493 Byte, entpackt 122880 Byte, 11 Einträge; SHA-256
  `0e9cbbcd1391756e6e3f64a24058b571177b1ec5d0dd6b84710657b57e7aedca`.
- `ff2-aws-us-20260816.tar.zst`: aws-us-Messreihen und -Piloten (Pilotlanes, Checksumgate-Kreuzzellen,
  Diskriminator-Matrix, Ergebnisdateien der drei aws-Paare, mtr-Traces, Skripte, SHA256SUMS);
  42765 Byte, entpackt 983040 Byte, 140 Einträge; SHA-256
  `bce14312b8b49abd6dabdf0d71b53725d5071eb654db268db293135778e04ade`.
- `ff2-gcp-us-20260816.tar.zst`: gcp-Pilot, Locus-Captures und Diskriminator-Matrix der
  Google-Compute-Messung; 8627 Byte, entpackt 102400 Byte, 18 Einträge; SHA-256
  `3850ed3a7798cff6a2fd24854e3e54f0100fd254a2524d5ede1fce405cc7d097`.
- `ff2-aws-ap-20260816.tar.zst`: der AP-Sweep über sechs Regionen (Vorregistrierung, Phasen M und B,
  Eskalationszellen, Berichte, SHA256SUMS); 78903 Byte, entpackt 1904640 Byte, 261 Einträge; SHA-256
  `097bd983d3777062036d1772a39cfd7c844a68ebadc4061f45de8bc2631b2870`.

Prüfung im Verzeichnis `thesis/evidence` (für jedes Archiv gleich):

```sh
for f in *.sha256; do shasum -a 256 -c "$f"; done
zstd -t <archiv>.tar.zst
zstd -dc <archiv>.tar.zst | tar -tf - > /dev/null
```

Geplante Versionierung: Nach der Kündigung der Messserver wird `thesis/evidence/` aus `.git/info/exclude`
genommen und mit allen Archiven versioniert; Verweise aus der Arbeit nennen dann das GitHub-Repository
(`github.com/ab7z/mcs-thesis-docs`), den Archivpfad und die SHA-256. Bis dahin gelten die lokalen Archive
mit den hier dokumentierten Prüfsummen.
