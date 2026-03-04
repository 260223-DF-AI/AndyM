"""Code to validate the CSV input"""
import re
from .exceptions import *

# regex generator to generate valid date matcher
VALID_DATE = r"\d{4}-\d{2}-\d{2}"

def validate_sales_record(record, line_number):
    line_number += 1 # for printing later
    """
    Validate a single sales record.
    
    Required fields: date, store_id, product, quantity, price
    Validation rules:
    - date must be in YYYY-MM-DD format
    - quantity must be a positive integer
    - price must be a positive number
    
    Returns: Validated record with converted types
    Raises: InvalidDataError or MissingFieldError
    """
    # make sure everything is there and populated
    #print("one", record)
    try:
        if not( record["date"] and record["store_id"] and record["product"] and record["quantity"] and record["price"]):
            raise MissingFieldError(f"line {line_number}: missing field in {record}")
    except KeyError as e: # if key doesn't exist, this will pop and we can re-raise
        raise MissingFieldError(f"line {line_number}: missing field in {record}")

    # match date to format
    test = re.match(VALID_DATE, record["date"])
    if not test:
        raise InvalidDataError(f"line {line_number}: invalid date format {record["date"]}")
    
    # match quantity to positive integer
    try:
        record["quantity"] = int(record["quantity"])
        if record["quantity"] <= 0: # not positive, send it to valueError
            raise ValueError("quantity must be positive")
    except ValueError as e:
        raise InvalidDataError(f"line {line_number}: quantity must be positive got: {record["quantity"]}")
    

    # match price is a positive number
    try:
        record["price"] = float(record["price"])
        if record["price"] <= 0: # not positive, send it to valueError
            raise ValueError("price must be positive")

    except ValueError as e:
        raise InvalidDataError(f"line {line_number}: price must be positive got: {record["price"]}")
    
    #print("returning...")
    # everything is fine?
    return record
    

def validate_all_records(records):
    """
    Validate all records, collecting errors instead of stopping.
    
    Returns: Tuple of (valid_records, error_list)
    """
    valid_records = []
    error_list = []
    for i, record in enumerate(records):
        try: # validate single record and append to valid_records
            tested_record = validate_sales_record(record, i)
            valid_records.append(tested_record)
        except Exception as e: # i don't care which exception it is, im just going to append them all to my errors_list
            log_it(f"at {record} appended an error to error_list {e}", INFO)
            error_list.append(e)

    #print("error list:", error_list)
    return (valid_records,error_list)
    

