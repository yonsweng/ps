from sys import stdin


def has_c(g, c, row=None, column=None):
    n = len(g)
    m = len(g[0])

    if row is not None:
        for j in range(m):
            if g[row][j] == c:
                return True
    else:
        for i in range(n):
            if g[i][column] == c:
                return True

    return False


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n, m = list(map(int, stdin.readline().split()))
        g = []
        for _ in range(n):
            l = stdin.readline().strip()
            g.append(l)

        if n == 1:
            if g[0][0] == g[0][m-1]:
                print("YES", flush=False)
            else:
                print("NO", flush=False)
            continue

        if m == 1:
            if g[0][0] == g[n-1][0]:
                print("YES", flush=False)
            else:
                print("NO", flush=False)
            continue

        if g[0][0] == g[n-1][m-1] or g[0][m-1] == g[n-1][0]:
            print("YES", flush=False)
            continue

        flag = False

        for c in ["B", "W"]:
            if g[0][0] == c and g[n-1][0] == c and has_c(g, c, column=m-1):
                flag = True
                break
            if g[0][0] == c and g[0][m-1] == c and has_c(g, c, row=n-1):
                flag = True
                break
            if g[0][m-1] == c and g[n-1][m-1] == c and has_c(g, c, column=0):
                flag = True
                break
            if g[n-1][0] == c and g[n-1][m-1] == c and has_c(g, c, row=0):
                flag = True
                break

        if flag:
            print("YES", flush=False)
        else:
            print("NO", flush=False)


if __name__ == "__main__":
    main()