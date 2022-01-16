from sys import stdin


def read_input():
    n, m, r, c = map(int, stdin.readline().split())
    grid = []
    for _ in range(n):
        grid.append(stdin.readline().rstrip())
    return n, m, r, c, grid


def all_white(grid, n, m):
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'B':
                return False
    return True


def same_line(grid, r, c, n, m):
    for j in range(m):
        if grid[r-1][j] == 'B':
            return True
    for i in range(n):
        if grid[i][c-1] == 'B':
            return True
    return False


def solve(n, m, r, c, grid):
    if all_white(grid, n, m):
        return -1
    elif grid[r-1][c-1] == 'B':
        return 0
    elif same_line(grid, r, c, n, m):
        return 1
    else:
        return 2


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
