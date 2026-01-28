from sys import stdin


def solve():
    Lj, P = map(int, stdin.readline().split())
    A = list(map(int, stdin.readline().split()))
    total = Lj * P
    B = [a - total for a in A]
    print(" ".join(map(str, B)))


if __name__ == "__main__":
    solve()
