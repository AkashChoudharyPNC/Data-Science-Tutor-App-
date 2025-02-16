import streamlit as st
import google.generativeai as genai

# Configure the API key
genai.configure(api_key=st.secrets("api_key"))  # Replace with your valid API key

# System prompt for AI model
system_prompt = """You are an advanced AI code reviewer powered by Google Gemini, designed to analyze code, detect bugs, and provide solutions with detailed explanations. Your goal is to:
Identify Bugs: Analyze the given code for logical, syntax, performance, and security issues.
Report Issues: Clearly describe each detected bug with its cause and potential impact.
Provide Solutions: Suggest an optimized fix for each issue and explain why your solution works.
Explain the Code: Offer a concise breakdown of what the code does and its intended functionality.
Maintain Clarity & Precision: Responses should be direct, easy to understand, and include code snippets if necessary.
If the code is correct, confirm its correctness and suggest any best practices or optimizations. Always ensure that solutions align with industry standards and best coding practices"""

# Initialize the AI model
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp", system_instruction=system_prompt)

# Streamlit UI
st.title("🤖 Ai Code Reviewer")

# User input field
user_prompt = st.text_area("Enter your query:", placeholder="Type your query here...")

# Button to generate response
if st.button("Generate Answer"):
    if user_prompt.strip():
        response = model.generate_content(user_prompt)
        st.write(response.text)  # Ensure correct output handling
    else:
        st.warning("Please enter a question before clicking the button.")
