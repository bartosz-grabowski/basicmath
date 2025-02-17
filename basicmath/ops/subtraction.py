# Copyright (c) 2025 bartosz-grabowski

from numbers import Number


def subtract(a: Number, b: Number) -> Number:
    """Returns the difference of a & b."""
    assert isinstance(a, Number)
    assert isinstance(b, Number)
    return a-b
