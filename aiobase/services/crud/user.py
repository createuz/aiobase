from typing import Any, Optional

from aiobase.utils.const import TIME_1M
from aiobase.models.user_dto import UserDto
from aiobase.models.sql import User
from aiobase.services.crud.base import CrudService
from aiobase.services.postgres import SQLSessionContext
from aiobase.services.redis import redis_cache
from aiobase.utils.key_builder import build_key


class UserService(CrudService):
    async def clear_cache(self, user_id: int) -> None:
        cache_key: str = build_key("cache", "get_user", user_id=user_id)
        await self.redis.delete(cache_key)

    async def create(
            self,
            user_id,
            username,
            first_name
    ) -> UserDto:
        db_user: User = User(
            user_id=user_id,
            username=username,
            first_name=first_name,
        )

        async with SQLSessionContext(session_pool=self.session_pool) as (repository, uow):
            await uow.commit(db_user)

        await self.clear_cache(user_id=user_id)
        return db_user.dto()

    @redis_cache(prefix="get_user", ttl=TIME_1M)
    async def get(self, user_id: int) -> Optional[UserDto]:
        async with SQLSessionContext(session_pool=self.session_pool) as (repository, uow):
            user = await repository.users.get(user_id=user_id)
            if user is None:
                return None
            return user.dto()

    async def count(self) -> int:
        async with SQLSessionContext(session_pool=self.session_pool) as (repository, uow):
            return await repository.users.count()

    async def update(self, user: UserDto, **data: Any) -> Optional[UserDto]:
        async with SQLSessionContext(session_pool=self.session_pool) as (repository, uow):
            for key, value in data.items():
                setattr(user, key, value)
            await self.clear_cache(user_id=user.user_id)
            user_db = await repository.users.update(user_id=user.user_id, **user.model_state)
            if user_db is None:
                return None
            return user_db.dto()
