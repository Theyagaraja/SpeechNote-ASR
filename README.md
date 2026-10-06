# SpeechNote – Speech Recognition & Transcription System

SpeechNote is a Python-based web application that converts spoken audio into text. It provides two input methods: microphone recording and audio-file upload. After transcription, the application presents the transcript together with basic word/sentence statistics and frequently occurring keywords.

The project is designed as an academic implementation of an **Automatic Speech Recognition (ASR) application** with a clean software structure and automated tests.

## Features

- Microphone-based speech recording
- Audio-file transcription
- English (India), English (US), and English (UK) language options
- Speech-to-text conversion
- Transcript normalization
- Word, sentence, and character statistics
- Deterministic keyword extraction based on word frequency
- Copy transcript to clipboard
- Download transcript as `.txt`
- Input validation and user-friendly error handling
- Automated unit and web-route tests

## Technology Stack

| Component | Technology |
|---|---|
| Programming language | Python |
| Web framework | Flask |
| Speech recognition | SpeechRecognition |
| Speech recognition service | Google Web Speech recognition endpoint |
| Microphone capture | sounddevice |
| Testing | pytest |
| Frontend | HTML, CSS, Jinja2 |

## System Flow

```text
Microphone / Audio File
          |
          v
   Audio Input Handler
          |
          v
  Speech Recognition Layer
          |
          v
       Text Output
          |
          v
  Text Processing Module
     /            \
Statistics       Keywords
     \            /
          v
    Web Result Page
```

## Project Structure

```text
SpeechNote_ASR/
├── app/
│   ├── __init__.py
│   ├── asr.py
│   ├── main.py
│   ├── recording.py
│   └── text_processing.py
├── static/
│   └── style.css
├── templates/
│   ├── base.html
│   ├── index.html
│   └── result.html
├── tests/
│   ├── test_text_processing.py
│   └── test_web.py
├── .gitignore
├── requirements.txt
├── run.py
└── README.md
```

## Requirements

- Python 3.10 or later
- Working microphone for live recording
- Internet connection for the speech recognition service
- Windows, macOS, or Linux

## Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd SpeechNote_ASR
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the application

```bash
python run.py
```

Open the local address displayed by Flask, normally:

```text
http://127.0.0.1:5000
```

## How to Use

### Microphone mode

1. Select the language.
2. Enter a recording duration from 1 to 120 seconds.
3. Click **Start Recording**.
4. Speak clearly into the microphone.
5. Wait for transcription.
6. Review, copy, or download the transcript.

### File mode

1. Select the language.
2. Choose a WAV, AIFF, or FLAC file.
3. Click **Transcribe Audio**.
4. Review the generated transcript and statistics.

## Testing

Run all automated tests:

```bash
pytest -q
```

The test suite covers:

- Text normalization
- Word counting
- Sentence counting
- Keyword extraction
- Statistics generation
- Home-page availability
- Missing upload validation

The ASR network call is intentionally not executed during unit tests so that tests remain deterministic and do not depend on internet availability.

## Limitations

- Recognition quality depends on audio quality, pronunciation, background noise, and the selected language.
- The speech recognition service requires an internet connection.
- The application accepts common uncompressed audio formats; it does not directly convert arbitrary media formats such as MP3 or MP4.
- Microphone recording uses the computer's default recording device.
- Keyword extraction is frequency-based and does not use semantic analysis.

## Future Improvements

- Add local/offline ASR support.
- Add more Indian language options.
- Add speaker identification.
- Add audio playback beside the transcript.
- Add persistent transcript history using SQLite.
- Add export to PDF.

## Academic Description

**Title:** SpeechNote – Speech Recognition & Transcription System

**Objective:**  
To design and implement a software system that accepts spoken audio and converts it into written text using an Automatic Speech Recognition interface.

**Outcome:**  
The completed application demonstrates audio input handling, speech recognition, text processing, web application development, validation, and software testing.

## Author

Developed as an academic CSE project.

> Note: This project uses a speech-recognition service through the Python SpeechRecognition library. It does not claim to train or develop a new speech recognition model.
