from sys import stdin


def get_min_cost(files):
    n = len(files)

    d = [[2000000000] * (n + 1) for _ in range(n + 1)]
    p = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        d[i - 1][i] = 0
        p[i - 1][i] = i

    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = s[i - 1] + files[i - 1]

    for l in range(2, n + 1):
        for j in range(l, n + 1):
            i = j - l
            for k in range(max(p[i][j - 1], i + 1), min(p[i + 1][j] + 1, j)):
                cost = d[i][k] + d[k][j] + s[j] - s[i]
                if d[i][j] > cost:
                    d[i][j] = cost
                    p[i][j] = k

    return d[0][n]


def solve():
    t = int(stdin.readline())
    for _ in range(t):
        _ = int(stdin.readline())
        files = list(map(int, stdin.readline().split()))
        print(get_min_cost(files), flush=False)


if __name__ == "__main__":
    solve()
