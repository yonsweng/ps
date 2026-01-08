from sys import stdin


def solve():
    N = int(stdin.readline().strip())

    i = 1
    while N // i >= 5:
        if N // i % 10 >= 5:
            N = N - N % (i * 10) + (i * 10)
        i *= 10

    print(N)


if __name__ == "__main__":
    solve()
