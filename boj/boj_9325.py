from sys import stdin


def solve():
    t = int(stdin.readline())
    for _ in range(t):
        s = int(stdin.readline())
        n = int(stdin.readline())
        for _ in range(n):
            q, p = map(int, stdin.readline().split())
            s += q * p
        print(s, flush=False)


if __name__ == "__main__":
    solve()
