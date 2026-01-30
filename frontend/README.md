# 🧠 Adverse Drug Effect Detection & Safety Analytics System

## 📌 Project Overview

The **Adverse Drug Effect Detection and Safety Analytics System** is a full-stack Machine Learning–based web application designed to identify potential adverse drug reactions (ADR/ADE) from clinical text and medical reports. The system also provides real-time safety analytics, dashboards, and risk assessment to support pharmacovigilance activities.

This project is developed as a **Final Year Major Project** and demonstrates real-world concepts used in hospital systems, pharmaceutical companies, and regulatory authorities.

---

## 🎯 Objectives

* Detect adverse drug reactions using Machine Learning
* Analyze drug safety trends in real time
* Allow medical report (PDF) uploads for prediction
* Store predictions permanently in a database
* Visualize KPIs using interactive dashboards
* Provide export and filtering functionality
* Maintain audit logs for medical analysis

---

## 🧩 System Architecture

```
Frontend (React + Tailwind)
        ↓ REST API
Backend (FastAPI)
        ↓
Machine Learning Model
        ↓
SQLite Database
```

---

## 🛠️ Technology Stack

### Frontend

* React.js
* Tailwind CSS
* Axios
* Recharts (Graphs)

### Backend

* FastAPI
* SQLAlchemy
* Pydantic
* PyPDF2

### Machine Learning

* TF-IDF Vectorization
* Logistic Regression / Random Forest
* Scikit-learn

### Database

* SQLite 

---

## 📂 Project Folder Structure

```
ADE-Drug-Safety-System
│
├── backend
│   ├── api
│   │   ├── main.py
│   │   ├── report_api.py
│   │   └── auth.py
│   │
│   ├── ml
│   │   ├── train_model.py
│   │   └── predict.py
│   │
│   ├── analytics
│   │   ├── dashboard.py
│   │   ├── risk_scoring.py
│   │   └── trend_analysis.py
│   │
│   ├── database
│   │   ├── db.py
│   │   └── models.py
│   │
│   ├── data
│   │   └── processed
│   │
│   └── models
│       ├── ade_model.pkl
│       └── vectorizer.pkl
│
├── frontend
│   ├── src
│   │   ├── pages
│   │   │   ├── Home.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── Analyze.jsx
│   │   │   ├── Reports.jsx
│   │   │   └── DrugRisk.jsx
│   │   ├── components
│   │   │   └── Navbar.jsx
│   │   └── App.jsx
│   └── package.json
│
└── README.md
```

---

## ⚙️ Features Implemented

### 🔍 ADE Prediction

* User enters clinical text or uploads medical report
* Text is cleaned and vectorized
* ML model predicts ADE or SAFE
* Confidence score generated

### 📄 Medical Report Upload

* Accepts PDF reports
* Extracts medical content automatically
* Predicts adverse reactions
* Saves results permanently in database

### 📊 Dashboard & Analytics

* Total predictions count
* ADE vs SAFE cases
* Pie chart and bar chart
* Real-time updates every few seconds

### ⚠️ Drug Risk Scoring

* Calculates drug risk using historical predictions
* Displays high-risk and low-risk drugs
* Updates dynamically from database

### 📈 Trend Analysis

* Time-based trend visualization
* Helps understand safety patterns

### 📤 Export Functionality

* Export prediction history to CSV
* Useful for audit and documentation

### 🔄 Real-Time Updates

* Dashboard auto-refresh
* Live analytics from database

---

## 🧠 Machine Learning Model

### Algorithm Used

* TF-IDF Vectorizer
* Logistic Regression / Random Forest

### Why this model?

* Works efficiently on text data
* High accuracy for binary classification
* Fast prediction speed

### Training Data

* FAERS drug safety data
* Drugs.com reviews dataset

### Output

* ADE (Adverse Drug Effect)
* SAFE (No detected adverse reaction)

---

## 🗄️ Database Design

### Prediction Table

| Column     | Description      |
| ---------- | ---------------- |
| id         | Primary key      |
| input_text | Medical text     |
| prediction | ADE / SAFE       |
| confidence | Model confidence |
| created_at | Timestamp        |

---

## 🚀 How to Run the Project

### Backend

```bash
cd backend
pip install -r requirements.txt
python -m uvicorn api.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

### Frontend

```bash
cd frontend
npm install
npm start
```

Frontend runs at:

```
http://localhost:3000
```

---

## 🔐 Security & Error Handling

* CORS enabled
* File validation for PDF uploads
* Try–except handling in ML pipeline
* Backend logging for audit

---

## 📊 Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-score

Model achieved **high prediction accuracy** on test data.

---

## 🎓 Academic Use

This project fulfills all major project requirements:

* Machine Learning implementation
* Database integration
* Full-stack development
* Real-time analytics
* Visualization dashboards

---

## 🔮 Future Enhancements

* Deep Learning (LSTM / BERT)
* Multi-drug interaction detection
* Role-based login (Doctor/Admin)
* Cloud deployment
* Integration with hospital systems

---

---

## 📜 Conclusion

The Adverse Drug Effect Detection and Safety Analytics System provides a scalable, intelligent, and real-time approach to pharmacovigilance. By combining Machine Learning with modern web technologies, the system helps improve patient safety, reduce medication risks, and support clinical decision-making.

---

✅ **This project demonstrates real-world healthcare AI implementation and meets industry-level standards.**
