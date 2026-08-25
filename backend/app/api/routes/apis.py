from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.db.database import get_db
from backend.app.db.models import MonitoredAPI
from backend.app.schemas.api import APIBase, APIResponse, HealthCheckResponse
from backend.app.Services.monitor_service import run_health_check
from backend.app.Services.metric_service import calculate_metrics
from backend.app.Services.incident_service import get_recent_health_checks
router = APIRouter()


@router.post("/apis", response_model=APIResponse)
def create_api(api: APIBase, db: Session = Depends(get_db)):
    new_api = MonitoredAPI(
        name=api.name,
        url=api.url,
        latency_threshold=api.latency_threshold,
        error_threshold=api.error_threshold
    )

    db.add(new_api)
    db.commit()
    db.refresh(new_api)

    return new_api


@router.post("/apis/{api_id}/check", response_model=HealthCheckResponse)
def check_monitored_api(api_id: int, db: Session = Depends(get_db)):

    api = db.query(MonitoredAPI).filter(
        MonitoredAPI.id == api_id
    ).first()

    if not api:
        raise HTTPException(
            status_code=404,
            detail="Monitored API not found"
        )

    if not api.is_active:
        raise HTTPException(
            status_code=400,
            detail="API monitoring is inactive"
        )

    return run_health_check(api, db)

@router.get("/apis/{api_id}/metrics")
def get_metrics(api_id: int, db: Session = Depends(get_db)):
    metrics=calculate_metrics(api_id,db)
    return metrics

@router.get("/apis/{api_id}/incidents")
def get_incident_history(api_id: int, db: Session = Depends(get_db)):
    incidents=get_incident_history(api_id,db)
    return incidents

@router.get("/apis/{api_id}/health-checks/recent")
def get_recent_checks(api_id: int, db: Session = Depends(get_db)):
    recent_checks=get_recent_health_checks(api_id,db)
    return recent_checks