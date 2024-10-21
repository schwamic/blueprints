from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from app.common.core.settings import settings
from app.users.models.users_account_model import UserAccount
from app.users.models.users_model import User


class MongoClient:
    @staticmethod
    async def openConnection(app: FastAPI):
        app.mongodb_client = AsyncIOMotorClient(
            settings.MONGO.connection_string, uuidRepresentation="standard"
        )
        await init_beanie(
            database=app.mongodb_client[settings.MONGO.database_name],
            document_models=[User, UserAccount],
        )

        # Init test user
        user_id = "012225b2-54b2-4220-91bf-f6ce2e0faedb"
        test_user = await User.get(user_id)
        if test_user is None:
            test_user = User(
                id=user_id,
                nickname="tester",
                avatar=None,
            )
            await test_user.insert()

    @staticmethod
    async def closeConnection(app: FastAPI):
        app.mongodb_client.close()
