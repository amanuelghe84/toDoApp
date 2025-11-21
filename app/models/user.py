from datetime import datetime
from typing import ClassVar

from pymongo import ASCENDING, IndexModel

from app.models.base import BaseDoc
from app.models.enums import Role


class User(BaseDoc):
    user_id: int
    full_name: str
    email: str
    password: str
    roles: Role
    created_at: datetime
    updated_at: datetime
    is_active: bool

    class Settings:
        name: ClassVar[str] = "user"
        indexes: ClassVar[list[IndexModel]] = [IndexModel([("createdAt", ASCENDING)])]
