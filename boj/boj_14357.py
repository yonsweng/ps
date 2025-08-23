import itertools
from sys import stdin


def solve():
    T = int(stdin.readline().strip())
    for t in range(T):
        N, K = map(int, stdin.readline().strip().split())
        P = list(map(float, stdin.readline().strip().split()))

        answer = 0

        for comb in itertools.combinations(P, K):
            dp = [[0] * (K // 2 + 1) for _ in range(K + 1)]
            dp[0][0] = 1

            for i in range(1, K + 1):
                for j in range(min(i, K // 2) + 1):
                    dp[i][j] = dp[i - 1][j] * (1 - comb[i - 1])
                    if j > 0:
                        dp[i][j] += dp[i - 1][j - 1] * comb[i - 1]

            answer = max(answer, dp[K][K // 2])

        print("Case #{}: {}".format(t + 1, answer), flush=False)


if __name__ == "__main__":
    solve()
