from collections import deque
from sys import stdin


def bfs(adj, dist, N):
    queue = deque([N])
    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    return dist


def solve():
    N = int(stdin.readline().strip())
    A = [0] + list(map(int, stdin.readline().strip().split()))

    adj = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        adj[A[i]].append(i)

    dist = [-1] * N + [0]
    dist = bfs(adj, dist, N)

    print("\n".join(map(str, dist[1:])))


if __name__ == "__main__":
    solve()
