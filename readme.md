# Data Science Tutor Application

This is a Streamlit application that uses Google's Generative AI to provide answers to data science-related questions. The AI model is configured to act as a helpful data science tutor.

## Features

- User-friendly interface to input queries.
- Generates detailed answers to data science-related questions.
- Politely declines to answer questions outside the scope of data science.

## Installation

1. Clone the repository:
    ```sh
    git clone (https://github.com/AkashChoudharyPNC/Data-Science-Tutor-App-.git)
    cd your-repo-name
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Navigate to the directory containing [app.py](http://_vscodecontentref_/0):
    ```sh
    cd streamlit_tutor_app
    ```

2. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

3. Open your web browser and go to `http://localhost:8501` to access the application.

## Configuration

- Replace the placeholder API key in [app.py](http://_vscodecontentref_/1) with your valid Google Generative AI API key:
    ```python
    genai.configure(api_key="YOUR_VALID_API_KEY")
    ```

## File Structure

Data-Science-Tutor-App/ │ ├── app.py # Main application file
                        ├── requirements.txt # List of required packages 
                        └── venv/ # Virtual environment directory