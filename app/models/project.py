
from datetime import datetime
from typing import ClassVar

from pymongo import ASCENDING, IndexModel

from app.models.base import BaseDoc


class Project(BaseDoc):
    project_id: int
    name: str
    description: str
    owner_id: str
    created_at: datetime
    updated_at: datetime
    is_active: bool

    class Settings:
        name: ClassVar[str] = "project"
        indexes: ClassVar[list[IndexModel]] = [IndexModel([("createdAt", ASCENDING)])]
