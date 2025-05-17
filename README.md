# QA Data Validation Pipeline

A data validation framework designed to process and validate customer sales data from CSV files. This pipeline performs schema validation, enforces business rules, and implements data cleaning operations to ensure data quality and consistency.

## Features

### Schema Validation
- Validates the presence and data types of required fields:
  - `customer_id` (integer)
  - `sales_amount` (float)
  - `region` (string)

### Business Rules Validation
- Enforces critical business rules:
  - Ensures all sales amounts are positive
  - Verifies no missing customer IDs
  - Checks for duplicate records

### Data Cleaning
- Automated cleaning operations:
  - Removes rows with non-positive sales amounts
  - Eliminates duplicate records

## Project Structure

```
qa-data-validation-pipeline/
├── qa/
│   ├── data_validator.py    # Core validation and cleaning logic
│   └── schema_definition.py # Schema and business rules definitions
├── tests/
│   └── test_data_validation.py # Test suite
└── data/
    └── mock_data_sales.csv    # Sample data file
```

## Usage

### Loading and Validating Data

```python
from qa.data_validator import load_data, validate_schema, check_business_rules, clean_data

# Load data from CSV
df = load_data("data/mock_data_sales.csv")

# Validate schema
errors = validate_schema(df)
if errors:
    print("Schema validation errors:", errors)

# Clean the data
cleaned_df = clean_data(df)

# Check business rules
failed_rules = check_business_rules(cleaned_df)
if failed_rules:
    print("Failed business rules:", failed_rules)
```

### Sample Data Format

Your CSV file should contain the following columns:
```csv
customer_id,sales_amount,region
1001,150.50,North
1002,75.25,South
```

## Testing

To run the test suite:

```bash
python -m pytest tests/test_data_validation.py -v
```

The tests verify:
- Schema validation functionality
- Business rules enforcement
- Data cleaning operations

## Requirements

- Python 3.x
- pandas
- pytest (for running tests)
