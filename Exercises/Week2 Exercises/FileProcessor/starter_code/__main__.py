from .processor import process_sales_file

def main():
    input_path = "./starter_code/sample_sales.csv"
    output_dir = "./starter_code/output/"
    process_sales_file(input_path, output_dir)
if __name__ == "__main__":
    main()