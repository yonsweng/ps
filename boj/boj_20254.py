from sys import stdin


def solve():
    ur, tr, uo, to = map(int, stdin.readline().strip().split())
    result = 56 * ur + 24 * tr + 14 * uo + 6 * to
    print(result)


if __name__ == "__main__":
    solve()
