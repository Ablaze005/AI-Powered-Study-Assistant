import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Read API key but do not raise on import; app handles missing keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME", "gemini-flash-latest")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(GEMINI_MODEL_NAME)
else:
    model = None


def is_api_key_loaded():
    return bool(GEMINI_API_KEY)


def get_model_info():
    return {
        "api_key_loaded": bool(GEMINI_API_KEY),
        "model_name": GEMINI_MODEL_NAME,
    }


def _generate_text(prompt):
    if model is None:
        raise RuntimeError(
            "GEMINI_API_KEY is not set. Add it to .env or set it in your environment."
        )

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"LLM generation failed: {e}"


def generate_summary(text):
    prompt = f"""
    You are an AI study assistant. Summarize the following text in a clear,
    simple, student-friendly way. Keep the key points, remove unnecessary details.

    Text to summarize:
    {text}
    """
    return _generate_text(prompt)


def generate_quiz(text, num_questions=5):
    prompt = f"""
    You are an AI study assistant. Create {num_questions} multiple-choice quiz questions
    based on the following text. Each question must have:

    - 1 correct answer
    - 3 incorrect options
    - A clear explanation for the correct answer

    Format the output like this:

    Q1: question text
    A) option
    B) option
    C) option
    D) option
    Correct Answer: A
    Explanation: ...

    Text to use:
    {text}
    """
    return _generate_text(prompt)


def generate_flashcards(text):
    prompt = f"""
    Create flashcards from the following text.
    Return them as a list of Q&A pairs.
    Each flashcard should have:
    - A short question
    - A short answer
    - No numbering
    - No extra explanation

    Text:
    {text}
    """

    response_text = _generate_text(prompt)
    if response_text.startswith("LLM generation failed:"):
        return [{"question": "Error", "answer": response_text}]

    lines = response_text.split("\n")
    flashcards = []
    current_q = None
    current_a = None

    for line in lines:
        line = line.strip()
        if line.lower().startswith("q:"):
            if current_q and current_a:
                flashcards.append({"question": current_q, "answer": current_a})
            current_q = line[2:].strip()
            current_a = None
        elif line.lower().startswith("a:"):
            current_a = line[2:].strip()

    if current_q and current_a:
        flashcards.append({"question": current_q, "answer": current_a})

    if not flashcards and response_text.strip():
        return [{"question": "Flashcards", "answer": response_text.strip()}]

    return flashcards


def explain_like_5(text):
    prompt = f"""
    Explain the following text in very simple language,
    as if you are talking to a 5-year-old.
    Keep it short, friendly, and easy to understand.
    No complex words. No technical terms.

    Text:
    {text}
    """
    return _generate_text(prompt).strip()


def extract_key_points(text):
    prompt = f"""
    Extract the key points from the following text.
    Return them as simple bullet points.
    No numbering.
    No long explanations.
    Only the most important points.

    Text:
    {text}
    """

    response_text = _generate_text(prompt)
    if response_text.startswith("LLM generation failed:"):
        return [response_text]

    lines = response_text.split("\n")
    points = []
    for line in lines:
        line = line.strip()
        if line.startswith("-") or line.startswith("•"):
            points.append(line.lstrip("-• ").strip())

    if not points and response_text.strip():
        return [response_text.strip()]

    return points
