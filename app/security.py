import logging
from fastapi import Header, HTTPException, Request
from app.config import settings

logger = logging.getLogger(__name__)


def verify_api_key(
    request: Request,
    x_api_key: str = Header(default=None)
):
    request_id = getattr(request.state, "request_id", "unknown")

    if not x_api_key:
        logger.warning(
            f"Missing API key | request_id={request_id}"
        )
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key"
        )

    if x_api_key != settings.API_KEY:
        logger.warning(
            f"Invalid API key attempt | request_id={request_id}"
        )
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key"
        )

    logger.info(
        f"API key verified | request_id={request_id}"
    )

    return True