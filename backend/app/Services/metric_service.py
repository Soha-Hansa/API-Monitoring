from sqlalchemy.orm import Session
from backend.app.db.models import APIHealthCheck

def calculate_metrics(api_id:int, db:Session):
    checks = db.query(APIHealthCheck).filter(
    APIHealthCheck.api_id==api_id
    ).all()
    if not checks:
        return None
    avg_latency=sum( s.latency for s in checks )/len(checks)
    uptime=sum(s.is_success for s in checks )/len(checks)*100
    failure_count = len(checks) - sum(s.is_success for s in checks)
    
    return {
        "average_latency" :avg_latency,
        "uptime":uptime,
        "failure_count":failure_count
    }