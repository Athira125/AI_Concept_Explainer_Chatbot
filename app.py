import streamlit as st
import requests

st.title("AI Concept Explainer")

question = st.text_input("Ask a question")

if st.button("Explain"):
    prompt = f"""
    Explain the following concept in simple terms.
    Give:
    1. Definition
    2. Real-life example
    3. Simple code example

    Question: {question}
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )

    answer = response.json()["response"]

    st.write(answer)