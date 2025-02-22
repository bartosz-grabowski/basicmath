# Copyright (c) 2025 bartosz-grabowski

import os
import pytest

from basicmath.ops.addition import add


def test_add_on_numbers():
    assert add(2, 3) == 5


def test_add_on_string():
    with pytest.raises(TypeError):
        add("a", 1)


def test_add_on_strings():
    with pytest.raises(TypeError):
        add("a", "tt")
