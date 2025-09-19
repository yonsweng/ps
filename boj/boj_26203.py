from sys import stdin


def solve():
    N = int(stdin.readline().strip())
    cuts = [tuple(map(int, stdin.readline().strip().split())) for _ in range(N + 1)]

    sheet = [[0] * 2003 for _ in range(2003)]
    for i in range(2003):
        sheet[0][i] = -1
        sheet[2002][i] = -1
        sheet[i][0] = -1
        sheet[i][2002] = -1
    sheet[cuts[0][0] * 2][cuts[0][1] * 2] = -1
    for i in range(1, N + 1):
        px, py = cuts[i - 1][0] * 2, cuts[i - 1][1] * 2
        qx, qy = cuts[i][0] * 2, cuts[i][1] * 2
        if px == qx:
            for y in range(min(py, qy), max(py, qy) + 1):
                if sheet[px][y] == 0:
                    sheet[px][y] = -1
        else:
            for x in range(min(px, qx), max(px, qx) + 1):
                if sheet[x][py] == 0:
                    sheet[x][py] = -1

    color = 1
    for i in range(1, 2002):
        for j in range(1, 2002):
            if sheet[i][j] == 0:
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    if sheet[x][y] == 0:
                        sheet[x][y] = color
                        if sheet[x + 1][y] == 0:
                            stack.append((x + 1, y))
                        if sheet[x - 1][y] == 0:
                            stack.append((x - 1, y))
                        if sheet[x][y + 1] == 0:
                            stack.append((x, y + 1))
                        if sheet[x][y - 1] == 0:
                            stack.append((x, y - 1))
                color += 1

    areas = [0] * color
    for i in range(1, 2002):
        for j in range(1, 2002):
            if sheet[i][j] >= 2 and i % 2 == 1 and j % 2 == 1:
                areas[sheet[i][j]] += 1

    print(max(areas))


if __name__ == "__main__":
    solve()
