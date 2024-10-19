from beanie import Document, Indexed
from pydantic import Field, AnyUrl, UUID4, BaseModel, EmailStr
from typing import Annotated
from uuid import uuid4


class TestUser(Document):
    test: str
    
    class Settings:
        keep_nulls = True
        name = "testusers_collection"
  

class User(Document):
    id: Annotated[UUID4, Indexed()] = Field(default_factory=uuid4, alias="_id", serialization_alias="id")
    nickname: str = Field(max_length=20)
    avatar: AnyUrl | None = Field(default=None, max_length=80)

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


class UserBase(BaseModel):
    nickname: str = Field(max_length=20)
    avatar: AnyUrl | None = Field(default=None, max_length=80)


class UserPublic(UserBase):
    id: str


class UserCreate(UserBase):
    email: EmailStr = Field(max_length=30)
