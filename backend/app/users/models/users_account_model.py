from sqlmodel import SQLModel, Field

# Sub-Resource
class UserAccountBase(SQLModel):
    subscription: str = Field(max_length=30)
    subscriptionChangeDate: str = Field(max_length=30)
    email: str = Field(max_length=30)

class UserAccount(UserAccountBase, table=True):
    id: str | None = Field(default=None, primary_key=True)

class UserAccountCreate(UserAccountBase):
    pass
