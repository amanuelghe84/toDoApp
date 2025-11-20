
from datetime import datetime

from app.models.base import BaseDoc


class Project(BaseDoc):
    id: int
    name: str
    description: str
    owner_id: str
    created_at: datetime
    updated_at: datetime
    is_active: bool

    class Settings:
        name = "project"
