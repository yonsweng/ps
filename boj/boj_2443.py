from sys import stdin


def solve():
    n = int(stdin.readline().strip())
    for i in range(n):
        print(" " * i + "*" * (2 * (n - i) - 1))


if __name__ == "__main__":
    solve()
