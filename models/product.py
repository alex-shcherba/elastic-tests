from datetime import datetime

from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int = Field(alias='_id')
    base_price: float
    discount_percentage: int
    quantity: int
    manufacturer: str
    tax_amount: float
    product_id: int
    category: str
    sku: str
    taxless_price: float
    unit_discount_amount: float
    min_price: float
    id: str
    discount_amount: float
    created_on: datetime
    product_name: str
    price: float
    taxful_price: float
    base_unit_price: float
