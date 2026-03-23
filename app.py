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
# Gold Standard: Vendor Integrity Score with Hover and Labels
# -----------------------------
st.subheader("Gold Standard: Vendor Integrity Score (Hover for Components)")

# Vendor Integrity Score = RiskScore
df['VIS'] = df['RiskScore']

# Sort by VIS descending (highest risk on top)
df_sorted = df.sort_values(by="VIS", ascending=False).reset_index(drop=True)

# Hover text per vendor (2D array to match z)
hover_text_2d = [[
    f"<b>Vendor:</b> {v}<br>"
    f"<b>VIS:</b> {vis}<br>"
    f"<b>Market Sentiment:</b> {ms}<br>"
    f"<b>Legacy Debt:</b> {ld}<br>"
    f"<b>Financial Velocity:</b> {fv}<br>"
    f"<b>Operational Fragility:</b> {of}"
] for v, vis, ms, ld, fv, of in zip(
    df_sorted['Vendor'], df_sorted['VIS'], df_sorted['Market Sentiment'], 
    df_sorted['Legacy Debt'], df_sorted['Financial Velocity'], df_sorted['Operational Fragility']
)]

# Create heatmap with numbers displayed inside cells
fig_heatmap = go.Figure(data=go.Heatmap(
    z=df_sorted[['VIS']].values,
    x=["Vendor Integrity Score"],
    y=df_sorted['Vendor'],
    colorscale='RdYlGn_r',
    text=[[f"{v:0.2f}" for v in row] for row in df_sorted[['VIS']].values],  # numbers inside cells
    texttemplate="%{text}",       # show numbers inside cells
    textfont={"size":14, "color":"black"},
    hoverinfo='text',
    hovertext=hover_text_2d       # detailed hover
))

# Display heatmap
st.plotly_chart(fig_heatmap, use_container_width=True)

# -----------------------------
# Ranked Vendor Table
# -----------------------------
st.subheader("Ranked Vendors by Integrity Score (VIS)")
df_ranked = df.sort_values(by="VIS", ascending=False).reset_index(drop=True)
st.write(df_ranked[["Vendor", "VIS"]])import streamlit as st
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

# Hover text per vendor (must be 2D array to match heatmap)
hover_text_2d = [[
    f"Vendor: {v}<br>"
    f"VIS: {vis}<br>"
    f"Market Sentiment: {ms}<br>"
    f"Legacy Debt: {ld}<br>"
    f"Financial Velocity: {fv}<br>"
    f"Operational Fragility: {of}"
] for v, vis, ms, ld, fv, of in zip(
    df['Vendor'], df['VIS'], df['Market Sentiment'], df['Legacy Debt'],
    df['Financial Velocity'], df['Operational Fragility']
)]

# Heatmap with each vendor as a row
fig_heatmap = go.Figure(data=go.Heatmap(
    z=df[['VIS']].values,            # N x 1 array
    x=["Vendor Integrity Score"],     # single column
    y=df['Vendor'],                  # each vendor is a row
    colorscale='RdYlGn_r',           # red=high risk, green=low risk
    text=hover_text_2d,              # matches shape of z
    hoverinfo='text'
))

st.plotly_chart(fig_heatmap, use_container_width=True)

# -----------------------------
# Ranked Vendor Table
# -----------------------------
st.subheader("Ranked Vendors by Integrity Score (VIS)")
df_ranked = df.sort_values(by="VIS", ascending=False).reset_index(drop=True)
st.write(df_ranked[["Vendor", "VIS"]])
