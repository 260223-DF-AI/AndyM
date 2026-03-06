import datetime
def create_pipeline(*stages):
    """
    Create a processing pipeline from multiple generator functions.
    
    Usage:
        pipeline = create_pipeline(
            read_lines,
            parse_json,
            filter_valid,
            transform
        )
        
        for result in pipeline('input.json'):
            save(result)
    """
    for stage in stages:
        yield stage


# Example pipeline stages:

def parse_csv_line(lines):
    """Convert CSV lines to dictionaries."""
    columns = lines[0]
    lines=lines[1:]

    for line in lines:
        d = {}
        skip = False
        for i in range(len(columns)): # populate dictionary
            key = columns[i]
            val = line[i]
            if not val:
                skip
            d[key] = val
        yield d
    yield d # return our list of dictionaries (each line is its own dictionary)




def validate_records(records):
    """Yield only valid records, skip invalid ones."""
    for record in records:
        if not record: # reject, record is empty
            continue
        for key, val in record:
            if not val: # value is empty
                continue # reject this one
        yield record
        


def enrich_records(records):
    """Add calculated fields to each record."""

    # time stamp the record
    for record in records:
        record["time_stamp"] = datetime.now()
    return records

def deduplicate(records, key_field):
    """Yield unique records based on a key field."""
    seen = set()
    for record in records:
        if record[key_field] in seen:
            continue
        else:
            seen.add(record[key_field])
            yield record