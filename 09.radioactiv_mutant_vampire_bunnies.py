from collections import deque


def matrix_init():
    n, m = [int(el) for el in input().split()]
    mat = []
    for _ in range(n):
        row_el = [el for el in input()]
        mat.append(row_el)
    return mat, n, m


def command_read():
    com = deque()
    data = input()
    for el in data:
        com.append(el)
    return com


matrix, row, col = matrix_init()
commands = command_read()
current_row = 0
current_col = 0

status = None

for r in range(row):
    for c in range(col):
        if matrix[r][c] == "P":
            current_row = r
            current_col = c

while commands:
    command = commands.popleft()

    list_with_b = []
    for row_b in range(row):
        for col_b in range(col):
            if matrix[row_b][col_b] == "B":
                list_with_b.append(row_b)
                list_with_b.append(col_b)

    for index in range(0, len(list_with_b), 2):
        row_b = list_with_b[index]
        col_b = list_with_b[index + 1]
        if row_b > 0:
            matrix[row_b - 1][col_b] = "B"
        if row_b < row - 1:
            matrix[row_b + 1][col_b] = "B"
        if col_b > 0:
            matrix[row_b][col_b - 1] = "B"
        if col_b < col - 1:
            matrix[row_b][col_b + 1] = "B"
    if not matrix[current_row][current_col] == "B":
        matrix[current_row][current_col] = "."
    if command == "R":
        if current_col < col - 1:
            current_col += 1
        else:
            status = True
            break
    elif command == "L":
        if current_col > 0:
            current_col -= 1
        else:
            status = True
            break
    elif command == "U":
        if current_row > 0:
            current_row -= 1
        else:
            status = True
            break
    elif command == "D":
        if current_row < row - 1:
            current_row += 1
        else:
            status = True
            break

    if matrix[current_row][current_col] == "B":
        status = False
        break


for el in matrix:
    print(''.join(el))

if status:
    print(f"won: {current_row} {current_col}")
else:
    print(f"dead: {current_row} {current_col}")

