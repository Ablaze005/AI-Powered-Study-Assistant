import streamlit as st
import PyPDF2

from llm_utils import (
    extract_key_points,
    explain_like_5,
    generate_flashcards,
    generate_quiz,
    generate_summary,
    is_api_key_loaded,
)

def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def main():
    st.title("AI Study Assistant")
    st.write("Upload text or a PDF, and I will summarize it or create quiz questions.")

    api_key_loaded = is_api_key_loaded()
    if not api_key_loaded:
        st.error(
            "Missing GEMINI_API_KEY. Add it to .env or set it in your environment, then restart Streamlit."
        )

    uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
    text_input = st.text_area("Or paste your text here")

    final_text = ""
    if uploaded_file is not None:
        final_text = extract_text_from_pdf(uploaded_file)
    elif text_input.strip():
        final_text = text_input.strip()

    if not final_text:
        st.info("Please upload a PDF or paste text to enable the actions below.")

    if st.button("Summarize", disabled=not api_key_loaded):
        if final_text:
            summary = generate_summary(final_text)
            if summary.startswith("LLM generation failed:"):
                st.error(summary)
            else:
                st.subheader("Summary")
                st.write(summary)
        else:
            st.warning("Please upload a PDF or enter text.")

    if st.button("Generate Quiz", disabled=not api_key_loaded):
        if final_text:
            quiz = generate_quiz(final_text)
            if quiz.startswith("LLM generation failed:"):
                st.error(quiz)
            else:
                st.subheader("Quiz Questions")
                st.write(quiz)
        else:
            st.warning("Please upload a PDF or enter text.")

    if st.button("Generate Flashcards", disabled=not api_key_loaded):
        if final_text:
            flashcards = generate_flashcards(final_text)
            if len(flashcards) == 1 and flashcards[0].get("question") == "Error":
                st.error(flashcards[0]["answer"])
            else:
                st.subheader("📘 Flashcards")
                for i, card in enumerate(flashcards, start=1):
                    st.markdown(f"**Flashcard {i}**")
                    st.write(f"**Q:** {card['question']}")
                    st.write(f"**A:** {card['answer']}")
                    st.markdown("---")
        else:
            st.warning("Please upload a PDF or enter text.")

    if st.button("Explain Like I'm 5", disabled=not api_key_loaded):
        if final_text:
            simple_text = explain_like_5(final_text)
            if simple_text.startswith("LLM generation failed:"):
                st.error(simple_text)
            else:
                st.subheader("🧸 Explain Like I'm 5")
                st.write(simple_text)
        else:
            st.warning("Please upload a PDF or enter text.")

    if st.button("Extract Key Points", disabled=not api_key_loaded):
        if final_text:
            key_points = extract_key_points(final_text)
            if isinstance(key_points, list) and len(key_points) == 1 and isinstance(key_points[0], str) and key_points[0].startswith("LLM generation failed:"):
                st.error(key_points[0])
            else:
                st.subheader("📌 Key Points")
                st.write(key_points)
        else:
            st.warning("Please upload a PDF or enter text.")


if __name__ == "__main__":
    main()


