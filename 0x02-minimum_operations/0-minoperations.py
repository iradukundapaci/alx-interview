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
    prime_factors = primeFactors(n)
    return sum(prime_factors)
