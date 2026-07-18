from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from config import GEMINI_MODEL

load_dotenv()

def get_llm():

    return ChatGoogleGenerativeAI(
        model=GEMINI_MODEL
    )