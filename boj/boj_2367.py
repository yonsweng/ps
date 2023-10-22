def main():
    n, k, d = map(int, input().split())

    adj = [[0] * (n + d + 2) for _ in range(n + d + 2)]
    for i in range(1, n + 1):
        adj[0][i] = k

    t = list(map(int, input().split()))
    for i, ti in enumerate(t, n + 1):
        adj[i][n + d + 1] = ti

    for i in range(1, n + 1):
        js = list(map(int, input().split()))
        for j in js[1:]:
            adj[i][n + j] = 1

    # maximum flow
    ans = 0
    while True:
        q = [0]
        prev = [-1] * (n + d + 2)
        while q:
            u = q.pop()
            for v in range(n + d + 2):
                if adj[u][v] > 0 and prev[v] == -1:
                    prev[v] = u
                    q.append(v)

        if prev[n + d + 1] == -1:
            break

        f = 1e9
        v = n + d + 1
        while v != 0:
            u = prev[v]
            f = min(f, adj[u][v])
            v = u

        v = n + d + 1
        while v != 0:
            u = prev[v]
            adj[u][v] -= f
            adj[v][u] += f
            v = u

        ans += f

    print(ans)


if __name__ == "__main__":
    main()
