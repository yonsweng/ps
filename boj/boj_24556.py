from sys import stdin


def dfs(i, p, adj, dp):
    # Add bounds checking
    if i < 0 or i >= len(dp):
        return [float('inf')] * 3
        
    if dp[i][0] != float('inf'):
        return dp[i]

    if len(adj[i]) == 0:
        dp[i] = [0, p[i], float('inf')]
        return dp[i]
    
    dp[i][0] = 0

    min_val = float('inf')
    for j in adj[i]:
        child_dp = dfs(j, p, adj, dp)
        min_val = min(min_val, child_dp[1])
    dp[i][1] = p[i] + min_val

    min_val = float('inf')
    for j in adj[i]:
        child_dp = dfs(j, p, adj, dp)
        min_val = min(min_val, child_dp[2])
    dp[i][2] = p[i] + min_val

    if len(adj[i]) >= 2:
        min1, min2 = float('inf'), float('inf')
        for j in adj[i]:
            child_dp = dfs(j, p, adj, dp)
            if child_dp[1] < min1:
                min2 = min1
                min1 = child_dp[1]
            elif child_dp[1] < min2:
                min2 = child_dp[1]
        dp[i][2] = min(dp[i][2], p[i] + min1 + min2)

    return dp[i]


def solve():
    n, m = map(int, stdin.readline().split())
    p = [0]
    while len(p) < n + 1:
        p += list(map(int, stdin.readline().split()))

    adj = [[] for _ in range(n + 10)]
    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        # Add bounds checking
        if 1 <= a <= n and 1 <= b <= n:
            adj[a].append(b)

    in_nodes = [-1] * (n + 10)
    for i in range(1, n + 1):
        for j in adj[i]:
            in_nodes[j] = i

    root_nodes = []
    for i in range(1, n + 1):
        if in_nodes[i] == -1:
            root_nodes.append(i)

    adj[0] = root_nodes

    dp = [[float('inf')] * 3 for _ in range(n + 10)]
    dp[0] = dfs(0, p, adj, dp)

    print(dp[0][2])


if __name__ == "__main__":
    solve()
