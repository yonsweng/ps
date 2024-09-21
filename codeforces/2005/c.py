from sys import stdin


def solve():
    narek = "narek"
    inf = 10**9

    t = int(stdin.readline())
    for _ in range(t):
        n, m = map(int, stdin.readline().split())
        s = [stdin.readline().strip() for _ in range(n)]

        dp = [0, -inf, -inf, -inf, -inf]
        for i in range(n):
            ndp = dp[:]
            for j in range(5):
                c = j
                cnt = 0
                for k in range(m):
                    if s[i][k] == narek[c]:
                        c = (c + 1) % 5
                        cnt += 1
                    elif s[i][k] in narek:
                        cnt -= 1
                ndp[c] = max(ndp[c], dp[j] + cnt)
            dp = ndp

        answer = 0
        for i in range(5):
            answer = max(answer, dp[i] - 2 * i)

        print(answer)


if __name__ == "__main__":
    solve()
