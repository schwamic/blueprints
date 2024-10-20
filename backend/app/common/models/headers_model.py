from pydantic import BaseModel, Field


class CommonHeaders(BaseModel):
    x_secret_token: str | None = Field(default=None)
