from sys import stdin


def solve():
    n = int(stdin.readline().strip())

    i, p, total = 1, 4, 3
    while total < n:
        i += 1
        total += p
        p *= 2
    print((i + 1) // 2)


if __name__ == "__main__":
    solve()
