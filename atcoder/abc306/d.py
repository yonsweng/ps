from sys import stdin


def solve():
    n = int(stdin.readline().rstrip())
    c = []
    for _ in range(n):
        a, b = map(int, stdin.readline().rstrip().split())
        c.append((a, b))

    dp = [[0, 0] for _ in range(n)]
    if c[0][0] == 0:
        dp[0][0] = max(0, c[0][1])
        dp[0][1] = -float("inf")
    else:
        dp[0][0] = 0
        dp[0][1] = c[0][1]

    for i in range(1, n):
        if c[i][0] == 0:
            dp[i][0] = max(
                max(dp[i - 1][0] + c[i][1], dp[i - 1][1] + c[i][1]), dp[i - 1][0]
            )
            dp[i][1] = dp[i - 1][1]
        else:
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = max(dp[i - 1][0] + c[i][1], dp[i - 1][1])

    print(max(dp[n - 1][0], dp[n - 1][1]))


if __name__ == "__main__":
    solve()
