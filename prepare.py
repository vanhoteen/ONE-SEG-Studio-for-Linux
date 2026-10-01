"""Prepare an isolated, finite One-Seg file test. Never starts RF."""
from pathlib import Path
import sys, subprocess, shutil, os, shlex, json
app_root = Path(__file__).resolve().parent
root = app_root/'Payload'
stage = Path(os.environ['ONESEG_DATA'])
work = stage/'work/oneseg'
out = stage/'outputs'
work.mkdir(parents=True, exist_ok=True); out.mkdir(exist_ok=True)
source, channel, gain = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
source = str(Path(source).resolve())
bitrate = int(sys.argv[4]) if len(sys.argv) > 4 else 80
if bitrate not in (80, 100, 200, 300):
    raise ValueError('Bitrate no admitido')
amplifier_arg = sys.argv[5] if len(sys.argv) > 5 else '0'
if amplifier_arg not in ('0', '1'):
    raise ValueError('Amplificador no válido')
amplifier = amplifier_arg == '1'

def default_command(rate):
    peak_rate = max(100, rate)
    return (
        "ffmpeg -y -hide_banner -loglevel warning -i INPUT -map 0:v:0 -map '0:a:0?' "
        "-vf 'scale=320:240:force_original_aspect_ratio=decrease,pad=320:240:(ow-iw)/2:(oh-ih)/2,setsar=1' "
        f"-r 15 -c:v libx264 -profile:v baseline -level:v 1.2 -pix_fmt yuv420p -b:v {rate}k "
        f"-maxrate:v {peak_rate}k -bufsize:v {peak_rate}k -g 15 -bf 0 -refs 1 "
        "-x264-params 'repeat-headers=1:aud=1:scenecut=0:force-cfr=1' "
        "-c:a aac -ar 24000 -ac 2 -b:a 48k -mpegts_service_id 1544 "
        "-mpegts_pmt_start_pid 4096 -streamid 0:256 -streamid 1:257 -muxrate 440563 -f mpegts OUTPUT"
    )

raw_command = sys.argv[6] if len(sys.argv) > 6 else default_command(bitrate)
tokens = shlex.split(raw_command)
if tokens[:1] == ['ffmpeg']:
    tokens = tokens[1:]
if tokens.count('INPUT') != 1 or tokens.count('OUTPUT') != 1 or tokens[-1:] != ['OUTPUT']:
    raise ValueError('FFmpeg command must contain INPUT once and end with OUTPUT')
if '-f' not in tokens or tokens[tokens.index('-f') + 1:tokens.index('-f') + 2] != ['mpegts']:
    raise ValueError('FFmpeg command must keep -f mpegts before OUTPUT')
ffmpeg_args = ['ffmpeg'] + [source if token == 'INPUT' else str(work/'base_440563.ts') if token == 'OUTPUT' else token for token in tokens]
# Preserve the known-working 80/100 profile; other profiles cap at their target.
peak = max(100, bitrate)
print(f'Vídeo {bitrate} kb/s; máximo {peak} kb/s; audio 48 kb/s', flush=True)
print('Editable FFmpeg command selected by user.', flush=True)
assert 13 <= channel <= 62 and 0 <= gain <= 47
def run(args): subprocess.run(args, cwd=stage, check=True)
for name in ['correct_transport.py','build_si_trial.py','pat.bin','pmt.bin','sdt.bin','sdt.xml','nit.bin']:
    shutil.copy2(root/'work/oneseg'/name, work/name)
shutil.copy2(root/'outputs/layer_b_oneseg.ts',out/'layer_b_oneseg.ts')
freq = 473142857.142857 + (channel-13)*6000000
nit = (root/'work/oneseg/nit.xml').read_text().replace('515142858',str(round(freq)))
(work/'nit.xml').write_text(nit)
run(['tstabcomp','--japan',str(work/'nit.xml'),'-o',str(work/'nit.bin')])
print('FFmpeg command: ' + ' '.join(shlex.quote(arg) for arg in ffmpeg_args), flush=True)
run(ffmpeg_args)
run([sys.executable,str(work/'correct_transport.py')])
run([sys.executable,str(work/'build_si_trial.py')])
# Match the browser renderer: fill the final partial frame with null TS packets
# and add four frames to flush the ISDB-T interleavers before RF playback.
layer_a = out/'layer_a_si_prueba.ts'
layer_a_iq = out/'layer_a_iq.ts'
packet_size, frame_packets = 188, 64
source_bytes = layer_a.read_bytes()
if not source_bytes or len(source_bytes) % packet_size:
    raise RuntimeError('La capa A no está alineada a paquetes MPEG-TS de 188 bytes.')
frame_bytes = packet_size * frame_packets
frames = (len(source_bytes) + frame_bytes - 1) // frame_bytes + 4
null_packet = bytes([0x47, 0x1f, 0xff, 0x10]) + bytes([0xff]) * 184
padding_packets = (frames * frame_bytes - len(source_bytes)) // packet_size
layer_a_iq.write_bytes(source_bytes + null_packet * padding_packets)

iq_path = out/'oneseg.cs8'
template = (root/'studio_iq.py.template').read_text()
for key, value in {
    '__FREQUENCY__': repr(freq), '__GAIN__': repr(gain), '__AMPLIFIER__': repr(amplifier),
    '__LAYER_A__': repr(str(layer_a_iq)), '__LAYER_B__': repr(str(out/'layer_b_si_prueba.ts')),
    '__IQ_FILE__': repr(str(iq_path)),
    # Mode 3 has 204 OFDM symbols per frame and 8,704 samples/symbol with 1/16 guard.
    '__EXPECTED_SAMPLES__': repr(frames * 204 * (8192 + 512)),
}.items():
    template = template.replace(key, value)
compile(template, 'studio_iq.py', 'exec')
(out/'studio_iq.py').write_text(template)
print(f'Renderizando {frames} tramas ISDB-T a I/Q local. El HackRF permanece apagado.', flush=True)
run([sys.executable, str(app_root/'render_iq.py'), str(out)])
manifest = {
    'format': 'CS8', 'sample_rate': 8_000_000, 'frequency_hz': round(freq),
    'vga_gain': gain, 'amplifier': amplifier, 'iq_file': iq_path.name,
    'frames': frames, 'duration_seconds': iq_path.stat().st_size / 16_000_000,
}
(out/'oneseg-iq.json').write_text(json.dumps(manifest, indent=2) + '\n')
print('IQ_PROGRESS 100', flush=True)
print('Señal I/Q preparada. RF detenida.', flush=True)
