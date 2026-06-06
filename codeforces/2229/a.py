from sys import stdin


def solve():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        a = list(map(int, stdin.readline().split()))
        m, M = min(a), max(a)
        print((M - m + 1) // 2, flush=False)


if __name__ == "__main__":
    solve()
