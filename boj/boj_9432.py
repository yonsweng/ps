from collections import deque
from sys import stdin

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def advance(stage):
    return chr((ord(stage) - ord("A") + 1) % 26 + ord("A"))


def bfs(grid, outbreaked, W, H, start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))

    while queue:
        x, y = queue.popleft()

        if grid[y][x] != "D":
            grid[y][x] = advance(grid[y][x])
            continue

        if outbreaked[y][x]:
            continue

        outbreaked[y][x] = True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < W and 0 <= ny < H:
                if grid[ny][nx] != "X":
                    queue.append((nx, ny))


def solve():
    N = int(stdin.readline().strip())
    for _ in range(N):
        W, H = map(int, stdin.readline().strip().split())

        grid = []
        for _ in range(H):
            row = list(stdin.readline().strip())
            grid.append(row)

        I = int(stdin.readline().strip())
        for _ in range(I):
            X, Y = map(int, stdin.readline().strip().split())

            if grid[Y][X] == "X":
                continue

            if grid[Y][X] != "D":
                grid[Y][X] = advance(grid[Y][X])
            else:
                outbreaked = [[False] * W for _ in range(H)]
                bfs(grid, outbreaked, W, H, X, Y)

        # Output the final grid state
        for row in grid:
            print("".join(row))


if __name__ == "__main__":
    solve()
