from sys import stdin


def solve():
    buy = int(stdin.readline().strip())
    m, n = map(int, stdin.readline().strip().split())
    a = [int(stdin.readline().strip()) for _ in range(m)]
    b = [int(stdin.readline().strip()) for _ in range(n)]

    a_cnt = [1] + [0] * 2000000
    b_cnt = [1] + [0] * 2000000

    for i in range(m):
        total = 0
        for j in range(i, m + i - 1):
            j %= m
            total += a[j]
            a_cnt[total] += 1
    a_cnt[sum(a)] += 1

    for i in range(n):
        total = 0
        for j in range(i, n + i - 1):
            j %= n
            total += b[j]
            b_cnt[total] += 1
    b_cnt[sum(b)] += 1

    answer = 0
    for i in range(buy + 1):
        if buy - i >= 0:
            answer += a_cnt[i] * b_cnt[buy - i]

    print(answer)


if __name__ == "__main__":
    solve()
