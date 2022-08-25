import numpy as np

# puzzle = """250014009
#             080009014
#             001070600
#             170000000
#             305000807
#             000000031
#             002050900
#             530900020
#             490120085"""


# def create_grid(puzzle_str):
#     # Deleting whitespaces and newlines (\n)
#     lines = puzzle_str.replace(',', '').replace('\n', '')
#     # Converting it to a list of digits
#     digits = list(map(int, lines))
#     # Turning it to a 9x9 numpy array
#     grid = np.array(digits).reshape(9, 9)
#     return grid


# print(create_grid(puzzle))

sudoku = [[6, 0, 0, 0, 0, 0, 1, 0, 0],
          [3, 0, 7, 0, 5, 0, 9, 0, 0],
          [0, 0, 0, 7, 9, 0, 0, 0, 5],
          [5, 4, 0, 3, 0, 7, 0, 6, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 2, 0, 5, 0, 3, 7],
          [8, 0, 0, 0, 2, 9, 0, 0, 0],
          [0, 0, 2, 0, 3, 0, 4, 0, 8],
          [0, 0, 5, 0, 0, 0, 0, 0, 6]]


def printsudoku():
    print("\n\n\n\n\n")
    for i in range(len(sudoku)):
        line = ""
        if i == 3 or i == 6:
            print("---------------------")
        for j in range(len(sudoku[i])):
            if j == 3 or j == 6:
                line += "| "
            line += str(sudoku[i][j])+" "
        print(line)


def findNextCellToFill(sudoku):
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                return x, y
    return -1, -1


def isValid(sudoku, i, j, e):
    rowOk = all([e != sudoku[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != sudoku[x][j] for x in range(9)])
        if columnOk:
            secTopX, secTopY = 3*(i//3), 3*(j//3)
            for x in range(secTopX, secTopX+3):
                for y in range(secTopY, secTopY+3):
                    if sudoku[x][y] == e:
                        return False
            return True
    return False


def solveSudoku(sudoku, i=0, j=0):
    i, j = findNextCellToFill(sudoku)
    if i == -1:
        return True
    for e in range(1, 10):
        if isValid(sudoku, i, j, e):
            sudoku[i][j] = e
            if solveSudoku(sudoku, i, j):
                return True
            sudoku[i][j] = 0
    return False


solveSudoku(sudoku)
printsudoku()
