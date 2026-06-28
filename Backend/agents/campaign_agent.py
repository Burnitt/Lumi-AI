"""
Campaign Agent
Uses OpenAI to generate ad campaign plans based on business goals.
This is the core brain of Lumi AI Phase 1.
"""

import os
from openai import AsyncOpenAI

SYSTEM_PROMPT = """
You are Lumi, an expert AI marketing strategist for small businesses.
Given a business's context, goals, and tone, generate a detailed,
actionable ad campaign plan. Include:
- 3 campaign concepts
- Platform recommendations (Meta, Google, TikTok, etc.)
- Ad copy for each concept
- Suggested posting schedule
- KPIs to track

Be specific, practical, and tailored to small business constraints (limited budget, small team).
"""


class CampaignAgent:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    async def create(self, context: dict) -> dict:
        user_message = f"""
Business: {context['business_name']}
Industry: {context['industry']}
Goals: {context['goals']}
Tone: {context['tone']}

Generate a full campaign plan.
        """

        response = await self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message},
            ],
            temperature=0.7,
        )

        return {
            "plan": response.choices[0].message.content,
            "model": response.model,
            "tokens_used": response.usage.total_tokens,
        }
