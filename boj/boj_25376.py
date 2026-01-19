from collections import deque
from sys import stdin


def binary_to_decimal(binary_list):
    result = 0
    for bit in binary_list:
        result = (result << 1) | bit
    return result


def bfs(s0, adj, n, dp):
    queue = deque([s0])
    while queue:
        s_t1 = queue.popleft()
        for i in range(n):
            if s_t1 & (1 << i) == 0:
                s_t2 = (s_t1 | (1 << i)) ^ adj[i]
                if dp[s_t2] == -1 or dp[s_t2] > dp[s_t1] + 1:
                    dp[s_t2] = dp[s_t1] + 1
                    queue.append(s_t2)


def solve():
    n = int(stdin.readline().strip())
    a = list(map(int, stdin.readline().strip().split()))
    adj = [0] * n
    for i in range(n):
        line = list(map(int, stdin.readline().strip().split()))
        for bi in line[1:]:
            adj[i] |= 1 << (bi - 1)

    s0 = binary_to_decimal(reversed(a))
    dp = [-1] * (1 << n)
    dp[s0] = 0

    bfs(s0, adj, n, dp)

    print(dp[(1 << n) - 1])


if __name__ == "__main__":
    solve()
