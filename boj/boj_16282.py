from sys import stdin


def solve():
    n = int(stdin.readline().strip())

    r = 1
    while True:
        max_n = (2 ** (r + 1)) * r + 2 ** (r + 1) - 1
        if n <= max_n:
            break
        r += 1

    print(r)


if __name__ == "__main__":
    solve()
