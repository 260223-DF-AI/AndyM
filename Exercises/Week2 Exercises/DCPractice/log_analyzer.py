from decorators import timer, logger, cache
from generators import read_lines, batch, filter_errors
from pipeline import create_pipeline

@timer
@logger
def analyze_logs(log_path):
    """
    Analyze a log file and return statistics.
    
    Uses generators for memory-efficient processing.
    Uses decorators for timing and logging.
    """
    gen = read_lines(log_path)

    error_info = {"ERROR": 0, "INFO" : 0, "WARN":0, "DEBUG":0, "OTHER":0}

    for log in gen:
        if "ERROR" in log:
            error_info["ERROR"] += 1
        elif "INFO" in log:
            error_info["INFO"] += 1
        elif "WARN" in log:
            error_info["WARN"] += 1
        elif "DEBUG" in log:
            error_info["DEBUG"] += 1
        else:
            error_info["OTHER"] += 1
    return error_info



@cache(max_size=1000)
def parse_log_line(line):
    """
    Parse a single log line into structured data.
    Cached because the same line format appears often.
    """
    data = {"Error_type":"", "text":""}
    if "ERROR" in line:
        data["error_type"] = "ERROR"
    elif "INFO" in line:
        data["error_type"] = "INFO"
    elif "WARN" in line:
        data["error_type"] = "WARN"
    elif "DEBUG" in line:
        data["DEBUG"] = "DEBUG"
    else:
        data["OTHER"] = "OTHER"

def count_by_level(log_path):
    """
    Count log entries by level (INFO, WARNING, ERROR).
    Use generators to process without loading entire file.
    """
    data = analyze_logs(log_path)

    return data


def get_error_summary(log_path, top_n=10):
    """
    Get top N most common error messages.
    """
    data = log_path

    values = data.values().sort()

    return values[:top_n]


def process_logs_in_batches(log_path, batch_size=1000):
    """
    Process logs in batches for database insertion.
    Yields batches of parsed log entries.
    """
    pass