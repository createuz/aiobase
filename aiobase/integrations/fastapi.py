from fastapi import FastAPI

from aiobase.integrations.endpoints import healthcheck


def setup_fastapi(app: FastAPI) -> FastAPI:
    app.include_router(healthcheck.router)
    app.state.shutdown_completed = False
    return app
