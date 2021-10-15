from sys import stdin
import sys


def find(i, parents):
    if parents[i] == 0:
        return i
    else:
        i_group = find(parents[i], parents)
        return i_group


def union(i, j, parents):
    i_group = find(i, parents)
    j_group = find(j, parents)

    if i_group == j_group:
        return

    parents[j_group] = i_group


def dfs(prev, i, toggle, visited, adj, groups):
    visited[i] = True
    all_sum, odd_sum = len(groups[i]), toggle * len(groups[i])

    for j in adj[i]:
        if j != prev and not visited[j]:
            all_cnt, odd_cnt = dfs(i, j, 1 - toggle, visited, adj, groups)
            all_sum += all_cnt
            odd_sum += odd_cnt

    return all_sum, odd_sum


def solve():
    sys.setrecursionlimit(100000)
    n, m = map(int, stdin.readline().split())

    imposter_edges = []
    parents = [0] * (n + 1)
    for _ in range(m):
        i, j, c = stdin.readline().split()
        i, j = int(i), int(j)
        if c == 'imposter':
            imposter_edges.append((i, j))
        else:
            union(i, j, parents)

    group = [0]
    groups = {}
    for i in range(1, n + 1):
        i_group = find(i, parents)
        group.append(i_group)
        if i_group not in groups:
            groups[i_group] = [i]
        else:
            groups[i_group].append(i)

    # check impossibility
    for i, j in imposter_edges:
        if group[i] == group[j]:
            return -1

    adj = [[] for _ in range(n + 1)]
    for i, j in imposter_edges:
        adj[group[i]].append(group[j])
        adj[group[j]].append(group[i])

    for i in range(n + 1):
        adj[i] = list(set(adj[i]))

    answer = 0
    visited = [False] * (n + 1)
    for i in groups:
        if not visited[i]:
            all_cnt, odd_cnt = dfs(0, i, 0, visited, adj, groups)
            answer += max(odd_cnt, all_cnt - odd_cnt)

    return answer


def main():
    t = int(stdin.readline())

    for _ in range(t):
        answer = solve()
        print(answer)


if __name__ == '__main__':
    main()
