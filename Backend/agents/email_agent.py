"""
Email Agent
Drafts marketing emails and (later) sends them via SendGrid.
"""

import os
from openai import AsyncOpenAI
# from sendgrid import SendGridAPIClient          # uncomment when ready to send
# from sendgrid.helpers.mail import Mail

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are Lumi, an expert email copywriter for small businesses.
Write engaging, concise marketing emails that feel personal, not spammy.
Always include: a compelling subject line, a short opening hook, 
the core message, a clear call-to-action, and a friendly sign-off.
"""


class EmailAgent:
    async def draft(self, req: dict) -> dict:
        user_message = f"""
Business: {req['business_name']}
Email subject: {req['subject']}
Purpose: {req['purpose']}
Target audience: {req['recipient_segment']}

Write the full email body.
        """

        response = await client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message},
            ],
            temperature=0.6,
        )

        return {
            "subject": req["subject"],
            "body": response.choices[0].message.content,
        }

    async def send(self, to_email: str, subject: str, body: str):
        """
        TODO: Integrate SendGrid when ready.
        sg = SendGridAPIClient(api_key=os.getenv("SENDGRID_API_KEY"))
        message = Mail(from_email=os.getenv("FROM_EMAIL"), to_emails=to_email,
                       subject=subject, plain_text_content=body)
        sg.send(message)
        """
        raise NotImplementedError("SendGrid integration not yet wired up.")

