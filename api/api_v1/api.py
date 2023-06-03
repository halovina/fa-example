from fastapi import APIRouter
from api.api_v1.endpoints import home, customers


api_router = APIRouter()
api_router.include_router(home.router, tags=["home"])
api_router.include_router(customers.router,prefix="/customers", tags=["customers"])
