from fastapi import APIRouter, status

api_router = APIRouter(prefix="/healthz")


@api_router.get("", status_code=status.HTTP_204_NO_CONTENT)
def get_health():
    pass
