from database.db import SessionLocal
from database.models import Prediction
from sqlalchemy import func

def get_real_time_risk():
    db = SessionLocal()

    data = db.query(
        Prediction.input_text,
        func.count(Prediction.id)
    ).group_by(Prediction.input_text).all()

    results = []

    for text, count in data:
        results.append({
            "drug": text[:20],
            "level": "High" if count > 3 else "Medium",
            "score": round(count / 5, 2)
        })

    db.close()
    return results
