"""Play a prepared CS8 I/Q file through HackRF. RF starts only here."""
import json
from pathlib import Path
import signal
import subprocess
import sys

child = None


def stop(*_):
    global child
    if child and child.poll() is None:
        child.terminate()


def main():
    global child
    directory = Path(sys.argv[1]).resolve()
    manifest = directory / 'oneseg-iq.json'
    iq = directory / 'oneseg.cs8'
    if not manifest.is_file() or not iq.is_file() or iq.stat().st_size == 0:
        raise RuntimeError('No hay una señal I/Q preparada. Pulsa Preparar vídeo antes de emitir.')
    settings = json.loads(manifest.read_text())
    if settings.get('format') != 'CS8' or settings.get('sample_rate') != 8_000_000:
        raise RuntimeError('La señal preparada no tiene el formato I/Q esperado.')
    args = [
        'hackrf_transfer', '-t', str(iq), '-f', str(settings['frequency_hz']),
        '-s', '8000000', '-x', str(settings['vga_gain']),
        '-a', '1' if settings['amplifier'] else '0',
    ]
    print('Iniciando reproducción I/Q preparada mediante HackRF.', flush=True)
    print(f"Frecuencia: {settings['frequency_hz']} Hz · VGA: {settings['vga_gain']} dB · AMP: {'on' if settings['amplifier'] else 'off'}", flush=True)
    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGINT, stop)
    child = subprocess.Popen(args)
    status = child.wait()
    child = None
    if status:
        raise SystemExit(status)
    print('Reproducción I/Q terminada. RF detenida.', flush=True)


if __name__ == '__main__':
    main()
