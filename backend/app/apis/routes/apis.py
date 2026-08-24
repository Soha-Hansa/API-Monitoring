from fastapi import APIRouter,Depends
from backend.app.db.database import get_db
from backend.app.schemas.api import APIBase,APIResponse
from sqlalchemy.orm import Session
from backend.app.db.models import MonitoredAPI
router=APIRouter()
@router.post("/apis",response_model=APIResponse)
def create_api(api:APIBase, db:Session=Depends(get_db)):
    new_api=MonitoredAPI(
        name=api.name,
        url=api.url ,
        latency_threshold=api.latency_threshold,
        error_threshold=api.error_threshold
    )
    db.add(new_api)
    db.commit()
    db.refresh(new_api)
    return new_api