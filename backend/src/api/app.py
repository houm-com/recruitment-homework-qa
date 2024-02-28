from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes.visits import router as visits_router
from src.settings import settings

app = FastAPI(docs_url="/docs", redoc_url=None)


origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Init FastAPI
base_router = APIRouter(prefix=settings.PREFIX_URL)
base_router.include_router(visits_router)
app.include_router(base_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"status": "OK"}
