from sys import stdin


def main():
    input = stdin.readline
    N, M = map(int, input().split())
    m = [0] + list(map(int, input().split()))
    c = [0] + list(map(int, input().split()))

    mc = [(m[i], c[i]) for i in range(N + 1)]
    mc.sort(key=lambda x: x[1])

    dp = [0] * 10001
    for i in range(1, N + 1):
        memory, cost = mc[i]
        for j in range(10000, cost - 1, -1):
            dp[j] = max(dp[j], dp[j - cost] + memory)

    for i in range(10001):
        if dp[i] >= M:
            print(i)
            break


if __name__ == "__main__":
    main()
