"""
Utility helpers shared across agents and services.
"""

import re
from datetime import datetime


def slugify(text: str) -> str:
    """Convert a string to a URL-safe slug."""
    text = text.lower().strip()
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"[^\w-]", "", text)
    return text


def timestamp_id(prefix: str = "") -> str:
    """Generate a timestamped ID, e.g. campaign-20240601-143022."""
    ts = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    return f"{prefix}-{ts}" if prefix else ts


def chunk_text(text: str, max_chars: int = 2000) -> list[str]:
    """Split long text into chunks for LLM context management."""
    chunks = []
    while len(text) > max_chars:
        split_at = text.rfind(" ", 0, max_chars)
        if split_at == -1:
            split_at = max_chars
        chunks.append(text[:split_at].strip())
        text = text[split_at:].strip()
    if text:
        chunks.append(text)
    return chunks
