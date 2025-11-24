from datetime import datetime
from typing import ClassVar

from pydantic import Field
from pymongo import ASCENDING, IndexModel

from app.models.base import BaseDoc


class Task(BaseDoc):
    task_id: int
    project_id: int
    assigned_to: str
    description: str | None = Field(..., alias="description")
    status: str | None =Field("assigned", "pending", "complete", alias="status")
    created_at: datetime= Field("%Y-%m-%d %H:%M:%S", alias="createdAt")
    updated_at: datetime = Field("%Y-%m-%d %H:%M:%S", alias="updatedAt")
    is_active: bool = Field(False, alias="is_active")

    class Settings:
        name: ClassVar[str] = "task"
        indexes: ClassVar[list[IndexModel]] = [IndexModel([("createdAt", ASCENDING)])]
