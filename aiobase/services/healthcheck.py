from typing import Any

from aiobase.integrations.healthcheck import CheckerResult, HealthcheckResponse
from aiobase.services.redis import RedisRepository


async def check_redis(response: HealthcheckResponse, redis: RedisRepository) -> None:
    try:
        redis_response: Any = await redis.client.ping()
        response.results.append(
            CheckerResult(
                name="redis",
                ok=True,
                message=str(redis_response),
            ),
        )
    except Exception as error:
        response.results.append(
            CheckerResult(
                name="redis",
                ok=False,
                message=str(error),
            ),
        )
