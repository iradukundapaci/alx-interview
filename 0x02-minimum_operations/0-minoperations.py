#!/usr/bin/python3
"""
Minimum operations
"""

primeFactors = __import__("primefactor").primeFactors


def minOperations(n: int) -> int:
    """
    Function calculates minimum operations

    args:
        n: max operation number

    return: operation number
    """
    if n <= 1:
        return 0
    else:
        prime_factors = primeFactors(n)
        return sum(prime_factors)
