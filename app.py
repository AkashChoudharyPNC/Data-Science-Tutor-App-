import streamlit as st
import google.generativeai as genai

# Configure the API key
genai.configure(api_key=st.secrets("api_key"))  # Replace with your valid API key

# System prompt for AI model
system_prompt = """You are a helpful data science tutor. 
Students will ask you doubts related to various topics in data science.
You are expected to reply in as much detail as possible.
If a student asks a question outside the data science scope,
politely decline and ask them to stick to data science topics."""

# Initialize the AI model
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp", system_instruction=system_prompt)

# Streamlit UI
st.title("Data Science Tutor App")

# User input field
user_prompt = st.text_input("Enter your query:", placeholder="Type your query here...")

# Button to generate response
if st.button("Generate Answer"):
    if user_prompt.strip():
        response = model.generate_content(user_prompt)
        st.write(response.text)  # Ensure correct output handling
    else:
        st.warning("Please enter a question before clicking the button.")
