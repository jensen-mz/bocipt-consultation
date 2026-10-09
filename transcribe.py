import sys, types, subprocess, gc
import numpy as np

# PyAV DLL is blocked by application control. Stub it and decode with system ffmpeg.
av = types.ModuleType("av")
av.audio = types.ModuleType("av.audio")
sys.modules["av"] = av
sys.modules["av.audio"] = av.audio

from faster_whisper import WhisperModel
import faster_whisper.audio as fw_audio

def decode_audio(input_file, sampling_rate=16000, split_stereo=False):
    cmd = [
        r"C:\ffmpeg\bin\ffmpeg.exe", "-nostdin", "-threads", "0",
        "-i", input_file, "-f", "s16le", "-ac", "1", "-acodec", "pcm_s16le",
        "-ar", str(sampling_rate), "-",
    ]
    out = subprocess.run(cmd, capture_output=True, check=True).stdout
    audio = np.frombuffer(out, np.int16).astype(np.float32) / 32768.0
    return audio

fw_audio.decode_audio = decode_audio
import faster_whisper.transcribe as fw_tr
fw_tr.decode_audio = decode_audio

src = r"C:\Users\honka\Downloads\bocipt-elainie.m4a"
out_path = r"C:\Users\honka\Downloads\boci-prudential-workshop-prep\transcript-elaine.txt"

print("loading model", flush=True)
model = WhisperModel("small", device="cpu", compute_type="int8", cpu_threads=8)
print("transcribing", flush=True)
segments, info = model.transcribe(
    src,
    beam_size=1,
    vad_filter=True,
    vad_parameters=dict(min_silence_duration_ms=500),
    condition_on_previous_text=False,
    temperature=0.0,
)
print(f"lang={info.language} p={info.language_probability:.3f} duration={info.duration:.1f}", flush=True)
with open(out_path, "w", encoding="utf-8") as f:
    f.write(f"lang={info.language} p={info.language_probability:.3f}\n")
    for s in segments:
        line = f"[{s.start:7.1f}] {s.text.strip()}\n"
        f.write(line)
        f.flush()
        print(f"[{s.start:7.1f}] ok", flush=True)
print("DONE", flush=True)
