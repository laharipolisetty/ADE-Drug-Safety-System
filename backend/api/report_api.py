from fastapi import APIRouter, UploadFile, File
from PyPDF2 import PdfReader
from ml.predict import predict_ade
from database.db import SessionLocal
from database.models import Prediction

router = APIRouter(prefix="/report", tags=["Report"])

@router.post("/upload")
async def upload_report(file: UploadFile = File(...)):
    reader = PdfReader(file.file)

    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""

    result = predict_ade(text)

    label = "ADE" if result["prediction"] == 1 else "SAFE"

    # ✅ SAVE INTO DB
    db = SessionLocal()
    record = Prediction(
        input_text=text[:500],
        prediction=label,
        confidence=result["confidence"]
    )
    db.add(record)
    db.commit()
    db.close()

    return {
        "prediction": label,
        "confidence": result["confidence"]
    }
