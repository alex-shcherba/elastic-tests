from inspections.purchase import PurchaseInspection
from inspections.validators import PurchaseValidator as Validator


def test_customer_currency(purchases):
    """The currency is on the list of allowed values"""
    validator = Validator(purchases)
    validator.check(PurchaseInspection.currency_is_allowed)
    validator.check_all()


def test_customer_full_name(purchases):
    """The first + last name is equal to full name"""
    validator = Validator(purchases)
    validator.check(PurchaseInspection.first_name_is_not_empty)
    validator.check(PurchaseInspection.last_name_is_not_empty)
    validator.check(PurchaseInspection.full_name_is_configured)
    validator.check_all()


def test_customer_gender(purchases):
    """The gender is on the list of allowed values"""
    validator = Validator(purchases)
    validator.check(PurchaseInspection.gender_is_allowed)
    validator.check_all()


def test_customer_email_format(purchases):
    """The email has a special format"""
    validator = Validator(purchases)
    validator.check(PurchaseInspection.email_has_special_format)
    validator.check_all()


def test_customer_phone_format(purchases):
    """The phone has a special format"""
    validator = Validator(purchases)
    validator.check(PurchaseInspection.phone_has_special_format)
    validator.check_all()


def test_date_day_of_week(purchases):
    """Check that date has right day (number)"""
    validator = Validator(purchases)
    validator.check(PurchaseInspection.day_of_week_match_date)
    validator.check(PurchaseInspection.day_of_week_number_match_date)
    validator.check_all()


def test_taxful_total_price(purchases):
    """The purchase tax full total price list consists of set values in the products"""
    validator = Validator(purchases)
    validator.check(PurchaseInspection.taxful_total_price_sum)
    validator.check_all()


def test_taxless_total_price(purchases):
    """The purchase tax less total price list consists of set values in the products"""
    validator = Validator(purchases)
    validator.check(PurchaseInspection.taxles_total_price_sum)
    validator.check_all()


def test_total_quantity_products(purchases):
    """Total quantity products is equal to sum of products quantities"""
    validator = Validator(purchases)
    validator.check(PurchaseInspection.total_quantity_products)
    validator.check_all()


def test_unique_products(purchases):
    """Unique quantity products is equal to number of products"""
    validator = Validator(purchases)
    validator.check(PurchaseInspection.uniq_quantity_products)
    validator.check(PurchaseInspection.uniq_products)
    validator.check_all()


def test_purchases_manufacturer(purchases):
    """The purchase manufacture list consists of set values in the products"""
    validator = Validator(purchases)
    validator.check(PurchaseInspection.manufacturer_is_collected)
    validator.check_all()


def test_purchases_category(purchases):
    """The purchase category list consists of set values in the products"""
    validator = Validator(purchases)
    validator.check(PurchaseInspection.category_is_collected)
    validator.check_all()


def test_purchases_sku(purchases):
    """The purchase sku list consists of set values in the products"""
    validator = Validator(purchases)
    validator.check(PurchaseInspection.sku_is_collected)
    validator.check_all()
