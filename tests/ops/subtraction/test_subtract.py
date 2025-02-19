# Copyright (c) 2025 bartosz-grabowski

import pytest

from basicmath.ops.subtraction import subtract


def test_subtract_on_numbers():
    assert subtract(2, 3) == -1


def test_subtract_on_string():
    with pytest.raises(TypeError):
        subtract("a", 1)


def test_subtract_on_strings():
    with pytest.raises(TypeError):
        subtract("a", "tt")
