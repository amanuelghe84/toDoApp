from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from app.models.enums import TaskStatus
from app.schemas.common import ResponseEnvelope


class TaskPostRequest(BaseModel):
    """Schema for creating a task via POST /tasks."""
    model_config = ConfigDict(extra="ignore")
    project_id: str = Field(
        ..., validation_alias="projectId", serialization_alias="projectId"
        )
    description: str
    assigned_to: str = Field(validation_alias="assignedTo")
    status: TaskStatus | None = Field(default=None)

class TaskRead(BaseModel):
    """Schema or getting a task record via GET"""
    id: str = Field(serialization_alias="id")
    project_id: str = Field(serialization_alias="projectId")
    description: str
    assigned_to: str | None = Field(default=None, validation_alias="assignedTo", serialization_alias="assignedTo")
    status: TaskStatus




class TaskPostResponse(ResponseEnvelope[TaskRead]):
    """Envelope wrapping the created task."""
