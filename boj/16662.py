def main():
    n, m = map(int, input().split())
    
    g = [[499] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        g[i][i] = 0

    for _ in range(m):
        line = list(map(int, input().split()))
        u = line[1]
        for v in line[2:]:
            g[u][v] = g[v][u] = 1
            u = v

    # Floyd-Warshall
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])

    for _ in range(n):
        candidates = set(range(1, n + 1))
        while len(candidates) >= 1:
            u = -1
            min_sum_distances = 249002
            for v in candidates:
                sum_distances = 0
                for w in candidates:
                    sum_distances += g[v][w]
                if sum_distances < min_sum_distances:
                    min_sum_distances = sum_distances
                    u = v
            
            print(u, flush=True)
            answer = input()
            if answer == 'FOUND':
                break

            new_candidates = set()
            v = int(answer.split()[1])
            for w in candidates:
                if g[v][w] < g[u][w]:
                    new_candidates.add(w)
            candidates = new_candidates


if __name__ == '__main__':
    main()
