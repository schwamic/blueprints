from sqlmodel import SQLModel, Field

class UserBase(SQLModel):
    nickname: str = Field(max_length==20)
    avatar: str = Field(max_length==80)

class User(UserBase, table=True):
    id: str | None = Field(default=None, primary_key=True)


class UserCreate(UserBase):
    pass
