import os
from qa.data_validator import load_data, validate_schema, check_business_rules, clean_data

DATA_PATH = os.path.join("data", "mock_data_sales.csv")

def test_schema_validation():
    df = load_data(DATA_PATH)
    errors = validate_schema(df)
    assert not errors, f"Schema errors found: {errors}"

def test_business_rules():
    df = load_data(DATA_PATH)
    df = clean_data(df)
    failed_rules = check_business_rules(df)
    assert not failed_rules, f"Business rule checks failed: {failed_rules}"
