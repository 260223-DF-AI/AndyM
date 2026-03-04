from .exceptions import *
from datetime import datetime
"""Writes a summary report based on the processed data and errors."""
def write_summary_report(filepath, valid_records, errors, aggregations):
    """
    Write a formatted summary report.
    
    Report should include:
    - Processing timestamp
    - Total records processed
    - Number of valid records
    - Number of errors (with details)
    - Sales by store
    - Top 5 products
    """
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total_records = len(valid_records) + len(errors)
    num_valid = len(valid_records)
    num_errors = len(errors)

    error_details = ""
    for error in errors:
        error_details += f"- {error}\n"
        
    sales_by_store = "\n".join([f"{store}: ${sales:.2f}" for store, sales in aggregations['aggregate_store'].items()])

    # top 5 products by quantity sold
    top_products = []
    for product, quantity in aggregations['aggregate_product'].items(): # figure out which ones are the top 5
        if len(top_products) < 5: # fill list
            top_products.append((product, quantity))
        else: # check if its bigger than the ones already inside
            for i in range(len(top_products)):
                if quantity > top_products[i][1]: # if the quantity is bigger than the one in the top products, replace it
                    top_products[i] = (product, quantity)
                    break

    top_products_str = ""
    for i in range(len(top_products)):
        top_products_str += f"{i+1}. {top_products[i][0]}: {top_products[i][1]} units\n"

        report_string = f"""
=== Sales Processing Report ===
Generated: {time_stamp}
Processing Statistics:
- Total records: {total_records}
- Valid records: {num_valid}
- Error records: {num_errors}
Errors:
{error_details}
Sales by Store:
{sales_by_store}
Top Products:
{top_products_str}
"""

        # actually write the report to the file  
        with open(filepath, "w") as f:
            f.write(report_string)

def write_clean_csv(filepath, records):
    """
    Write validated records to a clean CSV file.
    """
    try:
        with open(filepath, "w") as f:
            # write the header
            f.write("date,store_id,product,quantity,price,total\n")
            for record in records:
                line = f"{record['date']},{record['store_id']},{record['product']},{record['quantity']},{record['price']},{record['total']}\n"
                f.write(line)
    except FileNotFoundError as e:
        log_it(f"Failed to write CSV to file {filepath}", ERROR)
        raise FileNotFoundError(f"Failed to write clean CSV to {filepath}: {e}")

def write_error_log(filepath, errors):
    """
    Write processing errors to a log file.
    """
    try:
        with open(filepath, "w") as f:
            for error in errors:
                f.write(f"{error}\n")
    except FileNotFoundError as e:
        log_it(f"Failed to write error log to file {filepath}", ERROR)
        raise FileNotFoundError(f"Failed to write error log to {filepath}: {e}")