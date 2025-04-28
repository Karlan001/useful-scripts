from pydantic import BaseModel, ConfigDict, Field, model_validator, field_validator
from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from database import session, engine
from models import User


class UserBase(BaseModel):
    # model_config = ConfigDict(arbitrary_types_allowed=True)
    id: int
    name: str | None = None
    email: str | None = None
    password: str | None = None
    is_admin: bool | None = None
    account: List["AccountBase"] | None = []

    class Config:
        orm_model = True
        arbitrary_types_allowed = True


class AccountBase(BaseModel):
    balance: float
    user_id: int

    # class Config:
    #     orm_model = True
    #     arbitrary_types_allowed = True


class PaymentBase(BaseModel):
    id: int
    sum_payment: float
    user_id: int
    account_id: int

    class Config:
        orm_model = True


class AccountBaseOut(AccountBase):
    id: int

    class Config:
        orm_model = True
        arbitrary_types_allowed = True

class UserBaseIn(BaseModel):
    # model_config = ConfigDict(arbitrary_types_allowed=True)
    name: str
    email: str
    password: str
    is_admin: bool

    class Config:
        orm_model = True


class UserBasePut(BaseModel):
    # model_config = ConfigDict(arbitrary_types_allowed=True)
    id: int
    name: str | None = None
    email: str | None = None
    password: str | None = None
    is_admin: bool | None = None
    account: List["AccountBase"] | None = []





