T = int(input())

for x in range(1, T + 1):
    G = []
    G.append(list(map(int, input().split())))
    middle_row = list(map(int, input().split()))
    middle_row.insert(1, 0)
    G.append(middle_row)
    G.append(list(map(int, input().split())))

    possible = {}

    ways = [[(0, 0), (2, 2)], [(0, 1), (2, 1)], [(0, 2), (2, 0)], [(1, 0), (1, 2)]]
    for way in ways:
        i, j = way[0]
        k, l = way[1]

        s = G[i][j] + G[k][l]
        if s % 2 == 0:
            if s // 2 not in possible:
                possible[s // 2] = 0
            possible[s // 2] += 1

    answer = max(possible.values())

    for i in [0, 2]:
        if G[i][1] - G[i][0] == G[i][2] - G[i][1]:
            answer += 1

    for j in [0, 2]:
        if G[1][j] - G[0][j] == G[2][j] - G[1][j]:
            answer += 1

    print(f'Case #{x}: {answer}')
