from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.users.models.users_model import User
from app.users.models.users_account_model import UserAccount
from app.common.core.settings import settings


# TODO
# if env == 'test': prefix db_name ist "test_"

class MongoClient:
    @staticmethod
    async def openConnection(app: FastAPI):
        app.mongodb_client = AsyncIOMotorClient(settings.MONGO.connection_string, uuidRepresentation="standard")
        await init_beanie(database=app.mongodb_client[settings.MONGO.database_name], document_models=[User, UserAccount])

    @staticmethod
    async def closeConnection(app: FastAPI):
        app.mongodb_client.close()
