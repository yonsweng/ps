from sys import stdin


def solve():
    n = int(stdin.readline())
    a = [0] + list(map(int, stdin.readline().split()))

    c = []
    for i in range(1, n + 1):
        s = 0
        for j in range(i, n + 1):
            s += a[j]
            c.append((s, i, j))

    c.sort()

    INF = 5 * 10**17 + 1
    t = [[INF] * (n + 1) for _ in range(n + 1)]

    for k in range(1, len(c)):
        left = c[k - 1]
        right = c[k]

        l = min(left[1], right[1])
        r = min(max(left[1], right[1]) - 1, min(left[2], right[2]))
        if l <= r:
            t[l][r] = min(t[l][r], abs(right[0] - left[0]))

        l = max(min(left[2], right[2]) + 1, max(left[1], right[1]))
        r = max(left[2], right[2])
        if l <= r:
            t[l][r] = min(t[l][r], abs(right[0] - left[0]))

    for i in range(1, n):
        for j in range(n, 0, -1):
            t[i][j - 1] = min(t[i][j - 1], t[i][j])
            t[i + 1][j] = min(t[i + 1][j], t[i][j])

    for i in range(1, n + 1):
        print(t[i][i], flush=False)


if __name__ == "__main__":
    solve()
