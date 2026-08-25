from backend.app.db.models import MonitoredAPI
from sqlalchemy.orm import Session
from backend.app.Services.monitor_service import run_health_check

def run_monitoring(db: Session):
    active_apis = db.query(MonitoredAPI).filter(
        MonitoredAPI.is_active == True
    ).all()
    for api in active_apis:
        run_health_check(api,db)
    return len(active_apis)