# from typing import Dict
# fake_users_db: Dict[int, dict] = {
#     1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
#     2: {"id": 2, "name": "Bob", "email": "bob@example.com"}

    
# }

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from .config import settings

engine = create_async_engine(settings.DATABASE_URL_asyncpg, echo=True)

# Створюємо фабрику сесій
async_session_factory = async_sessionmaker(engine, expire_on_commit=False)

# Функція для отримання сесії (Dependency Injection)
async def get_db():
    async with async_session_factory() as session:
        yield session