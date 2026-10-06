"""Microphone recording helpers."""

from __future__ import annotations

import wave
from pathlib import Path

import sounddevice as sd


class RecordingError(Exception):
    """Raised when microphone recording fails."""


def record_wav(output_path: str, duration: int = 10, sample_rate: int = 16000) -> str:
    """Record mono PCM audio from the default microphone."""
    if duration < 1 or duration > 120:
        raise RecordingError("Recording duration must be between 1 and 120 seconds.")

    try:
        audio = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype="int16",
    device=1,
)
        sd.wait()
    except Exception as exc:
        raise RecordingError(
            "Microphone recording failed. Check microphone permissions and device."
        ) from exc

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with wave.open(str(path), "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(audio.tobytes())

    return str(path)
