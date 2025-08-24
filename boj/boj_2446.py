from sys import stdin


def solve():
    N = int(stdin.readline().strip())
    for i in range(N):
        print(" " * i + "*" * (2 * N - 2 * i - 1))
    for i in range(N-1):
        print(" " * (N - i - 2) + "*" * (2 * i + 3))


if __name__ == "__main__":
    solve()
