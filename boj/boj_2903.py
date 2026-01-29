from sys import stdin


def solve():
    n = int(stdin.readline())

    base = 2
    for _ in range(n):
        base = base * 2 - 1
    print(base**2)


if __name__ == "__main__":
    solve()
