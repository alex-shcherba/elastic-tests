from enums.errors import PurchaseError, ProductError


class Validator:
    __error_enum = None

    def __init__(self, items: list):
        self._items = items
        self._exec_func = []
        self._errors = {e: [] for e in self.__error_enum}

    def check(self, func):
        self._exec_func.append(func)

    def check_all(self):
        for item in self._items:
            for check_func in self._exec_func:
                error = check_func(item)
                if error:
                    self._errors[error].append(item)
        errors_data = [f"{err.value}: {len(value)}" for err, value in self._errors.items() if value]
        if errors_data:
            err_msg = ', '.join(errors_data)
            raise AssertionError(f"Errors with purchase data: ({err_msg})")


class PurchaseValidator(Validator):
    __error_enum = PurchaseError


class ProductValidator(Validator):
    __error_enum = ProductError