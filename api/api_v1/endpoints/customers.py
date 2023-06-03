from fastapi import APIRouter, Depends
from typing import Any
from schemas import customers
from sqlalchemy.orm import Session
from api import deps
from crud import crud_customers


router = APIRouter()

@router.get("/", response_model=list[customers.Customers])
def read_customes(db: Session = Depends(deps.get_db), skip: int=0, limit: int=5) -> Any:
    customers = crud_customers.customers.get_multi(db, skip=skip, limit=limit)
    return customers