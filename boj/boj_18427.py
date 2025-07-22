from sys import stdin


def solve():
    N, M, H = map(int, stdin.readline().split())
    block = [[]]
    for _ in range(N):
        block.append(list(map(int, stdin.readline().split())))

    dp = [[0] * (H + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(H + 1):
            dp[i][j] = dp[i - 1][j]  # not using the i-th block
            for k in range(len(block[i])):
                if j >= block[i][k]:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - block[i][k]]) % 10007

    print(dp[N][H])


if __name__ == "__main__":
    solve()
