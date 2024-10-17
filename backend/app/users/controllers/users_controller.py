from fastapi import APIRouter, HTTPException, Query
from app.users.models.users_model import UserPublic
from app.users.models.users_account_model import UserAccountPublic

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/{userId}", response_model=UserPublic)
async def get_user(userId: str):
    raise {"message": "TODO: Get user"}

@router.get("/", response_model=list[UserPublic])
async def list_users(offset: int = 0, limit: int = Query(default=100, le=100)):
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
@router.get("/{userId}/account", response_model=UserAccountPublic)
async def get_user_account(userId: str):
    raise {"message": "TODO: Get user account"}

@router.patch("/{userId}/account")
async def update_user_account(userId: str):
    raise HTTPException(status_code=405, detail="Method Not Allowed")

@router.post("/{userId}/account")
async def create_user_account():
    raise HTTPException(status_code=403, detail="Forbidden")

@router.delete("/{userId}/account")
async def delete_user_account():
    raise HTTPException(status_code=403, detail="Forbidden")

@router.put("/{userId}/account")
async def replace_user_account():
    raise HTTPException(status_code=403, detail="Forbidden")
