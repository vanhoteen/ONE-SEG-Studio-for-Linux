# ONE SEG Studio for Linux

## 🌐 Wähle deine Sprache

### [🇬🇧 English](README.md)
### [🇪🇸 Castellano](README.es.md)
### [<img src="Assets/flag-asturias.svg" width="32" alt="Asturias"> Asturianu](README.ast.md)
### [🇩🇪 Deutsch](README.de.md)
### [<img src="Assets/flag-catalunya.svg" width="32" alt="Catalunya"> Català](README.ca.md)

---

<img src="Assets/app-icon.png" width="180" alt="ONE SEG Studio">

> **EXPERIMENTELLE TESTVERSION — Ubuntu 26.04 LTS · amd64 (Intel/AMD, 64 Bit). Keine stabile Veröffentlichung.**

Ein Projekt von **vanhoteen**: Videos vorbereiten und mit einem HackRF One ein japanisches One-Seg-Fernsehsignal erzeugen. Bei der üblichen ISDB-T-Konfiguration versorgt das mittlere der dreizehn Segmente tragbare Empfänger mit Fernsehen geringerer Auflösung, ohne Internetempfang.

Der Autor hat Installation und Empfang mit einem Sony XDV-D500 unter Ubuntu 26.04 amd64 erfolgreich getestet. Andere Distributionen und Architekturen sind nicht geprüft.

## Installation

Lade [**ONE-SEG-Studio-Linux-preview6-Ubuntu26-amd64.zip aus Version 0.3**](https://github.com/vanhoteen/ONE-SEG-Studio-for-Linux/releases/download/0.3/ONE-SEG-Studio-Linux-preview6-Ubuntu26-amd64.zip) herunter. Die automatischen **Source code**-Archive sind keine Installer.

Den vollständigen Installer-Ordner herunterladen und entpacken. Beide `.deb`-Dateien, `INSTALL.sh`, `UBUNTU_VERSION` und `SHA256SUMS` zusammen lassen. Im Ordner ein Terminal öffnen:

```bash
bash INSTALL.sh
```

Internet und Administratorpasswort werden benötigt. Die Anwendung, TSDuck und Ubuntu-Abhängigkeiten werden installiert. Auf dem Zielcomputer muss nichts kompiliert werden. Anschließend ONE SEG Studio im Anwendungsmenü des Linux-Desktops öffnen.

HackRF anschließen, **Check tools** und **Detect HackRF** wählen, Video auswählen und **Prepare video** anklicken. **Transmit** startet die Aussendung; **Stop** beendet sie. Installation und Vorbereitung senden nicht.

## Ausgabe für leistungsschwache Rechner — Offline-I/Q-Test

> **Optionale, separate Testversion.** Wenn die normale Linux-Version auf einem leistungsschwachen Rechner unterbrochenes Video, schwarze Bilder oder kein Signal liefert, probiere den [Offline-I/Q-Test](https://github.com/vanhoteen/ONE-SEG-Studio-for-Linux/releases/tag/offline-iq-test-0.1). Er erzeugt die vollständige I/Q-Datei **vor** dem Öffnen des HackRF. Beim Senden spielt der HackRF die vorbereitete Datei ab. Das reduziert die CPU-Last in Echtzeit und vermeidet Modulationspausen während der HF-Ausgabe. Die Vorbereitung dauert länger und benötigt freien Speicherplatz; sie ist für Experimente gedacht, nicht als Standardversion.
>
> Diese Ausgabe enthält außerdem den **editierbaren FFmpeg-Befehl** für Video-, Audio-, GOP- und MPEG-TS-Experimente. Beim Bearbeiten müssen `INPUT`, der abschließende Platzhalter `OUTPUT` und das Ausgabeformat `mpegts` erhalten bleiben.
>
> Lade [das Offline-I/Q-Installer-ZIP](https://github.com/vanhoteen/ONE-SEG-Studio-for-Linux/releases/download/offline-iq-test-0.1/ONE-SEG-Studio-offline-iq-preview7-Ubuntu26-amd64.zip) herunter, entpacke es, wechsle nach `linux-ubuntu26-amd64`, führe `sha256sum -c SHA256SUMS` und danach `bash INSTALL.sh` aus. Die installierte normale Anwendung wird vorübergehend ersetzt und erscheint als ONE SEG Studio im Anwendungsmenü; installiere danach die normale Version erneut, wenn du zurückwechseln möchtest.

## Grenzen und Verantwortung

Die Linux-Oberfläche ist auf Spanisch und Englisch verfügbar. Kameraeingang und integrierte Signalanzeige fehlen; unterbrechungslose Wiederholung ist nicht garantiert. Keine Normzertifizierung. Vor dem Senden örtliche Frequenz-, Leistungs- und Genehmigungsvorschriften prüfen. Eine japanische Kanalnummer ist keine örtliche Sendegenehmigung. Schädliche Störungen vermeiden; der Nutzer ist für Genehmigungen und Betrieb verantwortlich. Soweit gesetzlich zulässig, übernimmt der Autor keine Verantwortung für unbefugten Betrieb oder vom Nutzer verursachte Störungen.

Weitere Angaben: [englische Anleitung](README.md), [Build-Anleitung](linux/README.md), [Lizenzen](LICENSE-NOTICE.md).

## Demo · One-Seg

[![One-Seg demo](https://img.youtube.com/vi/hW7jU8Ro0uk/hqdefault.jpg)](https://youtu.be/hW7jU8Ro0uk)

[macOS project](https://github.com/vanhoteen/ONE-SEG-Studio-)
