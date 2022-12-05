from typing import List

import pytest

from models.product import Product
from models.purchase import Purchase
from utils.files import read_json
from utils.helpers import make_chunks, make_date_chunks

elastic_data = read_json(filename='elastic_data.json')
purchases_data_raw = [hit['_source'] for hit in elastic_data['hits']['hits']]
purchases_data = [Purchase(**purchase_data) for purchase_data in purchases_data_raw]
products_data = [product for purchase in purchases_data for product in purchase.products]


@pytest.fixture(scope="session")
def purchases() -> List[Purchase]:
    """Top-level fixture with deserialization purchase's data files

    Note: option to update a way of data gathering without changing the result type
    :return: List[Purchase] - collection of purchases
    """
    return purchases_data


@pytest.fixture(scope="session", params=range(5), ids=lambda i: i + 1)
def purchases_by_date_period(request, purchases: List[Purchase]) -> List[Purchase]:
    """Parametrized fixture with purchases separated into equal groups"""
    time_periods = make_date_chunks(purchases, 5)
    return [purchase for purchase in purchases
            if time_periods[request.param] <= purchase.order_date < time_periods[request.param+1]]


@pytest.fixture(scope="session")
def products(purchases: List[Purchase]) -> List[Product]:
    """Top-level fixture with all products

    :param purchases: fixture with deserialization purchases
    :return: List[Product] - collection of all products
    """
    return products_data


@pytest.fixture(scope="session", params=range(20), ids=lambda i: i + 1)
def products_by_chunk(request, products: List[Product]) -> List[Product]:
    """Parametrized fixture with products which separated into equal groups"""
    return make_chunks(products, 20)[request.param]
