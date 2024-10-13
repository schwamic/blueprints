from sqlmodel import SQLModel, Field

class AccountBase(SQLModel):
    subscription: str = Field(max_length==30)
    subscriptionChangeDate: str = Field(max_length==30)
    email: str = Field(max_length==30)

class Account(AccountBase, table=True):
    id: str | None = Field(default=None, primary_key=True)

class AccountCreate(AccountBase):
    pass
