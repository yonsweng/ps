from sys import stdin


def is_connected(adj, src, dst):
    visited = [False] * len(adj)
    stack = [src]

    while stack:
        v = stack.pop()

        if v == dst:
            return True

        if not visited[v]:
            visited[v] = True
            stack.extend(adj[v])

    return False


def solve():
    n, m = map(int, stdin.readline().split())
    edges = [tuple(map(int, stdin.readline().split())) for _ in range(m)]

    answer = 0

    adj = [[] for _ in range(n)]

    for j, (a, b) in enumerate(edges[::-1], 1):
        i = m - j

        adj[a].append(b)
        adj[b].append(a)

        if is_connected(adj, 0, n - 1):
            adj[a].pop()
            adj[b].pop()

            answer = (answer + pow(3, i, 1000000007)) % 1000000007

    print(answer)


if __name__ == "__main__":
    solve()
