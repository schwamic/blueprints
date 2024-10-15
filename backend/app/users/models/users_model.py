from sqlmodel import SQLModel, Field
from pydantic import AnyUrl
import uuid

class UserBase(SQLModel):
    nickname: str | None = Field(default=None, max_length=20)
    avatar: str | None = Field(default=None, max_length=80)

class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

class UserPublic(UserBase):
    id: uuid.UUID
    avatar: AnyUrl
