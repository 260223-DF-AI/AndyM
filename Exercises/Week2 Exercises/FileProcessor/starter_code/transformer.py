"""does stuff with data"""

def calculate_totals(records):
    """
    Calculate line totals (quantity * price) for each record.
    Returns: Records with added 'total' field
    """
    for record in records:
        # naming the variables from record
        quantity = record["quantity"]
        price = record["price"]

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
    totals = calculate_totals(records) # get the totals for each record first

    counter = {} # maps store id to the number of times we see it in the sales log (number of sales)
    for record in totals:
        store_id = record["store_id"]
        if not counter.get(store_id): # if it doesn't exist, add it to our tracker and set default val to 1
            counter[store_id] = record["total"]
        else: # another instance of seeing this store in sales record, add to it
            counter[store_id] += record["total"]
    
    return counter

def aggregate_by_product(records):
    """
    Aggregate sales by product.
    Returns: Dict mapping product to total quantity sold
    """
    counter = {} # maps product to the total amount we've seen it sell

    for record in records:
        product = record["product"]
        quantity = record["quantity"]
        if not counter.get(product): # if it doesn't exist, add it to our tracker and set default val to quant
            counter[product] = quantity
        else: # another instance of seeing this product, add its sold quantity
            counter[product] += quantity
    return counter