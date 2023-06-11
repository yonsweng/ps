from sys import stdin


def solve():
    n = int(stdin.readline())
    d = []
    rm = []
    for _ in range(n):
        di, c = stdin.readline().rstrip().split()
        d.append(list(di))
        rm.append(int(c))
    bm = list(map(int, stdin.readline().rstrip().split()))

    t = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            t[i][j] += 1
            if d[i][j] == "R":
                t[i][j + 1] += t[i][j]
            else:
                t[i + 1][j] += t[i][j]

    cost = 0
    for i, rm_i in enumerate(rm):
        cost += rm_i * t[i][n]
    for j, bm_j in enumerate(bm):
        cost += bm_j * t[n][j]
    print(cost)

    q = int(stdin.readline())
    for _ in range(q):
        i, j = map(int, stdin.readline().rstrip().split())
        i -= 1
        j -= 1

        tt = t[i][j]

        ii, jj = i, j
        while True:
            if d[ii][jj] == "R":
                t[ii][jj + 1] -= tt
                if jj + 1 == n:
                    cost -= rm[ii] * tt
                    break
                jj += 1
            else:
                t[ii + 1][jj] -= tt
                if ii + 1 == n:
                    cost -= bm[jj] * tt
                    break
                ii += 1

        d[i][j] = "D" if d[i][j] == "R" else "R"

        ii, jj = i, j
        while True:
            if d[ii][jj] == "R":
                t[ii][jj + 1] += tt
                if jj + 1 == n:
                    cost += rm[ii] * tt
                    break
                jj += 1
            else:
                t[ii + 1][jj] += tt
                if ii + 1 == n:
                    cost += bm[jj] * tt
                    break
                ii += 1

        print(cost, flush=False)


if __name__ == "__main__":
    solve()
