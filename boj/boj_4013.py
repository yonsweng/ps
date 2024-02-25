from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    n, m = map(int, stdin.readline().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        adj[a].append(b)
    cashes = [0] + list(int(stdin.readline()) for _ in range(n))
    s, _ = map(int, stdin.readline().split())
    inters = set(map(int, stdin.readline().split()))

    # find strongly connected components using Tarjan's algorithm
    sccs = []
    scc_id = [0] * (n + 1)
    stack = []
    dfsn = [0] * (n + 1)
    closed = [False] * (n + 1)
    count = 1

    def dfs(v):
        nonlocal count
        dfsn[v] = count
        count += 1
        stack.append(v)
        result = dfsn[v]
        for w in adj[v]:
            if not dfsn[w]:
                result = min(result, dfs(w))
            elif not closed[w]:
                result = min(result, dfsn[w])
        if result == dfsn[v]:
            scc = []
            while True:
                w = stack.pop()
                scc.append(w)
                scc_id[w] = len(sccs)
                closed[w] = True
                if w == v:
                    break
            sccs.append(scc)
        return result

    for v in range(1, n + 1):
        if not closed[v]:
            dfs(v)

    # build new graph with strongly connected components
    new_n = len(sccs)
    new_adj = [[] for _ in range(new_n)]
    new_cashes = [0] * new_n
    new_inter = set()
    for v in range(1, n + 1):
        for w in adj[v]:
            if scc_id[v] != scc_id[w]:
                new_adj[scc_id[v]].append(scc_id[w])
    for i, scc in enumerate(sccs):
        for v in scc:
            new_cashes[i] += cashes[v]
            if v in inters:
                new_inter.add(i)

    # topological sort
    indegree = [0] * new_n
    for v in range(new_n):
        for w in new_adj[v]:
            indegree[w] += 1

    queue = []
    for i in range(new_n):
        if indegree[i] == 0 and i != scc_id[s]:
            queue.append(i)

    indegree[scc_id[s]] += 1
    while queue:
        v = queue.pop()
        for w in new_adj[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                queue.append(w)
    indegree[scc_id[s]] -= 1

    max_cash = [0] * new_n
    queue = []
    for i in range(new_n):
        if i == scc_id[s]:
            queue.append(i)
            max_cash[i] = new_cashes[i]
            break

    while queue:
        v = queue.pop()
        for w in new_adj[v]:
            indegree[w] -= 1
            max_cash[w] = max(max_cash[w], max_cash[v] + new_cashes[w])
            if indegree[w] == 0:
                queue.append(w)

    result = 0
    for i in range(new_n):
        if i in new_inter:
            result = max(result, max_cash[i])

    print(result)


if __name__ == "__main__":
    main()
