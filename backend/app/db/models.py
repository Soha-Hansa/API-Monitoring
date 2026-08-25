from sqlalchemy import Column, Integer,String,Float,DateTime,Boolean
from sqlalchemy.orm import declarative_base
from datetime import datetime
Base=declarative_base()

class MonitoredAPI(Base):
    __tablename__ = "monitored_apis"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    url=Column(String)
    latency_threshold=Column(Float)
    error_threshold=Column(Float)
    is_active=Column(Boolean,default=True)
    created_at=Column(DateTime,default=datetime.now)

class APIHealthCheck(Base):
    __tablename__ = "api_health_checks"
    id=Column(Integer,primary_key=True,index=True)
    api_id=Column(Integer)
    status_code=Column(Integer)
    latency=Column(Float)
    is_success=Column(Boolean)
    checked_at=Column(DateTime,default=datetime.now)

class Incident(Base):
    __tablename__ = "incidents"
    id=Column(Integer,primary_key=True, index=True)
    api_id=Column(Integer)
    incident_type=Column(String)
    severity=Column(String)
    message=Column(String)
    status=Column(String)
    created_at=Column(DateTime,default=datetime.now)
    resolved_at = Column(DateTime, nullable=True)