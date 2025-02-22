# Copyright (c) 2025 bartosz-grabowski

from numbers import Number


def add(a: Number, b: Number) -> Number:
    """Returns the sum of a & b."""
    if (not isinstance(a, Number)) or (not isinstance(b, Number)):
        raise TypeError
    return a + b
