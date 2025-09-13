from sys import stdin


def solve():
    N, k = map(int, stdin.readline().strip().split())
    x = list(map(int, stdin.readline().strip().split()))
    x.sort(reverse=True)
    print(x[k - 1])


if __name__ == "__main__":
    solve()
