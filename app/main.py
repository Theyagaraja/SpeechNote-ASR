"""SpeechNote web application."""

from __future__ import annotations

import io
import tempfile
from pathlib import Path

from flask import Flask, flash, redirect, render_template, request, send_file, url_for

from .asr import ASRError, SpeechRecognizer
from .recording import RecordingError, record_wav
from .text_processing import extract_keywords, normalize_text, summarize_statistics

BASE_DIR = Path(__file__).resolve().parent.parent

app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates"),
    static_folder=str(BASE_DIR / "static"),
)

app.config["SECRET_KEY"] = "speechnote-local-secret"
app.config["MAX_CONTENT_LENGTH"] = 20 * 1024 * 1024

ALLOWED_EXTENSIONS = {"wav", "aiff", "aif", "flac"}
LANGUAGES = {
    "en-IN": "English (India)",
    "en-US": "English (US)",
    "en-GB": "English (UK)",
}


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.get("/")
def index():
    return render_template("index.html", languages=LANGUAGES)


@app.post("/transcribe-upload")
def transcribe_upload():
    uploaded = request.files.get("audio")
    language = request.form.get("language", "en-IN")

    if not uploaded or not uploaded.filename:
        flash("Please select an audio file.", "error")
        return redirect(url_for("index"))

    if not allowed_file(uploaded.filename):
        flash("Please upload WAV, AIFF, or FLAC audio.", "error")
        return redirect(url_for("index"))

    suffix = Path(uploaded.filename).suffix.lower()
    temp_path = None

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp:
            uploaded.save(temp.name)
            temp_path = temp.name

        text = SpeechRecognizer(language).transcribe_file(temp_path)
        return render_result(text, language)
    except ASRError as exc:
        flash(str(exc), "error")
    finally:
        if temp_path:
            Path(temp_path).unlink(missing_ok=True)

    return redirect(url_for("index"))


@app.post("/record")
def record():
    language = request.form.get("language", "en-IN")
    try:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "recording.wav"
            record_wav(str(path), int(request.form.get("duration", 10)))
            text = SpeechRecognizer(language).transcribe_file(str(path))
        return render_result(text, language)
    except (RecordingError, ASRError, ValueError) as exc:
        flash(str(exc), "error")
        return redirect(url_for("index"))


def render_result(text: str, language: str):
    cleaned = normalize_text(text)
    return render_template(
        "result.html",
        text=cleaned,
        language=LANGUAGES.get(language, language),
        keywords=extract_keywords(cleaned),
        stats=summarize_statistics(cleaned),
    )


@app.post("/download")
def download():
    text = request.form.get("text", "").strip()
    if not text:
        flash("There is no transcript to download.", "error")
        return redirect(url_for("index"))

    data = io.BytesIO(text.encode("utf-8"))
    data.seek(0)
    return send_file(
        data,
        mimetype="text/plain; charset=utf-8",
        as_attachment=True,
        download_name="speechnote_transcript.txt",
    )


@app.errorhandler(413)
def request_too_large(_error):
    flash("The uploaded audio file is too large. Maximum size is 20 MB.", "error")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
