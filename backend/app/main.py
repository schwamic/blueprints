from fastapi import FastAPI
from app.users.controllers import users_controller
from app.health.controllers import health_controller
from app.common.core.settings import settings
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title=settings.PROJECT_NAME,
    root_path=settings.ROOT_PATH_V1
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS.allow_origins,
    allow_credentials=settings.CORS.allow_credentials,
    allow_methods=settings.CORS.allow_methods,
    allow_headers=settings.CORS.allow_headers,
)

app.include_router(health_controller.router)
app.include_router(users_controller.router)
