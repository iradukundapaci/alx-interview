#!/usr/bin/python3
"""
Find Prime factors
"""
import math
from typing import List


def primeFactors(n: int) -> List[int]:
    """
    Function that find prime factors of a number

    args:
        n: integer number

    return: list of prime factors
    """
    prime_factors: List[int] = []

    while n % 2 == 0:
        n //= 2
        prime_factors.append(2)

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            n //= i
            prime_factors.append(i)

    if n > 2:
        prime_factors.append(n)

    return prime_factors
