from asgi_lifespan import LifespanManager
from httpx import ASGITransport, AsyncClient
import pytest_asyncio

from app.main import app


@pytest_asyncio.fixture
async def async_client():
    async with LifespanManager(app):
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://localhost:8001"
        ) as ac:
            yield ac
