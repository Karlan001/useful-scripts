from sqlalchemy import select
from sqlalchemy.orm import selectinload
from starlette import status
from models import User
from schemas import UserBase
from fastapi.security import OAuth2PasswordBearer
from database import session
from typing import Annotated
from fastapi import Depends, HTTPException

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_user(email: str):
    query = (select(User).where(User.email == email).
             options(selectinload(User.account)))
    response = await session.execute(query)
    res = response.scalars().all()
    result = [UserBase.model_validate(row, from_attributes=True) for row in res]
    for user in result:
        return user


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = get_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(
        current_user: Annotated[User, Depends(get_current_user)],
):
    return current_user
