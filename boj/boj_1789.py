from sys import stdin


def solve():
    s = int(stdin.readline().rstrip())
    n = 1
    total = 0
    while True:
        total += n
        if total > s:
            print(n - 1)
            break
        n += 1


if __name__ == "__main__":
    solve()
