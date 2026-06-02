"""
OpenAI Service
Centralizes the OpenAI client so all agents share one instance.
Also good place to add retries, logging, and cost tracking later.
"""

import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()
