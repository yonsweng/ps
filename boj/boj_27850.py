from sys import stdin


def solve():
    t = int(stdin.readline())
    for _ in range(t):
        stdin.readline()
        n = int(stdin.readline())
        d = [list(stdin.readline().rstrip()) for _ in range(n)]
        k = int(stdin.readline())
        s = [[list(stdin.readline().rstrip()) for _ in range(k)]]

        for l in range(3):
            s.append([[s[l][j][i] for j in range(k - 1, -1, -1)] for i in range(k)])

        ans = [["."] * n for _ in range(n)]
        for i in range(n - k + 1):
            for j in range(n - k + 1):
                for l in range(4):
                    flag = True
                    for x in range(k):
                        for y in range(k):
                            if d[i + x][j + y] == "." and s[l][x][y] == "*":
                                flag = False
                                break
                        if not flag:
                            break
                    if flag:
                        for x in range(k):
                            for y in range(k):
                                if s[l][x][y] == "*":
                                    ans[i + x][j + y] = "*"

        if ans == d:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
