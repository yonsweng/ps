from sys import stdin


def solve():
    N, d = map(int, stdin.readline().split())

    digits = [i for i in range(1, 10) if i != d]  # usable digits (positive only)

    # DP to find minimal number of digits needed for each sum up to N
    INF = 10**9
    min_cnt = [INF] * (N + 1)
    min_cnt[0] = 0
    for s in range(1, N + 1):
        best = INF
        for dig in digits:
            if s >= dig and min_cnt[s - dig] + 1 < best:
                best = min_cnt[s - dig] + 1
        min_cnt[s] = best

    length = min_cnt[N]

    # Build lexicographically smallest number with that minimal length
    result = []
    remaining = N
    for pos in range(length):
        for dig in digits:
            if remaining >= dig and min_cnt[remaining - dig] == length - pos - 1:
                result.append(str(dig))
                remaining -= dig
                break

    print("".join(result))


if __name__ == "__main__":
    solve()
