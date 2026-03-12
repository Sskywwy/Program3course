from typing import Dict
fake_users_db: Dict[int, dict] = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob", "email": "bob@example.com"}

    
}

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

# `settings` lives in the core package, not under `db`.  Importing via a
# relative module path (`.config`) failed when the container tried to
# resolve `app.db.config`, which doesn't exist.  Referencing the absolute
# package path ensures the correct module is used.
from app.core.config import settings

# simple in-memory user dictionary used by API handlers during initial
# development.  This mirrors the earlier commented-out example at the top of
# the file and satisfies imports from `app.api.v1.endpoints.users`.
# TODO: remove once real database logic is implemented.
fake_users_db: dict[int, dict] = {}

engine = create_async_engine(settings.DATABASE_URL_asyncpg, echo=True)

# Створюємо фабрику сесій
async_session_factory = async_sessionmaker(engine, expire_on_commit=False)

# Функція для отримання сесії (Dependency Injection)
async def get_db():
    async with async_session_factory() as session:
        yield session