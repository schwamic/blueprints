from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.users.models.users_model import User
from app.users.models.users_account_model import UserAccount
from .settings import settings

async def startup_db_client(app: FastAPI):
    app.mongodb_client = AsyncIOMotorClient(settings.MONGO.connection_string)
    await init_beanie(database=app.mongodb_client.db_name, document_models=[User, UserAccount])

async def shutdown_db_client(app: FastAPI):
    app.mongodb_client.close()
