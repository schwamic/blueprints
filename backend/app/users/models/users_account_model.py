from sqlmodel import SQLModel, Field
from enum import Enum

class Subscription(str, Enum):
    FREE = "free plan"
    PRO = "pro plan"

# User Sub-Resource
class UserAccountBase(SQLModel):
    subscription: str = Field(default=Subscription.FREE, max_length=30)
    subscriptionChangeDate: str | None = Field(default=None, max_length=30)
    email: str = Field(max_length=30)

# ID has to be the same ID as the User
class UserAccount(UserAccountBase, table=True):
    id: str = Field(primary_key=True)

class UserAccountPublic(UserAccountBase):
    id: str = Field(serialization_alias='userId')
