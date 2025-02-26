PDF to Speech Converter

Overview

This project converts text from a PDF file into speech using pyttsx3, allowing users to listen to their documents instead of reading them. The script extracts text from each page of the selected PDF and reads it aloud.

Features

Allows users to select a PDF file via a file dialog.
Extracts text from each page of the PDF.
Uses text-to-speech (TTS) to read the extracted text aloud.
Skips empty pages to ensure a smooth reading experience.

Dependencies
Ensure you have the following libraries installed:

pyttsx3 (Text-to-Speech Engine)
PyPDF2 (PDF Text Extraction)
tkinter (For file selection, included with Python)

How It Works

The script prompts the user to select a PDF file.
It opens and reads the selected PDF.
It extracts text from each page and reads it aloud using pyttsx3.
The script prints the page number being read and skips empty pages.

Usage

A file dialog will appear—select the PDF you want to read.
The script will start reading the document page by page.

Future Enhancements

Add a GUI for better user experience.
Implement a pause/play feature.
Allow users to save the audio as an MP3 file.


Author
Akhil Nair

