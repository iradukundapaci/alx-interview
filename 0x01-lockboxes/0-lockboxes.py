#!/usr/bin/python3
"""
Module to handle lockboxes
"""
from typing import List, Set


def loopKeys(boxIndex: int, boxKeys: Set, allBoxes: List[List[int]]) -> None:
    """
    Function to store found keys in boxes

    args:
        boxIndex: index of the next box
        boxKeys: set of found box keys
        allBoxes: list of all boxes

    return: None
    """
    if boxIndex in boxKeys:
        return

    boxKeys.add(boxIndex)

    if len(allBoxes[boxIndex]) == 0:
        boxKeys.add(0)
        return

    for i in allBoxes[boxIndex]:
        loopKeys(i, boxKeys, allBoxes)


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Function that verifies if given boxes are unlockable

    arg:
        boxes: list of boxes

    return: True if box is unlockable
    """
    allBoxKeys: Set = set()

    loopKeys(0, allBoxKeys, boxes)

    if len(allBoxKeys) == len(boxes):
        return True
    return False
