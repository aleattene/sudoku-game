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
    for _ in range(n):
        line = []
        for j in range(n):
            number = random.choice(numbers)
            line.append(number)
            numbers.remove(number)
        mini_sudoku.append(line)
    return mini_sudoku


def generate_mini_sudoku_right(mini_sudoku):
    return mini_sudoku[2:] + mini_sudoku[:2]


def generate_mini_sudoku_down(mini_sudoku):
    mini_sudoku_down = [mini_sudoku[0][2:] + mini_sudoku[0][0:1] + mini_sudoku[0][1:2],
                        mini_sudoku[1][2:] + mini_sudoku[1][0:1] + mini_sudoku[1][1:2],
                        mini_sudoku[2][2:] + mini_sudoku[2][0:1] + mini_sudoku[2][1:2]]
    return mini_sudoku_down



for i in range(1, 4):
    print(f"Board number {i}")
    sudoku = []
    # MINI SUDOKU 01
    sudoku_one = generate_mini_sudoku(3)
    if check_mini_sudoku(sudoku_one):
        sudoku.append(sudoku_one)
    # MINI SUDOKU 02
    sudoku_two = generate_mini_sudoku_right(sudoku_one)
    if check_mini_sudoku(sudoku_two):
        sudoku.append(sudoku_two)
    # MINI SUDOKU 03
    sudoku_three = generate_mini_sudoku_right(sudoku_two)
    if check_mini_sudoku(sudoku_three):
        sudoku.append(sudoku_three)
    # MINI SUDOKU 04
    sudoku_four = generate_mini_sudoku_down(sudoku_one)
    if check_mini_sudoku(sudoku_four):
        sudoku.append(sudoku_four)
    # MINI SUDOKU 05
    sudoku_five = generate_mini_sudoku_right(sudoku_four)
    if check_mini_sudoku(sudoku_five):
        sudoku.append(sudoku_five)
    # MINI SUDOKU 06
    sudoku_six = generate_mini_sudoku_right(sudoku_five)
    if check_mini_sudoku(sudoku_six):
        sudoku.append(sudoku_six)
    # MINI SUDOKU 07
    sudoku_seven = generate_mini_sudoku_down(sudoku_four)
    if check_mini_sudoku(sudoku_seven):
        sudoku.append(sudoku_seven)
    # MINI SUDOKU 08
    sudoku_eight = generate_mini_sudoku_right(sudoku_seven)
    if check_mini_sudoku(sudoku_eight):
        sudoku.append(sudoku_eight)
    # MINI SUDOKU 09
    sudoku_nine = generate_mini_sudoku_right(sudoku_eight)
    if check_mini_sudoku(sudoku_nine):
        sudoku.append(sudoku_nine)

    for row in sudoku:
        print(row)
