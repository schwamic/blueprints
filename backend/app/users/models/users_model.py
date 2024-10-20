from beanie import Document, Indexed
from pydantic import Field, AnyUrl, UUID4, BaseModel, EmailStr, Strict, ConfigDict
from typing import Annotated
from uuid import uuid4


class TestUser(Document):
    test: str
    
    class Settings:
        keep_nulls = True
        name = "testusers_collection"
  

class User(Document):
    id: Annotated[UUID4, Indexed(), Strict(False)] = Field(default_factory=uuid4, alias="_id")
    nickname: str = Field(max_length=20)
    avatar: AnyUrl | None = Field(default=None, max_length=80)
    
    model_config = ConfigDict(
        json_schema_extra = {
                "example": {
                    "id": "012225b2-54b2-4220-91bf-f6ce2e0faedb",
                    "nickname": "schwamic",
                    "avatar": "https://avatar.me/schwamic.jpg",
                }
            }
    )

    class Settings:
        keep_nulls = True
        name = "users_collection"


class UserBase(BaseModel):
    nickname: str = Field(max_length=20)
    avatar: AnyUrl | None = Field(default=None, max_length=80)


class UserCreate(UserBase):
    email: EmailStr = Field(max_length=30)
