from sys import stdin


def main():
    n = int(stdin.readline())

    dp = [1] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 10007

    print(dp[n])


if __name__ == "__main__":
    main()
