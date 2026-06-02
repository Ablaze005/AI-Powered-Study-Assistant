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

## 🛠️ Installation & Setup

Follow these steps to run the AI-Powered Study Assistant on your local machine.

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Ablaze005/AI-Powered-Study-Assistant.git
cd AI-Powered-Study-Assistant

2️⃣ Create a Virtual Environment (optional but recommended)
bash
python -m venv venv
Activate it:

Windows:

bash
venv\Scripts\activate
macOS/Linux:

bash
source venv/bin/activate
3️⃣ Install Dependencies
bash
pip install -r requirements.txt
4️⃣ Add Your Gemini API Key
Create a .env file in the project folder:

Code
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL_NAME=gemini-flash-latest
Make sure your .env file is NOT committed to GitHub.

5️⃣ Run the App
bash
streamlit run app.py
Your browser will open automatically at:

Code
http://localhost:8501
6️⃣ Start Using the App 🎉
You can now:

Summarize text

Generate quizzes

Create flashcards

Get ELI5 explanations

Extract key points

All powered by Gemini Flash.

Code

---

If you want, I can also help you add:

✨ A “Screenshots” section  
✨ A “Demo GIF” section  
✨ A “Tech Stack Badges” section  
✨ A “Contributors” section  
✨ A “Version History” section  

Just tell me what you want next.

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
