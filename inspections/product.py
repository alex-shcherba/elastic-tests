from enums.errors import ProductError
from models.product import Product


class ProductInspection:

    @staticmethod
    def base_price_is_allowed(product: Product):
        if product.base_price < 0 or product.base_price < product.min_price:
            return ProductError.INVALID_BASE_PRICE

    @staticmethod
    def base_unit_price_is_allowed(product: Product):
        if product.base_price < 0 or product.base_price < product.min_price:
            return ProductError.INVALID_BASE_UNIT_PRICE

    @staticmethod
    def discount_percent_is_allowed(product: Product):
        if 0 < product.discount_percentage > 100:
            return ProductError.INVALID_DISCOUNT_PERCENT

    @staticmethod
    def quantity_is_allowed(product: Product):
        if product.quantity <= 0:
            return ProductError.INVALID_QUANTITY

    @staticmethod
    def manufacturer_is_allowed(product: Product):
        if product.manufacturer == '':
            return ProductError.EMPTY_MANUFACTURER

    @staticmethod
    def tax_amount_is_allowed(product: Product):
        if product.tax_amount <= 0:
            return ProductError.INVALID_TAX_AMOUNT

    @staticmethod
    def category_is_allowed(product: Product):
        if product.category == '':
            return ProductError.EMPTY_CATEGORY

    @staticmethod
    def sku_is_allowed(product: Product):
        if product.sku == '':
            return ProductError.EMPTY_SKU
        elif not product.sku.startswith('Z'):
            return ProductError.INVALID_SKU

    @staticmethod
    def taxless_price_is_allowed(product: Product):
        if product.taxless_price <= 0:
            return ProductError.INVALID_TAXLESS_PRICE

    @staticmethod
    def taxful_price_is_allowed(product: Product):
        if product.taxful_price <= 0:
            return ProductError.INVALID_TAXFUL_PRICE

    @staticmethod
    def min_price_is_allowed(product: Product):
        if product.min_price <= 0:
            return ProductError.INVALID_MIN_PRICE

    @staticmethod
    def unit_discount_amount_is_allowed(product: Product):
        if product.unit_discount_amount < 0:
            return ProductError.INVALID_UNIT_DISCOUNT_AMOUNT

    @staticmethod
    def discount_amount_is_allowed(product: Product):
        if product.discount_amount < 0:
            return ProductError.INVALID_DISCOUNT_AMOUNT
        elif product.discount_amount != product.price * product.discount_percentage * product.quantity:
            return ProductError.INVALID_DISCOUNT_AMOUNT
