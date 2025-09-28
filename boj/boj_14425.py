from sys import stdin


def solve():
    N, M = map(int, stdin.readline().strip().split())
    S = [stdin.readline().strip() for _ in range(N)]
    count = 0
    for _ in range(M):
        t = stdin.readline().strip()
        if t in S:
            count += 1
    print(count)


if __name__ == "__main__":
    solve()
