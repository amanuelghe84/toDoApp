from pathlib import Path
from typing import Literal

from pydantic import Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

# Resolve repo root (two levels up from this file: app/core/config.py -> app/ -> repo root)
ROOT_DIR = Path(_file_).resolve().parents[2]
ENV_FILE = ROOT_DIR / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(ENV_FILE)
        if ENV_FILE.exists()
        else None,  # <- load .env if it exists, otherwise use env vars
        case_sensitive=False,
        extra="ignore",
        env_ignore_empty=True,  # Ignore empty environment variables
    )
.....

def get_settings()-> Settings:
    
    settings = get_settings()