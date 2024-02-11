from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def find(parent, weight, a):
    if parent[a] == a:
        return a
    root = find(parent, weight, parent[a])
    weight[a] += weight[parent[a]]
    parent[a] = root
    return root


def union(parent, weight, a, b, w):
    root_a = find(parent, weight, a)
    root_b = find(parent, weight, b)
    if root_a == root_b:
        return
    parent[root_a] = root_b
    weight[root_a] = weight[b] - weight[a] + w


def main():
    while True:
        n, m = map(int, stdin.readline().split())
        if n == 0 and m == 0:
            break

        parent = [i for i in range(n + 1)]
        weight = [0 for _ in range(n + 1)]
        for _ in range(m):
            cmd = stdin.readline().split()
            if cmd[0] == "!":
                a, b, w = map(int, cmd[1:])
                union(parent, weight, a, b, w)
            else:
                a, b = map(int, cmd[1:])
                if find(parent, weight, a) == find(parent, weight, b):
                    print(weight[a] - weight[b], flush=False)
                else:
                    print("UNKNOWN", flush=False)


if __name__ == "__main__":
    main()
