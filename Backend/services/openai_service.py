"""
OpenAI Service
Centralizes the OpenAI client so all agents share one instance.
Also good place to add retries, logging, and cost tracking later.
"""

import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()


_client: AsyncOpenAI | None = None


def get_openai_client() -> AsyncOpenAI:
    global _client
    if _client is None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise EnvironmentError("OPENAI_API_KEY not set in environment.")
        _client = AsyncOpenAI(api_key=api_key)
    return _client
