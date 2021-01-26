def matrix_init():
    n = int(input())
    m = []
    for _ in range(n):
        current_row = [int(el) for el in input().split()]
        m.append(current_row)
    return m, n


matrix, size = matrix_init()

data = input()
coord = []
for index in range(len(data)):
    if data[index].isdigit():
        num = int(data[index])
        coord.append(num)

for i in range(0, len(coord), 2):
    row = coord[i]
    col = coord[i + 1]
    current_value = matrix[row][col]
    if current_value > 0:
        if row > 0:
            if matrix[row - 1][col] > 0:
                matrix[row - 1][col] -= current_value
        if row > 0 and col > 0:
            if matrix[row - 1][col - 1] > 0:
                matrix[row - 1][col - 1] -= current_value
        if row > 0 and col < size - 1:
            if matrix[row - 1][col + 1] > 0:
                matrix[row - 1][col + 1] -= current_value
        if col > 0:
            if matrix[row][col - 1] > 0:
                matrix[row][col - 1] -= current_value
        if col < size - 1:
            if matrix[row][col + 1] > 0:
                matrix[row][col + 1] -= current_value
        if row < size - 1 and col > 0:
            if matrix[row + 1][col - 1] > 0:
                matrix[row + 1][col - 1] -= current_value
        if row < size - 1:
            if matrix[row + 1][col] > 0:
                matrix[row + 1][col] -= current_value
        if row < size - 1 and col < size - 1:
            if matrix[row + 1][col + 1] > 0:
                matrix[row + 1][col + 1] -= current_value
        matrix[row][col] = 0

alive_cells = []
for el in matrix:
    for e in el:
        if e > 0:
            alive_cells.append(e)


print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
for e in matrix:
    print(*e)
