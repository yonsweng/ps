from sys import stdin


def solve():
    N = int(stdin.readline())
    for i in range(1, N):
        print("*" * i + " " * (2 * (N - i)) + "*" * i)
    print("*" * (2 * N))
    for i in range(N - 1, 0, -1):
        print("*" * i + " " * (2 * (N - i)) + "*" * i)


if __name__ == "__main__":
    solve()
