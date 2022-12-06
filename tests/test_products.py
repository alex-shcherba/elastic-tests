from inspections.product import ProductInspection
from inspections.validators import PurchaseValidator as Validator


def test_product_prices(products_by_chunk):
    """The product price calculation (unknown math)"""
    validator = Validator(products_by_chunk)
    validator.check(ProductInspection.min_price_is_allowed)
    validator.check(ProductInspection.base_price_is_allowed)
    validator.check(ProductInspection.base_unit_price_is_allowed)
    validator.check(ProductInspection.taxless_price_is_allowed)
    validator.check(ProductInspection.taxful_price_is_allowed)
    validator.check_all()


def test_tax_amount(products_by_chunk):
    """The product's manufacturer"""
    validator = Validator(products_by_chunk)
    validator.check(ProductInspection.tax_amount_is_allowed)
    validator.check_all()


def test_quantity(products_by_chunk):
    """The product's quantity"""
    validator = Validator(products_by_chunk)
    validator.check(ProductInspection.quantity_is_allowed)
    validator.check_all()


def test_discounts(products_by_chunk):
    """The product's discount allowed values and calculation (unknown math)"""
    validator = Validator(products_by_chunk)
    validator.check(ProductInspection.unit_discount_amount_is_allowed)
    validator.check(ProductInspection.discount_amount_is_allowed)
    validator.check(ProductInspection.discount_percent_is_allowed)
    validator.check_all()


def test_manufacturer(products_by_chunk):
    """The product's manufacturer is allowed"""
    validator = Validator(products_by_chunk)
    validator.check(ProductInspection.manufacturer_is_allowed)
    validator.check_all()


def test_category(products_by_chunk):
    """The product's category is allowed"""
    validator = Validator(products_by_chunk)
    validator.check(ProductInspection.category_is_allowed)
    validator.check_all()


def test_sku(products_by_chunk):
    """The product's SKU has a special format"""
    validator = Validator(products_by_chunk)
    validator.check(ProductInspection.sku_is_allowed)
    validator.check_all()
