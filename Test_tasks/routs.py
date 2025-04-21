from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from database import engine, session
from typing import List, Annotated
from auth import get_current_user, get_user
import models
import schemas

# assistance@5dhub.tech
app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await session.close()
    await engine.dispose()


async def get_token(token):
    res = schemas.UserBase(token=token + "GetToken")
    return res


@app.get('/users/', response_model=List[schemas.UserBase], tags=["Users"])
async def get_all_users(current_user: Annotated[schemas.UserBase, Depends(get_current_user)]):
    user = await current_user
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Available only to users with the administrator role")
    query = (select(models.User).
             options(selectinload(models.User.account)))
    response = await session.execute(query)
    res = response.scalars().all()
    return res


@app.get('/accounts/', response_model=List[schemas.AccountBase], tags=["Accounts"])
async def get_all_accounts():
    response = await session.execute(select(models.Account))
    return response.scalars().all()

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = await get_user(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = user_dict
    hashed_password = form_data.password
    print(hashed_password)
    if not hashed_password == user.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": user.email, "token_type": "bearer"}
#
#
@app.get("/users/me")
async def read_users_me(current_user: Annotated[schemas.UserBase, Depends(get_current_user)]):
    return await current_user
