import streamlit as st
import pandas as pd
from risk_model import calculate_risk

df = pd.read_csv("vendors.csv")

df = calculate_risk(df)

st.title("Predictive Business Sabermetrics")

st.write(df)

st.bar_chart(df.set_index("Vendor")["RiskScore"])
