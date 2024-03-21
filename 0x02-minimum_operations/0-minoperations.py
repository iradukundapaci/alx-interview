#!/usr/bin/python3
"""
Minimum operations
"""
from typing import List
import math


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


def retreiveLastOperation(list_of_operations: List[str]) -> str:
    """
    Function that retrieves last operation done

    args:
        list_of_operation: operations done

    return: last operation done
    """
    return list_of_operations[-1]


def pasteOperation(recent_operation: str, current_copy_string: str) -> str:
    """
    Function that pastes to create new operation

    args:
        copy_string: current copy value

    return: new operation
    """
    return recent_operation + current_copy_string


def minOperations(n: int) -> int:
    """
    Function calculates minimum operations

    args:
        n: max operation number

    return: operation number
    """
    operations = ["H"]
    prime_factors = primeFactors(n)
    copy_op = retreiveLastOperation(operations)

    if len(prime_factors) == 1 and prime_factors[0] == n:
        return n

    for i in prime_factors:
        if i % 2 == 0:
            while len(retreiveLastOperation(operations)) != i:
                copy_op = retreiveLastOperation(operations)
                operations.append(pasteOperation(copy_op, copy_op))
        else:
            while len(retreiveLastOperation(operations)) != i:
                operations.append(
                    pasteOperation(retreiveLastOperation(operations), copy_op)
                )
    if len(retreiveLastOperation(operations)) != n:
        copy_op = retreiveLastOperation(operations)
        operations.append(pasteOperation(copy_op, copy_op))
        operations.append(pasteOperation(copy_op, copy_op))

    while len(retreiveLastOperation(operations)) != n:
        paste_op = pasteOperation(retreiveLastOperation(operations), copy_op)
        operations.append(paste_op)

    return len(operations)
