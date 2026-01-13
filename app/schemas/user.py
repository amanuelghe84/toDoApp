from __future__ import annotations

from pydantic import BaseModel, Field

from app.models.enums import Role
from app.schemas.common import ResponseEnvelope


class TaskPostRequest(BaseModel):
    """Schema for creating a task via POST /tasks."""
    username: str
    email: str
    password: str
    roles: Role

class TaskRead(BaseModel):
    id: str = Field(serialization_alias="id")
    username: str
    email: str
    roles: Role


class TaskPostResponse(ResponseEnvelope[TaskRead]):
    """Envelope wrapping the created task."""

