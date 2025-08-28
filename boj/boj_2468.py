from collections import deque
from sys import stdin


def solve():
    N = int(stdin.readline().strip())
    region = [[0] * (N + 2) for _ in range(N + 2)]
    for i in range(1, N + 1):
        row = list(map(int, stdin.readline().strip().split()))
        for j in range(1, N + 1):
            region[i][j] = row[j - 1]
    
    answer = 1
    for height in range(1, 100):
        visited = [[False] * (N + 2) for _ in range(N + 2)]
        safe_area = 0
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if region[i][j] > height and not visited[i][j]:
                    safe_area += 1
                    queue = deque()
                    queue.append((i, j))
                    visited[i][j] = True
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = x + dx, y + dy
                            if region[nx][ny] > height and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
        answer = max(answer, safe_area)
    print(answer)


if __name__ == "__main__":
    solve()
