import pytest
import pytest_asyncio
from asgi_lifespan import LifespanManager
from httpx import ASGITransport, AsyncClient

from app.common.core.settings import settings
from app.main import app


@pytest.fixture
def test_user_id():
    return "012225b2-54b2-4220-91bf-f6ce2e0faedb"


@pytest.fixture
def base_url():
    return "http://localhost:8001"


@pytest.fixture
def auth_header():
    return {
        "content-type": "application/json",
        "X-Secret-Token": settings.X_SECRET_TOKEN,
    }


@pytest_asyncio.fixture
async def async_client(base_url):
    async with LifespanManager(app):
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url=base_url
        ) as ac:
            yield ac
