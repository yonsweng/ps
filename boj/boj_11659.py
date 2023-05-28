from sys import stdin


def solve():
    n, m = map(int, stdin.readline().split())
    a = [0] + list(map(int, stdin.readline().split()))
    q = [(i, tuple(map(int, stdin.readline().split()))) for i in range(m)]

    # Mo's algorithm
    ans = [0] * m
    q.sort(key=lambda x: (x[1][0] // int(n**0.5), x[1][1]))
    l, r = q[0][1][0], q[0][1][1]
    for i in range(l, r + 1):
        ans[q[0][0]] += a[i]
    for i in range(1, m):
        ans[q[i][0]] = ans[q[i - 1][0]]
        l_, r_ = q[i][1][0], q[i][1][1]
        while l_ < l:
            l -= 1
            ans[q[i][0]] += a[l]
        while r < r_:
            r += 1
            ans[q[i][0]] += a[r]
        while l < l_:
            ans[q[i][0]] -= a[l]
            l += 1
        while r_ < r:
            ans[q[i][0]] -= a[r]
            r -= 1

    for i in range(m):
        print(ans[i], flush=False)


if __name__ == "__main__":
    solve()
