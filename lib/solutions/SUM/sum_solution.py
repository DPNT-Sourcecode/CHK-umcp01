# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(number_1: int, number_2: int) -> int:
    if number_1 > 100 or number_1 < 0:
        raise ValueError("{} must be greater than 0 and less than 100." % number_1)
    raise NotImplementedError()

