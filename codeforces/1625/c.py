from sys import stdin


def read_input():
    n, l, k = map(int, stdin.readline().split())
    d = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    return n, l, k, d, a


def solve(n, l, k, d, a):
    d.append(l)
    dp = [[10 ** 9] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        for j in range(min(i, k + 1)):
            for l in range(1, min(i, j + 1) + 1):
                val = dp[i-l][j-l+1] + (d[i] - d[i-l]) * a[i-l]
                dp[i][j] = min(dp[i][j], val)

    return min(dp[i])


def main():
    t = 1
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
