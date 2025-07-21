from fastapi import FastAPI, UploadFile, File
from .import ingestion, parser, models, database

app = FastAPI()

@app.post("/upload/")
async def upload_reciept(file: UploadFile = File(...)):
    validated_file = ingestion.validate_file(file)
    if not validated_file:
        return {"error": "Invalid file format" }
    
    extracted_data = await parser.extract_data(file)
    database.insert_data(extracted_data)
    return {"status": "success", "data": extracted_data }
