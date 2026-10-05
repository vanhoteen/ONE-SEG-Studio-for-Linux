# ONE SEG Studio for Linux

## 🌐 Escueyi la to llingua

### [🇬🇧 English](README.md)
### [🇪🇸 Castellano](README.es.md)
### [<img src="Assets/flag-asturias.svg" width="32" alt="Asturias"> Asturianu](README.ast.md)
### [🇩🇪 Deutsch](README.de.md)
### [<img src="Assets/flag-catalunya.svg" width="32" alt="Catalunya"> Català](README.ca.md)

---

<img src="Assets/app-icon.png" width="180" alt="ONE SEG Studio">

> **VERSIÓN EXPERIMENTAL DE PRUEBES — Ubuntu 26.04 LTS · amd64 (Intel/AMD de 64 bits). Nun ye una versión estable.**

Proyeutu de **vanhoteen** pa preparar vídeos y xenerar una señal xaponesa One-Seg con HackRF One. Na configuración habitual, el segmentu central de los trece d'ISDB-T lleva televisión pa pequeños receptores, ensin Internet.

L'autor probó la instalación y la recepción nuna Sony XDV-D500 con Ubuntu 26.04 amd64. Otres distribuciones y arquitectures nun tán verificaes.

## Instalación

Descarga [**ONE-SEG-Studio-Linux-preview6-Ubuntu26-amd64.zip de la versión 0.3**](https://github.com/vanhoteen/ONE-SEG-Studio-for-Linux---Ubuntu-26.04-amd64-Preview/releases/download/0.3/ONE-SEG-Studio-Linux-preview6-Ubuntu26-amd64.zip). Los archivos automáticos **Source code** nun son l'instalador.

Descarga y descomprime la carpeta completa. Caltién xuntos los dos `.deb`, `INSTALL.sh`, `UBUNTU_VERSION` y `SHA256SUMS`. Abre una terminal nella y executa:

```bash
bash INSTALL.sh
```

Necesites Internet y contraseña d'alministrador. Instálense la aplicación, TSDuck y les dependencies de Ubuntu; nun fai falta compilar. Abre ONE SEG Studio nel menú d'aplicaciones del escritoriu.

Conecta HackRF, pulsa **Check tools** y **Detect HackRF**, escueyi un vídeo y pulsa **Prepare video**. **Transmit** entama la emisión; **Stop** pá­rala. La instalación y la preparación nun emiten.

## Edición pa ordenadores con pocos recursos — I/Q ensin conexón

> **Versión de pruebes opcional y separada.** Si la versión Linux normal amuesa vídeo intermitente, fotogrames negros o ensin señal nun ordenador poco potente, prueba la [edición I/Q ensin conexón](https://github.com/vanhoteen/ONE-SEG-Studio-for-Linux---Ubuntu-26.04-amd64-Preview/releases/tag/offline-iq-test-0.1). Xenera'l ficheru I/Q completu **enantes** d'abrir el HackRF. Al emitir, HackRF reproduce esi ficheru preparáu, reduciendo'l trabayu de CPU en tiempu real y evitando pauses de modulación na salida RF. La preparación tarda más y necesita espaciu llibre nel discu; ta pensada pa esperimentos, non como versión predeterminada.
>
> Esta edición caltién tamién el **comandu FFmpeg editable** pa esperimentar con vídeo, audiu, GOP y MPEG-TS. Al editalu, caltién `INPUT`, el marcador final `OUTPUT` y el formatu de salida `mpegts`.
>
> Descarga [el ZIP instalador I/Q ensin conexón](https://github.com/vanhoteen/ONE-SEG-Studio-for-Linux---Ubuntu-26.04-amd64-Preview/releases/download/offline-iq-test-0.1/ONE-SEG-Studio-offline-iq-preview7-Ubuntu26-amd64.zip), descomprímilu, entra en `linux-ubuntu26-amd64`, executa `sha256sum -c SHA256SUMS` y depués `bash INSTALL.sh`. Sustitúi temporalmente l'aplicación normal instalada y va apaecer como ONE SEG Studio nel menú d'aplicaciones; reinstala depués la versión normal si quies volver a ella.

## Llendes y responsabilidá

Interfaz disponible en castellanu ya inglés. Nun inclúi cámara nin gráfica integrada; nun garantiza un bucle continuu nin certificación de la norma. Comprueba les frecuencies, potencies y permisos del to país antes d'emitir. Un canal xaponés nun da autorización local. Evita interferencies; l'usuariu ye responsable de los permisos y del usu del equipu. Na midida permitida pola llei, l'autor nun asume responsabilidá por usos non autorizaos o interferencies causaes pol usuariu.

Más detalles na [guía en castellano](README.es.md), les [notes de compilación](linux/README.md) y les [licencies](LICENSE-NOTICE.md).

## Demo · One-Seg

[![One-Seg demo](https://img.youtube.com/vi/hW7jU8Ro0uk/hqdefault.jpg)](https://youtu.be/hW7jU8Ro0uk)

[macOS project](https://github.com/vanhoteen/ONE-SEG-Studio-)
