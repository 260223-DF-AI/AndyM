"""
1. Takes the results from all quality checks
2. Generates a Markdown report with:
   - Header with timestamp
   - Summary statistics (total rows, total issues found)
   - Detailed results for each check
   - A severity rating (PASS / WARNING / FAIL)
   - Recommendations for each issue found
"""
import datetime
import pandas as pd

from quality_checks import check_nulls, check_duplicates, check_negative_values, check_future_dates, check_email_format, check_status_values

def generate_report(df: pd.DataFrame):
    # Generate report header
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = f"# Data Quality Report - {timestamp}\n\n"

    # Generate summary statistics
    total_rows = 50

    # check for issues with null values and report it, the return type of check_null is a dict of the counts of nulls per column
    null_issues = check_nulls(df)

    # check for duplicate rows based on the 'order_id' column and report it, the return type of check_duplicates is a dict of boolean values indicating if each row is a duplicate based on the key column
    duplicate_issues = check_duplicates(df, 'order_id')

    # check for negative values in the 'amount' column and report it, the return type of check_negative_values is a dict of the counts of negative values per column
    negative_value_issues = check_negative_values(df, ['amount'])

    # check for future dates in the 'order_date' column and report it, the return type of check_future_dates is a dict of the counts of future dates per column
    future_date_issues = check_future_dates(df, 'order_date')

    # check for invalid email formats in the 'email' column and report it, the return type of check_email_format is a dict of the counts of invalid email formats per column    
    email_format_issues = check_email_format(df, 'email')

    # check for invalid status values in the 'status' column and report it, the return type of check_status_values is a dict of the counts of invalid status values per column
    status_value_issues = check_status_values(df, 'status', ['pending', 'completed', 'cancelled'])

    # Calculate total issues found
    total_issues = sum(null_issues.values()) + sum(duplicate_issues.values()) + sum(negative_value_issues.values()) + sum(future_date_issues.values()) + sum(email_format_issues.values())

    # Add summary to report
    report += f"## Summary\n\n"
    report += f"- Total Rows: {total_rows}\n"
    report += f"- Total Issues Found: {total_issues}\n\n"

    # Add details to report
    report += f"## Detailed Results\n\n"
    report += f"### Null Values\n\n"
    # add count of null values per column to report
    for column, count in null_issues.items():
        report += f"- {column}: {count} null values\n"
    report += "\n"

    report += f"### Duplicate Rows\n\n"
    # add count of duplicate rows based on the 'order_id' column to report
    for column, is_duplicate in duplicate_issues.items():
        if is_duplicate:
            report += f"- Row {column} is a duplicate based on 'order_id'\n"
    report += "\n"

    report += f"### Negative Values\n\n"
    # add count of negative values in the 'amount' column to report
    for column, count in negative_value_issues.items():
        report += f"- {column}: {count} negative values\n"
    report += "\n"    

    report += f"### Future Dates\n\n"   

    # add count of future dates in the 'order_date' column to report
    for column, count in future_date_issues.items():
        report += f"- {column}: {count} future dates\n"    
    report += "\n"

    report += f"### Invalid Email Formats\n\n"

    # add count of invalid email formats in the 'email' column to report
    for column, count in email_format_issues.items():
        report += f"- {column}: {count} invalid email formats\n"    
    report += "\n"

    # add count of invalid status values in the 'status' column to report
    report += f"### Invalid Status Values\n\n"
    for column, count in status_value_issues.items():
        report += f"- {column}: {count} invalid status values\n"
    report += "\n"


    # Add severity rating to report
    if total_issues == 0:
        report += "## Severity Rating: PASS\n\n"
    elif total_issues <= 5:
        report += "## Severity Rating: WARNING\n\n"
    else:
        report += "## Severity Rating: FAIL\n\n"

    # Add recommendations to report
    report += "## Recommendations\n\n"
    report += "- Fix null values\n"
    report += "- Remove duplicate rows\n"
    report += "- Fix negative values\n"
    report += "- Fix future dates\n"
    report += "- Fix invalid email formats\n"

    return report


