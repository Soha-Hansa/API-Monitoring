from fastapi import FastAPI

from backend.app.db.models import Base
from backend.app.db.database import engine
from backend.app.api.routes.apis import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router, prefix="/api")


@app.get("/")
def home():
    return {
        "message": "everything works fine"
    }