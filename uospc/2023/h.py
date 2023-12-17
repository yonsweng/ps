from sys import stdin

MAX_K = 512


def main():
    n = int(stdin.readline())
    t = list(map(int, stdin.readline().split()))

    dp = [[[-MAX_K] * MAX_K for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i][t[i]] = 1
    for s in range(1, n):
        for j in range(s, n):
            i = j - s
            for k in range(MAX_K):
                dp[i][j][k] = max(dp[i + 1][j][k], dp[i][j - 1][k])
                dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k ^ t[j]] + 1)
                dp[i][j][k] = max(dp[i][j][k], dp[i + 1][j][k ^ t[i]] + 1)

    q = int(stdin.readline())
    for _ in range(q):
        l, r = map(int, stdin.readline().split())
        answer = 0
        for k in range(MAX_K):
            answer = max(answer, dp[l - 1][r - 1][k] + k)
        print(answer)


if __name__ == "__main__":
    main()
