from sys import stdin, setrecursionlimit

setrecursionlimit(1000010)

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def is_escaping(x, y, c, escaping, visited):
    if not (0 <= x < len(c) and 0 <= y < len(c[0])):
        return 1

    if escaping[x][y] != 0:
        return escaping[x][y]

    if visited[x][y]:
        escaping[x][y] = -1
        return -1
    visited[x][y] = True

    if c[x][y] == "?":
        for di, dj in d:
            nx = x + di
            ny = y + dj
            if is_escaping(nx, ny, c, escaping, visited) == -1:
                escaping[x][y] = -1
                return -1

        escaping[x][y] = 1
        return 1

    nx, ny = x, y
    if c[x][y] == "U":
        nx = x - 1
        ny = y
    elif c[x][y] == "R":
        nx = x
        ny = y + 1
    elif c[x][y] == "D":
        nx = x + 1
        ny = y
    elif c[x][y] == "L":
        nx = x
        ny = y - 1

    escaping[x][y] = is_escaping(nx, ny, c, escaping, visited)
    return escaping[x][y]


def solve():
    t = int(stdin.readline())
    for _ in range(t):
        n, m = map(int, stdin.readline().split())
        c = []
        for _ in range(n):
            c.append(list(stdin.readline().strip()))

        escaping = [[0] * m for _ in range(n)]
        visited = [[False] * m for _ in range(n)]

        answer = 0
        for i in range(n):
            for j in range(m):
                e = is_escaping(i, j, c, escaping, visited)
                if e == -1:
                    answer += 1

        print(answer, flush=False)


if __name__ == "__main__":
    solve()
