import asyncio
from backend.app.db.database import SessionLocal
from backend.app.Services.monitor_worker import run_monitoring
async def monitor_loop():
    while True:
        db=SessionLocal()
        try:
            run_monitoring(db)
        finally:
            db.close()
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(monitor_loop())
            