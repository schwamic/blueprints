from uuid import UUID

from fastapi import HTTPException

from app.users.models.users_account_model import UserAccount
from app.users.models.users_model import User, UserCreate, UserUpdate


class UsersService:
    async def get_user(self, user_id: str) -> User:
        user = await User.get(user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    async def create_user(self, user_create: UserCreate) -> User:
        user_account = await UserAccount.find_one(
            UserAccount.email == user_create.email
        )
        if user_account is not None:
            raise HTTPException(
                status_code=400, detail="User with this email already exists"
            )
        user = User(nickname=user_create.nickname)
        await user.insert()
        user_account = UserAccount(userId=user.id, email=user_create.email)
        await user_account.insert()
        return user

    async def update_user(self, user_id: str, user: UserUpdate) -> User:
        current_user = await User.get(user_id)
        if current_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        update_data = user.model_dump(exclude_unset=True)
        updated_user = await current_user.set(update_data)
        return updated_user

    async def get_user_account(self, user_id: str) -> UserAccount:
        user_account = await UserAccount.find_one(UserAccount.userId == UUID(user_id))
        if user_account is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user_account


users_service = UsersService()
