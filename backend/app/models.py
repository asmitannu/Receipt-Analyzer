from pydantic import BaseModel
from datetime import datetime

class Receipt_Data(BaseModel):
    vendor: str
    date : datetime
    amount: float
    currency: str = "INR"
    category: str = "Uncategorized"