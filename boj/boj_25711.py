from math import sqrt
from sys import stdin


def solve():
    N, Q = map(int, stdin.readline().split())
    x = [0] + list(map(int, stdin.readline().split()))
    y = [0] + list(map(int, stdin.readline().split()))

    length = [0] * (N + 1)
    coef = [0] * (N + 1)
    for i in range(2, N + 1):
        length[i] = sqrt((x[i] - x[i - 1]) ** 2 + (y[i] - y[i - 1]) ** 2)

        if y[i - 1] < y[i]:
            coef[i] = 3
        elif y[i - 1] == y[i]:
            coef[i] = 2
        else:
            coef[i] = 1

    accu1 = [0] * (N + 1)
    accu2 = [0] * (N + 1)
    for i in range(2, N + 1):
        accu1[i] = accu1[i - 1] + length[i] * coef[i]
    for i in range(N - 1, 0, -1):
        accu2[i] = accu2[i + 1] + length[i + 1] * (4 - coef[i + 1])

    for _ in range(Q):
        i, j = map(int, stdin.readline().split())

        if i < j:
            total_length = accu1[j] - accu1[i]
            print(total_length, flush=False)
        else:
            total_length = accu2[j] - accu2[i]
            print(total_length, flush=False)


if __name__ == "__main__":
    solve()
