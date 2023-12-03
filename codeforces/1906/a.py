from sys import stdin

candidates = []
d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def solve(grid, selected, i, j, pi, pj, n):
    if n == 0:
        selected_ = "".join(selected)
        candidates.append(selected_)
        return

    for k in range(8):
        x = i + d[k][0]
        y = j + d[k][1]
        if 0 <= x < 3 and 0 <= y < 3 and (x, y) != (pi, pj):
            selected.append(grid[x][y])
            solve(grid, selected, x, y, i, j, n - 1)
            selected.pop()


def main():
    grid = []
    for _ in range(3):
        grid.append(stdin.readline().strip())

    selected = []
    for i in range(3):
        for j in range(3):
            selected.append(grid[i][j])
            solve(grid, selected, i, j, -1, -1, 2)
            selected.pop()

    candidates.sort()
    print(candidates[0])


if __name__ == "__main__":
    main()
