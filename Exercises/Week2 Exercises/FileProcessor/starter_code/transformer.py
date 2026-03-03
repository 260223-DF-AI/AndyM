"""does stuff with data"""

def calculate_totals(records):
    """
    Calculate line totals (quantity * price) for each record.
    Returns: Records with added 'total' field
    """
    for record in records:
        # naming the variables from record
        quantity = record[3]
        price = record[4]

        # mathing
        total = quantity * price

        # adding total to the dict
        record["total"] = total
    return records

def aggregate_by_store(records):
    """
    Aggregate sales by store_id.
    Returns: Dict mapping store_id to total sales
    """
    counter = {} # maps store id to the number of times we see it in the sales log (number of sales)
    for record in records:
        store_id = record[1]
        if not counter.get(store_id): # if it doesn't exist, add it to our tracker and set default val to 0
            counter[store_id] = 0
        else: # another instance of seeing this store in sales record, add to it
            counter[store_id] += 1
    
    return counter

def aggregate_by_product(records):
    """
    Aggregate sales by product.
    Returns: Dict mapping product to total quantity sold
    """
    counter = {} # maps product to the total amount we've seen it sell

    for record in records:
        product = record[2]
        quantity = record[3]
        if not counter.get(product): # if it doesn't exist, add it to our tracker and set default val to 0
            counter[product] = 0
        else: # another instance of seeing this product, add its sold quantity
            counter[quantity] += 1
