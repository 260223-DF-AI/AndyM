import pytest
import pandas as pd
from analysis import *

@pytest.fixture
def sample_data():
    """Create sample data for testing."""
    return pd.DataFrame({
        'order_id': [1, 2, 3,3],
        'customer_id': ['C001', 'C002', 'C001','C001'],
        'order_date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-02','2024-01-02']),
        'product_name': ['Widget', 'Gadget', 'Widget', 'Widget'],
        'category': ['Electronics', 'Electronics', 'Electronics', 'Electronics'],
        'quantity': [2, 1, 3,3],
        'unit_price': [10.00, 25.00, 10.00,10.00],
        'region': ['North', 'South', 'North', 'North']
    })

def test_clean_data_removes_duplicates(sample_data):
    """Test that clean_data removes duplicate rows."""
    expected = pd.DataFrame({
        'order_id': [1, 2, 3],
        'customer_id': ['C001', 'C002', 'C001'],
        'order_date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-02']),
        'product_name': ['Widget', 'Gadget', 'Widget'],
        'category': ['electronics', 'electronics', 'electronics'],
        'quantity': [2, 1, 3],
        'unit_price': [10.00, 25.00, 10.00],
        'region': ['north', 'south', 'north']
    })
    result = clean_data(sample_data)
    #print(result)
    #print("\n\n", expected)
    #print(expected.compare(result))

    assert expected.equals(result)


def test_sales_by_category_calculation(sample_data):
    """Test that category totals are calculated correctly."""
    expected = pd.DataFrame({
        "category":["Electronics"],
        "total_sales": [9],
        "order_count": [4],
        "avg_order_value":[13.75]

    })

    result = sales_by_category(sample_data)
    #print("expected:",expected)
    #print("\n\nresult:",result)
    assert result.equals(expected)


def test_top_products_returns_correct_count(sample_data):
    """Test that top_products returns requested number of items."""
    result = top_products(sample_data)
   # print(result)
    salesdata = pd.DataFrame({
        "product_name":["Gadget", "Widget"],
        "category": ["Electronics", "Electronics"],
        "total_sales": [25.0,80.0],
        "units_sold":[1,8]

    })
    assert result.equals(salesdata)