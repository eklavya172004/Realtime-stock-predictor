#Stock-related API routes

from fastapi import APIRouter,HTTPException
from app.services.stock_service import stock_data

router = APIRouter(
    prefix="/stocks",
    tags=["Stocks"]
)

@router.get("/fetch")
def fetch_data(symbol: str,interval:str="1min",outputsize: str="compact"):
    data = stock_data(symbol,interval,outputsize)
# def stoc_data(symbol:str,interval:str="1min",outputsize: str="compact"):
    if "error" in data:
        raise HTTPException(status_code=400,detail=data["error"])
    return data