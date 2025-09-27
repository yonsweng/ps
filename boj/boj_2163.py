from sys import stdin


def solve():
    N, M = map(int, stdin.readline().split())
    print(N * M - 1)


if __name__ == "__main__":
    solve()
