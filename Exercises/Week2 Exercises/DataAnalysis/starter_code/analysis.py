
import pandas as pd
def load_data(filepath):
    """
    Load the orders dataset.
    - Parse dates correclsctly
    - Handle missing values
    - Return a clean DataFrame
    """
    # loading
    df = pd.read_csv(filepath, parse_dates=["order_date"]) # handles dates and all missing values are nan by default (which is what I want)

    return df




def explore_data(df):
    """
    Print basic statistics about the dataset:
    - Shape (rows, columns)
    - Data types
    - Missing value counts
    - Basic statistics for numeric columns
    - Date range covered
    """
    data_types_str = ",".join(df.iloc[0].apply(lambda x: str(type(x)))) # gets the types of all columns
    

    print(f"""
    ------Basic Information------
    shape: {df.shape}
    data types: {data_types_str}
    missing value counts: {df.isnull().sum().sum()}
    basic stats on quant, price
        - max price: {max(df["unit_price"])}
        - min price: {min(df["unit_price"])}
        - average quantity sold: {df["quantity"].mean()}
    
    date range: {min(df["order_date"])} - {max(df["order_date"])}

""")
    

def clean_data(df):
    """
    Clean the dataset:
    - Remove duplicates
    - Fill or drop missing values (document your strategy)
    - Standardize text columns (strip whitespace, consistent case)
    - Add calculated columns: 'total_amount' = quantity * unit_price
    """
    # drop duplicates
    df.drop_duplicates(inplace=True)

    # fill/drop missing values, my strategy is to drop an entire row if it has missing data.
    df.dropna(inplace = True)

    standardize = lambda x : x.strip().lower()

    # standardize text columns : I think only category and region makes sense for this
    df["category"] = df["category"].apply(standardize) # strips white space from category and make it all lower case
    df["region"] = df["region"].apply(standardize)

    return df


def add_time_features(df):
    """
    Add time-based features:
    - day_of_week (0=Monday, 6=Sunday)
    - month
    - quarter
    - is_weekend (boolean)
    """
    dates = df["order_date"]

    # get which day it is based off the info
    day_dictionary = {0: "Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
    #print("date:",dates.dt.day, "type:", type(dates.dt.day))
    day_of_the_week = dates.dt.day.apply(lambda x : day_dictionary[x%7])
    #print("Day of the week:", day_of_the_week)
    #print(df)

    # get the month
    month = dates.dt.month

    # which quarter is it in
    quarter = month.apply(lambda x: x % 4)

    # check if day is sunday or saturday
    is_weekend = []
    for day in day_of_the_week:
        if day == "Saturday" or day == "Sunday":
            is_weekend.append(True)
        else:
            is_weekend.append(False)

    # adding features to the df
    df["day"] = day_of_the_week
    df["month"] = month
    df["quarter"] = quarter
    df["weekend"] = is_weekend
    return df


def sales_by_category(df):
    """
    Calculate total sales and order count by category.
    Returns: DataFrame with columns [category, total_sales, order_count, avg_order_value]
    Sorted by total_sales descending.
    """
    categories = df.groupby("category") # groupby object that I act on (seperates into categories)
    total_sales = categories["quantity"].sum() # gets sum of quantity
    order_count = categories.size() # counts length of each group after groupby
    avg_order_amt = categories["unit_price"].mean() # gets mean unit_price
    #print(list(categories.groups.keys()))
    salesdata = {
        "category":list(categories.groups.keys()),
        "total_sales": list(total_sales),
        "order_count": list(order_count),
        "avg_order_value":list(avg_order_amt)

    }
    return pd.DataFrame(salesdata)

    

def sales_by_region(df):
    """
    Calculate total sales by region.
    Returns: DataFrame with columns [region, total_sales, percentage_of_total]
    """
    # same structure as sales_by_category except we group by region
    
    # this is still called categories because its the same code, its actually regions
    categories = df.groupby("region") # groupby object that I act on (seperates into REGIONS)
    total_sales = categories["quantity"].sum() # gets sum of quantity
    order_count = categories.size() # counts length of each group after groupby
    avg_order_amt = categories["unit_price"].mean() # gets mean unit_price
    #print("TEST",categories["unit_price"].mean())
    #print(list(categories.groups.keys()))
    salesdata = {
        "region":list(categories.groups.keys()),
        "total_sales": list(total_sales),
        "order_count": list(order_count),
        "avg_order_value":list(avg_order_amt)

    }
    return pd.DataFrame(salesdata)
    

def top_products(df, n=10):
    """
    Find top N products by total sales.
    Returns: DataFrame with columns [product_name, category, total_sales, units_sold]
    """
    ordered_df = df

    ordered_df["total_sales"] = ordered_df["quantity"] * ordered_df["unit_price"] # get a total sales column for my math
    ordered_df.sort_values(by=["total_sales"]) # sorts values by the total sales we just made

    product_group = ordered_df.groupby("product_name")
    total_sales = product_group["total_sales"].sum()
    units_sold = product_group["quantity"].sum()
    product_name = product_group.groups.keys()
    category = product_group["category"].apply(lambda x: x)

    salesdata = {
        "product_name":list(product_name),
        "category": list(category),
        "total_sales": list(total_sales),
        "units_sold":list(units_sold)

    }
    return pd.DataFrame(salesdata)



def daily_sales_trend(df):
    """
    Calculate daily sales totals.
    Returns: DataFrame with columns [date, total_sales, order_count]
    """
    # reusing code to add total_sales
    ordered_df = df

    ordered_df["total_sales"] = ordered_df["quantity"] * ordered_df["unit_price"] # get a total sales column for my math

    daily_group = ordered_df.groupby("product_name")
    total_sales = daily_group["total_sales"].sum()
    date = daily_group.groups.keys()
    order_count = daily_group.size()

    salesdata = {
        "date":list(date),
        "total_sales": list(total_sales),
        "order_count": list(order_count)

    }
    return pd.DataFrame(salesdata)

def customer_analysis(df):
    """
    Analyze customer purchasing behavior.
    Returns: DataFrame with columns [customer_id, total_spent, order_count, 
             avg_order_value, favorite_category]
    """
    # reusing code to add total_sales
    ordered_df = df

    ordered_df["total_sales"] = ordered_df["quantity"] * ordered_df["unit_price"] # get a total sales column for my math

    customer_group = ordered_df.groupby("customer_id")
    total_spent = customer_group["total_sales"].sum()
    order_count = customer_group.size()
    avg_order_value = customer_group["total_sales"].mean()
    favorite_category = list(customer_group["category"].agg(pd.Series.mode).iloc[0]) # get most frequent seen category per customer
    
    salesdata = {
        "customer_id":list(customer_group.groups.keys()),
        "total_spent": list(total_spent),
        "order_count": list(order_count),
        "avg_order_value" : list(avg_order_value),
        "favorite_category" : list(favorite_category)

    }
    return pd.DataFrame(salesdata)
    #print("cat:", favorite_category)
    #print("END---")

def weekend_vs_weekday(df):
    """
    Compare weekend vs weekday sales.
    Returns: Dict with weekend and weekday total sales and percentages.
    """
    time_df = add_time_features(df)
    # reusing code to add total_sales
    ordered_df = time_df
    ordered_df["total_sales"] = ordered_df["quantity"] * ordered_df["unit_price"] # get a total sales column for my math

    time_group = ordered_df.groupby("weekend")
    total_sales = time_group["total_sales"].sum()
    percentages = time_group.size()/time_df.shape[0]

    
    salesdata = {
        "is_weekend":list(time_group.groups.keys()),
        "total_sales": list(total_sales),
        "percentages": list(percentages)

    }
    return pd.DataFrame(salesdata)


if __name__ == "__main__":
    df = load_data("orders.csv")
    #explore_data(df)

    df2 = load_data("malformed_order.csv")
    #explore_data(df2)

    #print("before:", df2)
    #print("\n\nAfter:",clean_data(df2))

    df2 = clean_data(df2)

    #df3 = add_time_features(df2)
    #print("TESTING time features\n\n\n",df3)
    

    #salesDF = sales_by_category(df)
    #print(salesDF)

    #regionDF = sales_by_region(df)
    #print(regionDF)

    #productsDF = top_products(df)
    #print(productsDF)

    #customerDF = customer_analysis(df)
    #print(customerDF)

    weekendDF = weekend_vs_weekday(df2)
    print(weekendDF)