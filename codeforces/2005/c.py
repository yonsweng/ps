from sys import stdin
from bisect import bisect_left


def solve():
    t = int(stdin.readline())
    for _ in range(t):
        n, m, q = map(int, stdin.readline().split())
        b = list(map(int, stdin.readline().split()))
        a = list(map(int, stdin.readline().split()))
        b.sort()

        for ai in a:
            j = bisect_left(b, ai)
            if j == 0:
                print(b[0] - 1, flush=False)
            elif j == m:
                print(n - b[m - 1], flush=False)
            else:
                print((b[j] - b[j - 1]) // 2, flush=False)


if __name__ == "__main__":
    solve()
