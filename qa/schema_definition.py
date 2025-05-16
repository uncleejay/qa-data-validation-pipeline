SCHEMA = {
    "customer_id": int,
    "sales_amount": float,
    "region": str
}

BUSINESS_RULES = {
    "sales_positive": lambda df: (df["sales_amount"] > 0).all(),
    "no_missing_customer_id": lambda df: df["customer_id"].notnull().all(),
    "no_duplicates": lambda df: not df.duplicated().any()
}
