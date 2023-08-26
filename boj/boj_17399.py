from sys import stdin


def lca_and_dist(a, b, m, depth, parent):
    p, q = a, b
    if depth[p] > depth[q]:
        p, q = q, p

    # find LCA of a and b
    for j in range(m, -1, -1):
        if depth[q] - depth[p] >= (1 << j):
            q = parent[q][j]

    lca = q
    if p != q:
        for j in range(m, -1, -1):
            if parent[p][j] != parent[q][j]:
                p = parent[p][j]
                q = parent[q][j]
        lca = parent[p][0]

    dist = depth[a] + depth[b] - 2 * depth[lca]

    return lca, dist


def mid_and_dist(a, b, m, depth, parent) -> (int, int):
    lca, dist = lca_and_dist(a, b, m, depth, parent)

    p, q = a, b
    if depth[p] > depth[q]:
        p, q = q, p

    if dist % 2 == 0:
        # a and b are in the same depth
        if depth[p] == depth[q]:
            return lca, dist

        target_depth = depth[lca] + (depth[q] - depth[p]) // 2
        for j in range(m, -1, -1):
            if depth[q] - target_depth >= (1 << j):
                q = parent[q][j]
        return q, dist

    return -1, dist


def main():
    n = int(stdin.readline().rstrip())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        x, y = map(int, stdin.readline().rstrip().split())
        adj[x].append(y)
        adj[y].append(x)

    # make LCA array
    m = 1
    while (1 << m) <= n:
        m += 1
    parent = [[0] * (m + 1) for _ in range(n + 1)]
    depth = [0] * (n + 1)
    visited = [False] * (n + 1)
    q = [1]
    visited[1] = True
    while q:
        x = q.pop()
        for y in adj[x]:
            if not visited[y]:
                visited[y] = True
                parent[y][0] = x
                depth[y] = depth[x] + 1
                q.append(y)
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            parent[i][j] = parent[parent[i][j - 1]][j - 1]

    q = int(stdin.readline().rstrip())
    for _ in range(q):
        d, e, f = map(int, stdin.readline().rstrip().split())

        mid_de, dist_de = mid_and_dist(d, e, m, depth, parent)
        mid_ef, dist_ef = mid_and_dist(e, f, m, depth, parent)
        mid_df, dist_df = mid_and_dist(d, f, m, depth, parent)

        if (
            mid_de != -1
            and lca_and_dist(mid_de, f, m, depth, parent)[1] == dist_de // 2
        ):
            print(mid_de, flush=False)
        elif (
            mid_ef != -1
            and lca_and_dist(mid_ef, d, m, depth, parent)[1] == dist_ef // 2
        ):
            print(mid_ef, flush=False)
        elif (
            mid_df != -1
            and lca_and_dist(mid_df, e, m, depth, parent)[1] == dist_df // 2
        ):
            print(mid_df, flush=False)
        else:
            print(-1, flush=False)


if __name__ == "__main__":
    main()
