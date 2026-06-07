"""
Media Agent
Handles media generation jobs. Currently stubs out the HiggsField / AWS Lambda
integration -- will be wired up in Phase II.
"""

import uuid


class MediaAgent:
    async def enqueue(self, req: dict) -> str:
        """
        TODO!!!! Phase II: Send a job to AWS Lambda / SQS.
        For now, generates a fake job_id so the API contract is in place.
        """
        job_id = str(uuid.uuid4())
        print(f"[MediaAgent] Enqueued job {job_id} for {req['business_name']}")
        # Future: push to SQS / trigger Lambda
        return job_id

    async def get_status(self, job_id: str) -> dict:
        """
        TODO Phase II: Query the job status from DynamoDB or S3.
        """
        return {
            "job_id": job_id,
            "state": "pending",
            "message": "Media generation not yet implemented (Phase II).",
        }
