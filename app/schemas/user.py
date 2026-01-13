from __future__ import annotations

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.models.enums import Role
from app.schemas.common import ResponseEnvelope


class TaskPostRequest(BaseModel):
    """Schema for creating a task via POST /tasks.

    Fields:
    - username (public API name; stored internally as full_name)
    - email
    - password
    - roles (option)

    Extra fields are ignored to keep the payload strict but flexible.
    """

    model_config = ConfigDict(extra="ignore")

    username: str = Field(..., description="Public display name")
    email: EmailStr
    password: str
    roles: list[Role] | None = Field(default=None)


class TaskRead(BaseModel):
    """Shape of a user returned by the API (no password)."""

    id: str = Field(serialization_alias="id")
    username: str = Field(..., description="Public display name")
    email: EmailStr
    roles: list[Role]


class TaskPostResponse(ResponseEnvelope[TaskRead]):
    """Envelope wrapping the created task."""
