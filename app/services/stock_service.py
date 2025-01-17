import os 
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALPHA_VINTAGE_API_KEYS")
BASE_URL = "https://www.alphavantage.co/query"

def stock_data(symbol:str,interval:str="1min",outputsize: str="compact"):

    try:
        params = {
            "function":"TIME_SERIES_INTRADAY",
            "symbol":symbol,
            "interval":interval,
            "apikey":API_KEY,
            "outputsize":outputsize
        }

        response = requests.get(BASE_URL,params=params)
        response.raise_for_status()

        data = response.json()

        if "Error Message" in data:
            return {"error":data["Error Message"]}
        if "Note" in data:
            return {"error":"API call limit reached. Please try again later."}
        
        return data
    
    except Exception as e:
        return {"error": str(e)}