from sys import stdin


def solve():
    N, K = map(int, stdin.readline().split())

    c = [1] * (N + 1)
    for _ in range(2, K + 1):
        for n in range(1, N + 1):
            c[n] = (c[n] + c[n - 1]) % 1000000000

    print(c[N])


if __name__ == "__main__":
    solve()
