from collections import deque


def matrix_init():
    n = int(input())
    commands_data = input().split()
    q = deque()
    for c in commands_data:
        q.append(c)
    m = []
    for _ in range(n):
        row_el = [el for el in input().split()]
        m.append(row_el)
    return m, n, q


matrix, size, commands = matrix_init()

current_row = 0
current_col = 0
all_coal = 0
coal = 0

for r in range(size):
    for c in range(size):
        if matrix[r][c] == "s":
            current_row = r
            current_col = c
        elif matrix[r][c] == "c":
            all_coal += 1


while commands:
    command = commands.popleft()

    if command == "left":
        if current_col > 0:
            current_col -= 1
    elif command == "right":
        if current_col < size-1:
            current_col += 1
    elif command == "up":
        if current_row > 0:
            current_row -= 1
    elif command == "down":
        if current_row < size -1:
            current_row += 1
    current_position = matrix[current_row][current_col]
    if current_position == "e":
        print(f"Game over! ({current_row}, {current_col})")
        break
    elif current_position == "c":
        coal += 1
        matrix[current_row][current_col] = "*"
    if all_coal == coal:
        print(f"You collected all coals! ({current_row}, {current_col})")
        break
    if not commands:
        remaining_coal = all_coal - coal
        print(f"{remaining_coal} coals left. ({current_row}, {current_col})")

