from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import func

from database.db import engine, SessionLocal
from database.models import Base, Prediction

from ml.predict import predict_ade
from api.report_api import router as report_router
from analytics.risk_scoring import get_real_time_risk
from analytics.trend_analysis import get_trend_data
from api.auth import router as auth_router

from api.prediction_api import router as prediction_router
from api.export_api import router as export_router

from api.export_api import router as export_router



import logging
import os

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# --------------------------------
# Create tables
# --------------------------------
Base.metadata.create_all(bind=engine)

# --------------------------------
# Create app
# --------------------------------
app = FastAPI(title="Drug Safety AI System")

# --------------------------------
# Enable CORS
# --------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------
# Schema
# --------------------------------
class TextInput(BaseModel):
    text: str

# --------------------------------
# Home
# --------------------------------
@app.get("/")
def home():
    return {"message": "Drug Safety Backend Running"}

# --------------------------------
# Prediction API (SAVE TO DB)
# --------------------------------
@app.post("/predict")
def predict(data: TextInput):
    result = predict_ade(data.text)

    # ✅ define label FIRST
    if result["prediction"] == 1:
        label = "ADE"
    else:
        label = "SAFE"

    logging.info(f"Prediction made: {label}")

    db = SessionLocal()

    record = Prediction(
        input_text=data.text,
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

# --------------------------------
# Dashboard (DB ONLY)
# --------------------------------
@app.get("/dashboard")
def dashboard():
    db = SessionLocal()

    total = db.query(Prediction).count()
    ade = db.query(Prediction).filter(Prediction.prediction == "ADE").count()
    safe = db.query(Prediction).filter(Prediction.prediction == "SAFE").count()

    db.close()

    return {
        "total_predictions": total,
        "ade_cases": ade,
        "safe_cases": safe
    }
from fastapi import Query

@app.get("/predictions")
def get_predictions(type: str = Query(None)):
    db = SessionLocal()

    if type:
        records = db.query(Prediction).filter(
            Prediction.prediction == type
        ).all()
    else:
        records = db.query(Prediction).all()

    db.close()

    return [
        {
            "text": r.input_text,
            "prediction": r.prediction,
            "confidence": r.confidence,
            "time": r.created_at
        }
        for r in records
    ]

# --------------------------------
# Drug risk scoring
# --------------------------------
@app.get("/drug-risk")
def drug_risk():
    return get_real_time_risk()

# --------------------------------
# Trend analysis
# --------------------------------
@app.get("/trend")
def trend():
    return get_trend_data()


@app.get("/report/reports")
def get_reports():
    db = SessionLocal()
    reports = db.query(Prediction).order_by(Prediction.id.desc()).all()
    db.close()

    return [
        {
            "text": r.input_text,
            "prediction": r.prediction,
            "confidence": r.confidence,
            "time": r.created_at
        }
        for r in reports
    ]

# --------------------------------
# Routers
# --------------------------------
app.include_router(report_router)
app.include_router(auth_router)
app.include_router(prediction_router)
app.include_router(export_router)
app.include_router(export_router)
app.include_router(export_router)




