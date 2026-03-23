import pandas as pd

def calculate_risk(df):

    sentiment_weight = 0.30
    legacy_weight = 0.30
    financial_weight = 0.20
    fragility_weight = 0.20

    df["RiskScore"] = (
        df["MarketSentiment"] * sentiment_weight +
        df["LegacyDebt"] * legacy_weight +
        (100 - df["FinancialVelocity"]) * financial_weight +
        df["OperationalFragility"] * fragility_weight
    )

    return df
