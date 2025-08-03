from sys import stdin


def solve():
    n, m = map(int, stdin.readline().split())
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        adj[a].add(b)
        adj[b].add(a)

    group = [0] * (n + 1)
    v2, v3 = 0, 0
    exists = True

    for j in range(1, n + 1):
        if j in adj[1]:
            if v2 == 0:
                v2 = j
        else:
            group[j] = 1

    for j in range(v2, n + 1):
        if j in adj[v2]:
            if v3 == 0 and group[j] != 1:
                v3 = j
        else:
            if group[j] == 1:
                exists = False
                break
            group[j] = 2

    if not exists:
        print(-1)
        return
    
    for j in range(v3, n + 1):
        if j in adj[v3]:
            if group[j] != 1 and group[j] != 2:
                exists = False
                break
        else:
            if group[j] == 1 or group[j] == 2:
                exists = False
                break
            group[j] = 3

    if not exists:
        print(-1)
        return
    
    cnt = [0, 0, 0, 0]
    for i in range(1, n + 1):
        if group[i] == 1:
            cnt[1] += 1
        elif group[i] == 2:
            cnt[2] += 1
        elif group[i] == 3:
            cnt[3] += 1

    for i in range(1, n + 1):
        if cnt[group[i] % 3 + 1] + cnt[(group[i] + 1) % 3 + 1] != len(adj[i]):
            exists = False
            break
        for j in adj[i]:
            if group[i] == group[j]:
                exists = False
                break

    if not exists:
        print(-1)
        return
    
    print(" ".join(map(str, group[1:])))


if __name__ == "__main__":
    solve()
