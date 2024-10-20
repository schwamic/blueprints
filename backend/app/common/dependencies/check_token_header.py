from typing import Annotated
from fastapi import Header, HTTPException
from app.common.core.settings import settings
from app.common.models.headers_model import CommonHeaders


async def check_token_header(headers: Annotated[CommonHeaders, Header()]):
    if headers.x_secret_token != settings.X_SECRET_TOKEN:
        raise HTTPException(status_code=400, detail="X-Secret-Token invalid")
