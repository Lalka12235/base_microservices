from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import Field
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    """
    Класс настроек приложения, загружающий переменные из окружения.
    Использует Pydantic-Settings для безопасной и удобной работы с конфигурацией.
    """

    # --- Настройки базы данных ---
    DB_HOST: str = Field(..., description="Хост базы данных PostgreSQL")
    DB_PORT: int = Field(..., description="Порт базы данных PostgreSQL")
    DB_USER: str = Field(..., description="Имя пользователя базы данных PostgreSQL")
    DB_PASS: str = Field(..., description="Пароль пользователя базы данных PostgreSQL")
    DB_NAME: str = Field(..., description="Имя базы данных PostgreSQL")

    @property
    def sync_db_url(self):
        return f'postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
    
    @property
    def async_db_url(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
    
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / '.env',
        extra='ignore'
    )



settings = Settings()