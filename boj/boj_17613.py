from sys import stdin


def f(x, y, d):
    if (x, y) in d:
        return d[(x, y)]

    if x == 0 and y == 0:
        d[(0, 0)] = 0
        return 0

    ret = 0
    for i in range(1, 30):
        b = (1 << i) - 1
        s = b
        e = (1 << (i + 1)) - 2
        s = max(s, x)
        e = min(e, y)
        if s <= e:
            ret = max(ret, f(s - b, e - b, d) + i)

    d[(x, y)] = ret
    return ret


def main():
    d = {}

    input = stdin.readline
    T = int(input())
    for _ in range(T):
        x, y = map(int, input().split())
        print(f(x, y, d))


if __name__ == "__main__":
    main()
