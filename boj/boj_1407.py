from sys import stdin


def solve():
    A, B = map(int, stdin.readline().split())

    result = 0
    pos = 1
    while pos <= B:
        temp = (B + pos) // (pos * 2) - (A + pos - 1) // (pos * 2)
        result += temp * pos
        pos *= 2

    print(result)


if __name__ == "__main__":
    solve()
