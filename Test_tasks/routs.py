from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy import select, update
from sqlalchemy.orm import joinedload, selectinload
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette.responses import JSONResponse

from database import engine, session
from typing import List, Annotated
from auth import get_current_user, get_user, get_current_active_user
import models
import schemas

# assistance@5dhub.tech
app = FastAPI()
router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await session.close()
    await engine.dispose()


# async def check_role(current_user: Annotated[schemas.UserBase, Depends(get_current_user)]):
#     user = await current_user
#     return user.is_admin


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


@app.get("/users/me")
async def read_users_me(current_user: Annotated[schemas.UserBase, Depends(get_current_user)]):
    return await current_user


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


@app.post('/users/', response_model=schemas.UserBase, tags=["Users"])
async def create_user(current_user: Annotated[schemas.UserBase, Depends(get_current_user)],
                      user_for_create: schemas.UserBaseIn):
    user = await current_user
    if user.is_admin:
        try:
            async with session:
                new_user = models.User(**user_for_create.dict())
                session.add(new_user)
                await session.commit()
            return new_user
        except:
            return JSONResponse({"Error": "Email already used"}, 422)


@app.put('/users/', response_model=schemas.UserBase, tags=["Users"])
async def update_user(current_user: Annotated[schemas.UserBase, Depends(get_current_user)],
                      user_for_update: schemas.UserBasePut):
    user = await current_user
    updated_user = user_for_update.dict().values()
    print(updated_user)
    if user.is_admin:
        try:
            async with session:
                update_user = (update(models.User)
                               .where(models.User.id == user_for_update.id)
                               .values(updated_user))
                await session.commit()
                return update_user
        except:
            return JSONResponse({"Error": "User not found"}, 422)


@app.get('/accounts/', response_model=List[schemas.AccountBaseOut], tags=["Accounts"])
async def get_accounts(current_user: Annotated[schemas.UserBase, Depends(get_current_user)]):
    user = await current_user
    if user.is_admin:
        response = await session.execute(select(models.Account))
        return response.scalars().all()
    response = await session.execute(select(models.Account).where(models.Account.user_id == user.id))
    return response.scalars().all()


@app.post('/accounts/', response_model=schemas.AccountBaseOut, tags=["Create account"])
async def post_accounts(current_user: Annotated[schemas.UserBase, Depends(get_current_active_user)],
                        account: schemas.AccountBase):
    user = await current_user
    if user.is_admin:
        new_account = models.Account(**account.dict())
        session.add(new_account)
        await session.commit()
        return new_account


@app.get('/payments/', response_model=List[schemas.PaymentBase], tags=['Payments'])
async def get_all_payments(current_user: Annotated[schemas.UserBase, Depends(get_current_user)]):
    user = await current_user
    if user.is_admin:
        response = await session.execute(select(models.Payment))
        return response.scalars().all()
    response = await session.execute(select(models.Payment).where(user.id == models.Payment.user_id))
    return response
