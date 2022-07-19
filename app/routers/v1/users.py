from fastapi import APIRouter, Depends

from ...auth import get_current_user
from ...schemas import User

api_router = APIRouter()


@api_router.get("/user", response_model=User)
def get_user(current_user: User = Depends(get_current_user)):
    return current_user
