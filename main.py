"""
Challenge SUDOKU
A Sudoku is a 9x9 grid that is completed when every 3x3 square, row and column consist of the numbers 1-9.
For this task, you will be given a completed 3x3 square, in the form of a two-dimensional array.
Create a function that checks to make sure this 3x3 square contains each number from 1-9 exactly once.
Make sure there are no duplicates, and no numbers outside this range
"""

import random


def check_mini_sudoku(matrix):
    return True if "123456789" == "".join(str(item) for item in sorted(matrix[0] + matrix[1] + matrix[2])) else False


# TESTS
print(check_mini_sudoku([[1, 3, 2], [9, 7, 8], [4, 5, 6]]))  # True
print(check_mini_sudoku([[1, 1, 3], [6, 5, 4], [8, 7, 9]]))  # False - The 1 is repeated twice
print(check_mini_sudoku([[0, 1, 2], [6, 4, 5], [9, 8, 7]]))  # False - The 0 is included (outside range)
print(check_mini_sudoku([[8, 9, 2], [5, 6, 1], [3, 7, 4]]))  # True

sudoku = []


def generate_mini_sudoku(n):
    numbers = [x for x in range(1, 10)]
    mini_sudoku = []
    for num in range(n):
        i = [x for x in random.sample(numbers, n)]
        print(i)
        mini_sudoku.append(i)
    return mini_sudoku
