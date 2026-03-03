"""Custom Exceptions, log -> reraise exception"""

LOG_FILE = "log.txt"
ERROR = "ERROR"
INFO = "INFO"

def log_it(text, level):
    from datetime import datetime
    timestamp = datetime.now()
    with open(LOG_FILE, "a") as f:
        f.write(f"<{timestamp}> [{level}]: + {text}")


class FileProcessingError(Exception):
    """Base exception for file processing errors."""
    def __init__(self, filename):
        log_it(f"File processing Error has occured processing {filename}", ERROR)
        raise RuntimeError()

class InvalidDataError(FileProcessingError):
    """Raised when data validation fails."""
    def __init__(self, data):
        log_it(f"validation has failed on: {data}", ERROR)
        raise RuntimeError()

class MissingFieldError(FileProcessingError):
    """Raised when a required field is missing."""
    def __init__(self, field):
        log_it(f"required {field} is missing", ERROR)
        raise RuntimeError()
