"""
Challenge SUDOKU
"""

import random


def check_mini_sudoku(matrix):
    """
    This function checks if the mini Sudoku puzzle (passed as an argument) is correct or not.
    If it is correct it returns True otherwise False.
        =======
        1  2  3
        4  5  6    ->  True
        7  8  9
        =======
        1  1  3
        4  5  3    ->  False
        7  4  9
        =======
    :param matrix: list
    :return: boolean
    """
    return True if "123456789" == "".join(str(item) for item in sorted(matrix[0] + matrix[1] + matrix[2])) else False


def generate_mini_sudoku(n):
    """
    This function generates a correct mini Sudoku puzzle.
    For example: =======
                 1  3  4
                 2  5  6
                 7  8  9
                 =======
    :param n: int
    :return: list
    """
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
    """
    This function generates a correct mini Sudoku puzzle to the right of another previous mini Sudoku puzzle.
    :param mini_sudoku: list
    :return: list
    """
    return mini_sudoku[2:] + mini_sudoku[:2]


def generate_mini_sudoku_down(mini_sudoku):
    """
    This function generates a correct mini Sudoku puzzle under another previous mini Sudoku puzzle.
    :param mini_sudoku: list
    :return: list
    """
    mini_sudoku_down = [mini_sudoku[0][2:] + mini_sudoku[0][0:1] + mini_sudoku[0][1:2],
                        mini_sudoku[1][2:] + mini_sudoku[1][0:1] + mini_sudoku[1][1:2],
                        mini_sudoku[2][2:] + mini_sudoku[2][0:1] + mini_sudoku[2][1:2]]
    return mini_sudoku_down


def generate_row(previous_mini_sudoku, num_cols):
    """
    This function generates a line of mini sudoku puzzles starting from an initial reference mini sudoku puzzle.
    :param previous_mini_sudoku: list
    :param num_cols: int
    :return: list
    """
    for col in range(num_cols - 1):
        next_mini_sudoku = generate_mini_sudoku_right(previous_mini_sudoku)
        if check_mini_sudoku(next_mini_sudoku):
            sudoku.append(next_mini_sudoku)
            previous_mini_sudoku = next_mini_sudoku
        else:
            pass


def print_sudoku(sudoku_board):
    print("")
    print(" " * 10 + "╔" + "═" * 35 + "╗")
    print(" " * 10 + "║", end="")
    print(" " * 11 + "SUDOKU Board", end="")
    print(" " * 12 + "║")
    print(" " * 10 + "╠" + "═" * 11 + "╦" + "═" * 11 + "╦" + "═" * 11 + "╣")
    for row in range(0, 9):
        if row > 0 and row % 3 == 0:
            print(" " * 10 + "╠" + "═" * 11 + "╬" + "═" * 11 + "╬" + "═" * 11 + "╣")
        print(" " * 10, end="")
        for col in range(3):
            print("║", end="  ")
            for number in sudoku_board[row][col]:
                print(number, end="  ")
        print("║")
    print(" " * 10 + "╚" + "═" * 11 + "╩" + "═" * 11 + "╩" + "═" * 11 + "╝")


for i in range(1, 2):
    sudoku = []
    # MINI SUDOKU 01
    sudoku_one = generate_mini_sudoku(3)
    if check_mini_sudoku(sudoku_one):
        sudoku.append(sudoku_one)
    # MINI SUDOKU 02 AND MINI SUDOKU 03
    generate_row(sudoku_one, 3)
    # MINI SUDOKU 04
    sudoku_four = generate_mini_sudoku_down(sudoku_one)
    if check_mini_sudoku(sudoku_four):
        sudoku.append(sudoku_four)
    # MINI SUDOKU 05 AND MINI SUDOKU 06
    generate_row(sudoku_four, 3)
    # MINI SUDOKU 07
    sudoku_seven = generate_mini_sudoku_down(sudoku_four)
    if check_mini_sudoku(sudoku_seven):
        sudoku.append(sudoku_seven)
    # MINI SUDOKU 08 AND MINI SUDOKU 09
    generate_row(sudoku_seven, 3)
    # DISPLAY SUDOKU board
    print_sudoku(sudoku)
