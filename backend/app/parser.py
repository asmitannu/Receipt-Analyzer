#DATA PARSING : PARSING AND EXTRACTING DATA FROM UPLOADED FILE
import pytesseract
from PIL import Image
import fitz  # PyMuPDF
import re
from datetime import datetime
from .models import Receipt_Data
import io

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# CURRENCY MAPPING

CURRENCY_SYMBOLS = {
    '₹': 'INR', '$': 'USD', '€': 'EUR', '£': 'GBP', 'AED': 'AED', 'Rs.': 'INR', 'INR': 'INR'
}

async def extract_data(file):
    # Step 1: Load the file into bytes
    file_bytes = await file.read()

    # Step 2: Detect file type
    text = ""
    if file.filename.endswith(".pdf"):
        pdf = fitz.open(stream=file_bytes, filetype="pdf")
        for page in pdf:
            text += page.get_text()
        pdf.close()

    elif file.filename.endswith((".jpg", ".jpeg", ".png")):
        image = Image.open(io.BytesIO(file_bytes))
        text = pytesseract.image_to_string(image)

    elif file.filename.endswith(".txt"):
        text = file_bytes.decode("utf-8")

    else:
        raise ValueError("Unsupported file format")

    # Step 3: Extract fields from text
    vendor = re.search(r"(?i)(vendor|biller):?\s*(\w+)", text)

    amount = None
    currency = "INR"    #default
    for symbol, code in CURRENCY_SYMBOLS.items():
        pattern = rf"{symbol}\s?(\d+(\.\d{{1,2}})?)"
        match = re.search(pattern, text)
        if match:
            amount = float(match.group(1))
            currency = code
            break

    date = re.search(r"\d{2}/\d{2}/\d{4}", text)
    parsed_date = datetime.strptime(date.group(), "%d/%m/%Y") if date else datetime.now()

    return Receipt_Data(       #calling receipt_data func, with fallback defaults
        vendor=vendor.group(2) if vendor else "Unknown",
        date=parsed_date,
        amount=amount if amount else 0.0,
        currency=currency
    )

