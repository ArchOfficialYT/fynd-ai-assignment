import json
import os
import time
import random
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted

# Configure Gemini
API_KEY = os.getenv("GOOGLE_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("models/gemini-flash-lite-latest")

DATA_FILE = "data.json"


def safe_generate(prompt):
    try:
        return model.generate_content(prompt).text
    except Exception:
        return "Thank you for your feedback. We appreciate you taking the time to share your experience."

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
