from typing import Optional

from sqlalchemy import String, Integer, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from aiobase.models.user_dto import UserDto
from aiobase.utils.custom_types import Int64
from .mixins import TimestampMixin
from aiobase.models.base import Base


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[Optional[Int64]] = mapped_column(BigInteger, unique=True, index=True, nullable=False)
    username: Mapped[Optional[str]] = mapped_column(String(length=64), nullable=True)
    first_name: Mapped[Optional[str]] = mapped_column(String(length=100), nullable=True)

    def dto(self) -> UserDto:
        return UserDto.model_validate(self)
