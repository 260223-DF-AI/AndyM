# Exercise: AI Code Review Challenge

## Exercise ID: e024

## Overview

In this exercise, you will review AI-generated code for correctness, security, and best practices. You will act as the senior engineer reviewing pull requests from an "AI junior developer." This exercise builds the critical review skills necessary for production-quality AI-assisted development.

## Learning Objectives

- Review AI-generated code systematically for bugs and vulnerabilities
- Identify common patterns where AI produces incorrect or insecure code
- Apply a structured review checklist to AI output
- Improve AI-generated code to meet production standards

## Prerequisites

- Python 3.10+ knowledge
- SQL/BigQuery knowledge
- Completed Thursday written content on AI testing and debugging

## Time Estimate

45-60 minutes

---

## Part 1: Bug Detection (20 minutes)

Review the following AI-generated code snippets. Each contains at least one bug. Find and fix all bugs.

### Snippet 1: Data Deduplication

The AI was asked: "Write a Python function to deduplicate a DataFrame keeping the most recent record."

```python
def deduplicate_records(df, key_column, date_column):
    """Remove duplicate records, keeping the most recent."""
    if df is None:
        raise ValueError("DataFrame cannot be None")
    
    if key_column not in df.columns:
        raise KeyError(f"Key column '{key_column}' not found in DataFrame")
    
    if date_column not in df.columns:
        raise KeyError(f"Date column '{date_column}' not found in DataFrame")
    
    df_sorted = df.sort_values(date_column, ascending=True)
    df_deduped = df_sorted.drop_duplicates(subset=key_column, keep='last')
    return df_deduped
```

**Questions:**

1. What bug(s) exist in this code?
    - Ascending would cause everything except the oldest record to be dropped
    - `keep` should be `last`
2. What is the fix?
    - change `keep` to `last`
3. What edge cases are not handled?
    - df is empty
    - df has mismatched formats
    - random garbage inside df

### Snippet 2: BigQuery Table Creation

The AI was asked: "Write a function to create a partitioned BigQuery table."

```python
from google.cloud import bigquery
from google.api_core.exceptions import Conflict

def create_partitioned_table(project_id, dataset_id, table_id, overwrite=False):
    """
    Create a partitioned BigQuery table with best practices.

    Args:
        project_id (str): Google Cloud project ID
        dataset_id (str): BigQuery dataset ID
        table_id (str): Table ID
        overwrite (bool): Whether to overwrite if table exists

    Returns:
        bigquery.Table
    """
    client = bigquery.Client(project=project_id)

    table_ref = f"{project_id}.{dataset_id}.{table_id}"

    # Define schema (FIXED: amount uses NUMERIC)
    schema = [
        bigquery.SchemaField("order_id", "INT64", mode="REQUIRED"),
        bigquery.SchemaField("customer_id", "INT64", mode="REQUIRED"),
        bigquery.SchemaField("order_date", "DATE", mode="REQUIRED"),
        bigquery.SchemaField("amount", "NUMERIC", mode="REQUIRED"),
    ]

    table = bigquery.Table(table_ref, schema=schema)

    # Partitioning
    table.time_partitioning = bigquery.TimePartitioning(
        type_=bigquery.TimePartitioningType.DAY,
        field="order_date",
        # Removed expiration for production safety
    )

    # Optional: clustering for performance
    table.clustering_fields = ["customer_id"]

    try:
        if overwrite:
            table = client.create_table(table, exists_ok=True)
            print(f"Table {table_id} created or replaced.")
        else:
            table = client.create_table(table)
            print(f"Table {table_id} created.")

    except Conflict:
        print(f"Table {table_id} already exists.")
        if overwrite:
            client.delete_table(table_ref, not_found_ok=True)
            table = client.create_table(table)
            print(f"Table {table_id} overwritten.")
        else:
            table = client.get_table(table_ref)

     return table
```

**Questions:**

1. Is this code functionally correct?
    - probably
2. What happens if the table already exists?
    - it would fail and not overwrite because we didn't specify overwrite
3. What data type issue exists with the `amount` field for financial data?
    - float, which could be inaccurate for currency
4. Is `expiration_ms` appropriate for a production fact table? What risks does it create?
    - maybe not since it's not immediadely readable
    - not good because it could silently delete after 90 days

    ### Snippet 3: CSV Processing Pipeline

    The AI was asked: "Write a function to process CSV files and load to BigQuery."

    ```python
    import pandas as pd
    import logging
    from google.cloud import bigquery
    from google.api_core.exceptions import GoogleAPIError

    logging.basicConfig(level=logging.INFO)

    def process_and_load(file_path, table_id):
        client = bigquery.Client()

        try:
            # Read CSV
            df = pd.read_csv(file_path)
            logging.info(f"Loaded file: {file_path} with {len(df)} rows")

        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
            return

        # Validate required columns
        required_cols = {'date', 'amount'}
        if not required_cols.issubset(df.columns):
            logging.error(f"Missing required columns: {required_cols}")
            return

        # Convert date safely
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        invalid_dates = df['date'].isna().sum()

        # Convert amount safely (use numeric, not float)
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
        invalid_amounts = df['amount'].isna().sum()

        # Drop only critical nulls
        before_rows = len(df)
        df = df.dropna(subset=['date', 'amount'])
        dropped_rows = before_rows - len(df)

        logging.info(f"Dropped {dropped_rows} rows")
        logging.info(f"Invalid dates: {invalid_dates}, invalid amounts: {invalid_amounts}")

        # BigQuery load config
        job_config = bigquery.LoadJobConfig(
            write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
        )

        try:
            job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
            job.result()

            logging.info(f"Loaded {len(df)} rows to {table_id}")
            logging.info(f"Job ID: {job.job_id}")

        except GoogleAPIError as e:
            logging.error(f"BigQuery load failed: {e}")
            return
    ```



    **Questions:**

    1. What happens if the file does not exist?
    - it would fail, filenotfound err
    2. What happens if the `date` column contains invalid dates?
    - it would fail, throwing an error when you try to convert
    3. Is `dropna()` appropriate? What data might be lost?
    - dropna is considered very aggressive and you could lose a lot of data
    4. What write disposition is used by default? Is this safe?
    - no clue
    - AI says its WRITE_APPEND which appends data to existing table
    5. What logging/monitoring is missing?
    - everything

---

## Part 2: Security Review (15 minutes)

Review these AI-generated snippets for security issues.

### Snippet 4: Database Connection

```python
import os
from google.cloud import bigquery

def get_client():
    # Service account credentials
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/app/keys/service-account.json'
    client = bigquery.Client(project='production-project-12345')
    return client

def run_query(query_text):
    client = get_client()
    query = f"SELECT * FROM analytics.customers WHERE name = '{query_text}'"
    results = client.query(query).result()
    return [dict(row) for row in results]
```
```python
    from google.cloud import bigquery
from google.cloud.bigquery import QueryJobConfig, ScalarQueryParameter
import logging

# Create client ONCE (uses default credentials / IAM role)
client = bigquery.Client(project="production-project-12345")

def run_query(name: str):
    """
    Safely query customer data by name.
    """

    # Basic input validation
    if not name or len(name) > 100:
        raise ValueError("Invalid name input")

    # Parameterized query (PREVENTS SQL INJECTION)
    query = """
        SELECT customer_id, name
        FROM `production-project-12345.analytics.customers`
        WHERE name = @name
        LIMIT 100
    """

    job_config = QueryJobConfig(
        query_parameters=[
            ScalarQueryParameter("name", "STRING", name)
        ]
    )

    try:
        job = client.query(query, job_config=job_config)
        results = job.result()

        rows = [dict(row) for row in results]

        logging.info(f"Query executed. Rows returned: {len(rows)} | Job ID: {job.job_id}")

        return rows

    except Exception as e:
        logging.error(f"Query failed: {e}")
        raise

```


**Questions:**

1. Identify ALL security issues in this code
    - easy to sql injection
2. For each issue, explain the risk
    - malicious user input could ruin your DB, leak sensitive data
3. Rewrite the code with proper security practices


### Snippet 5: API Key Usage

```python
import requests

OPENAI_API_KEY = "sk-proj-abc123def456ghi789..."

def generate_summary(text):
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-4",
            "messages": [{"role": "user", "content": text}]
        }
    )
    return response.json()['choices'][0]['message']['content']
```

```python
    import os
import requests

def generate_summary(text):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY not set")

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-4",
            "messages": [{"role": "user", "content": text}]
        },
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    return data["choices"][0]["message"]["content"]

```


**Questions:**

1. What is the primary security issue?
    - the key is stored in plaintext
2. What happens if this code is committed to a public repository?
    - it would be exposed
    - boss gets email and mad
3. Rewrite using secure credential management
    - ok

---

## Part 3: Best Practices Review (10 minutes)

### Snippet 6: Data Validation

The AI was asked: "Write data validation for our ETL pipeline."

```python
def validate(df):
    if len(df) == 0:
        return False
    if df.isnull().sum().sum() > 0:
        return False
    for col in df.columns:
        if df[col].dtype == 'object':
            if df[col].str.len().max() > 1000:
                return False
    return True
```

**Questions:**

1. What are the code quality issues?
    - no input validation
    - we just return false if any issues
2. The function returns a boolean -- is this sufficient for production use?
    - no we would want to see what failed, what cols
3. Rewrite to provide detailed validation results (which checks failed and why)
4. Add proper logging and documentation


```python
import logging
from typing import Dict, Any
import pandas as pd

logging.basicConfig(level=logging.INFO)

def validate_dataframe(
    df: pd.DataFrame,
    max_string_length: int = 1000,
    required_columns: list[str] | None = None
) -> Dict[str, Any]:
    """
    Validate a pandas DataFrame against basic data quality rules.

    Args:
        df (pd.DataFrame): Input DataFrame to validate
        max_string_length (int): Maximum allowed string length
        required_columns (list[str], optional): Columns that must not contain nulls

    Returns:
        dict: Validation result with:
            - is_valid (bool)
            - errors (list)
            - warnings (list)
            - metrics (dict)
    """

    result = {
        "is_valid": True,
        "errors": [],
        "warnings": [],
        "metrics": {}
    }

    # ✅ Input validation
    if not isinstance(df, pd.DataFrame):
        msg = "Input is not a pandas DataFrame"
        logging.error(msg)
        result["errors"].append(msg)
        result["is_valid"] = False
        return result

    # ✅ Empty DataFrame check
    if df.empty:
        msg = "DataFrame is empty"
        logging.error(msg)
        result["errors"].append(msg)
        result["is_valid"] = False

    # ✅ Null checks (configurable)
    null_counts = df.isnull().sum()
    total_nulls = int(null_counts.sum())

    result["metrics"]["total_nulls"] = total_nulls

    if total_nulls > 0:
        msg = f"DataFrame contains {total_nulls} null values"
        logging.warning(msg)
        result["warnings"].append(msg)

    # Required columns null check
    if required_columns:
        for col in required_columns:
            if col not in df.columns:
                msg = f"Missing required column: {col}"
                logging.error(msg)
                result["errors"].append(msg)
                result["is_valid"] = False
                continue

            null_count = int(df[col].isnull().sum())
            if null_count > 0:
                msg = f"Column '{col}' has {null_count} null values"
                logging.error(msg)
                result["errors"].append(msg)
                result["is_valid"] = False

    # ✅ String length validation
    for col in df.select_dtypes(include=["object", "string"]).columns:
        try:
            max_len = df[col].astype(str).str.len().max()
        except Exception as e:
            msg = f"Error processing column '{col}': {e}"
            logging.error(msg)
            result["errors"].append(msg)
            result["is_valid"] = False
            continue

        result["metrics"][f"{col}_max_length"] = int(max_len) if pd.notna(max_len) else 0

        if max_len and max_len > max_string_length:
            msg = f"Column '{col}' exceeds max length ({max_len} > {max_string_length})"
            logging.error(msg)
            result["errors"].append(msg)
            result["is_valid"] = False

    # ✅ Final status
    if result["is_valid"]:
        logging.info("Validation passed")
    else:
        logging.error("Validation failed")

    return result

```

---

## Part 4: Improvement Exercise (Optional, 15 minutes)

Take any ONE snippet from above and create a production-ready version:

1. Fix all bugs and security issues
2. Add comprehensive error handling
3. Add logging
4. Add type hints and docstrings
5. Add input validation
6. Write 3 unit tests for the improved code

You may use AI assistance for this task, but you must review every line of the AI's output and justify each acceptance or modification.

---

## Review Checklist (Print and Use)

For each code snippet:

| # | Check | Status |
| - | ----- | ------ |
| 1 | Does it do what was requested? | |
| 2 | Input validation present? | |
| 3 | Error handling present? | |
| 4 | No hardcoded credentials? | |
| 5 | SQL injection prevention? | |
| 6 | Appropriate logging? | |
| 7 | Type hints included? | |
| 8 | Docstrings present? | |
| 9 | Edge cases handled? | |
| 10 | Would pass code review? | |

## Submission

Submit:

1. Your bug findings for each snippet (Part 1)
2. Your security analysis (Part 2)
3. Your best practices review (Part 3)
4. Your improved code (Part 4, if completed)
5. Brief reflection: What patterns did you notice in AI-generated code issues?



REFLECTION:
a lot of the code given to us was similar, it had very little error handling, and it was missing a lot of input validation. The security issues were mostly credential based.
