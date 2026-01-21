from sys import stdin


def solve():
    h, w, n = map(int, stdin.readline().split())
    grid = [["."] * w for _ in range(h)]
    for i in range(n):
        r1, c1, r2, c2 = map(int, stdin.readline().split())
        for r in [r1 - 1, r2 - 1]:
            for c in range(c1 - 1, c2):
                grid[r][c] = chr(i + ord("a"))
        for c in [c1 - 1, c2 - 1]:
            for r in range(r1 - 1, r2):
                grid[r][c] = chr(i + ord("a"))

    for row in grid:
        print("".join(str(cell) for cell in row))


if __name__ == "__main__":
    solve()
