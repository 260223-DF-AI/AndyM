"""Code to validate the CSV input"""
import re
from exceptions import *

# regex generator to generate valid date matcher
VALID_DATE = "^\d{4}-\d{2}-\d{2}$"

def validate_sales_record(record, line_number):
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
    try:
        if not( record["date"] and record["store_id"] and record["product"] and record["quantity"] and record["price"]):
            raise MissingFieldError()
    except KeyError as e: # if key doesn't exist, this will pop and we can re-raise
        raise MissingFieldError()

    # match date to format
    test = re.match(VALID_DATE, record[0])
    if not test:
        raise InvalidDataError(record[0])
    
    # match quantity to positive integer
    try:
        record[3] = int(record[3])
    except ValueError as e:
        raise InvalidDataError(record[3])
    

    # match price is a positive number
    try:
        record[4] = float(record[4])
        if record[4] <= 0: # not positive, send it to valueError
            raise ValueError()

    except ValueError as e:
        raise InvalidDataError(record[4])
    
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
            log_it(f"appended an error to error_list {e}", INFO)
            error_list.append(e)

        return (valid_records,error_list)
    

