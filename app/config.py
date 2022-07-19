from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Users API"
    app_jwt_secret: str
