from fastapi import FastAPI

from .dependencies import get_settings
from .routers import healthz
from .routers.v1 import api as v1_api


def create_app():
    settings = get_settings()
    app = FastAPI(title=settings.app_name)

    app.include_router(healthz.api_router)
    app.include_router(v1_api.api_router)

    return app
