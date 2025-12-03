from typing import ClassVar

from beanie import Link
from pydantic import Field
from pymongo import ASCENDING, IndexModel

from app.models.base import BaseDoc
from app.models.user import User


class Project(BaseDoc):
    project_id: int
    name: str = Field(..., alias="name")
    description: str | None = Field(defualt=None, alias="description")
    owner: Link[User] = Field(..., alias="ownerId")

    class Settings:
        name: ClassVar[str] = "projects"
        indexes: ClassVar[list[IndexModel]] = [IndexModel([("createdAt", ASCENDING)])]
