visited = set()
adj = {i: [] for i in range(17)}
best = 0


def dfs(i, sheep, wolf, info):
    global visited, adj, best

    if sheep <= wolf:
        return

    if sheep > best:
        best = sheep

    visited.add(i)

    candi = set()
    for here in visited:
        for there in adj[here]:
            if there not in visited:
                candi.add(there)

    for j in candi:
        if info[j] == 0:
            dfs(j, sheep+1, wolf, info)
        else:
            dfs(j, sheep, wolf+1, info)

    visited.remove(i)


def solution(info, edges):
    for edge in edges:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])

    dfs(0, 1, 0, info)

    return best


info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

# info = [0,1,0,1,1,0,1,0,0,1,0]
# edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]

result = solution(info, edges)
print(result)
