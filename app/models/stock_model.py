from pydantic import BaseModel

class StockRequest(BaseModel):
    symbol:str
    interval:str = "1min"
    outputsize:str="compact"
    