from fastapi import APIRouter
from datetime import datetime
from app.models.response import HealthResponse

router = APIRouter(prefix="/health", tags=["Health"])

@router.get("/", response_model=HealthResponse)
def health_check():
    return HealthResponse(
        status="ok",
        timestamp=datetime.utcnow().isoformat(),
        message="FastAPI skeleton is up and running "
    )
