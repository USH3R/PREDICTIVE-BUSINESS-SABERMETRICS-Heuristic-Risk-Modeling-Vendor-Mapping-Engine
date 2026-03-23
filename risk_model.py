import pandas as pd

def calculate_risk(df):

    sentiment_weight = 0.35
    legacy_weight = 0.40
    financial_weight = 0.25

    df["RiskScore"] = (
        df["MarketSentiment"] * sentiment_weight +
        df["LegacyDebt"] * legacy_weight +
        (100 - df["FinancialVelocity"]) * financial_weight
    )

    return df
