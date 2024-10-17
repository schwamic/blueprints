from beanie import Document, Indexed
from pydantic import Field, EmailStr, UUID4
from datetime import datetime
from typing import Annotated
from enum import Enum


class Subscription(str, Enum):
    FREE = "free plan"
    PRO = "pro plan"


# User Sub-Resource
class UserAccount(Document):
    userId: Annotated[UUID4, Indexed(unique=True)]
    subscription: Subscription = Field(default=Subscription.FREE, max_length=30)
    subscriptionChangeDate: datetime | None = Field(default=datetime.now())
    email: EmailStr = Field(max_length=30)
    
    class Settings:
        keep_nulls = True
        name = "usersaccounts_collection"

    class Config:
            schema_extra = {
                "example": {
                    "userId": "123456789",
                    "subscription": "free",
                    "subscriptionChangeDate": "2032-04-23T10:20:30.400+02:30",
                    "email": "schwamic@mail.me",
                }
            }
