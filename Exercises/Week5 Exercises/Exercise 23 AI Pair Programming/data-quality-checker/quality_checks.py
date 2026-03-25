"""
data columns : order_id,customer_name,email,order_date,amount,status

Functionality:
1. **Null values**: Count nulls per column
2. **Duplicates**: Find duplicate rows based on a key column
3. **Negative values**: Flag negative values in numeric columns
4. **Date validation**: Check for future dates
5. **Email validation**: Validate email format


"""
import re

import pandas as pd

def check_nulls(df: pd.DataFrame) -> dict:
    """Check for null values in each column."""
    df.replace(["", "NA", "null"], pd.NA).isnull().sum().to_dict()
    # return dict where keys are col names and values are the count of null values in that column
    return df.isnull().sum().to_dict()

def check_duplicates(df: pd.DataFrame, key_column: str) -> dict:
    """Find duplicate rows based on a key column."""
    if key_column not in df.columns:
        raise ValueError(f"Column '{key_column}' not found")
    return df.duplicated(subset=[key_column], keep='first').to_dict() # returns a dictionary where keys are row indices and values are boolean indicating if the row is a duplicate based on the key column

def check_negative_values(df: pd.DataFrame, numeric_columns: list) -> dict:
    """Flag negative values in specified numeric columns."""
    df[numeric_columns] = df[numeric_columns].apply(lambda x: x < 0, axis=1)
    return df[numeric_columns].sum().to_dict() # returns a dictionary where keys are column names and values are the count of negative values in that column

def check_future_dates(df: pd.DataFrame, date_column: str) -> dict:
    """Check for dates in the future."""
    # checks current date and compares it with the dates in the specified date column, returns a dictionary with the count of future dates
    current_date = pd.Timestamp.now()
    # returns a dictionary where keys are column names and values are the count of future dates in that column
    future_dates = pd.to_datetime(df[date_column], errors='coerce') > current_date
    return future_dates[future_dates].to_dict()
def check_email_format(df: pd.DataFrame, email_column: str) -> dict:
    """Validate email format in the specified column."""
    # uses regex to check for valid email format, returns a dictionary with the count of invalid email formats
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    # applies the regex and returns the invalid emails as a dictionary where keys are column names and values are the count of invalid email formats in that column
    invalid =  df[email_column].apply(lambda x: not pd.isna(x) and not re.match(email_pattern, x)) # returns the count of invalid email formats in the specified email column
    return invalid[invalid].to_dict()

def check_status_values(df: pd.DataFrame, status_column: str, valid_statuses: list) -> dict:
    """Check for invalid status values."""
    # checks if the status values in the specified column are in the list of valid statuses, returns a dictionary with the count of invalid status values
    invalid_statuses = ~df[status_column].isin(valid_statuses)
    return invalid_statuses[invalid_statuses].to_dict()

