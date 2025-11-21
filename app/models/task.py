from datetime import datetime
from typing import ClassVar

from pymongo import ASCENDING, IndexModel

from app.models.base import BaseDoc


class Task(BaseDoc):
    task_id: int
    project_id: int
    assigned_to: str
    description: str
    status: str
    created_at: datetime
    updated_at: datetime
    is_active: bool

    class Settings:
        name: ClassVar[str] = "task"
        indexes: ClassVar[list[IndexModel]] = [IndexModel([("createdAt", ASCENDING)])]
