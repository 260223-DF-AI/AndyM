"""Entry point for the data quality checker."""
import datetime
import pandas as pd
from report_generator import generate_report


def main():
    # Load data
    print("Loading data...")
    df = pd.read_csv('sample_data.csv')

    # Generate report
    print("Generating report...")
    report = generate_report(df)

    # Save report to file
    print("Saving report... to output/data_quality_report.md")
    with open('output/data_quality_report.md', 'w') as f:
        f.write(report)


if __name__ == "__main__":
    main()