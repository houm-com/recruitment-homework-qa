from fastapi import APIRouter, FastAPI

from src.api.routes.visits import router as visits_router
from src.settings import settings

app = FastAPI()

# Init FastAPI
app = FastAPI(docs_url="/docs", redoc_url=None)
base_router = APIRouter(prefix=settings.PREFIX_URL)
base_router.include_router(visits_router)
app.include_router(base_router)


@app.get("/")
async def root():
    return {"status": "OK"}
