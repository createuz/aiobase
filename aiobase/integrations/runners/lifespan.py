from __future__ import annotations

import logging
from typing import Final

from aiobase.services.redis import RedisRepository

logger: Final[logging.Logger] = logging.getLogger(name=__name__)


async def close_sessions(
        redis: RedisRepository,
) -> None:
    await redis.close()
    logger.info("Closed all existing connections")
