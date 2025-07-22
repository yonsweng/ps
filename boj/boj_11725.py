from sys import stdin


def solve():
    N = int(stdin.readline().strip())
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, stdin.readline().strip().split())
        adj[a].append(b)
        adj[b].append(a)

    # Process the adjacency list as needed
    parent = [0] * (N + 1)
    visited = [False] * (N + 1)

    # Use iterative DFS to avoid recursion limit
    stack = [(1, 0)]  # (node, parent)
    
    while stack:
        node, par = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        parent[node] = par
        
        for neighbor in adj[node]:
            if not visited[neighbor]:
                stack.append((neighbor, node))

    for i in range(2, N + 1):
        print(parent[i], flush=False)


if __name__ == "__main__":
    solve()
