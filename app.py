import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Predefined FAQ answers
faq_answers = {
    "What is your name?": "I am FAQBot, your helpful assistant.",
    "What can you do?": "I can answer common questions you might have!",
    "Who created you?": "I was created by Vandana Chohan using OpenAI.",
    "How do you work?": "I work by matching your question to a list of known FAQs.",
    "Can you learn new things?": "Not yet! I only answer basic questions for now."
}

# Streamlit UI
st.set_page_config(page_title="FAQ Bot", page_icon="💬")
st.title("💬 FAQ Chatbot")
st.markdown("Select a question from the dropdown menu below:")

# Dropdown for selecting a question
selected_question = st.selectbox("👇 Choose a question:", [""] + list(faq_answers.keys()))

# Display the selected answer
if selected_question:
    answer = faq_answers[selected_question]
    st.success(f"🤖 {answer}")

# Sample FAQs section
with st.expander("📚 View all FAQ options"):
    for q in faq_answers.keys():
        st.write(f"• {q}")
