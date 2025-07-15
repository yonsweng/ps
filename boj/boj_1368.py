from sys import stdin


def solve():
    N = int(stdin.readline().strip())
    W = [0]
    for _ in range(N):
        W.append(int(stdin.readline().strip()))
    P = [W]
    for i in range(1, N + 1):
        P.append([W[i]] + list(map(int, stdin.readline().strip().split())))

    # Kruskal's algorithm
    edges = []
    for i in range(0, N + 1):
        for j in range(i + 1, N + 1):
            edges.append((P[i][j], i, j))
    edges.sort()
    parent = list(range(N + 1))
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_y] = root_x
    total_cost = 0
    for cost, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            total_cost += cost
    print(total_cost)


if __name__ == "__main__":
    solve()
