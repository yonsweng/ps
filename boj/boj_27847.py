from sys import stdin
from bisect import bisect_left


def solve():
    g, n = map(int, stdin.readline().split())

    grazed = []
    for _ in range(g):
        grazed.append(tuple(map(int, stdin.readline().split())))
    grazed.sort(key=lambda x: x[2])

    answer = 0
    for _ in range(n):
        x, y, t = map(int, stdin.readline().split())

        ok = False

        i = bisect_left(grazed, t, key=lambda p: p[2])
        if i < g:
            if t == grazed[i][2]:
                if x != grazed[i][0] or y != grazed[i][1]:
                    ok = True
            else:
                if (x - grazed[i][0]) ** 2 + (y - grazed[i][1]) ** 2 > (
                    t - grazed[i][2]
                ) ** 2:
                    ok = True
                i -= 1
                if i >= 0:
                    if (x - grazed[i][0]) ** 2 + (y - grazed[i][1]) ** 2 > (
                        t - grazed[i][2]
                    ) ** 2:
                        ok = True
        else:
            i -= 1
            if i >= 0:
                if (x - grazed[i][0]) ** 2 + (y - grazed[i][1]) ** 2 > (
                    t - grazed[i][2]
                ) ** 2:
                    ok = True

        if ok:
            answer += 1

    print(answer)


if __name__ == "__main__":
    solve()
