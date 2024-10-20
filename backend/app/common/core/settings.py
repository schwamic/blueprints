from typing import Literal, List
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Mongo(BaseModel):
    connection_string: str
    database_name: str


class Cors(BaseModel):
    allow_origins: List[str]
    allow_credentials: bool
    allow_methods: List[str]
    allow_headers: List[str]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="BP_",
        env_nested_delimiter="__",
    )

    MONGO: Mongo
    CORS: Cors
    ROOT_PATH_V1: str
    ENVIRONMENT: Literal["local", "staging", "production"]
    PROJECT_NAME: str
    X_SECRET_TOKEN: str


settings = Settings()
