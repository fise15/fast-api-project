import asyncio
import pytest

from app.main import engine, Base


@pytest.fixture(scope="session", autouse=True)
def create_test_db():
    async def create():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    asyncio.run(create())
