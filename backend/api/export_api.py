from fastapi import APIRouter
from fastapi.responses import FileResponse
import csv
from database.db import SessionLocal
from database.models import Prediction

router = APIRouter(prefix="/export", tags=["Export"])

@router.get("/csv")
def export_csv():
    db = SessionLocal()
    records = db.query(Prediction).all()
    db.close()

    file_path = "data/predictions_export.csv"

    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Text", "Prediction", "Confidence", "Timestamp"])

        for r in records:
            writer.writerow([
                r.input_text,
                r.prediction,
                r.confidence,
                r.created_at
            ])

    return FileResponse(
        path=file_path,
        filename="drug_predictions.csv",
        media_type="text/csv"
    )
