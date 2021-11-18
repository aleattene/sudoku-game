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
# print(check_mini_sudoku([[1, 3, 2], [9, 7, 8], [4, 5, 6]]))  # True
# print(check_mini_sudoku([[1, 1, 3], [6, 5, 4], [8, 7, 9]]))  # False - The 1 is repeated twice
# print(check_mini_sudoku([[0, 1, 2], [6, 4, 5], [9, 8, 7]]))  # False - The 0 is included (outside range)
# print(check_mini_sudoku([[8, 9, 2], [5, 6, 1], [3, 7, 4]]))  # True


def generate_mini_sudoku(n):
    numbers = [x for x in range(1, 10)]
    mini_sudoku = []
    for i in range(n):
        row = []
        for j in range(n):
            number = random.choice(numbers)
            row.append(number)
            numbers.remove(number)
        mini_sudoku.append(row)
    return mini_sudoku


def generate_mini_sudoku_right(mini_sudoku):
    return mini_sudoku[2:] + mini_sudoku[:2]


def generate_mini_sudoku_down(mini_sudoku):
    mini_sudoku_down = []
    mini_sudoku_down.append(mini_sudoku[0][2:] + mini_sudoku[0][0:1] + mini_sudoku[0][1:2])
    mini_sudoku_down.append(mini_sudoku[1][2:] + mini_sudoku[1][0:1] + mini_sudoku[1][1:2])
    mini_sudoku_down.append(mini_sudoku[2][2:] + mini_sudoku[2][0:1] + mini_sudoku[2][1:2])
    return mini_sudoku_down


for i in range(1, 4):
    print(f"Board number {i}")
    sudoku = []
    # 1
    sudoku_one = generate_mini_sudoku(3)
    sudoku.append(sudoku_one)
    # 2
    sudoku_two = generate_mini_sudoku_right(sudoku_one)
    sudoku.append(sudoku_two)
    # 3
    sudoku_three = generate_mini_sudoku_right(sudoku_two)
    sudoku.append(sudoku_three)
    # 4
    sudoku_four = generate_mini_sudoku_down(sudoku_one)
    sudoku.append(sudoku_four)
    # 5
    sudoku_five = generate_mini_sudoku_right(sudoku_four)
    sudoku.append(sudoku_five)
    # 6
    sudoku_six = generate_mini_sudoku_right(sudoku_five)
    sudoku.append(sudoku_six)
    # 7
    sudoku_seven = generate_mini_sudoku_down(sudoku_four)
    sudoku.append(sudoku_seven)
    # 8
    sudoku_eight = generate_mini_sudoku_right(sudoku_seven)
    sudoku.append(sudoku_eight)
    # 9
    sudoku_nine = generate_mini_sudoku_right(sudoku_eight)
    sudoku.append(sudoku_nine)

    for row in sudoku:
        print(row)