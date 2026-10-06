"""Speech recognition service used by SpeechNote."""

from __future__ import annotations

import speech_recognition as sr


class ASRError(Exception):
    """Base exception for ASR-related failures."""


class SpeechRecognizer:
    """Convert recorded speech/audio into text."""

    def __init__(self, language: str = "en-IN") -> None:
        self.language = language
        self.recognizer = sr.Recognizer()

    def transcribe_file(self, audio_path: str) -> str:
        """Transcribe a WAV/AIFF/FLAC audio file using the configured ASR service."""
        try:
            with sr.AudioFile(audio_path) as source:
                audio = self.recognizer.record(source)
        except (OSError, ValueError) as exc:
            raise ASRError("The selected audio file could not be opened.") from exc

        try:
            text = self.recognizer.recognize_google(
                audio, language=self.language
            )
        except sr.UnknownValueError as exc:
            raise ASRError("Speech could not be understood clearly.") from exc
        except sr.RequestError as exc:
            raise ASRError(
                "The speech recognition service is unavailable. "
                "Check your internet connection."
            ) from exc

        return text.strip()
