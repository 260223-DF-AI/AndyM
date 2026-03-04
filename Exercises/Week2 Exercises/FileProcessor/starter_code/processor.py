from exceptions import *
from file_reader import read_csv_file
from validator import validate_all_records
from transformer import calculate_totals, aggregate_by_store, aggregate_by_product
from report_writer import write_summary_report, write_clean_csv, write_error_log
import os

def process_sales_file(input_path, output_dir):
    """
    Main processing pipeline.
    
    1. Read the input file
    2. Validate all records
    3. Transform valid records
    4. Generate reports
    5. Handle any errors gracefully
    
    Returns: ProcessingResult with statistics
    """
    # read the input file
    #print("1. Reading input file...")
    try:
        records = read_csv_file(input_path)
    except FileProcessingError as e:
        log_it(f"Failed to read input file: {e}", ERROR)
        return False # failed to run
    
    #print("2. Validating records...")
    # validate all records
    valid_records, errors = validate_all_records(records)

    # use transformer on valid records
    transformed_records = calculate_totals(valid_records)
    aggregations = {
        "aggregate_store": aggregate_by_store(transformed_records),
        "aggregate_product": aggregate_by_product(transformed_records)
    }
    
    #print("3. Generating reports...")
    # Generate reports
    report_filepath = output_dir + "sales_report.txt"
    write_summary_report(report_filepath, valid_records, errors, aggregations)
    
    clean_csv_filepath = output_dir + "clean_sales.csv"
    write_clean_csv(clean_csv_filepath, transformed_records)
    
    error_log_filepath = output_dir + "error_log.txt"
    write_error_log(error_log_filepath, errors)
    
    # return result
    return True # completed

if __name__ == "__main__":
    # Process from command line
    process_sales_file("sample_sales.csv", "output/")