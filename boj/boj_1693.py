from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 5 + 10)

MAX = 10 ** 9
MAX_COLOR = 10


def dfs(u, parent, parent_color, tree, d):
    if d[u][parent_color] != MAX:
        return d[u][parent_color]

    for color in range(1, MAX_COLOR + 1):
        if color != parent_color:
            cost = color
            for v in tree[u]:
                if v != parent:
                    cost += dfs(v, u, color, tree, d)
            d[u][parent_color] = min(d[u][parent_color], cost)

    return d[u][parent_color]


def main():
    n = int(stdin.readline())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, stdin.readline().split())
        tree[u].append(v)
        tree[v].append(u)

    d = [[MAX] * (MAX_COLOR + 1) for _ in range(n + 1)]

    print(dfs(1, 0, 0, tree, d))


if __name__ == "__main__":
    main()
