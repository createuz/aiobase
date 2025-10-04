from __future__ import annotations

from typing import TYPE_CHECKING

import uvicorn
from fastapi import FastAPI

if TYPE_CHECKING:
    from aiobase.config import AppConfig


def run_app(app: FastAPI, config: AppConfig) -> None:
    return uvicorn.run(
        app=app,
        host=config.server.host,
        port=config.server.port,
        access_log=False,
    )
