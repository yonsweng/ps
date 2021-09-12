T = int(input())
for i in range(1, T+1):
    N, M, A, B = map(int, input().split())
    g = [[1] * M for _ in range(N)]
    g[N-1][0] = B - N - M + 2
    g[N-1][M-1] = A - N - M + 2
    if g[N-1][0] > 0 and g[N-1][M-1] > 0:
        print(f'Case #{i}: Possible')
        for r in g:
            print(' '.join(map(str, r)))
    else:
        print(f'Case #{i}: Impossible')
