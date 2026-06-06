# Chatbot

A simple AI chatbot built in Python using the Groq API and Llama models.

## Features

- Conversational AI chatbot powered by Groq (Llama 3.1)
- Conversation memory during runtime
- Customizable system prompt/personality
- Secure API key storage using a `.env` file
- Exit command to close the chatbot
- Real-time text-to-speech responses

---

## Text-to-Speech

The chatbot uses the Windows Speech API via `pywin32` to convert AI responses into speech.

- Reliable continuous speech output on Windows
- Replaces earlier `pyttsx3` implementation due to stability issues
- Speaks every AI response in real time

---

## Requirements

- Python 3.10+
- Groq API key
- `groq`, `python-dotenv`, `pywin32`

