from sys import stdin


def solve():
    n, k = map(int, stdin.readline().split())
    d = list(map(int, stdin.readline().split()))
    ans = 1 + k
    for i in range(1, n):
        ans += min(1 + k, d[i] - d[i - 1])
    print(ans)


if __name__ == "__main__":
    solve()
