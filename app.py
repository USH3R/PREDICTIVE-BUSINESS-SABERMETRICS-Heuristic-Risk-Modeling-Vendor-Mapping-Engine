# ---------------------------------------------------------
# APPLIED SABERMETRICS: The Integrated Heatmap Engine
# ---------------------------------------------------------

import plotly.express as px
import streamlit as st

def render_sabermetric_heatmap(df):
    # The VIS (Vendor Integrity Score) is our Dependent Variable
    df['VIS'] = df['RiskScore']
    
    # These are the Independent Variables we want to "Peek" at via Hover
    # Market Sentiment, Legacy Debt, Financial Velocity, Operational Fragility
    
    fig_heatmap = px.imshow(
        [df['VIS'].values], 
        labels=dict(x="Vendor", y="Integrity", color="Risk Level"),
        x=df['Vendor'],
        y=["VIS"],
        color_continuous_scale='RdYlGn_r', # Red=High Risk, Green=Secure
        text_auto=True
    )

    # The "Sabermetrics" Hover Tooltip Logic
    fig_heatmap.update_traces(
        customdata=df[['Market Sentiment', 'Legacy Debt', 'Financial Velocity', 'Operational Fragility']],
        hovertemplate=(
            "<b>Vendor: %{x}</b><br>" +
            "Total Risk Score: %{z}<br>" +
            "<span style='color:lightgrey'>-------------------------</span><br>" +
            "Market Sentiment: %{customdata[0]}%<br>" +
            "Legacy Debt: %{customdata[1]}%<br>" +
            "Financial Velocity: %{customdata[2]}/5<br>" +
            "Operational Fragility: %{customdata[3]}%<extra></extra>"
        )
    )

    fig_heatmap.update_layout(height=300, margin=dict(l=20, r=20, t=30, b=20))
    
    return fig_heatmap

# In your main app.py, you simply call:
# st.plotly_chart(render_sabermetric_heatmap(df), use_container_width=True)
