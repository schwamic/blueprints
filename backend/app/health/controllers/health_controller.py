from fastapi import APIRouter, Depends, HTTPException

from app.common.dependencies.check_token_header import check_token_header
from app.health.models.health_model import HealthLivePublic
from app.health.services.health_services import HealthService

router = APIRouter(
    prefix="/health",
    tags=["health"],
    dependencies=[Depends(check_token_header)],
)


@router.post(":live", response_model=HealthLivePublic)
async def check_health_live():
    healthService = HealthService()
    return healthService.isLive()


@router.get("/")
async def get_health():
    raise HTTPException(status_code=405, detail="Method Not Allowed")


@router.post("/")
async def create_health():
    raise HTTPException(status_code=405, detail="Method Not Allowed")


@router.patch("/")
async def update_health():
    raise HTTPException(status_code=405, detail="Method Not Allowed")


@router.delete("/")
async def delete_health():
    raise HTTPException(status_code=405, detail="Method Not Allowed")


@router.put("/")
async def replace_health():
    raise HTTPException(status_code=405, detail="Method Not Allowed")
