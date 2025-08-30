import os
from pathlib import Path
from dotenv import load_dotenv


ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
if ENV_PATH.exists():
	load_dotenv(ENV_PATH)


class Settings:
	SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret-change-me")
	ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))
	DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+pysqlite:///./apsmikro.db")
	API_PREFIX: str = "/api"


settings = Settings()
