#!/usr/bin/python3
"""
Minimum operations
"""


def minOperations(n: int) -> int:
    """
    Function calculates minimum operations

    args:
        n: max operation number

    return: operation number
    """
    if n <= 1:
        return 0

    prime_factors_sum = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            prime_factors_sum += divisor
            n //= divisor
        else:
            divisor += 1

    return prime_factors_sum
