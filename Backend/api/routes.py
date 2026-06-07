"""
API Routes
Thin layer: validates input, calls the right agent, returns results.
Add new endpoint groups here as the product grows.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from agents.campaign_agent import CampaignAgent
from agents.email_agent import EmailAgent
from agents.media_agent import MediaAgent

router = APIRouter()

campaign_agent = CampaignAgent()
email_agent = EmailAgent()
media_agent = MediaAgent()
