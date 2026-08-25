from sqlalchemy.orm import Session

from backend.app.db.models import MonitoredAPI, APIHealthCheck
from backend.app.Services.health_checker import check_api


def run_health_check(api: MonitoredAPI, db: Session):
    result = check_api(api.url)

    health_check = APIHealthCheck(
        api_id=api.id,
        status_code=result["status_code"],
        latency=result["latency"],
        is_success=result["is_success"]
    )

    db.add(health_check)
    db.commit()
    db.refresh(health_check)

    return health_check