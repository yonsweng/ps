from sys import stdin


def solve():
    t = int(stdin.readline().rstrip())
    for _ in range(t):
        n = int(stdin.readline().rstrip())
        a, b, c, p, s = 0, 0, 0, 0, 0
        no = False
        for _ in range(n):
            ai, bi, ci, pi = map(int, stdin.readline().rstrip().split())
            if max(ai - a, 0) + max(bi - b, 0) + max(ci - c, 0) > pi - p - 1 + s:
                no = True
            else:
                s += (pi - p - 1) - max(ai - a, 0) - max(bi - b, 0) - max(ci - c, 0)
                a, b, c = max(a, ai), max(b, bi), max(c, ci)
                p = pi
        if no:
            print("NO", flush=False)
        else:
            print("YES", flush=False)


if __name__ == "__main__":
    solve()
