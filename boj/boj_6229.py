from collections import deque
from sys import stdin


def solve():
    M, N, M1, M2 = map(int, stdin.readline().strip().split())
    pond = [list(map(int, stdin.readline().strip().split())) for _ in range(M)]

    start, end = None, None
    for i in range(M):
        for j in range(N):
            if pond[i][j] == 3:
                start = (i, j)
            elif pond[i][j] == 4:
                end = (i, j)

    jumps = [[float("inf")] * N for _ in range(M)]
    jumps[start[0]][start[1]] = 0
    queue = deque([start])
    directions = [
        (-M1, -M2),
        (-M1, M2),
        (M1, -M2),
        (M1, M2),
        (-M2, -M1),
        (-M2, M1),
        (M2, -M1),
        (M2, M1),
    ]
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and (pond[nx][ny] == 1 or pond[nx][ny] == 4):
                if jumps[nx][ny] > jumps[x][y] + 1:
                    jumps[nx][ny] = jumps[x][y] + 1
                    queue.append((nx, ny))
    result = jumps[end[0]][end[1]]
    print(result if result != float("inf") else -1)


if __name__ == "__main__":
    solve()
