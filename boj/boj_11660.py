from sys import stdin


def solve():
    N, M = map(int, stdin.readline().split())
    table = [list(map(int, stdin.readline().split())) for _ in range(N)]
    acc = [[0] * (N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            acc[i][j] = table[i][j]
            if i > 0:
                acc[i][j] += acc[i - 1][j]
            if j > 0:
                acc[i][j] += acc[i][j - 1]
            if i > 0 and j > 0:
                acc[i][j] -= acc[i - 1][j - 1]
    for _ in range(M):
        x1, y1, x2, y2 = map(int, stdin.readline().split())
        result = acc[x2 - 1][y2 - 1]
        if x1 > 1:
            result -= acc[x1 - 2][y2 - 1]
        if y1 > 1:
            result -= acc[x2 - 1][y1 - 2]
        if x1 > 1 and y1 > 1:
            result += acc[x1 - 2][y1 - 2]
        print(result, flush=False)


if __name__ == "__main__":
    solve()
