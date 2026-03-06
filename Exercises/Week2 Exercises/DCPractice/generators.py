def read_lines(filepath, encoding='utf-8'):
    """
    Yield lines from a file one at a time.
    - Strip whitespace from each line
    - Skip empty lines
    - Handle encoding errors gracefully
    
    Usage:
        for line in read_lines('large_file.txt'):
            process(line)
    """
    print("OI AM HERE")
    try:
        with open(filepath, "r") as f:
            for line in f:
                print("line:",line)
                cleaned_line = line.strip() # strip wspace
                if not cleaned_line: # skip empty lines
                    print("found empty line")
                    continue
                else:
                    yield cleaned_line # good

    except FileNotFoundError as e:
        print("FILE NOT FOUND")
        return None # file wasn't found just give them nothing
    except UnicodeError as e:
        if encoding == 'utf-8':
            read_lines(filepath, encoding='latin-1')
        else:
            raise # cry
    except Exception as e:
        print("ERROR:",e)
        raise


#### Task 2.2: Batch Generator (20 min)

def batch(iterable, size):
    """
    Yield items in batches of the specified size.
    
    Usage:
        list(batch([1,2,3,4,5,6,7], 3))
        # [[1,2,3], [4,5,6], [7]]
    """
    batch = []
    #it = iter(iterable)
    #print("iterable,",iterable)
    for item in iterable:
        if len(batch) < size:
            batch.append(item)
        else:
            yield batch
            batch = [item]
    yield batch

#### Task 2.3: Filter Generator (20 min)

def filter_by(iterable, predicate):
    """
    Yield items that match the predicate.
    
    Usage:
        evens = filter_by(range(10), lambda x: x % 2 == 0)
        list(evens)  # [0, 2, 4, 6, 8]
    """

    for item in iterable:
        if predicate(item):
            yield item
        else:
            continue


def filter_errors(log_lines):
    """
    Yield only lines containing 'ERROR'.
    """
    lines = log_lines.split("\n")
    for line in lines:
        line = line.strip()
        if "ERROR" in line:
            yield line


def filter_by_field(records, field, value):
    """
    Yield records where record[field] == value.
    
    Usage:
        active_users = filter_by_field(users, 'status', 'active')
    """
    for record in records:
        if record[field] == value:
            yield record