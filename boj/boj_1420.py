from sys import stdin
from collections import deque

INF = 10**9


def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


def in_node_index(x, y, m):
    return (x*m + y) * 2 + 1


def out_node_index(x, y, m):
    return (x*m + y) * 2 + 2


def get_input():
    n, m = map(int, stdin.readline().split())
    board = [list(stdin.readline().strip()) for _ in range(n)]
    return n, m, board


def add_edge(cap, flow, u, v, w):
    cap[u][v] = w
    if u not in cap[v]:
        cap[v][u] = 0
    flow[u][v] = 0
    flow[v][u] = 0


def solve(n, m, board):
    cap = [{} for _ in range(n*m*2+2)]
    flow = [{} for _ in range(n*m*2+2)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    node_k = None
    node_h = None

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'K':
                node_k = in_node_index(i, j, m)
            elif board[i][j] == 'H':
                node_h = in_node_index(i, j, m)
            elif board[i][j] == '#':
                continue

            if board[i][j] == 'K' or board[i][j] == 'H':
                add_edge(cap, flow, in_node_index(i, j, m), out_node_index(i, j, m), INF)
            else:
                add_edge(cap, flow, in_node_index(i, j, m), out_node_index(i, j, m), 1)

            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if in_range(nx, ny, n, m) and board[nx][ny] != '#':
                    add_edge(cap, flow, out_node_index(i, j, m), in_node_index(nx, ny, m), INF)
                    add_edge(cap, flow, out_node_index(nx, ny, m), in_node_index(i, j, m), INF)

    # if node_k and node_h are adjacent
    if node_k is None or node_h is None or node_h in cap[node_k+1]:
        return -1

    start_node = 0
    end_node = n*m*2+1
    add_edge(cap, flow, start_node, node_k, INF)
    add_edge(cap, flow, node_h + 1, end_node, INF)

    # calculate max flow from start_node to end_node
    total_flow = 0
    while True:
        q = deque([start_node])
        parent = {}
        while q:
            u = q.popleft()
            for v in cap[u]:
                if v not in parent and cap[u][v] > flow[u][v]:
                    parent[v] = u
                    q.append(v)
                    if v == end_node:
                        break
        if end_node not in parent:
            break

        # calculate flow
        current_flow = INF
        v = end_node
        while v != start_node:
            u = parent[v]
            current_flow = min(current_flow, cap[u][v] - flow[u][v])
            v = u

        # update flow
        v = end_node
        while v != start_node:
            u = parent[v]
            flow[u][v] = flow[u].get(v, 0) + current_flow
            flow[v][u] = flow[v].get(u, 0) - current_flow
            v = u

        total_flow += current_flow

    return total_flow


if __name__ == '__main__':
    n, m, board = get_input()
    answer = solve(n, m, board)
    print(answer)
