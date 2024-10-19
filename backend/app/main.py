from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.users.controllers.users_controller import router as users_router
from app.health.controllers.health_controller import router as health_router
from app.common.core.settings import settings
from starlette.middleware.cors import CORSMiddleware
from app.common.clients.mongo_client import MongoClient


@asynccontextmanager
async def lifespan(app: FastAPI):
    await MongoClient.openConnection(app)    
    yield
    await MongoClient.closeConnection(app)


app = FastAPI(
    title=settings.PROJECT_NAME,
    root_path=settings.ROOT_PATH_V1,
    lifespan=lifespan
)


if settings.ENVIRONMENT=='local':
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS.allow_origins,
        allow_credentials=settings.CORS.allow_credentials,
        allow_methods=settings.CORS.allow_methods,
        allow_headers=settings.CORS.allow_headers,
    )


app.include_router(users_router)
app.include_router(health_router)
