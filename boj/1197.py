from sys import stdin


parent = dict()
rank = dict()


# vertice 초기화
def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0


# 해당 vertice의 최상위 정점을 찾는다
def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]


# 두 정점을 연결한다
def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1


def kruskal(graph):
    minimum_spanning_tree = []

    # 초기화
    for vertice in graph["vertices"]:
        make_set(vertice)

    # 간선 weight 기반 sorting
    edges = graph["edges"]
    edges.sort()

    # 간선 연결 (사이클 없게)
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.append(edge)

    return sum(a[0] for a in minimum_spanning_tree)


graph = {
    "vertices": None,
    "edges": [],
}

v, e = map(int, input().split())
graph["vertices"] = [i for i in range(1, v + 1)]
for _ in range(e):
    a, b, c = map(int, stdin.readline().split())
    graph["edges"].append((c, a, b))
    graph["edges"].append((c, b, a))


print(kruskal(graph))
