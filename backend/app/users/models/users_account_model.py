from datetime import datetime
from enum import Enum
from typing import Annotated

from beanie import Document, Indexed
from pydantic import UUID4, ConfigDict, EmailStr, Field, Strict


class Subscription(str, Enum):
    FREE = "free plan"
    PRO = "pro plan"


# User Sub-Resource
class UserAccount(Document):
    userId: Annotated[UUID4, Indexed(unique=True), Strict(False)]
    subscription: Subscription = Field(default=Subscription.FREE, max_length=30)
    subscriptionChangeDate: datetime = Field(default=datetime.now())
    email: Annotated[EmailStr, Indexed(unique=True)] = Field(max_length=30)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "userId": "012225b2-54b2-4220-91bf-f6ce2e0faedb",
                "subscription": "free plan",
                "subscriptionChangeDate": "2032-04-23T10:20:30.400+02:30",
                "email": "schwamic@mail.me",
            }
        }
    )

    class Settings:
        keep_nulls = True
        name = "usersaccounts_collection"
