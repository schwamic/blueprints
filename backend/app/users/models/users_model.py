from beanie import Document
from pydantic import BaseModel, EmailStr
from pydantic import Field, AnyUrl
from uuid import UUID, uuid4


class BaseUser(BaseModel):
    nickname: str | None = Field(default=None, max_length=20)
    avatar: AnyUrl | None = Field(default=None, max_length=80)

class User(Document, BaseUser):
    id: UUID = Field(default_factory=uuid4)
    
    class Settings:
        keep_nulls = True
        name = "users_collection"

    class Config:
            schema_extra = {
                "example": {
                    "id": "123456789",
                    "nickname": "schwamic",
                    "avatar": "https://avatar.me/schwamic.jpg",
                }
            }


class CreateUser(BaseUser):
    email: EmailStr = Field(max_length=30)