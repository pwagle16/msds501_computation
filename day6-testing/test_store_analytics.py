"""
test_store_analytics.py

Starter file for the "write your own tests" exercise.

pytest and the module under test are already imported below, and there's
one fully-worked example test to show you the pattern. Everything after
that is up to you: add your own test functions (name them test_something)
that check store_analytics.py against its docstrings.

Run your tests from this folder with:
    pytest -v
"""

import pytest
from store_analytics import (
    parse_order_row,
    compute_line_total,
    summarize_by_product,
    top_n_products,
    apply_bulk_discount,
    loyalty_tier,
    load_orders_from_csv,
    write_top_products_report,
)


# --- Example test (already written for you) -------------------------------

def test_parse_order_row_valid_row():
    row = ["1001", "Widget", "4", "9.99", "alice@example.com"]
    order = parse_order_row(row)
    assert order == {
        "order_id": "1001",
        "product": "widget",
        "quantity": 4,
        "unit_price": 9.99,
        "customer_email": "alice@example.com",
    }


# --- Your tests go below here ----------------------------------------------
def test_parse_order_row_negative_num():
    row = ['1003', 'Widget', '-1', '5.00', 'carol@example.com']
    with pytest.raises (ValueError):
        parse_order_row(row)

def test_parse_order_row_string():
    row = ['1004', 'Gizmo', 'abc', '3.50', 'carol@example.com']
    with pytest.raises (ValueError):
        parse_order_row(row)

def test_compute_line_total_multiply():
    order = {
        'order_id': '1001',
        'product': 'widget',
        'quantity':4,
        'unit_price': 9.99,
        'customer_email': 'alice@example.com'
    }
    total = compute_line_total(order)
    assert total == 39.96

def test_summarize_by_product_empty():
    order = []
    result = summarize_by_product(order)
    assert result == {}

def test_summarize_by_product_dict():
    order = [{
        'order_id': '1001',
        'product': 'widget',
        'quantity':4,
        'unit_price': 9.99,
        'customer_email': 'alice@example.com'},
    {
        'order_id': '1003',
        'product': 'widget',
        'quantity': 1,
        'unit_price': 5.00,
        'customer_email': 'carol@example.com'}]

    result = summarize_by_product(order)
    assert result == {
        'widget': {
            'total_quantity': 5,
            'total_revenue': 44.96,
            'order_count': 2
        }}

def test_loyalty_tier_none():
    total_spent = 99
    result = loyalty_tier(total_spent)
    assert result == 'none'

def test_loyalty_tier_silver():
    total_spent = 100
    result = loyalty_tier(total_spent)
    assert result == 'silver'

def test_loyalty_tier_valueE():
    total_spent = -1
    with pytest.raises(ValueError):
        loyalty_tier(total_spent)

def test_sort_key_products():
    


def test_top_n_products():





    

