from app.users.models.users_model import User, UserCreate, UserPublic
from app.users.models.users_account_model import UserAccount


class UsersService:
    async def get_user(self, userId: str) -> User | None:
        print('userId', userId)
        return await User.get(userId)
    
    async def create_user(self, user_create: UserCreate) -> UserPublic:
        user = User(nickname=user_create.nickname)
        await user.insert()
        user_account = UserAccount(user_id=user.id, email=user.email)
        await user_account.insert()
        return user


users_service = UsersService()
