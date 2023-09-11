from enum import Enum
import requests
from src.text_generation.config import GPTConfig


class Role(Enum):
    SYSTEM = "system" # The system role is used to give truths to the chatbot
    ASSISTANT = "assistant" # The assistant role is the chatbot itself
    USER = "user" # The user role is used to give input to the chatbot

def chat_with_gpt(prompt):
    # API endpoint (this is a hypothetical endpoint; refer to the official documentation for the exact endpoint)
    endpoint = "https://api.openai.com/v1/chat/completions"
    
    
    # Your API key (make sure to keep it secret)
    api_key = GPTConfig().API_KEY
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    
    history = [
        { "role": Role.USER.value, "content": prompt },
    ]
    
    data = {
        "max_tokens": 150,
        "model": GPTConfig().MODEL_NAME,
        "temperature": 0.9,
        "messages": history,
        
    }
    
    response = requests.post(endpoint, headers=headers, json=data)
    
    if response.status_code == 200:
        response_data = response.json()
        # return response_data["choices"][0]["text"]['content']
        return response_data
    else:
        print("Error:", response.status_code)
        print("Error:", response.json())

        return None

if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    response = chat_with_gpt(prompt)
    if response:
        print("GPT Response:", response)
