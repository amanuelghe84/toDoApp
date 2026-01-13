from __future__ import annotations

from pydantic import BaseModel, Field

from app.schemas.common import ResponseEnvelope, Status


class TaskPostRequest(BaseModel):
    """Schema for creating a task via POST /tasks."""
    project_id: str = Field(serialization_alias="projectId")
    description: str
    assigned_to: str = Field(validation_alias="assignedTo")
    status: Status = Field(default=Status.success/)

class TaskRead(BaseModel):
    """Schema or getting a task record via GET"""
    id: str = Field(serialization_alias="id")
    project_id: str = Field(serialization_alias="projectId")
    description: str
    assigned_to: str
    status: Status = Field(default=Status.success)



class TaskPostResponse(ResponseEnvelope[TaskRead]):
    """Envelope wrapping the created task."""
