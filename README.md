
# 🤖 Jarvis - Your Personal AI Assistant

**Jarvis** is a voice-controlled AI assistant built in Python that performs a wide range of tasks like answering questions, opening applications, automating workflows, and even generating code. It uses **Google's Gemini model** for natural language understanding and smart response generation.

---

## 🚀 Features

- 🎤 Voice command recognition using `SpeechRecognition`
- 🔊 Text-to-speech output using `pyttsx3`
- 🌐 Answers general queries using **Gemini (Google AI)**
- 🧾 Opens apps, sends emails, searches the web
- 🧠 Generates and explains code snippets via LLM
- 📁 Automates file and system operations (e.g., shutdown, open folders)
- 🛠️ Easily extendable for custom commands

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Libraries Used:**  
  - `speech_recognition`  
  - `pyttsx3`  
  - `google.generativeai` (Gemini API)  
  - `os`, `datetime`, `webbrowser`, `wikipedia`, `smtplib`  
  - `dotenv` (for secure API key management)

---

## 🔐 Gemini API Integration

This project uses the **Gemini API (Google Generative AI)**. You’ll need to:

1. Get an API key from: [https://makersuite.google.com/app](https://makersuite.google.com/app)
2. Store it in a `.env` file like this:

```
GEMINI_API_KEY=your-api-key-here
```

3. Load the key in your script using:

```python
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
```

---

## 🎥 Demo

*Coming soon — add a GIF or screen recording here!*

---

## 🧪 How to Run

1. Clone the repo  
   ```bash
   git clone https://github.com/yourusername/Jarvis.git
   cd Jarvis
   ```
2. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your `.env` file with Gemini API key  
4. Run the assistant  
   ```bash
   python jarvis.py
   ```

---

## 📂 Folder Structure

```
Jarvis/
├── jarvis.py
├── .env
├── requirements.txt
├── README.md
└── assets/ (optional)
```

---

## 🌱 Future Enhancements

- GUI using `Tkinter` or `PyQt`  
- Multilingual voice commands  
- Contextual conversation memory  
- IoT integration  

---

## 🤝 Contributing

Pull requests are welcome! Feel free to fork the repo, create a feature branch, and send a PR.

---



