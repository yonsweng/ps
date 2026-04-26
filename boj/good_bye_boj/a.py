from sys import stdin


def solve():
    n = int(stdin.readline())
    for i in range(n):
        print(" " * (2 * n - i - 1) + "*" + " " * (i + 1), end="")
        print(" " * (n - i - 1) + "*" + " " * (i + 1), end="")
        print(" " * i + "*" + " " * (n - i - 1))
    for i in range(n):
        print(" " * (2 * n - i - 1 - n) + "*" + " " * (i + 1), end="")
        print(" " * (i + n) + "*" + " " * (n - i - 1), end="")
        print(" " * (n - i) + "*" + " " * i)


if __name__ == "__main__":
    solve()
