from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import read_config


def get_database_session():
    url = read_config("rds_uri")
    engine = create_async_engine(url)
    SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    return SessionLocal


async def get_session():
    try:
        session: AsyncSession = get_database_session()()
        yield session
    finally:
        await session.close()


Base = declarative_base()
