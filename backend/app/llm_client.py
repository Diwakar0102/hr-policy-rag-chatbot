import os
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load .env file from project root automatically
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

LLM_API_URL = os.getenv("LLM_API_URL")
LLM_API_KEY = os.getenv("LLM_API_KEY")

def call_llm(prompt: str, max_tokens=300):
    if not LLM_API_KEY or not LLM_API_URL:
        raise ValueError("Missing LLM_API_KEY or LLM_API_URL in environment variables")

    headers = {
        "Authorization": f"Bearer {LLM_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mixtral-8x7b-instruct",  # Groq free model
        "messages": [
            {"role": "system", "content": "You are a helpful HR assistant."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": max_tokens,
        "temperature": 0.2
    }

    resp = requests.post(LLM_API_URL, headers=headers, json=payload, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"]
