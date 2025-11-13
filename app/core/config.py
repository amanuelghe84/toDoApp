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

    app_name: str = Field("ToDo App", alias="APP_NAME")
    app_version: str = Field("0.1.0", alias="APP_VERSION")
    app_description: str = Field(
        "A simple task management application", alias="APP_DESCRIPTION")
    app_debug: bool = Field(True, alias="APP_DEBUG")
    app_host: str = Field("127.0.0.1", alias="APP_HOST")
    app_port: int = Field(8000, alias="APP_PORT")
    app_reload: bool = Field(True, alias="APP_RELOAD")
    app_api_docs_url: str = Field("/docs", alias="APP_API_DOCS_URL")
    app_redoc_url: str = Field("/redoc", alias="APP_REDOC_URL")
    app_scalar_url: str = Field("/scalar", alias="APP_SCALARA_URL")
    app_openapi_url: str = Field("/openapi.json", alias="APP_OPENAPI_URL")

    # Security settings
    security_secret_key: str = Field(
        "secrets.token_bytes(num_bytes=32)", alias="SECURITY_SECRET_KEY"
    )
    security_jwt_algorithm: str = Field("HS256", alias="SECURITY_JWT_ALGORITHM")
    security_access_token_expire_minutes: int = Field(
        30, alias="SECURITY_ACCESS_TOKEN_EXPIRE_MINUTES"
    )

    # Database settings
    database_host: str = Field("localhost", alias="DATABASE_HOST")
    database_port: int = Field(27017, alias="DATABASE_PORT")
    database_name: str = Field("todo_app_db", alias="DATABASE_NAME")
    database_user: str = Field("todo_user", alias="DATABASE_USER")
    database_password: str = Field("change-me-in-production", alias="DATABASE_PASSWORD")
    database_auth_source: str = Field("admin", alias="DATABASE_AUTH_SOURCE")

    # Redis settings
    redis_host: str = Field("localhost", alias="REDIS_HOST")
    redis_port: int = Field(6379, alias="REDIS_PORT")
    redis_password: str | None = Field(None, alias="REDIS_PASSWORD")
    redis_db: int = Field(0, alias="REDIS_DB")
    redis_username: str | None = Field(None, alias="REDIS_USERNAME")
    redis_ssl: bool = Field(False, alias="REDIS_SSL")
    redis_ssl_cert_reqs: str = Field("none", alias="REDIS_SSL_CERT_REQS")
    redis_socket_connect_timeout: int = Field(10, alias="REDIS_SOCKET_CONNECT_TIMEOUT")
    redis_socket_timeout: int = Field(30, alias="REDIS_SOCKET_TIMEOUT")
    redis_connection_pool_max_connections: int = Field(
        100, alias="REDIS_CONNECTION_POOL_MAX_CONNECTIONS"
    )
    redis_decode_responses: bool = Field(True, alias="REDIS_DECODE_RESPONSES")

    # Logger settings
    log_level: Literal[
        "trace", "debug", "info", "warning", "error", "critical"
    ] = Field("debug", alias="LOG_LEVEL")
    log_format: Literal["text", "json", "csv"] = Field("text", alias="LOG_FORMAT")
    log_file: str = Field("/var/log/app.log", alias="LOG_FILE")
    log_retention: str = Field("7d", alias="LOG_RETENTION")
    log_rotation: str = Field("1d", alias="LOG_ROTATION")
    log_date_format: str = Field("%Y-%m-%d %H:%M:%S", alias="LOG_DATE_FORMAT")
    log_handlers_raw: str = Field("console,file", alias="LOG_HANDLERS")



def get_settings() -> Settings:
    return Settings()

settings = get_settings()


