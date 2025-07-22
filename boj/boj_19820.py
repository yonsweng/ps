from sys import stdin


def solve():
    n, m = map(int, stdin.readline().split())
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, stdin.readline().split())
        adj[u].add(v)
        adj[v].add(u)

    p, q = 0, 0
    for i in range(1, n + 1):
        if len(adj[i]) == n - 1:
            continue

        for j in range(i + 1, n + 1):
            if j not in adj[i]:
                p, q = i, j
                break

        if p != 0:
            break

    a = [0] * (n + 1)
    b = [0] * (n + 1)
    cnt = 3
    for i in range(1, n + 1):
        if i == p:
            a[i] = 1
            b[i] = 1
        elif i == q:
            a[i] = 2
            b[i] = 1
        else:
            a[i] = cnt
            b[i] = cnt
            cnt += 1

    if p == 0:
        print("NO")
    else:
        print("YES")
        print(*a[1:])
        print(*b[1:])


if __name__ == "__main__":
    solve()
