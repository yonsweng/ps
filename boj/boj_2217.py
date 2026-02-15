from sys import stdin


def solve():
    n = int(stdin.readline())
    a = [int(stdin.readline().strip()) for _ in range(n)]
    a.sort(reverse=True)
    result = 0
    for i in range(n):
        result = max(result, a[i] * (i + 1))
    print(result)


if __name__ == "__main__":
    solve()
