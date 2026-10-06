# SpeechNote – Mini Project Report

## 1. Introduction

Speech recognition is the process of converting human speech into machine-readable text. It is widely used in transcription systems, voice-controlled applications, accessibility software, customer-service systems, and educational tools.

SpeechNote demonstrates the implementation of an ASR-based application through a web interface.

## 2. Problem Statement

Manual transcription of spoken content can be time-consuming. A simple software system that accepts speech and produces a written transcript can reduce repetitive manual work and make spoken information easier to store, search, and reuse.

## 3. Objectives

1. Accept speech through a microphone or audio file.
2. Convert speech into text.
3. Display the resulting transcript clearly.
4. Provide basic transcript statistics.
5. Identify frequently occurring keywords.
6. Allow the transcript to be copied or downloaded.
7. Validate inputs and handle common errors.
8. Test the application's core modules automatically.

## 4. Methodology

The system is divided into independent modules:

- `recording.py` handles microphone input.
- `asr.py` handles speech recognition.
- `text_processing.py` performs deterministic text processing.
- `main.py` manages web routes and application flow.
- HTML templates provide the user interface.
- pytest tests verify core behaviour.

## 5. Advantages

- Simple user interface
- Clear modular design
- Easy to run locally
- Supports both microphone and file input
- Includes automated testing
- Transcript can be saved for later use

## 6. Challenges

- Background noise can reduce recognition accuracy.
- Different accents and speaking speeds may affect results.
- Network connectivity is required by the selected recognition service.
- Microphone permissions and device configuration can affect recording.

## 7. Conclusion

SpeechNote provides a practical implementation of an Automatic Speech Recognition application. The project combines audio capture, speech-to-text conversion, text processing, web development, validation, and testing in a single application.
