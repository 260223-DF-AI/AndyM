"""Custom Exceptions, log -> reraise exception"""

LOG_FILE = "log.txt"
ERROR = "ERROR"
INFO = "INFO"
WARNING = "WARNING"

def log_it(text, level):
    from datetime import datetime
    timestamp = datetime.now()
    with open(LOG_FILE, "a") as f:
        f.write(f"<{timestamp}> [{level}]: + {text}" + "\n")


class FileProcessingError(Exception):
    """Base exception for file processing errors."""
    def __init__(self, filename):
        log_it(f"File processing Error has occured processing {filename}", ERROR)
        super().__init__(f"Error processing file: {filename}")

class InvalidDataError(FileProcessingError):
    """Raised when data validation fails."""
    def __init__(self, msg):
        log_it(f"validation has failed on: {msg}", ERROR)
        super().__init__(msg)

class MissingFieldError(FileProcessingError):
    """Raised when a required field is missing."""
    def __init__(self,msg):
        log_it("required field is missing", ERROR)
        super().__init__(msg)
