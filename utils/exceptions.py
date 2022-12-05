class PurchaseValidationError(AssertionError):
    """Errors for purchase logic"""

    def __init__(self, message):
        super().__init__(message)


class ProductValidationError(AssertionError):
    """Errors for product data"""

    def __init__(self, message):
        super().__init__(message)
