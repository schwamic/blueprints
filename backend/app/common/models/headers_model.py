from pydantic import BaseModel

class CommonHeaders(BaseModel):
    # model_config = {"extra": "forbid"}
    x_secret_token: str
