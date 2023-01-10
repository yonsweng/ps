from sys import stdin


MAX_H = 500000


def main():
    n = int(stdin.readline())
    h = [0] + list(map(int, stdin.readline().split()))

    d = [[-1] * (MAX_H + 1) for _ in range(n + 1)]
    d[0][0] = 0

    for i in range(1, n + 1):
        for j in range(MAX_H):
            d[i][j] = d[i - 1][j]
            if j + h[i] <= MAX_H and d[i - 1][j + h[i]] != -1:
                d[i][j] = max(d[i][j], d[i - 1][j + h[i]])
            if j - h[i] >= 0 and d[i - 1][j - h[i]] != -1:
                d[i][j] = max(d[i][j], d[i - 1][j - h[i]] + h[i])
            if h[i] - j >= 0 and d[i - 1][h[i] - j] != -1:
                d[i][j] = max(d[i][j], d[i - 1][h[i] - j] + j)

    if d[n][0] == 0:
        print(-1)
    else:
        print(d[n][0])


if __name__ == "__main__":
    main()
