from fastapi import APIRouter, HTTPException
from database.db import SessionLocal
from database.models import Prediction

router = APIRouter(prefix="/predictions", tags=["Predictions"])

# -----------------------------
# READ ALL
# -----------------------------
@router.get("/")
def get_all_predictions():
    db = SessionLocal()
    data = db.query(Prediction).all()
    db.close()
    return data

# -----------------------------
# READ ONE
# -----------------------------
@router.get("/{pid}")
def get_prediction(pid: int):
    db = SessionLocal()
    record = db.query(Prediction).filter(Prediction.id == pid).first()
    db.close()

    if not record:
        raise HTTPException(status_code=404, detail="Not found")

    return record

# -----------------------------
# UPDATE
# -----------------------------
@router.put("/{pid}")
def update_prediction(pid: int, new_label: str):
    db = SessionLocal()
    record = db.query(Prediction).filter(Prediction.id == pid).first()

    if not record:
        db.close()
        raise HTTPException(status_code=404, detail="Not found")

    record.prediction = new_label
    db.commit()
    db.close()

    return {"message": "Updated successfully"}

# -----------------------------
# DELETE
# -----------------------------
@router.delete("/{pid}")
def delete_prediction(pid: int):
    db = SessionLocal()
    record = db.query(Prediction).filter(Prediction.id == pid).first()

    if not record:
        db.close()
        raise HTTPException(status_code=404, detail="Not found")

    db.delete(record)
    db.commit()
    db.close()

    return {"message": "Deleted successfully"}
