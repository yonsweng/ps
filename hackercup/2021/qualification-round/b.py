T = int(input())

for case_num in range(1, T + 1):
    N = int(input())
    C = []

    for i in range(N):
        C.append(list(input()))

    max_x_cnt = -1

    for i in range(N):
        x_cnt = 0
        fail = False

        for j in range(N):
            if C[i][j] == 'O':
                fail = True
                break

            if C[i][j] == 'X':
                x_cnt += 1

        if not fail:
            max_x_cnt = max(x_cnt, max_x_cnt)

    for j in range(N):
        x_cnt = 0
        fail = False

        for i in range(N):
            if C[i][j] == 'O':
                fail = True
                break

            if C[i][j] == 'X':
                x_cnt += 1

        if not fail:
            max_x_cnt = max(x_cnt, max_x_cnt)

    if max_x_cnt == -1:
        print(f'Case #{case_num}: Impossible')
        continue

    max_row_col_dots = []

    for i in range(N):
        x_cnt = 0
        fail = False

        for j in range(N):
            if C[i][j] == 'O':
                fail = True
                break

            if C[i][j] == 'X':
                x_cnt += 1

        if not fail and x_cnt == max_x_cnt:
            dots = []

            for j in range(N):
                if C[i][j] == '.':
                    dots.append((i, j))

            max_row_col_dots.append(tuple(dots))

    for j in range(N):
        x_cnt = 0
        fail = False

        for i in range(N):
            if C[i][j] == 'O':
                fail = True
                break

            if C[i][j] == 'X':
                x_cnt += 1

        if not fail and x_cnt == max_x_cnt:
            dots = []

            for i in range(N):
                if C[i][j] == '.':
                    dots.append((i, j))

            max_row_col_dots.append(tuple(dots))

    print(f'Case #{case_num}: {N-max_x_cnt} {len(set(max_row_col_dots))}')

'''
8
2
XO
..
2
X.
.O
3
...
...
...
3
.OX
X..
..O
3
OXO
X.X
OXO
3
.XO
O.X
XO.
4
X...
.O.O
.XX.
O.XO
5
OX.OO
X.XXX
OXOOO
OXOOO
XXXX.

'''