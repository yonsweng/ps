from sys import stdin


def solve():
    n = int(stdin.readline().strip())
    a = list(map(int, stdin.readline().strip().split()))
    b = list(map(int, stdin.readline().strip().split()))

    M = 0
    i = 0
    for j in range(n):
        while i < n and a[i] < b[j]:
            i += 1
        if i == n:
            break
        M = max(M, j + 1)
        i += 1

    m = n
    i = n - 1
    for j in range(n - 1, -1, -1):
        while i >= 0 and a[i] > b[j]:
            i -= 1
        if i < 0:
            break
        m = min(m, j)
        i -= 1

    print(M - m + 1)
    for c in range(m, M + 1):
        print(c, end=" ", flush=False)


if __name__ == "__main__":
    solve()
