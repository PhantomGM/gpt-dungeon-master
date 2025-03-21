import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# add langsmith api to env as LANGSMITH_API_KEY = "your_api_key" on EU server
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY", "no_key")
LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2", "true")
LANGCHAIN_ENDPOINT = "https://eu.api.smith.langchain.com"
LANGCHAIN_PROJECT = "GPT-gm"
print(LANGSMITH_API_KEY)
print(LANGCHAIN_TRACING_V2)

if __name__ == "__main__":
    print(f"[INFO] OPENAI_API_KEY: {OPENAI_API_KEY}")
    if LANGSMITH_API_KEY:
        print(f"[INFO] LANGSMITH_API_KEY: {LANGSMITH_API_KEY}")
