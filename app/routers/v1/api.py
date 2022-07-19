from fastapi import APIRouter

from .users import api_router as users_api_router

api_router = APIRouter(prefix="/v1")
api_router.include_router(users_api_router)
