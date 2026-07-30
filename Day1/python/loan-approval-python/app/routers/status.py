import logging
import time

from fastapi import APIRouter

from app.schemas.status import StatusResponse

logger = logging.getLogger(__name__)

start_time = time.time()

router = APIRouter(prefix="/api", tags=["status"])


@router.get("/status", response_model=StatusResponse)
def get_status() -> StatusResponse:
    """Return current service health and uptime metadata.

    Returns:
        StatusResponse containing service name, version, and uptime in seconds.
    """
    uptime = time.time() - start_time
    logger.info("Status requested, uptime_seconds: %s", uptime)
    return StatusResponse(
        service="loan-approval-service",
        version="1.0.0",
        uptime_seconds=uptime,
    )
