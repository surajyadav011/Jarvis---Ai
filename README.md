# 🎙️ Jarvis Voice Assistant (Python)

A simple voice-controlled assistant built using Python that can listen to your commands, respond with speech, open websites, and play music.

---

## 🚀 Features

* 🎤 Voice recognition using microphone
* 🔊 Text-to-speech response
* 🌐 Open websites like YouTube, Facebook, Chrome
* 🎵 Play songs from a custom music library
* 🧠 Wake word detection ("Jarvis")

---

## 🛠️ Technologies Used

* **speech_recognition** → for converting voice to text
* **pyttsx3** → for text-to-speech (offline)
* **webbrowser** → to open websites
* **musiclibrary (custom module)** → to store and play songs

---

## 📂 Project Structure

```
├── main.py
├── musiclibrary.py
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```
git clone https://github.com/your-username/jarvis-voice-assistant.git
```

2. Install required libraries:

```
pip install SpeechRecognition pyttsx3 pyaudio
```

> ⚠️ Note: If `pyaudio` gives error, install it using wheel file or:

```
pip install pipwin
pipwin install pyaudio
```

---

## ▶️ How to Run

```
python main.py
```

---

## 🎯 How It Works

1. Program continuously listens through microphone
2. When it detects the wake word **"Jarvis"**
3. It activates and listens for the next command
4. Executes commands like:

   * "Open YouTube"
   * "Open Facebook"
   * "Play [song name]"

---

## 🎵 Example musiclibrary.py

```python
music = {
    "song1": "https://youtube-link",
    "song2": "https://youtube-link"
}
```

---

## 💡 Future Improvements

* Add ChatGPT integration 🤖
* Open system applications (Notepad, VS Code, etc.)
* Add GUI interface
* Add more smart commands

---
k

