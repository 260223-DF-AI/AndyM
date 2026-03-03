"""Main file to read a csv file and generate report"""
from exceptions import *
import os

def read_csv_file(filepath):
    """
    Read a CSV file and return a list of dictionaries.
    
    Should handle:
    - FileNotFoundError
    - UnicodeDecodeError (try utf-8, then latin-1)
    - Empty files
    
    Returns: List of dictionaries (one per row)
    Raises: FileProcessingError with descriptive message
    """
    try:
        # make sure filepath exists
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"{filepath} not found")
        
        columns = []
        entries = []
        # start reading the file
        with open(filepath, "r") as f:
            for i, line in enumerate(f):

                if line.endswith("\n"): # if the line ends with \n, get rid of it
                    line = line[:len(line)-1]

                row = line.split(",") # the row of data

                if i == 0: # capture the column names
                    columns = row
                    continue


                # create the dictionary entry
                entry = {
                    columns[0]:row[0], # date
                    columns[1]:row[1], # store_id
                    columns[2]:row[2], # product
                    columns[3]:row[3], # quantity
                    columns[4]:row[4] # price
                }

                # append to our return thing
                entries.append(entry)
        return entries

    # most the logging is already done in exceptions.py, just re-raise
    except FileNotFoundError as e: # file wasn't found, tell user and have them try again?
        print(f"The filepath provided: {filepath} is invalid.")
        raise FileProcessingError(filepath)
        
    except UnicodeDecodeError: # try utf-8 first, then latin-1 if utf fails
        raise FileProcessingError(filepath)
    except Exception as e: # not expecting such an error, log it and exit for now
        print("e:",e)
        log_it(f"Generic Error has occured : {e}", ERROR)
        raise FileProcessingError(filepath)
    


if __name__ == "__main__":
    rows = read_csv_file("sample_sales.csv")
    for row in rows:
        print(row)
    empty = read_csv_file("empty_file.csv")
    print("should be empty:", empty)