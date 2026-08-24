from pydantic import BaseModel,ConfigDict
from datetime import datetime
class APIResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    url: str
    latency_threshold: float
    error_threshold: float
    is_active: bool
    created_at: datetime
    
class APIBase(BaseModel):
    name: str
    url: str
    latency_threshold: float
    error_threshold: float