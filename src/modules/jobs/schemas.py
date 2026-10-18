from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field , field_validator

class JobStatus(str,Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    
class JobCreate(BaseModel):
   title: str = Field(min_length=3, max_length=100)
   description: str | None = Field(default=None,max_length=500, description="The description of the job")
   
class JobUpdate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str | None = Field(default=None,max_length=500, description="The description of the job")
    status:JobStatus | None = None
    
    @field_validator("title","status")
    @classmethod
    def cannot_be_null(cls, v):
        if v is None:
            raise ValueError("Field cannot be null")
        return v
    
class JobResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: JobStatus
    created_at: datetime