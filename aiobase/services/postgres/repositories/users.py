from typing import Any, Optional, cast

from sqlalchemy import select
from sqlalchemy.sql.functions import count

from aiobase.models.sql import User
from aiobase.services.postgres.repositories.base import BaseRepository


# noinspection PyTypeChecker
class UsersRepository(BaseRepository):
    async def get(self, user_id: int) -> Optional[User]:
        return await self._get(User, User.user_id == user_id)

    async def update(self, user_id: int, **data: Any) -> Optional[User]:
        return await self._update(
            model=User,
            conditions=[User.user_id == user_id],
            load_result=True,
            **data,
        )

    async def count(self) -> int:
        return cast(int, await self.session.scalar(select(count(User.user_id))))
