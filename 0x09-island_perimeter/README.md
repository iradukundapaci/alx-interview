Island Perimeter
This project contains interview coding challenges.

Tasks To Complete 0. Island Perimeter
0-island_perimeter.py contains a module with a function having the prototype function def island_perimeter(grid):, which returns the perimeter of the island described in grid, with the following requirements:
grid is a list of list of integers:
0 represents water.
1 represents land.
Each cell is square, with a side length of 1.
Cells are connected horizontally/vertically (not diagonally).
grid is rectangular, with its width and height not exceeding 100.
The grid is completely surrounded by water.
There is only one island (or nothing).
The island doesn't have "lakes' (water inside that isn't connected to the water surrounding the island).

Usage:

guillaume@ubuntu:~/0x09$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = **import**('0-island_perimeter').island_perimeter

if **name** == "**main**":
grid = [
[0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[0, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))

guillaume@ubuntu:~/0x09$
guillaume@ubuntu:~/0x09$ ./0-main.py
12
guillaume@ubuntu:~/0x09$
