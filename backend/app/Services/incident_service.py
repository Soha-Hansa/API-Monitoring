from sqlalchemy.orm import Session
from backend.app.db.models import APIHealthCheck
def get_incident_history(api_id: int, db: Session):
    incidents=db.query(Model).filter(
    Model.field == value
    ).all()
    return incidents

def get_recent_health_checks(api_id: int, db: Session):
    checks = db.query(APIHealthCheck).filter(
        APIHealthCheck.api_id == api_id
    ).order_by(
        APIHealthCheck.checked_at.desc()
    ).limit(10).all()
    return checks
    