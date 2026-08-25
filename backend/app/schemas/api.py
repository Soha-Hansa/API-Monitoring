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
    
class HealthCheckResponse(BaseModel):
    id: int
    api_id: int
    status_code: int | None
    latency: float | None
    is_success: bool
    checked_at: datetime

    model_config = ConfigDict(from_attributes=True)