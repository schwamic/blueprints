from fastapi import (
    APIRouter, 
    HTTPException
)
from app.health.models.health_model import HealthLivePublic
from app.health.services.health_services import HealthService

router = APIRouter(
    prefix="/health",
    tags=["health"],
)

@router.get("/live}", response_model=HealthLivePublic)
async def get_health_live():
    healthService = HealthService()
    return healthService.isLive()

@router.post("/live")
async def create_health_live():
    raise HTTPException(status_code=405, detail="Method Not Allowed")

@router.patch("/live")
async def update_health_live(userId: str):
    raise HTTPException(status_code=405, detail="Method Not Allowed")

@router.delete("/live")
async def delete_health_live(userId: str):
    raise HTTPException(status_code=405, detail="Method Not Allowed")

@router.put("/live")
async def replace_health_live(userId: str):
    raise HTTPException(status_code=405, detail="Method Not Allowed")
