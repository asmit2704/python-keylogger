# 🔑 Python Keylogger (Ethical Learning Only)

> ⚠️ **Educational Use Only**  
> This project is meant solely for learning how keylogging works in cybersecurity.  
> Running a keylogger on any device without permission is **illegal and unethical**.  
> Use this tool **only on your own machine**.

---

## 📌 Overview

This project is a **simple Python-based keylogger** built for educational purposes.  
It helps you understand how keystroke capturing works internally — a fundamental concept in cybersecurity and ethical hacking.

The project includes:

- 🖥️ A **Keylogger** script that logs keystrokes in real-time  
- 📁 A **logs folder** where keystrokes are saved  
- 📊 An **Analysis script** to show the most frequently pressed keys  

This is a beginner-friendly cybersecurity project to practice:
- Python scripting  
- Event listening  
- File handling  
- Basic data analysis  
- Malware awareness (ethical)

---

## 📂 Folder Structure

learnkey/
├── keylogger.py # Main keylogger script
├── analyze_keys.py # Key frequency analyzer
└── logs/
└── keystrokes.txt # Auto-created log file

yaml
Copy code

---

## 🚀 Getting Started

### 1️⃣ Install the required library

The keylogger uses **pynput** to capture keyboard events.

```bash
pip install pynput
▶️ Running the Keylogger
Start the keylogger:

```bash
Copy code
python keylogger.py
You will see:

vbnet
Copy code
🎯 Keylogger started. Press ESC to stop.
👉 Press ESC anytime to stop the keylogger.

All keystrokes will be saved to:

```bash
Copy code
logs/keystrokes.txt
📊 Analyze Logged Keystrokes
To see which keys you press the most:

```bash
Copy code
python analyze_keys.py
Example output:

perl
Copy code
🔍 Top 10 most used keys:
  e → 54 times
  [SPACE] → 42 times
  a → 33 times
  [Key.enter] → 15 times
This teaches you how data from keyloggers can be interpreted.

🧠 What You Learn From This Project :

How keyloggers work internally

How attacks like credential theft begin

How to detect & defend against keylogging

Python automation

Event-driven programming

Cybersecurity ethics

Perfect for resumes, GitHub portfolios, internships, and MS in Cybersecurity applications.

🔐 Ethical Disclaimer :
This project is intended for:

✔️ Personal learning

✔️ Educational demonstrations

✔️ Understanding malware behavior

✔️ Cybersecurity research mindset

❌ Do NOT use this tool for illegal monitoring.
❌ Do NOT run this on someone else’s device.

Misuse can lead to serious legal action.

🛠️ Tech Stack :

Python 3.x

pynput (keyboard listener)

collections.Counter

File I/O

🧑‍💻 Author :
Asmit
Cybersecurity Enthusiast | Python Developer | Ethical Hacker in Progress

📄 License :
This project is licensed under the MIT License.
You are free to use, modify, and distribute this project for learning purposes.