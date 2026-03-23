import pandas as pd

def calculate_risk(df):

    sentiment_weight = 0.30
    legacy_weight = 0.30
    financial_weight = 0.20
    fragility_weight = 0.20

    df["Market Sentiment"] * sentiment_weight +
        df["Legacy Debt"] * legacy_weight +
        (100 - df["Financial Velocity"]) * financial_weight +
        df["Operational Fragility"] * fragility_weight
    )

    return df
