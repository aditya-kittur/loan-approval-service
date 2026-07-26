from pydantic import BaseModel, ConfigDict


class StatusResponse(BaseModel):
    """Response model for the service status endpoint.

    Attributes:
        service: Name of the service.
        version: Current version string of the service.
        uptime_seconds: Number of seconds the service has been running.
    """

    model_config = ConfigDict(frozen=True)

    service: str
    version: str
    uptime_seconds: float
