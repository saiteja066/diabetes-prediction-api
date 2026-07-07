# 🩺 Diabetes Prediction API using FastAPI

A Machine Learning API built with **FastAPI** to predict whether a person is diabetic based on medical parameters. The model is trained using **Scikit-learn** and deployed as a REST API.

---

## 🚀 Features

* FastAPI-based REST API
* Machine Learning prediction using Scikit-learn
* Automatic API documentation with Swagger UI
* JSON request and response
* Easy integration with React, Android, or any frontend

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Scikit-learn
* Pandas
* NumPy
* Uvicorn
* Pydantic

---

## 📁 Project Structure

```
Diabetes-Prediction-API/
│
├── ml_api.py
├── diabetes_model.sav
├── requirements.txt
├── api_implementation.py
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
```

Go to the project folder:

```bash
cd Diabetes-Prediction-API
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn ml_api:app --reload
```

---

## 🌐 API Endpoint

### POST `/diabetes_prediction`

### Sample Request

```json
{
  "Pregnancies": 6,
  "Glucose": 148,
  "BloodPressure": 72,
  "SkinThickness": 35,
  "Insulin": 0,
  "BMI": 33.6,
  "DiabetesPedigreeFunction": 0.627,
  "Age": 50
}
```

### Sample Response

```json
{
  "prediction": 1,
  "result": "The person is diabetic"
}
```

---

## 📖 API Documentation

After starting the server, open:

```
http://127.0.0.1:8000/docs
```

Interactive Swagger UI will be available for testing the API.

---

## 👨‍💻 Author

**Gudapala Venkata Sai Teja**

B.Tech – Computer Science and Engineering

Machine Learning & AI Enthusiast
