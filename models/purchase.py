from datetime import datetime
from typing import List

from pydantic import BaseModel

from models.event import Event
from models.geoip import Geoip
from models.product import Product


class Purchase(BaseModel):
    category: List[str]
    currency: str
    customer_first_name: str
    customer_full_name: str
    customer_gender: str
    customer_id: int
    customer_last_name: str
    customer_phone: str
    day_of_week: str
    day_of_week_i: int
    email: str
    manufacturer: List[str]
    order_date: datetime
    order_id: int
    products: List[Product]
    sku: List[str]
    taxful_total_price: float
    taxless_total_price: float
    total_quantity: int
    total_unique_products: int
    type: str
    user: str
    geoip: Geoip
    event: Event
