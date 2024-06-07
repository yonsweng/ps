grid = []
for _ in range(9):
    grid.append(list(map(int, input().split())))
max_val = 0
max_pos = (0, 0)
for i in range(9):
    for j in range(9):
        if grid[i][j] > max_val:
            max_val = grid[i][j]
            max_pos = (i, j)
print(max_val)
print(max_pos[0] + 1, max_pos[1] + 1)
