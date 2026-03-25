# Data Quality Report - 2026-03-25 11:22:02

## Summary

- Total Rows: 50
- Total Issues Found: 9

## Detailed Results

### Null Values

- order_id: 0 null values
- customer_name: 3 null values
- email: 0 null values
- order_date: 0 null values
- amount: 0 null values
- status: 0 null values

### Duplicate Rows

- Row 10 is a duplicate based on 'order_id'
- Row 20 is a duplicate based on 'order_id'

### Negative Values

- amount: 2 negative values

### Future Dates

- 35: True future dates

### Invalid Email Formats

- 8: True invalid email formats

### Invalid Status Values

- 40: True invalid status values

## Severity Rating: FAIL

## Recommendations

- Fix null values
- Remove duplicate rows
- Fix negative values
- Fix future dates
- Fix invalid email formats
