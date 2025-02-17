# Copyright (c) 2025 bartosz-grabowski

from numbers import Number


def add(a: Number, b: Number) -> Number:
    """Returns the sum of a & b."""
    assert isinstance(a, Number)
    assert isinstance(b, Number)
    return a+b
