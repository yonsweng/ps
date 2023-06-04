from sys import stdin, setrecursionlimit


def dfs(src, adj, depth, parent, cnt):
    n = 1
    for next in adj[src]:
        if next != parent[0][src]:
            depth[next] = depth[src] + 1
            parent[0][next] = src
            n += dfs(next, adj, depth, parent, cnt)
    cnt[src] = n
    return cnt[src]


def build_lca_tree(adj, root):
    n = len(adj)

    depth = [0] * n
    parent = [[0] * n for _ in range(20)]
    cnt = [0] * n

    dfs(root, adj, depth, parent, cnt)

    for i in range(1, 20):
        for v in range(n):
            parent[i][v] = parent[i - 1][parent[i - 1][v]]

    return depth, parent, cnt


def calc_lca(u, v, depth, parent):
    if depth[u] < depth[v]:
        u, v = v, u

    for i in range(19, -1, -1):
        if depth[u] - depth[v] >= 1 << i:
            u = parent[i][u]

    if u == v:
        return u

    for i in range(19, -1, -1):
        if parent[i][u] != parent[i][v]:
            u = parent[i][u]
            v = parent[i][v]

    return parent[0][u]


def move(u, k, parent):
    for i in range(19, -1, -1):
        if k >= 1 << i:
            u = parent[i][u]
            k -= 1 << i
    return u


def calc_answer(R, U, N, depth, parent, cnt):
    if R == U:
        return N
    if calc_lca(R, U, depth, parent) == U:
        return N - cnt[move(R, depth[R] - depth[U] - 1, parent)]
    return cnt[U]


def solve():
    setrecursionlimit(100010)

    T = int(stdin.readline())
    for case_num in range(1, T + 1):
        print(f"Case #{case_num}:")

        N, Q, R = map(int, stdin.readline().split())

        adj = [set() for _ in range(N + 1)]

        for _ in range(N - 1):
            A, B = map(int, stdin.readline().split())
            adj[A].add(B)
            adj[B].add(A)

        depth, parent, cnt = build_lca_tree(adj, R)

        for _ in range(Q):
            S, U = map(int, stdin.readline().split())
            if S == 0:
                R = U
            else:
                print(calc_answer(R, U, N, depth, parent, cnt), flush=False)


if __name__ == "__main__":
    solve()
