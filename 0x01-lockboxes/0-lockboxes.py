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
    total_boxes = len(boxes)
    visited_boxes: Set[int] = set()
    stack = [0]

    while stack:
        current_box = stack.pop()
        visited_boxes.add(current_box)
        for key in boxes[current_box]:
            if key not in visited_boxes and key < total_boxes:
                stack.append(key)

    return len(visited_boxes) == total_boxes
