markdown
# 🎓 AI-Powered Study Assistant  
A modern, intelligent study companion built with **Streamlit** and **Google Gemini Flash**.  
This app helps students learn faster with **summaries, quizzes, flashcards, ELI5 explanations, and key point extraction** — all in one clean interface.

---

## 🚀 Features

### 📝 1. Smart Summaries  
Turn long paragraphs into short, clear summaries.

### ❓ 2. Auto‑Generated Quizzes  
Creates multiple‑choice questions from your text to test your understanding.

### 🧠 3. Flashcards  
Generates simple Q/A flashcards for revision.

### 🧸 4. Explain Like I’m 5 (ELI5)  
Rewrites complex text into super‑simple language anyone can understand.

### 📌 5. Key Points Extractor  
Pulls out the most important bullet points from any text.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Google Gemini Flash API**
- **dotenv** for environment variables
- **Modular architecture** (`app.py` + `llm_utils.py`)

---

## 📂 Project Structure

AI-Powered-Study-Assistant/
│
├── app.py               # Streamlit UI
├── llm_utils.py         # All AI logic (summaries, quizzes, ELI5, etc.)
├── .env                 # API key (not included in repo)
├── requirements.txt     # Dependencies
└── README.md            # Project documentation

Code

---

## 🔧 Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Ablaze005/AI-Powered-Study-Assistant.git
cd AI-Powered-Study-Assistant
2️⃣ Install dependencies
bash
pip install -r requirements.txt
3️⃣ Add your Gemini API key
Create a .env file:

Code
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL_NAME=gemini-flash-latest
4️⃣ Run the app
bash
streamlit run app.py
🎨 UI/UX Philosophy
This project focuses on:

Clean layout

Minimal buttons

Fast interactions

Readable output

Beginner‑friendly design

A full UI redesign (dark mode, animations, layout improvements) is planned for v2.0.

🧭 Roadmap
✔️ v1.0 — Core Features
Summaries

Quizzes

Flashcards

ELI5

Key Points

🔜 v1.5 — UI/UX Upgrade
Better layout

Icons + colors

Section cards

Improved spacing

🔮 v2.0 — Advanced Features
PDF upload

Chat mode

Save flashcards

Export quizzes

AI tutor mode

🤝 Contributing
Pull requests are welcome!
If you want to improve UI/UX, add features, or fix bugs — feel free to contribute.

📜 License
This project is open‑source under the MIT License.

🌟 Author
Ablaze Pariyar  
International student & aspiring AI developer

Code
