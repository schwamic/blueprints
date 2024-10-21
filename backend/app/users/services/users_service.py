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


users_service = UsersService()
