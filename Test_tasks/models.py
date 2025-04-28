from sqlalchemy import Integer, String, ForeignKey, Float
from sqlalchemy.orm import DeclarativeBase, relationship, backref
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import List

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str]
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str]
    is_admin: Mapped[bool]
    account: Mapped[List["Account"] | None] = relationship("Account", backref="user", lazy='noload')


class Account(Base):
    __tablename__ = 'account'
    id: Mapped[int] = mapped_column(primary_key=True)
    balance: Mapped[float] = mapped_column(nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))




class Payment(Base):
    __tablename__ = "payments"
    id: Mapped[int] = mapped_column(primary_key=True)
    sum_payment: Mapped[float] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    account_id: Mapped[int] = mapped_column(ForeignKey("account.id"), nullable=False)
