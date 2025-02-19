# Copyright (c) 2025 bartosz-grabowski

from numbers import Number


def subtract(a: Number, b: Number) -> Number:
    """Returns the difference of a & b."""
    if (not isinstance(a, Number)) or (not isinstance(a, Number)):
        raise TypeError
    return a-b
