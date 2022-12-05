class CustomerValidationError(AssertionError):
    """Errors for customer data"""

    def __init__(self, message):
        super().__init__(message)


class PurchaseValidationError(AssertionError):
    """Errors for purchase logic"""

    def __init__(self, message):
        super().__init__(message)
