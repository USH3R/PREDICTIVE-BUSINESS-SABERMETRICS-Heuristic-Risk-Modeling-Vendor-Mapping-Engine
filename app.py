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

# Hover text per vendor
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
    texttemplate="%{text}",
    textfont={"size":14, "color":"black"},
    hoverinfo='text',
    hovertext=hover_text_2d
))

fig_heatmap.update_layout(
    hoverlabel=dict(
        bgcolor="white",
        font_size=13,
        font_family="Arial",
        bordercolor="black"
    ),
    hovermode="closest"
)

st.plotly_chart(fig_heatmap, use_container_width=True)

# -----------------------------
# Ranked Vendors & Pie Chart Side by Side
# -----------------------------
st.subheader("Vendor Integrity Overview")

# Columns layout: Pie chart left, table right
col1, col2 = st.columns([2,3])

# Pie chart
with col1:
    st.markdown("### Vendor VIS Distribution")
    fig_pie = go.Figure(data=[go.Pie(
        labels=df_sorted['Vendor'],
        values=df_sorted['VIS'],
        hoverinfo='label+percent+value',
        textinfo='label+value',
        textfont_size=14
    )])
    st.plotly_chart(fig_pie, use_container_width=True)

# Ranked table
with col2:
    st.markdown("### Ranked Vendors by Integrity Score (VIS)")
    st.write(df_sorted[['Vendor', 'VIS']])
