from sys import stdin


def find(x, g):
    if g[x] != x:
        g[x] = find(g[x], g)
    return g[x]


def union(x, y, g):
    x = find(x, g)
    y = find(y, g)
    if x != y:
        g[y] = x


def solve():
    N, M = map(int, stdin.readline().strip().split())
    p = [0] + list(map(int, stdin.readline().strip().split()))

    wormholes = []
    for _ in range(M):
        a, b, w = map(int, stdin.readline().strip().split())
        wormholes.append((a, b, w))

    wormholes.sort(key=lambda x: x[2], reverse=True)

    g = [i for i in range(N + 1)]
    answer = -1
    i = 1
    for a, b, w in wormholes:
        while i <= N and find(i, g) == find(p[i], g):
            i += 1

        if i > N:
            break

        a, b = find(a, g), find(b, g)
        if a != b:
            union(a, b, g)
            answer = w

    print(answer)


if __name__ == "__main__":
    solve()
