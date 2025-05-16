import pandas as pd
from qa.schema_definition import SCHEMA, BUSINESS_RULES

def load_data(file_path):
    return pd.read_csv(file_path)

def validate_schema(df):
    errors = []
    for col, dtype in SCHEMA.items():
        if col not in df.columns:
            errors.append(f"Missing column: {col}")
        elif not pd.api.types.is_dtype_equal(df[col].dtype, pd.Series([], dtype=dtype).dtype):
            errors.append(f"Wrong type in column {col}: expected {dtype}, got {df[col].dtype}")
    return errors

def check_business_rules(df):
    failed = {}
    for rule_name, rule_func in BUSINESS_RULES.items():
        if not rule_func(df):
            failed[rule_name] = False
    return failed
