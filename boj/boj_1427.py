from sys import stdin


def solve():
    n = stdin.readline().rstrip()
    n = sorted(n, reverse=True)
    print("".join(n))


if __name__ == "__main__":
    solve()
