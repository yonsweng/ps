from sys import stdin


def precompute_parent(parent, N, max_log):
    for j in range(1, max_log):
        for i in range(N):
            if parent[i][j-1] != -1:
                parent[i][j] = parent[parent[i][j-1]][j-1]
            else:
                parent[i][j] = -1
    return parent


def find_lca(parent, level, x, y):
    if level[x] < level[y]:
        x, y = y, x

    # Lift x to the same level as y
    diff = level[x] - level[y]
    for i in range(12):
        if (diff >> i) & 1:
            x = parent[x][i]

    if x == y:
        return x

    # Lift both x and y until their parents match
    for i in range(11, -1, -1):
        if parent[x][i] != parent[y][i]:
            x = parent[x][i]
            y = parent[y][i]

    return parent[x][0]


def main():
    N = int(stdin.readline().strip())
    b = [0] + list(map(int, stdin.readline().strip()))
    X, Y = map(int, stdin.readline().strip().split())
    
    node = [0] * (2*N + 1)
    parent = [[-1] * 12 for _ in range(N)]
    child = [[] for _ in range(N)]
    level = [0] * N
    new_node = 0
    curr_node = -1
    curr_level = -1
    for k in range(1, N*2 + 1):
        if b[k] == 0:
            if curr_node != -1:
                child[curr_node].append(new_node)
            parent[new_node][0] = curr_node
            node[k] = new_node
            new_node += 1
            curr_node = node[k]
            curr_level += 1
            level[curr_node] = curr_level
        else:
            node[k] = curr_node
            curr_node = parent[curr_node][0]
            curr_level -= 1

    parent = precompute_parent(parent, N, 12)
    lca = find_lca(parent, level, node[X], node[Y])

    answer = []
    for i in range(1, 2*N + 1):
        if node[i] == lca:
            answer.append(i)

    print(' '.join(map(str, answer)))


if __name__ == "__main__":
    main()
