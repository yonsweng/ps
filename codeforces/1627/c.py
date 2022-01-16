from sys import stdin
from collections import deque


def read_input():
    n = int(stdin.readline())
    edges = {}
    for i in range(n - 1):
        u, v = map(int, stdin.readline().split())
        u, v = min(u, v), max(u, v)
        edges[u, v] = i
    return n, edges


def solve(n, edges):
    adj = {}
    for u, v in edges:
        if u not in adj:
            adj[u] = []
        if v not in adj:
            adj[v] = []
        adj[u].append(v)
        adj[v].append(u)

    answer = [0] * (n - 1)

    for i in range(1, n + 1):
        if len(adj[i]) != 1:
            continue

        q = deque([(i, 3, 0)])
        while len(q) > 0:
            u, x, prev = q.popleft()
            cnt = 0
            for v in adj[u]:
                if v == prev:
                    continue
                cnt += 1
                if cnt >= 2:
                    return -1
                answer[edges[min(u, v), max(u, v)]] = 5 - x
                q.append((v, 5 - x, u))

        break

    return ' '.join(map(str, answer))


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
