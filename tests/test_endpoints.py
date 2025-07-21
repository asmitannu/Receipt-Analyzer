from fastapi.testclient import TestClient
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.app.main import app
import io

client = TestClient(app)

def test_upload_txt_file():
    content = "Vendor: Swiggy\nDate: 2025-06-20\nAmount: ₹350.00"
    byte_data = content.encode("utf-8")  # Convert to bytes safely
    response = client.post("/upload/", files={"file": ("test.txt", byte_data, "text/plain")})
    assert response.status_code == 200
    data = response.json()
    if "vendor" in data:
        assert data["vendor"] == "Swiggy"
    elif "data" in data and "vendor" in data["data"]:
        assert data["data"]["vendor"] == "Swiggy"
    else:
        raise AssertionError(f"Unexpected response format: {data}")