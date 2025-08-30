from datetime import datetime, timedelta, timezone
from typing import Optional

from jose import jwt, JWTError
from passlib.context import CryptContext

from .config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(subject: str, expires_minutes: Optional[int] = None) -> str:
	expires_delta = timedelta(minutes=expires_minutes or settings.ACCESS_TOKEN_EXPIRE_MINUTES)
	expire = datetime.now(tz=timezone.utc) + expires_delta
	to_encode = {"sub": subject, "exp": expire}
	return jwt.encode(to_encode, settings.SECRET_KEY, algorithm="HS256")


def verify_password(plain_password: str, password_hash: str) -> bool:
	return pwd_context.verify(plain_password, password_hash)


def hash_password(plain_password: str) -> str:
	return pwd_context.hash(plain_password)


def decode_token(token: str) -> Optional[str]:
	try:
		payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
		return payload.get("sub")
	except JWTError:
		return None
