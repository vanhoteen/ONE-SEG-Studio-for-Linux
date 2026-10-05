# ONE SEG Studio for Linux

## 🌐 Choose your language

### [🇬🇧 English](README.md)
### [🇪🇸 Castellano](README.es.md)
### [<img src="Assets/flag-asturias.svg" width="32" alt="Asturias"> Asturianu](README.ast.md)
### [🇩🇪 Deutsch](README.de.md)
### [<img src="Assets/flag-catalunya.svg" width="32" alt="Catalunya"> Català](README.ca.md)

---

<img src="Assets/app-icon.png" width="180" alt="ONE SEG Studio">

> **EXPERIMENTAL TEST BUILD — Ubuntu 26.04 LTS · amd64 (Intel/AMD 64-bit). Not a stable release.**

Created by **vanhoteen**, ONE SEG Studio prepares video and generates a Japanese One-Seg television signal using a HackRF One. In the usual Japanese ISDB-T configuration, the central one of thirteen segments carries a lower-resolution service for portable receivers, without Internet reception.

## Interface

ONE SEG Studio for Linux includes a **Spanish and English** interface. The language selector changes the complete application interface, including preparation, HackRF detection, transmission controls and status messages.

![ONE SEG Studio for Linux — Spanish interface](Assets/linux-preview-current.jpg)

## What has been tested?

The author successfully compiled and installed this Linux preview on Ubuntu 26.04 amd64 and confirmed reception on a Sony XDV-D500. The preparation test also passed H.264 320×240 video, AAC audio and TS packet-alignment checks, reporting zero continuity errors. This is a successful user test, not certification of compliance or a guarantee for every receiver.

## Download and installation

[Open Releases — installer downloads](https://github.com/vanhoteen/ONE-SEG-Studio-for-Linux/releases)

Download [**ONE-SEG-Studio-Linux-preview6-Ubuntu26-amd64.zip** from release 0.3](https://github.com/vanhoteen/ONE-SEG-Studio-for-Linux/releases/download/0.3/ONE-SEG-Studio-Linux-preview6-Ubuntu26-amd64.zip). GitHub's automatic **Source code** archives are for building, not the ready-to-install package.

Download and extract the **complete installer folder**. Keep both `.deb` packages, `INSTALL.sh`, `UBUNTU_VERSION` and `SHA256SUMS` together. Open a terminal in that folder and run:

```bash
bash INSTALL.sh
```

Enter your administrator password and wait. The installer verifies the packages and installs ONE SEG Studio, TSDuck and the required Ubuntu dependencies, including GNU Radio, FFmpeg, Python and HackRF support. **Internet is required; no compilation is needed on the destination computer.** Existing dependencies are reused. The small download is not a self-contained runtime like the Mac DMG.

## Low-resource computer edition — Offline I/Q test

> **Optional separate test release.** If the normal Linux version gives intermittent video, black frames or no signal on a low-power computer, try the [Offline I/Q test release](https://github.com/vanhoteen/ONE-SEG-Studio-for-Linux/releases/tag/offline-iq-test-0.1). It renders the complete I/Q file **before** opening the HackRF. Transmit then plays that prepared file, reducing real-time CPU work and avoiding modulation pauses during RF output. Preparation takes longer and needs free disk space; it is intended for experiments, not as the default release.
>
> This edition also keeps the **editable FFmpeg command** for video, audio, GOP and MPEG-TS experiments. Keep `INPUT`, the final `OUTPUT` placeholder and the `mpegts` output format when editing.
>
> Download [the Offline I/Q installer ZIP](https://github.com/vanhoteen/ONE-SEG-Studio-for-Linux/releases/download/offline-iq-test-0.1/ONE-SEG-Studio-offline-iq-preview7-Ubuntu26-amd64.zip), extract it, enter `linux-ubuntu26-amd64`, run `sha256sum -c SHA256SUMS`, then run `bash INSTALL.sh`. It temporarily replaces the installed normal application and appears as ONE SEG Studio in Applications; reinstall the normal release afterwards if you want to return to it.

## Experimental encoder controls and logs

The Linux preview shows the complete **editable FFmpeg command** for receiver experiments. Its known-working baseline is `320×240`, `15 fps`, H.264 Baseline level 1.2, `-g 15 -bf 0 -refs 1`, repeat headers, AAC 24 kHz / 48 kb/s and the One-Seg transport settings. The user may modify video, audio, GOP and TS encoder arguments before preparation. `INPUT` and the final `OUTPUT` placeholder must remain; the output format must remain `mpegts`. Each operation also writes a log in `~/.local/share/one-seg-studio/logs/`.

Open **ONE SEG Studio** from the desktop applications menu. A graphical desktop is required; a plain SSH terminal will not display the window.

## First use

1. Connect HackRF by USB.
2. Click **Check tools**, then **Detect HackRF**.
3. Select a video, channel, bitrate and gain.
4. Click **Prepare video** and wait.
5. **Transmit** starts RF; **Stop** ends it. Installation, checking tools and preparation do not start transmission.

Video: 320×240 at 15 fps. Bitrates: 80, 100, 200 or 300 kb/s; AAC audio at 48 kb/s. The RF amplifier starts enabled and VGA gain defaults to 47 dB. Changing settings requires preparing the video again.

## Preview limitations

Spanish and English Linux interface. Other distributions and architectures are unverified. Files are finite tests; seamless looping is not guaranteed. Camera/capture inputs and the integrated waveform display are not implemented. A legacy log message may mention a graph although this Linux interface has none. SI tables use a dated file snapshot. Work files live in `~/.local/share/one-seg-studio` by default.

## RF responsibility

Check your country's frequency, power and licensing requirements before transmitting. A Japanese channel number does not authorize use of that frequency elsewhere. Use an appropriate conducted or shielded setup where needed and avoid harmful interference. The user is responsible for authorization, configuration and operation. This educational project does not grant permission to transmit. To the extent allowed by law, the author assumes no responsibility for unauthorized operation or interference caused by the user.

## Build from source

On the target Ubuntu machine, run `bash linux/build-deb.sh --install-deps`. This builds gr-isdbt against that machine's Python and GNU Radio, performs a preparation test without RF and produces the installer folder. The builder supports 24.04 and 26.04; **only 26.04 amd64 has been tested by the author**. Packages are specific to the Ubuntu/Python/GNU Radio versions used to build them. See [Linux build notes](linux/README.md) and [licensing](LICENSE-NOTICE.md).

## Demo · One-Seg

[![One-Seg demo](https://img.youtube.com/vi/hW7jU8Ro0uk/hqdefault.jpg)](https://youtu.be/hW7jU8Ro0uk)

[macOS project](https://github.com/vanhoteen/ONE-SEG-Studio-)
