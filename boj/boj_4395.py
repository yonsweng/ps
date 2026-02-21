from sys import stdin


def solve():
    n = int(stdin.readline())
    for _ in range(n):
        x, y = map(int, stdin.readline().split())
        diff = y - x
        s, l = 0, 0
        while diff > l:
            s += 1
            l += (s + 1) // 2
        print(s, flush=False)


if __name__ == "__main__":
    solve()
