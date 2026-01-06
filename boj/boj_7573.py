from bisect import bisect_left, bisect_right
from sys import stdin


def solve():
    N, l, M = map(int, stdin.readline().split())
    positions = [tuple(map(int, stdin.readline().split())) for _ in range(M)]

    xs = sorted(set(x for x, y in positions))
    ys = sorted(set(y for x, y in positions))

    # 2D prefix sum
    prefix = [[0] * (len(ys) + 1) for _ in range(len(xs) + 1)]
    for x, y in positions:
        xi = bisect_left(xs, x)
        yi = bisect_left(ys, y)
        prefix[xi + 1][yi + 1] += 1

    for i in range(len(xs) + 1):
        for j in range(len(ys) + 1):
            if i > 0:
                prefix[i][j] += prefix[i - 1][j]
            if j > 0:
                prefix[i][j] += prefix[i][j - 1]
            if i > 0 and j > 0:
                prefix[i][j] -= prefix[i - 1][j - 1]

    def query(mx, Mx, my, My):
        li = bisect_left(xs, mx)
        ri = bisect_right(xs, Mx)
        bi = bisect_left(ys, my)
        ti = bisect_right(ys, My)
        return prefix[ri][ti] - prefix[li][ti] - prefix[ri][bi] + prefix[li][bi]

    max_fish_count = 0
    for mx in xs:
        for my in ys:
            for xl in range(1, l // 2):
                yl = l // 2 - xl
                max_fish_count = max(max_fish_count, query(mx, mx + xl, my, my + yl))

    print(max_fish_count)


if __name__ == "__main__":
    solve()
