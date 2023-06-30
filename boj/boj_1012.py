from sys import stdin
from collections import deque


def solve():
    t = int(stdin.readline())
    for _ in range(t):
        m, n, k = map(int, stdin.readline().split())
        a = [[0 for _ in range(m)] for _ in range(n)]
        for _ in range(k):
            x, y = map(int, stdin.readline().split())
            a[y][x] = 1

        answer = 0
        for y in range(n):
            for x in range(m):
                if a[y][x] == 0:
                    continue

                answer += 1

                q = deque([(y, x)])
                while q:
                    cy, cx = q.popleft()
                    if cy < 0 or cy >= n or cx < 0 or cx >= m:
                        continue

                    if a[cy][cx] == 0:
                        continue

                    a[cy][cx] = 0
                    q.append((cy - 1, cx))
                    q.append((cy + 1, cx))
                    q.append((cy, cx - 1))
                    q.append((cy, cx + 1))

        print(answer, flush=False)


if __name__ == "__main__":
    solve()
