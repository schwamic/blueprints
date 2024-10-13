from fastapi import FastAPI
from .users.controllers import users_controller

app = FastAPI()

app.include_router(users_controller.router)
