from enum import Enum


class PurchaseError(Enum):
    NO_ERROR = 'No error'
    EMPTY_CURRENCY = 'Empty currency'
    INVALID_CURRENCY = 'Invalid currency'
    EMPTY_GENDER = 'Empty gender'
    INVALID_GENDER = 'Invalid gender'
    EMPTY_FIRST_NAME = 'Empty first name'
    EMPTY_LAST_NAME = 'Empty last name'
    EMPTY_FULL_NAME = 'Empty full name'
    INVALID_FULL_NAME = 'Invalid full name'
    EMPTY_EMAIL = 'Empty email'
    INVALID_EMAIL = 'Invalid email format'
    EMPTY_PHONE = 'Empty phone number'
    EMPTY_WEEK_DAY = 'Empty week day'
    INVALID_WEEK_DAY = 'Invalid week day'
    EMPTY_WEEK_DAY_NUMBER = 'Empty week day number'
    INVALID_WEEK_DAY_NUMBER = 'Invalid week day number'
    NEGATIVE_TAXFUL_TOTAL = 'Negative value of tax full'
    INVALID_TAXFUL_TOTAL = 'Invalid tax full value'
    NEGATIVE_TAXLES_TOTAL = 'Negative value of tax les'
    INVALID_TAXLES_TOTAL = 'Invalid tax les value'
    NEGATIVE_QUANTITY_TOTAL = 'Negative value of total quantity'
    INVALID_QUANTITY_TOTAL = 'Invalid total quantity value'
    NEGATIVE_UNIQ_TOTAL = 'Negative value of unique quantity'
    INVALID_UNIQ_TOTAL = 'Invalid unique quantity value'
    INVALID_MANUFACTURED = 'Invalid manufactured collection'
    EMPTY_MANUFACTURED = 'Empty manufactured collection'
    INVALID_CATEGORY = 'Invalid category collection'
    EMPTY_CATEGORY = 'Empty category collection'
    INVALID_SKU = 'Invalid sku collection'
    EMPTY_SKU = 'Empty sku collection'


class ProductError(Enum):
    NO_ERROR = 'No error'
