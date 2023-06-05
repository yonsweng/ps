from sys import stdin
from bisect import bisect_left


def solve():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    m = int(stdin.readline())
    b = list(map(int, stdin.readline().split()))

    a.sort()
    for bi in b:
        idx = bisect_left(a, bi)
        if idx < len(a) and a[idx] == bi:
            print(1, flush=False)
        else:
            print(0, flush=False)


if __name__ == "__main__":
    solve()
