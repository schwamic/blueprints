from fastapi import APIRouter, HTTPException, Query
from pydantic import UUID4

from app.users.models.users_account_model import UserAccount
from app.users.models.users_model import User, UserCreate, UserUpdate
from app.users.services.users_service import users_service


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/{user_id}", response_model=User)
async def get_user(user_id: UUID4):
    user = await users_service.get_user(user_id)
    return user


@router.get("/", response_model=list[User])
async def list_users(offset: int = 0, limit: int = Query(default=100, le=100)):
    raise HTTPException(status_code=405, detail="Method Not Allowed")


@router.post("/", response_model=User)
async def create_user(user: UserCreate):
    created_user = await users_service.create_user(user)
    return created_user


@router.patch("/{user_id}", response_model=User)
async def update_user(user_id: str, user: UserUpdate):
    updated_user = await users_service.update_user(user_id, user)
    return updated_user


@router.delete("/{user_id}")
async def delete_user(user_id: str):
    raise HTTPException(status_code=405, detail="Method Not Allowed")


@router.put("/{user_id}")
async def replace_user(user_id: str):
    raise HTTPException(status_code=405, detail="Method Not Allowed")


# Sub Resource: User Account
@router.get("/{user_id}/account/", response_model=UserAccount)
async def get_user_account(user_id: str):
    user_account = await users_service.get_user_account(user_id)
    return user_account


@router.patch("/{user_id}/account/")
async def update_user_account():
    raise HTTPException(status_code=405, detail="Method Not Allowed")


@router.post("/{user_id}/account/")
async def create_user_account():
    raise HTTPException(status_code=403, detail="Forbidden")


@router.delete("/{user_id}/account/")
async def delete_user_account():
    raise HTTPException(status_code=403, detail="Forbidden")


@router.put("/{user_id}/account/")
async def replace_user_account():
    raise HTTPException(status_code=403, detail="Forbidden")
