from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field , field_validator

class JobStatus(str,Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    CANCELLED = "cancelled"