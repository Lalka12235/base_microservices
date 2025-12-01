import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()

@dataclass(frozen=True,slots=True)
class DatabaseSettings:
    APP_CONFIG_DB_URL: str = os.getenv('APP_CONFIG_DB_URL')
    DB_HOST: str = os.getenv('DB_HOST')
    DB_PORT: int = os.getenv('DB_PORT')
    DB_USER: str = os.getenv('DB_USER')
    DB_PASS: str = os.getenv('DB_PASS')
    DB_NAME: str = os.getenv('DB_NAME')

    @property
    def sync_db_url(self) -> str:
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


@dataclass(frozen=True,slots=True)
class Settings:
    db: DatabaseSettings = DatabaseSettings()


settings = Settings()