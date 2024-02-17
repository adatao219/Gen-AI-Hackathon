# /kani/config.py

from kani.engines.openai import OpenAIEngine
from kani import Kani

from dotenv import load_dotenv
import os

load_dotenv()  # loads the environment variables from .env
GPT_API_KEY = os.getenv("GPT_API_KEY")


def create_kani_engine(api_key: str = GPT_API_KEY, model: str = "gpt-4"):
    """
    Initialize and return a Kani engine configured with OpenAI GPT.
    """
    engine = OpenAIEngine(api_key, model=model)
    return Kani(engine)
