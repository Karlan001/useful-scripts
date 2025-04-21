from pydantic import BaseModel, ConfigDict, Field
from typing import List, Optional
from models import User, Account

class UserBase(BaseModel):
    # model_config = ConfigDict(arbitrary_types_allowed=True)
    id: int
    name: str
    email: str
    password: str
    is_admin: bool
    account: list["AccountBase"]

    class Config:
        orm_model = True
        arbitrary_types_allowed = True

class AccountBase(BaseModel):
    id: int
    balance: float
    user_id: int

    class Config:
        orm_model = True
        arbitrary_types_allowed = True

class PaymentBase(BaseModel):
    id: int
    sum_payment: float
    user_id: int
    account_id: int
    class Config:
        orm_model = True