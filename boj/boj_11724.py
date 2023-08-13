from sys import stdin, setrecursionlimit

setrecursionlimit(10**5)

n, m = map(int, stdin.readline().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
cnt = 0


# number of connected components
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)
