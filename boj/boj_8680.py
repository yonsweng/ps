from sys import stdin


def solve():
    n, h = map(int, stdin.readline().split())

    # represent n-1 as a binary number of length h
    b = bin((n - 1) % (2**h))[2:].zfill(h)
    # print(b)

    # convert the reverse of b to decimal
    ans = 0
    for i, c in enumerate(b):
        if c == "1":
            ans += 2**i

    print(ans)


if __name__ == "__main__":
    solve()
