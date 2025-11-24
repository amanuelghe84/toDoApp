from datetime import datetime
from typing import ClassVar

from pydantic import Field
from pymongo import ASCENDING, IndexModel

from app.models.base import BaseDoc
from app.models.enums import Role


class User(BaseDoc):
    user_id: int = Field(..., alias="user_id")
    full_name: str = Field(..., alias="full_name")
    email: str = Field(..., alias="email")
    password: str = Field(..., alias="password")
    roles: Role = Field(..., alias="roles")
    created_at: datetime = Field("%Y-%m-%d %H:%M:%S", alias="createdAt")
    updated_at: datetime = Field("%Y-%m-%d %H:%M:%S", alias="updatedAt")
    is_active: bool = Field(False, alias="is_active")

    class Settings:
        name: ClassVar[str] = "user"
        indexes: ClassVar[list[IndexModel]] = [IndexModel([("createdAt", ASCENDING)])]
