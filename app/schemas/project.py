from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from app.schemas.common import ResponseEnvelope


class ProjectPostRequest(BaseModel):
    """Schema for creating a project via POST /project."""
    # CLIENT => SERVER
    model_config = ConfigDict(extra="ignore")
    #ownerId => owner_id
    owner_id: str = Field(
        ..., validation_alias="ownerId", serialization_alias="ownerId"
    )
    name: str
    description: str


class ProjectRead(BaseModel):
    """Schema or getting a project record via GET"""
    #server => Client
    id: str = Field(serialization_alias="id")
    owner_id: str = Field(serialization_alias="owner_id")
    name: str
    description: str

class ProjectPostResponse(ResponseEnvelope[ProjectRead]):
    """Envelope wrapping the created project record. CREATE/UPDATE/DELETE"""
