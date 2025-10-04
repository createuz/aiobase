from __future__ import annotations

from aiobase.config.env import (
    AppConfig,
    PostgresConfig,
    RedisConfig,
    ServerConfig,
    SQLAlchemyConfig,
)


# noinspection PyArgumentList
def create_app_config() -> AppConfig:
    return AppConfig(
        postgres=PostgresConfig(),
        sql_alchemy=SQLAlchemyConfig(),
        redis=RedisConfig(),
        server=ServerConfig(),
    )
