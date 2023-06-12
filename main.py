from fastapi import FastAPI
from api.api_v1.api import api_router
from core.config import settings
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
app.include_router(api_router, prefix=settings.API_V1_STR)
