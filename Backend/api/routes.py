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


# ---------- Models ----------

class BusinessContext(BaseModel):
    business_name: str
    industry: str
    goals: str                  # e.g. "increase foot traffic by 20%"
    tone: str = "friendly"      # e.g. "professional", "casual", "bold"


class EmailRequest(BaseModel):
    business_name: str
    subject: str
    purpose: str                # e.g. "promote weekend sale"
    recipient_segment: str = "all customers"


class MediaRequest(BaseModel):
    business_name: str
    campaign_id: str
    style: str = "modern"


# ---------- Endpoints ----------

@router.post("/campaign/create")
async def create_campaign(ctx: BusinessContext):
    """Generate a full ad campaign plan from business context."""
    try:
        result = await campaign_agent.create(ctx.dict())
        return {"success": True, "campaign": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/email/draft")
async def draft_email(req: EmailRequest):
    """Draft a marketing email ready to send via SendGrid."""
    try:
        result = await email_agent.draft(req.dict())
        return {"success": True, "email": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/media/generate")
async def generate_media(req: MediaRequest):
    """Kick off a media generation job (video/image) via AWS."""
    try:
        job_id = await media_agent.enqueue(req.dict())
        return {"success": True, "job_id": job_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/media/status/{job_id}")
async def media_status(job_id: str):
    """Poll the status of a media generation job."""
    try:
        status = await media_agent.get_status(job_id)
        return {"job_id": job_id, "status": status}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
