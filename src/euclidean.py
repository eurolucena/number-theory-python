"""
Euclidean algorithm and Extended Euclidean algorithm.

This module provides elementary implementations for computing:

1. gcd(a, b): the greatest common divisor of two integers.
2. extended_gcd(a, b): integers x and y such that

       ax + by = gcd(a, b)

These algorithms are fundamental tools in elementary and
computational number theory.
"""


def gcd(a: int, b: int) -> int:
    """
    Compute the greatest common divisor of two integers
    using the Euclidean algorithm.

    Parameters
    ----------
    a, b : int
        Integers whose greatest common divisor is required.

    Returns
    -------
    int
        The non-negative greatest common divisor of a and b.
    """
    a, b = abs(a), abs(b)

    while b != 0:
        a, b = b, a % b

    return a


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Extended Euclidean algorithm.

    Returns integers g, x, y satisfying

        ax + by = g,

    where g = gcd(a, b).

    Parameters
    ----------
    a, b : int

    Returns
    -------
    tuple[int, int, int]
        (g, x, y), where g = gcd(a, b).
    """
    old_r, r = abs(a), abs(b)
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        q = old_r // r

        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    x = old_s if a >= 0 else -old_s
    y = old_t if b >= 0 else -old_t

    return old_r, x, y


if __name__ == "__main__":
    a = 252
    b = 198

    print(f"gcd({a}, {b}) = {gcd(a, b)}")

    g, x, y = extended_gcd(a, b)

    print(f"{a}({x}) + {b}({y}) = {g}")
