import streamlit as st
import pandas as pd
from risk_model import calculate_risk
import plotly.express as px

# -----------------------------
# Load vendor data
# -----------------------------
df = pd.read_csv("vendors.csv")

# -----------------------------
# Calculate risk
# -----------------------------
df = calculate_risk(df)

# -----------------------------
# Streamlit title
# -----------------------------
st.title("Predictive Business Sabermetrics")

# -----------------------------
# Table view of vendor data
# -----------------------------
st.subheader("Vendor Risk Table")
st.write(df)

# -----------------------------
# Bar chart of RiskScore
# -----------------------------
st.subheader("RiskScore Bar Chart")
st.bar_chart(df.set_index("Vendor")["RiskScore"])

# -----------------------------
# Gold Standard: Vendor Integrity Score
# -----------------------------
st.subheader("Gold Standard: Vendor Integrity Score")

# Vendor Integrity Score (VIS) = RiskScore
df['VIS'] = df['RiskScore']

# Heatmap visualization
fig_heatmap = px.imshow(
    [df['VIS'].values],  # single-row heatmap
    labels=dict(x="Vendor", y="Score", color="Vendor Integrity Score"),
    x=df['Vendor'],
    y=["Vendor Integrity Score"],
    color_continuous_scale='RdYlGn_r'  # red=high risk, green=low risk
)
st.plotly_chart(fig_heatmap, use_container_width=True)

# -----------------------------
# Ranked Vendor Table
# -----------------------------
st.subheader("Ranked Vendors by Integrity Score (VIS)")
df_ranked = df.sort_values(by="VIS", ascending=False).reset_index(drop=True)
st.write(df_ranked[["Vendor", "VIS"]])import streamlit as st
import pandas as pd
from risk_model import calculate_risk

df = pd.read_csv("vendors.csv")

df = calculate_risk(df)

st.title("Predictive Business Sabermetrics")

st.write(df)

st.bar_chart(df.set_index("Vendor")["RiskScore"])
