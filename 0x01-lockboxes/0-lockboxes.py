#!/usr/bin/python3
"""
Module to handle lockboxes
"""
from typing import List, Set


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Function to verify if all box are unlockable

    arg:
        boxes: list of boxes

    return: True if lox are unlockable Flase otherwise
    """
    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    if len(keys) == len(boxes):
        return True
    return False
