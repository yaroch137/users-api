import logging
from datetime import timedelta, datetime
from typing import Optional

from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from .dependencies import get_settings
from .schemas import User

JWT_SIGNING_ALGORITHM = "HS256"

logger = logging.getLogger(__name__)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(user: dict, expires_delta: Optional[timedelta] = None):
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode = {"user": user, "exp": expire, "sub": user["user_email"]}
    settings = get_settings()
    return jwt.encode(to_encode, settings.app_jwt_secret, algorithm=JWT_SIGNING_ALGORITHM)


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Not authenticated",
        headers={"WWW-Authenticate": "Bearer"},
    )
    settings = get_settings()
    try:
        payload = jwt.decode(token, settings.app_jwt_secret, algorithms=[JWT_SIGNING_ALGORITHM])
    except JWTError:
        logger.exception("Failed to validate jwt?!")
        raise credentials_exception
    user = User(**payload["user"])
    return user
