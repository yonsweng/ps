from sys import setrecursionlimit, stdin

setrecursionlimit(110000)


def max_route(adj, visited, node):
    visited[node] = True
    max_route_fuel = 0

    for neighbor, fuel in adj[node]:
        if not visited[neighbor]:
            route_fuel = fuel + max_route(adj, visited, neighbor)
            max_route_fuel = max(max_route_fuel, route_fuel)

    return max_route_fuel


def solve():
    n, s = map(int, stdin.readline().split())

    total = 0
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, c = map(int, stdin.readline().split())
        adj[a].append((b, c))
        adj[b].append((a, c))
        total += c

    visited = [False] * (n + 1)

    result = 2 * total - max_route(adj, visited, s)
    print(result)


if __name__ == "__main__":
    solve()
