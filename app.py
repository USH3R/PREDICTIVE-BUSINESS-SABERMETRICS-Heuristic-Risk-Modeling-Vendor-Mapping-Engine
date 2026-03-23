import streamlit as st
import pandas as pd
from risk_model import calculate_risk
import plotly.graph_objects as go

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
# Gold Standard: Vendor Integrity Score with Hover Details
# -----------------------------
st.subheader("Gold Standard: Vendor Integrity Score (Hover for Components)")

# Vendor Integrity Score = RiskScore
df['VIS'] = df['RiskScore']

# Hover text per vendor
hover_text = [
    f"Vendor: {v}<br>"
    f"VIS: {vis}<br>"
    f"Market Sentiment: {ms}<br>"
    f"Legacy Debt: {ld}<br>"
    f"Financial Velocity: {fv}<br>"
    f"Operational Fragility: {of}"
    for v, vis, ms, ld, fv, of in zip(
        df['Vendor'], df['VIS'], df['Market Sentiment'], df['Legacy Debt'],
        df['Financial Velocity'], df['Operational Fragility']
    )
]

# Heatmap with a row per vendor
fig_heatmap = go.Figure(data=go.Heatmap(
    z=df[['VIS']].values,          # N x 1 array
    x=["Vendor Integrity Score"],   # single column
    y=df['Vendor'],                # each vendor is its own row
    colorscale='RdYlGn_r',         # red=high risk, green=low risk
    text=hover_text,
    hoverinfo='text'
))

st.plotly_chart(fig_heatmap, use_container_width=True)

# -----------------------------
# Ranked Vendor Table
# -----------------------------
st.subheader("Ranked Vendors by Integrity Score (VIS)")
df_ranked = df.sort_values(by="VIS", ascending=False).reset_index(drop=True)
st.write(df_ranked[["Vendor", "VIS"]])
