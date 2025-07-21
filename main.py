import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

# Streamlit UI
st.set_page_config(page_title="🎉 Happy Birthday, Shurem!", page_icon="🎂")
st.title("🎉 Happy Birthday, Syed Shurem Ali!")
st.markdown("Let's celebrate with AI-generated wishes and surprises! 🎁")

# Section 1 – Gemini Birthday Wish
if st.button("🎈 Get Your Birthday Wish"):
    with st.spinner("Generating your wish..."):
        response = model.generate_content("Write a fun, friendly, heartfelt birthday wish for Syed Shurem Ali")
        st.success(response.text)

# Section 2 – Surprise Message
if st.button("🎁 Tap for a Secret Surprise"):
    with st.spinner("Generating your surprise..."):
        surprise = model.generate_content("Tell a fun birthday quote and one line of inspiring advice for the coming year")
        st.balloons()
        st.info(surprise.text)
