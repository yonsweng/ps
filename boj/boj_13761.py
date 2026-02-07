from sys import stdin


def solve():
    digits = stdin.readline().strip()
    n = len(digits)
    digits = [0] + [int(d) for d in digits]
    letters = stdin.readline().strip()
    m = len(letters)
    letters = " " + letters

    accum = [0] * (n + 1)
    for i in range(1, n + 1):
        accum[i] = accum[i - 1] + digits[i]

    dp = [0] * (n + 1)
    for i in range(1, m + 1):
        new_dp = [0] * (n + 1)
        k = ord(letters[i]) - ord("a") + 1
        for j in range(k, n + 1):
            new_dp[j] = max(new_dp[j - 1], dp[j - k] + accum[j] - accum[j - k])
        dp = new_dp

    print(dp[n])


if __name__ == "__main__":
    solve()
