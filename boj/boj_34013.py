import heapq
from sys import stdin


def solve():
    N = int(stdin.readline().strip())

    adj = [[] for _ in range(N * N)]

    for i in range(1, N):
        line = [0] + list(map(int, stdin.readline().strip().split()))
        for j in range(1, len(line)):
            u = (i - 1) * N + (j - 1)
            v = (i - 1) * N + j
            w = line[j]
            adj[u].append((v, w, 0))
            adj[v].append((u, w, 0))
        line = [0] + list(map(int, stdin.readline().strip().split()))
        for j in range(1, len(line)):
            u = (i - 1) * N + (j - 1)
            v = i * N + (j - 1)
            w = line[j]
            adj[u].append((v, w, 1))
            adj[v].append((u, w, 1))
    line = [0] + list(map(int, stdin.readline().strip().split()))
    for j in range(1, len(line)):
        u = (N - 1) * N + (j - 1)
        v = (N - 1) * N + j
        w = line[j]
        adj[u].append((v, w, 0))
        adj[v].append((u, w, 0))

    dist = [[(float("inf"), 0)] * 2 for _ in range(N * N)]
    dist[0] = [(0, 0), (0, 0)]
    pq = [(0, 0, -1)]  # (cost, node, is_vertical)
    while pq:
        cost, u, is_vertical = heapq.heappop(pq)

        n_pivot_turns = dist[u][is_vertical][1] if is_vertical != -1 else 1

        if is_vertical != -1 and dist[u][is_vertical] < (cost, n_pivot_turns):
            continue

        for v, w, is_edge_vertical in adj[u]:
            new_cost = cost + w

            if is_edge_vertical == is_vertical:
                new_pivot_turns = n_pivot_turns
            else:
                new_pivot_turns = n_pivot_turns - 1

            if dist[v][is_edge_vertical] > (new_cost, new_pivot_turns):
                dist[v][is_edge_vertical] = (new_cost, new_pivot_turns)
                heapq.heappush(pq, (new_cost, v, is_edge_vertical))

    ans = (float("inf"), 0)
    for is_vertical in range(2):
        final = dist[N * N - 1][is_vertical]
        if final < ans:
            ans = final

    print(ans[0], -ans[1])


if __name__ == "__main__":
    solve()
