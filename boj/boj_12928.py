from sys import stdin


def f(s, r, p, dp):
    if p > s:
        return 0

    if dp[r][p] != -1:
        pass

    elif r == 0:
        dp[r][p] = 1 if p == s else 0

    else:
        for i in range(1, r + 1):
            if f(s, r - i, p + i * (i + 1) // 2, dp) == 1:
                dp[r][p] = 1
                return dp[r][p]
        dp[r][p] = 0

    return dp[r][p]


def solve():
    n, s = map(int, stdin.readline().split())
    dp = [[-1] * (s + 1) for _ in range(n - 1)]
    answer = f(s, n - 2, 0, dp)
    print(answer)


if __name__ == "__main__":
    solve()
