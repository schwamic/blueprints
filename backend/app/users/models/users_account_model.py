from sqlmodel import SQLModel, Field
from enum import Enum
# from pydantic import EmailStr: currently not supported by SQLModel

class Subscription(str, Enum):
    FREE = "free plan"
    PRO = "pro plan"

# User Sub-Resource
class UserAccountBase(SQLModel):
    subscription: str = Field(default=Subscription.FREE, max_length=30)
    subscriptionChangeDate: str | None = Field(default=None, max_length=30, exclude=True)
    email: str = Field(max_length=30)

class UserAccount(UserAccountBase, table=True):
    userId: str = Field(primary_key=True, foreign_key="user.id", ondelete="CASCADE")

class UserAccountPublic(UserAccountBase):
    userId: str
