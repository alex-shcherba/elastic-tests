import re
from collections import Counter

from enums.errors import PurchaseError
from models.purchase import Purchase
from utils.helpers import get_precision


class PurchaseInspection:

    @staticmethod
    def currency_is_allowed(purchase: Purchase):
        if purchase.currency == '':
            return PurchaseError.EMPTY_CURRENCY
        elif purchase.currency not in ['EUR', 'USD']:
            return PurchaseError.INVALID_CURRENCY

    @staticmethod
    def gender_is_allowed(purchase: Purchase):
        if purchase.customer_gender == '':
            return PurchaseError.EMPTY_GENDER
        elif purchase.customer_gender not in ['MALE', 'FEMALE']:
            return PurchaseError.INVALID_GENDER

    @staticmethod
    def first_name_is_not_empty(purchase: Purchase):
        if purchase.customer_first_name == '':
            return PurchaseError.EMPTY_FIRST_NAME

    @staticmethod
    def last_name_is_not_empty(purchase: Purchase):
        if purchase.customer_last_name == '':
            return PurchaseError.EMPTY_LAST_NAME

    @staticmethod
    def full_name_is_configured(purchase: Purchase):
        if purchase.customer_full_name == '':
            return PurchaseError.EMPTY_FULL_NAME
        elif purchase.customer_full_name != f'{purchase.customer_first_name} {purchase.customer_last_name}':
            return PurchaseError.INVALID_FULL_NAME

    @staticmethod
    def email_has_special_format(purchase: Purchase):
        if purchase.email == '':
            return PurchaseError.EMPTY_EMAIL
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', purchase.email):
            return PurchaseError.INVALID_EMAIL

    @staticmethod
    def phone_has_special_format(purchase: Purchase):
        if purchase.customer_phone == '':
            return PurchaseError.EMPTY_PHONE
        # TODO: implement format validation

    @staticmethod
    def day_of_week_match_date(purchase: Purchase):
        if purchase.day_of_week == '':
            return PurchaseError.EMPTY_WEEK_DAY
        elif purchase.day_of_week != purchase.order_date.strftime('%A'):
            return PurchaseError.INVALID_WEEK_DAY

    @staticmethod
    def day_of_week_number_match_date(purchase: Purchase):
        if purchase.day_of_week_i != purchase.order_date.weekday():
            return PurchaseError.INVALID_WEEK_DAY_NUMBER

    @staticmethod
    def taxful_total_price_sum(purchase: Purchase):
        if purchase.taxful_total_price <= 0:
            return PurchaseError.NEGATIVE_TAXFUL_TOTAL
        precision = get_precision(purchase.taxful_total_price)
        expected_total_price = round(sum([product.taxful_price for product in purchase.products]), precision)
        if purchase.taxful_total_price != expected_total_price:
            return PurchaseError.INVALID_TAXFUL_TOTAL

    @staticmethod
    def taxles_total_price_sum(purchase: Purchase):
        if purchase.taxless_total_price <= 0:
            return PurchaseError.NEGATIVE_TAXLES_TOTAL
        precision = get_precision(purchase.taxless_total_price)
        expected_total_price = round(sum([product.taxless_price for product in purchase.products]), precision)
        if purchase.taxless_total_price != expected_total_price:
            return PurchaseError.INVALID_TAXLES_TOTAL

    @staticmethod
    def total_quantity_products(purchase: Purchase):
        if purchase.total_quantity <= 0:
            return PurchaseError.NEGATIVE_QUANTITY_TOTAL
        elif purchase.total_quantity != sum([product.quantity for product in purchase.products]):
            return PurchaseError.INVALID_QUANTITY_TOTAL

    @staticmethod
    def uniq_quantity_products(purchase: Purchase):
        if purchase.total_unique_products <= 0:
            return PurchaseError.NEGATIVE_QUANTITY_TOTAL
        elif purchase.total_unique_products != len(purchase.products):
            return PurchaseError.INVALID_QUANTITY_TOTAL

    @staticmethod
    def uniq_products(purchase: Purchase):
        unique_products = set([product.product_id for product in purchase.products])
        if purchase.total_unique_products != len(unique_products):
            return PurchaseError.UNIQUE_PRODUCTS

    @staticmethod
    def manufacturer_is_collected(purchase: Purchase):
        if not purchase.manufacturer:
            return PurchaseError.EMPTY_MANUFACTURED
        expected_manufacturer = set([product.manufacturer for product in purchase.products])
        if Counter(purchase.manufacturer) != Counter(expected_manufacturer):
            return PurchaseError.INVALID_MANUFACTURED

    @staticmethod
    def category_is_collected(purchase: Purchase):
        if not purchase.category:
            return PurchaseError.EMPTY_CATEGORY
        expected_category = set([product.category for product in purchase.products])
        if Counter(purchase.category) != Counter(expected_category):
            return PurchaseError.INVALID_CATEGORY

    @staticmethod
    def sku_is_collected(purchase: Purchase):
        if not purchase.sku:
            return PurchaseError.EMPTY_SKU
        expected_sku = set([product.sku for product in purchase.products])
        if Counter(purchase.sku) != Counter(expected_sku):
            return PurchaseError.INVALID_SKU
