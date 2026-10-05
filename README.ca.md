# ONE SEG Studio for Linux

## 🌐 Tria el teu idioma

### [🇬🇧 English](README.md)
### [🇪🇸 Castellano](README.es.md)
### [<img src="Assets/flag-asturias.svg" width="32" alt="Asturias"> Asturianu](README.ast.md)
### [🇩🇪 Deutsch](README.de.md)
### [<img src="Assets/flag-catalunya.svg" width="32" alt="Catalunya"> Català](README.ca.md)

---

<img src="Assets/app-icon.png" width="180" alt="ONE SEG Studio">

> **VERSIÓ EXPERIMENTAL DE PROVES — Ubuntu 26.04 LTS · amd64 (Intel/AMD de 64 bits). No és una versió estable.**

Projecte de **vanhoteen** per preparar vídeos i generar un senyal japonès One-Seg amb un HackRF One. En la configuració habitual d'ISDB-T, el segment central dels tretze porta televisió de menys resolució per a receptors petits, sense Internet.

L'autor ha provat la instal·lació i la recepció en una Sony XDV-D500 amb Ubuntu 26.04 amd64. Altres distribucions i arquitectures no s'han verificat.

## Instal·lació

Descarrega [**ONE-SEG-Studio-Linux-preview6-Ubuntu26-amd64.zip de la versió 0.3**](https://github.com/vanhoteen/ONE-SEG-Studio-for-Linux---Ubuntu-26.04-amd64-Preview/releases/download/0.3/ONE-SEG-Studio-Linux-preview6-Ubuntu26-amd64.zip). Els fitxers automàtics **Source code** no són l'instal·lador.

Descarrega i descomprimeix la carpeta completa. Mantén junts els dos `.deb`, `INSTALL.sh`, `UBUNTU_VERSION` i `SHA256SUMS`. Obre un terminal dins de la carpeta i executa:

```bash
bash INSTALL.sh
```

Cal Internet i la contrasenya d'administrador. S'instal·len l'aplicació, TSDuck i les dependències d'Ubuntu; no cal compilar a l'ordinador de destinació. Obre ONE SEG Studio des del menú d'aplicacions de l'escriptori Linux.

Connecta el HackRF, prem **Check tools** i **Detect HackRF**, tria un vídeo i prem **Prepare video**. **Transmit** inicia l'emissió; **Stop** l'atura. Instal·lar i preparar no emet.

## Edició per a ordinadors amb pocs recursos — I/Q sense connexió

> **Versió de prova opcional i separada.** Si la versió normal de Linux mostra vídeo intermitent, fotogrames negres o cap senyal en un ordinador poc potent, prova l'[edició I/Q sense connexió](https://github.com/vanhoteen/ONE-SEG-Studio-for-Linux---Ubuntu-26.04-amd64-Preview/releases/tag/offline-iq-test-0.1). Genera el fitxer I/Q complet **abans** d'obrir el HackRF. En emetre, el HackRF reprodueix el fitxer ja preparat, reduint la feina de CPU en temps real i evitant pauses de modulació durant la sortida RF. La preparació triga més i necessita espai lliure al disc; està pensada per experimentar, no com a versió predeterminada.
>
> Aquesta edició també conserva l'**ordre FFmpeg editable** per experimentar amb vídeo, àudio, GOP i MPEG-TS. En editar-la, conserva `INPUT`, el marcador final `OUTPUT` i el format de sortida `mpegts`.
>
> Descarrega [el ZIP instal·lador I/Q sense connexió](https://github.com/vanhoteen/ONE-SEG-Studio-for-Linux---Ubuntu-26.04-amd64-Preview/releases/download/offline-iq-test-0.1/ONE-SEG-Studio-offline-iq-preview7-Ubuntu26-amd64.zip), descomprimeix-lo, entra a `linux-ubuntu26-amd64`, executa `sha256sum -c SHA256SUMS` i després `bash INSTALL.sh`. Substitueix temporalment l'aplicació normal instal·lada i apareixerà com ONE SEG Studio al menú d'aplicacions; reinstal·la després la versió normal si hi vols tornar.

## Limitacions i responsabilitat

Interfície Linux disponible en castellà i anglès. No inclou càmera ni gràfica integrada, i no garanteix un bucle continu ni certificació de la norma. Comprova les freqüències, potències i autoritzacions del teu país abans d'emetre. Un canal japonès no concedeix autorització local. Evita interferències; l'usuari és responsable dels permisos i de l'ús de l'equip. En la mesura permesa per la llei, l'autor no assumeix responsabilitat pels usos no autoritzats o les interferències causades per l'usuari.

Més detalls a la [guia en castellà](README.es.md), les [notes de compilació](linux/README.md) i les [llicències](LICENSE-NOTICE.md).

## Demo · One-Seg

[![One-Seg demo](https://img.youtube.com/vi/hW7jU8Ro0uk/hqdefault.jpg)](https://youtu.be/hW7jU8Ro0uk)

[macOS project](https://github.com/vanhoteen/ONE-SEG-Studio-)
