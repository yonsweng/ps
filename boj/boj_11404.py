from sys import stdin


def solve():
    n = int(stdin.readline().strip())
    m = int(stdin.readline().strip())
    graph = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0
    for _ in range(m):
        u, v, w = map(int, stdin.readline().strip().split())
        graph[u - 1][v - 1] = min(graph[u - 1][v - 1], w)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    for i in range(n):
        for j in range(n):
            if graph[i][j] == float('inf'):
                print("0", end=" ")
            else:
                print(graph[i][j], end=" ")
        print()


if __name__ == "__main__":
    solve()
