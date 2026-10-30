# 🌐 AI-Powered Translation App

An interactive, full-stack translation application that uses advanced natural language processing (NLP) powered by **AI21's Jamba-mini model** to translate English text into multiple languages with preserved tone and context. Built with **Flask (backend)** and a sleek **TailwindCSS + HTML/JS frontend**, this app delivers fast, accurate, and voice-supported translations.

---

## 🚀 Features

- 🔤 Translate English into multiple languages: Urdu, Arabic, Hindi, Spanish, French, German, Farsi, Italian
- 🧠 AI-based tone-aware and context-preserving translations
- 🗣️ Speech synthesis for reading translated text aloud
- 📋 One-click copy to clipboard
- 🎨 Responsive, animated UI with smooth transitions
- 🔐 Secure API key management with `.env` and CORS support

---

## 🛠️ Tech Stack

| Layer      | Technology |
|------------|------------|
| **Frontend** | HTML, JavaScript, TailwindCSS |
| **Backend**  | Python, Flask, Flask-CORS |
| **AI/NLP**   | AI21 Labs (Jamba-mini via `ai21` SDK) |
| **Utilities**| dotenv, Speech Synthesis API, Clipboard API |

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/sarmadumer/Translation-App-With-Ai.git
cd Translation-App-With-Ai

SetUp Backend

### cd server
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt


Make sure to create a .env file inside the server/ directory with your AI21 API key:

AI21_API_KEY=your_api_key_here



Run the Flask Server
bash
Copy
Edit
python app.py


Open Frontend
Simply open the index.html file from the frontend/ or project root in your browser.

🧠 Prompt Logic
The AI prompt is carefully engineered to:

Maintain sentence tone

Translate even single words

Avoid adding extra explanation

Ensure direct and accurate output

📸 UI Preview
(Include screenshots or a short demo video if available)

🤝 Contribution
Contributions are welcome! Open issues or submit a pull request if you find bugs or have feature suggestions.


🙋‍♂️ Authors
Sarmad Umer and mawaz 
🧠 AI Enthusiast | Full Stack Developer | Cybersecurity Learner


🔗 Useful websites / Documentation
AI21 Labs
Flask Documentation
Tailwind CSS
