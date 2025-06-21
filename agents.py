import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Hugging Face token from environment
HF_TOKEN = os.getenv("HF_API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

def query_hf(prompt):
    response = requests.post(
        API_URL,
        headers=headers,
        json={
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 500,
                "do_sample": True,
                "temperature": 0.7
            }
        }
    )
    result = response.json()
    if isinstance(result, list):
        return result[0]['generated_text']
    else:
        raise Exception(f"API Error: {result}")

def spin_chapter(text):
    print("🌀 Rewriting chapter with HuggingFace...")
    prompt = f"Rewrite the following chapter in better English, improving flow and readability:\n\n{text}"
    return query_hf(prompt)

def review_chapter(text):
    print("🔍 Reviewing rewritten chapter...")
    prompt = f"Act as an editor. Polish this chapter further:\n\n{text}"
    return query_hf(prompt)
