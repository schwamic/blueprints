from fastapi import APIRouter, HTTPException
from ..models.users_model import User

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/{userId}", response_model=User)
async def get_user(userId: str):
    raise {"message": "TODO: Get user"}

@router.get("/")
async def list_users():
    raise HTTPException(status_code=405, detail="Method Not Allowed")

@router.post("/")
async def create_user():
    return {"message": "TODO: Create user"}

@router.patch("/{userId}")
async def update_user(userId: str):
    raise HTTPException(status_code=405, detail="Method Not Allowed")

@router.delete("/{userId}")
async def delete_user(userId: str):
    raise HTTPException(status_code=405, detail="Method Not Allowed")

@router.put("/{userId}")
async def replace_user(userId: str):
    raise HTTPException(status_code=405, detail="Method Not Allowed")

# Sub Resource: User Account
@router.get("/{userId}/account")
async def get_user_account(userId: str):
    raise {"message": "TODO: Get user account"}

@router.patch("/{userId}/account")
async def update_user_account(userId: str):
    raise {"message": "TODO: Update user account"}

@router.post("/{userId}/account")
async def create_user_account():
    raise HTTPException(status_code=403, detail="Forbidden")

@router.delete("/{userId}/account")
async def delete_user_account():
    raise HTTPException(status_code=403, detail="Forbidden")

@router.put("/{userId}/account")
async def replace_user_account():
    raise HTTPException(status_code=403, detail="Forbidden")
