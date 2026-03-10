# app.py
import streamlit as st
from openai import OpenAI

# --- Initialize OpenAI client ---
client = OpenAI()

# --- Streamlit UI ---
st.title("Investment Research Assistant")
st.markdown("""
This app uses a fine-tuned OpenAI model to analyze SEC 10-K filings.
You can ask for summaries, risks, or strategy comparisons.
""")

# Text input for user's prompt
user_prompt = st.text_area("Enter your investment research prompt:", height=150)

# Button to submit the prompt
if st.button("Get Analysis"):
    if user_prompt.strip() == "":
        st.warning("Please enter a prompt before submitting.")
    else:
        with st.spinner("Generating response..."):
            try:
                response = client.chat.completions.create(
                    model="ft:gpt-3.5-turbo-0125:personal::D8zPtSHE",  # replace with your fine-tuned model ID
                    messages=[
                        {"role": "system", "content": "You are an investment analyst."},
                        {"role": "user", "content": user_prompt}
                    ],
                    max_tokens=500
                )
                # Extract model's answer
                answer = response.choices[0].message.content
                st.subheader("Model Output")
                st.write(answer)
            except Exception as e:
                st.error(f"Error generating response: {e}")
