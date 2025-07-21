import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.app.parser import extract_data
import pytest
from fastapi import UploadFile
import io

@pytest.mark.asyncio
async def test_extract_data_from_txt():
    text = "Vendor: Zomato\nDate: 15/06/2025\nAmount: ₹430.00"
    file = UploadFile(filename="sample.txt", file=io.BytesIO(text.encode("utf-8")))  # encode safely

    result = await extract_data(file)
    assert result.vendor == "Zomato"
    assert result.amount == 430.0
    assert result.currency == "INR"
