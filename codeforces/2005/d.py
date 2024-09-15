from sys import stdin


def solve():
    narek = "narek"

    t = int(stdin.readline())
    for _ in range(t):
        n, m = map(int, stdin.readline().split())
        s = [stdin.readline().strip() for _ in range(n)]

        score_n = [[[0] * len(narek) for _ in range(len(narek))] for _ in range(n)]
        for k in range(n):
            for j in range(len(narek)):
                r = s[k].rfind(narek[j])
                for i in range(len(narek)):
                    c = (i + 1) % len(narek)
                    for l in range(r + 1):
                        if s[k][l] == narek[c]:
                            if c == len(narek) - 1:
                                score_n[k][i][j] += len(narek)
                            c = (c + 1) % len(narek)
                    score_n[k][i][j] -= m - score_n[k][i][j]

        dp = [[0] * len(narek) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(len(narek)):
                for k in range(i):
                    for l in range(len(narek)):
                        dp[i][j] = max(dp[i][j], dp[k][l] + score_n[i - 1][l][j])

        print(dp)


if __name__ == "__main__":
    solve()
