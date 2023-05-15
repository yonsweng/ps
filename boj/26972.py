from sys import stdin, setrecursionlimit
from queue import PriorityQueue

setrecursionlimit(10**6)


def dfs(u, p, h, adj, avg, sol):
    sum_balance = 0

    for v in adj[u]:
        if v == p:
            continue
        balance = dfs(v, u, h, adj, avg, sol)
        if balance > 0:
            sol.append((v, u, balance))
        elif balance < 0:
            sol.append((u, v, -balance))

        sum_balance += balance

    return sum_balance + h[u] - avg


def main():
    n = int(stdin.readline())
    h = [0] + list(map(int, stdin.readline().split()))
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = list(map(int, stdin.readline().split()))
        adj[u].append(v)
        adj[v].append(u)

    # get the index that has the maximum value in h
    hi = 0
    for i in range(1, n + 1):
        if h[i] > h[hi]:
            hi = i

    avg = sum(h) // n

    sol = []
    dfs(hi, 0, h, adj, avg, sol)

    # adjacent list of sol
    adj = [[] for _ in range(n + 1)]
    inbound = [0] * (n + 1)
    for u, v, w in sol:
        adj[u].append((v, w))
        inbound[v] += 1

    # topological sort with adj
    pq = PriorityQueue()
    for i in range(1, n + 1):
        if inbound[i] == 0:
            pq.put(i)

    sol = []
    while not pq.empty():
        u = pq.get()
        for v, w in adj[u]:
            inbound[v] -= 1
            if inbound[v] == 0:
                pq.put(v)
            sol.append((u, v, w))

    # print sol
    print(len(sol))
    for u, v, w in sol:
        print(u, v, w, flush=False)


if __name__ == "__main__":
    main()
