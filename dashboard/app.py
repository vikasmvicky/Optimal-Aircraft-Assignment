import os
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# BLOCKCHAIN IMPORT
# =========================

import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_ROOT = os.path.dirname(CURRENT_DIR)

sys.path.append(PROJECT_ROOT)

from blockchain.blockchain import Blockchain

# =========================
# CREATE BLOCKCHAIN
# =========================

blockchain = Blockchain()

# =========================
# ABSOLUTE PATH SETUP
# =========================

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_ROOT = os.path.dirname(CURRENT_DIR)

MODEL_PATH = os.path.join(
    PROJECT_ROOT,
    "notebooks",
    "models",
    "rf_model.pkl"
)

COLUMNS_PATH = os.path.join(
    PROJECT_ROOT,
    "notebooks",
    "models",
    "model_columns.pkl"
)

# =========================
# LOAD MODEL
# =========================

model = joblib.load(MODEL_PATH)

model_columns = joblib.load(COLUMNS_PATH)

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Optimal Aircraft Assignment",
    layout="wide"
)

st.title("Optimal Aircraft Assignment System")

st.write(
    "AI-powered aircraft recommendation system using Machine Learning and Blockchain."
)

# =========================
# USER INPUTS
# =========================

st.sidebar.header("Flight Configuration")

passengers = st.sidebar.slider(
    "Passengers",
    min_value=50,
    max_value=500,
    value=180
)

flight_hours = st.sidebar.slider(
    "Flight Hours",
    min_value=1.0,
    max_value=15.0,
    value=3.5
)

season = st.sidebar.selectbox(
    "Season",
    ["Peak", "Off-Peak", "Shoulder"]
)

route_category = st.sidebar.selectbox(
    "Route Category",
    ["Short Haul", "Medium Haul", "Long Haul"]
)

demand_level = st.sidebar.selectbox(
    "Demand Level",
    ["Low", "Medium", "High"]
)

# =========================
# AIRCRAFT CONFIGURATIONS
# =========================

aircraft_configs = {

    'Airbus A320': {
        'Aircraft_Capacity': 180,
        'Fuel_Cost': 25000,
        'Maintenance_Cost': 12000
    },

    'Boeing 737-800': {
        'Aircraft_Capacity': 190,
        'Fuel_Cost': 27000,
        'Maintenance_Cost': 13000
    },

    'Boeing 787-9': {
        'Aircraft_Capacity': 290,
        'Fuel_Cost': 50000,
        'Maintenance_Cost': 25000
    },

    'Boeing 777-300ER': {
        'Aircraft_Capacity': 396,
        'Fuel_Cost': 65000,
        'Maintenance_Cost': 32000
    },

    'Airbus A350-900': {
        'Aircraft_Capacity': 325,
        'Fuel_Cost': 58000,
        'Maintenance_Cost': 28000
    },

    'Airbus A380': {
        'Aircraft_Capacity': 500,
        'Fuel_Cost': 85000,
        'Maintenance_Cost': 40000
    }
}

# =========================
# PREDICTION ENGINE
# =========================

results = []

for aircraft in aircraft_configs:

    capacity = aircraft_configs[aircraft]['Aircraft_Capacity']

    sample_input = {

        'Aircraft_Capacity': capacity,

        'Passengers': passengers,

        'Load_Factor': passengers / capacity,

        'Flight_Hours': flight_hours,

        'Fuel_Cost': aircraft_configs[aircraft]['Fuel_Cost'],

        'Maintenance_Cost': aircraft_configs[aircraft]['Maintenance_Cost'],

        'Crew_Cost': 8000,

        'Depreciation_Cost': 6000,

        'Insurance_Cost': 3000,

        'Airport_Fees': 5000,

        'Catering_Cost': 2000,

        'Handling_Cost': 1500,

        'Navigation_Fees': 2500,

        'Sales_Distribution_Cost': 1200,

        'Passenger_Service_Cost': 2200,

        'Overhead_Cost': 1800,

        'Marketing_Cost': 1000,

        'IT_Systems_Cost': 900,

        'Ticket_Revenue': passengers * 500,

        'Ancillary_Revenue': passengers * 50,

        'Month': 6,

        'Day': 15,

        'Weekday': 2,

        'Aircraft_Type': aircraft,

        'Season': season,

        'Route_Category': route_category,

        'Demand_Level': demand_level
    }

    temp_df = pd.DataFrame([sample_input])

    temp_df = pd.get_dummies(temp_df)

    temp_df = temp_df.reindex(columns=model_columns, fill_value=0)

    temp_df = temp_df.fillna(0)

    try:

        predicted_profit = model.predict(temp_df)[0]

    except Exception as e:

        st.error(f"Prediction Error: {e}")

        st.write(temp_df.head())

        st.stop()

    results.append({
        'Aircraft_Type': aircraft,
        'Predicted_Profit': predicted_profit
    })

# =========================
# RESULTS
# =========================

results_df = pd.DataFrame(results)

results_df = results_df.sort_values(
    by='Predicted_Profit',
    ascending=False
)

best_aircraft = results_df.iloc[0]

# =========================
# ADD BLOCK TO BLOCKCHAIN
# =========================

blockchain.add_block({

    "Passengers": passengers,

    "Flight Hours": flight_hours,

    "Season": season,

    "Route Category": route_category,

    "Demand Level": demand_level,

    "Recommended Aircraft": best_aircraft['Aircraft_Type'],

    "Predicted Profit": float(best_aircraft['Predicted_Profit'])
})

# =========================
# BEST RECOMMENDATION
# =========================

st.subheader("Best Aircraft Recommendation")

st.success(
    f"""
    Recommended Aircraft: {best_aircraft['Aircraft_Type']}

    Predicted Profit: {best_aircraft['Predicted_Profit']:.2f}
    """
)

# =========================
# TABLE OUTPUT
# =========================

st.subheader("Aircraft Profit Comparison Table")

st.dataframe(results_df)

# =========================
# VISUALIZATION
# =========================

st.subheader("Predicted Profit by Aircraft Type")

fig, ax = plt.subplots(figsize=(10, 6))

sns.barplot(
    x='Aircraft_Type',
    y='Predicted_Profit',
    data=results_df,
    ax=ax
)

plt.xticks(rotation=45)

plt.ylabel("Predicted Profit")

plt.xlabel("Aircraft Type")

st.pyplot(fig)

# =========================
# BLOCKCHAIN LEDGER
# =========================

st.subheader("Blockchain Recommendation Ledger")

chain_data = blockchain.display_chain()

st.dataframe(chain_data)