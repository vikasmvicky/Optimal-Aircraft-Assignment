# Optimal Aircraft Assignment System

An AI-powered airline decision-support system that recommends the most profitable aircraft for a given flight scenario using Machine Learning and Blockchain integration.

---

# Project Overview

This project analyzes airline operational parameters such as:

* passenger demand
* flight duration
* route category
* seasonal demand
* operational costs

and predicts the most profitable aircraft assignment using a trained Random Forest Regression model.

The system also integrates a lightweight blockchain ledger to securely store aircraft recommendation records with immutable hash chaining.

---

# Key Features

* Machine Learning-based profit prediction
* Aircraft recommendation engine
* Streamlit interactive dashboard
* Blockchain-based recommendation logging
* Profit comparison visualization
* Real-time user input system

---

# Technologies Used

| Technology              | Purpose             |
| ----------------------- | ------------------- |
| Python                  | Core development    |
| Pandas                  | Data preprocessing  |
| Scikit-learn            | Machine Learning    |
| Random Forest Regressor | Profit prediction   |
| Streamlit               | Dashboard UI        |
| Matplotlib / Seaborn    | Visualization       |
| Blockchain (Python)     | Immutable logging   |
| Joblib                  | Model serialization |

---

# Machine Learning Workflow

```text id="mlflow"
Dataset
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Model Training
   ↓
Profit Prediction
   ↓
Aircraft Optimization
```

---

# Blockchain Integration

The project implements a lightweight blockchain system to store:

* flight recommendation history
* predicted profit
* operational inputs
* timestamps
* hash values

This ensures:

* transparency
* traceability
* tamper-resistant logging

---

# Aircraft Types Supported

* Airbus A320
* Boeing 737-800
* Boeing 787-9
* Boeing 777-300ER
* Airbus A350-900
* Airbus A380

---

# Dashboard Features

The Streamlit dashboard allows users to:

* select passenger count
* choose flight duration
* select season and route category
* compare aircraft profitability
* view optimal aircraft recommendation
* inspect blockchain ledger records

---

# Project Structure

```text id="projectstructure"
Optimal-Aircraft-Assignment/
│
├── blockchain/
│   ├── __init__.py
│   └── blockchain.py
│
├── dashboard/
│   └── app.py
│
├── notebooks/
│   ├── 01_eda.ipynb
│   └── models/
│       ├── rf_model.pkl
│       └── model_columns.pkl
│
├── data/
│
└── README.md
```

---

# How To Run

## Install Dependencies

```bash id="installreq"
pip install pandas numpy matplotlib seaborn scikit-learn streamlit joblib
```

---

## Run Dashboard

```bash id="runstream"
streamlit run dashboard/app.py
```

---

# Output

The system provides:

* best aircraft recommendation
* predicted profitability
* aircraft comparison table
* profitability visualization
* blockchain recommendation ledger

---

# Future Improvements

* Smart contract integration
* Real-time airline APIs
* Cloud deployment
* Database integration
* Advanced optimization algorithms
* Multi-route scheduling

---

# Author

Vikas M Vicky

GitHub Repository:

[Optimal-Aircraft-Assignment Repository](https://github.com/vikasmvicky/Optimal-Aircraft-Assignment.git?utm_source=chatgpt.com)
