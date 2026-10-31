from functools import lru_cache
from pathlib import Path
from pydantic import Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='../.env', extra='ignore')
    database_url: str = 'postgresql+psycopg://ai_dmc:ai_dmc@localhost:5432/ai_dmc'
    jwt_secret: str = Field(min_length=32)
    jwt_expire_minutes: int = Field(default=60, ge=1)
    storage_dir: Path = Path('../storage')
    pipeline_mode: str = 'mock'
    pipeline_import: str = 'pipeline.main:process_document'
    taxonomy_path: Path = Path('../pipeline/config/taxonomy.json')
    confidence_threshold: float = Field(default=0.85, ge=0, le=1)
    cors_origins: str = 'http://localhost:3000'
    app_environment: str = 'development'
    seed_password: str | None = None

    @model_validator(mode='after')
    def validate_mode(self):
        if self.pipeline_mode not in {'mock', 'real'}:
            raise ValueError('PIPELINE_MODE harus mock atau real')
        if self.app_environment == 'production' and self.pipeline_mode == 'mock':
            raise ValueError('Mock tidak diizinkan pada production')
        return self


@lru_cache
def get_settings():
    return Settings()
