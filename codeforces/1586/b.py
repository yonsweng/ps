from sys import stdin


def solve():
    n, m = map(int, stdin.readline().split())

    s = set(range(1, n+1))

    for _ in range(m):
        a, b, c = map(int, stdin.readline().split())
        if b in s:
            s.remove(b)

    center = s.pop()

    for u in range(1, n+1):
        if u != center:
            print(center, u)


def main():
    t = int(stdin.readline())

    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
