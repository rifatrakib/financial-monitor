from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_database_session
from .crud import create_new_user, get_user_by_id
from .schemas import User, UserCreate

router = APIRouter(prefix="/auth")


async def get_session():
    try:
        session: AsyncSession = get_database_session()()
        yield session
    finally:
        await session.close()


@router.post("/users/", response_model=User)
async def create_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    user = await create_new_user(session, user)
    return user


@router.get("/users/", response_model=User)
async def read_user(user_id: int, session: AsyncSession = Depends(get_session)):
    user = await get_user_by_id(session, user_id)
    return user
