"""Render prepared One-Seg transport to finite HackRF CS8 I/Q. Never starts RF."""
from pathlib import Path
import os
import sys

RATE = 8_000_000


def main():
    directory = Path(sys.argv[1]).resolve()
    sys.path.insert(0, str(directory))
    from studio_iq import studio_iq

    output = directory / 'oneseg.cs8'
    output.unlink(missing_ok=True)
    print('Generando I/Q local. El HackRF permanece apagado.', flush=True)
    tb = studio_iq()
    try:
        tb.start()
        tb.wait()
    finally:
        tb.cs8_file_sink.close()
    if not output.is_file() or output.stat().st_size == 0:
        raise RuntimeError('La renderización I/Q no produjo ningún dato.')
    seconds = output.stat().st_size / (RATE * 2)
    print(f'I/Q preparado: {output.stat().st_size / 1e6:.1f} MB · {seconds:.2f} s · CS8 a 8 MS/s.', flush=True)
    print('Preparación terminada. RF detenida.', flush=True)


if __name__ == '__main__':
    main()
