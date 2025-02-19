# Copyright (c) 2025 bartosz-grabowski

from basicmath.ops.addition import add
from basicmath.ops.subtraction import subtract


def main():
    a = 3
    b = 1
    print(f"Sum of a={a} and b={b} is equal to {add(a, b)}")
    print(f"Difference of a={a} and b={b} is equal to {subtract(a, b)}")


if __name__ == "__main__":
    main()
