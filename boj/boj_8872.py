from sys import stdin, setrecursionlimit


max_total_time = 0
max_node = -1


def dfs1(i, total_time, adj, visited):
    global max_total_time, max_node

    visited[i] = True

    if len(adj[i]) == 1 and total_time > max_total_time:
        max_total_time = total_time
        max_node = i

    for j, time in adj[i]:
        if visited[j]:
            continue
        dfs1(j, total_time + time, adj, visited)


def dfs2(i, total_time, adj, visited, prev, dist):
    global max_total_time, max_node

    visited[i] = True

    dist[i] = total_time
    if len(adj[i]) == 1 and dist[i] > max_total_time:
        max_total_time = dist[i]
        max_node = i

    for j, time in adj[i]:
        if visited[j]:
            continue
        prev[j] = i
        dfs2(j, total_time + time, adj, visited, prev, dist)


def solve():
    global max_total_time, max_node

    setrecursionlimit(100010)

    n, m, l = map(int, stdin.readline().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b, t = map(int, stdin.readline().split())
        adj[a].append((b, t))
        adj[b].append((a, t))

    answer = 0
    prev = [-1] * n
    dist = [0] * n
    visited1 = [False] * n
    visited2 = [False] * n
    paths = []
    for i in range(n):
        if visited1[i]:
            continue
        max_total_time = 0
        max_node = i
        dfs1(i, 0, adj, visited1)
        max_total_time = 0
        dfs2(max_node, 0, adj, visited2, prev, dist)
        paths.append((max_node, dist[max_node]))
        answer = max(answer, dist[max_node])

    durations = []
    for i, total_time in paths:
        min_radius = total_time
        while i != -1:
            radius = max(dist[i], total_time - dist[i])
            min_radius = min(min_radius, radius)
            i = prev[i]
        durations.append(min_radius)

    durations.sort(reverse=True)

    if len(durations) >= 2:
        answer = max(answer, durations[0] + durations[1] + l)
    if len(durations) >= 3:
        answer = max(answer, durations[1] + durations[2] + 2 * l)
    print(answer)


if __name__ == "__main__":
    solve()
