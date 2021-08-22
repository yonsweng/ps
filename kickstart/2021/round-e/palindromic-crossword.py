from bisect import bisect_left
from collections import deque

T = int(input())

for x in range(1, T + 1):
    N, M = map(int, input().split())

    R = []
    for _ in range(N):
        R.append(list(input()))

    blacks_row = [[] for _ in range(N)]
    blacks_col = [[] for _ in range(M)]

    for i in range(N):
        blacks_row[i].append(-1)
    for j in range(M):
        blacks_col[j].append(-1)

    for i in range(N):
        for j in range(M):
            if R[i][j] == '#':
                blacks_row[i].append(j)
                blacks_col[j].append(i)

    for i in range(N):
        blacks_row[i].append(M)
    for j in range(M):
        blacks_col[j].append(N)

    q = deque()

    for i in range(N):
        for j in range(M):
            if R[i][j] != '#' and R[i][j] != '.':
                q.append((i, j))

    y = 0

    while len(q) > 0:
        i, j = q.popleft()

        top = blacks_col[j][bisect_left(blacks_col[j], i) - 1]
        bottom = blacks_col[j][bisect_left(blacks_col[j], i)]
        left = blacks_row[i][bisect_left(blacks_row[i], j) - 1]
        right = blacks_row[i][bisect_left(blacks_row[i], j)]

        oppo_i = top + bottom - i
        oppo_j = left + right - j

        if i != oppo_i and R[oppo_i][j] == '.':
            R[oppo_i][j] = R[i][j]
            q.append((oppo_i, j))
            y += 1
        if j != oppo_j and R[i][oppo_j] == '.':
            R[i][oppo_j] = R[i][j]
            q.append((i, oppo_j))
            y += 1

    print(f'Case #{x}: {y}')
    for i in range(N):
        print(''.join(R[i]))
