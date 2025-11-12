from pathlib import Path
from typing import Literal

from pydantic import Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).resolve().parents[2]
ENV_FILE = ROOT_DIR / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(ENV_FILE)
        if ENV_FILE.exists()
        else None,
        case_sensitive=False,
        extra="ignore",
        env_ignore_empty=True, 
    )

settings: Settings | None = None

def get_settings() -> Settings:
    global settings
    if settings is None:
        settings = Settings.model_validate(
            {}
        )
    return settings


settings = get_settings()
