# -----------------------------
# Gold Standard: Vendor Integrity Score with Hover Details
# -----------------------------
st.subheader("Gold Standard: Vendor Integrity Score (Hover for Components)")

# Vendor Integrity Score (VIS) = RiskScore
df['VIS'] = df['RiskScore']

# Prepare hover data
hover_data = df[['Market Sentiment', 'Legacy Debt', 'Financial Velocity', 'Operational Fragility']]

# Heatmap visualization with hover
fig_heatmap = px.imshow(
    [df['VIS'].values],  # single-row heatmap
    labels=dict(x="Vendor", y="Score", color="Vendor Integrity Score"),
    x=df['Vendor'],
    y=["Vendor Integrity Score"],
    color_continuous_scale='RdYlGn_r',  # red=high risk, green=low risk
    text_auto=True
)

# Add hover info for each vendor
for i, vendor in enumerate(df['Vendor']):
    fig_heatmap.data[0].customdata = hover_data.values
    fig_heatmap.data[0].hovertemplate = (
        "<b>%{x}</b><br>"
        "VIS: %{z}<br>"
        "Market Sentiment: %{customdata[0]}<br>"
        "Legacy Debt: %{customdata[1]}<br>"
        "Financial Velocity: %{customdata[2]}<br>"
        "Operational Fragility: %{customdata[3]}<extra></extra>"
    )

st.plotly_chart(fig_heatmap, use_container_width=True)
