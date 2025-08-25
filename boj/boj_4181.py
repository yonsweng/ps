from functools import cmp_to_key
from sys import stdin


def compare(a, b):
    if a[0] == b[0] == 0:
        return b[1] - a[1]
    if a[0] == 0:
        return 1
    if b[0] == 0:
        return -1
    return a[1] * b[0] - b[1] * a[0]


def compare_x(a, b):
    return a[0] - b[0]


def compare_x_reverse(a, b):
    return b[0] - a[0]


def solve():
    n = int(stdin.readline().strip())
    points = []
    for _ in range(n):
        x, y, is_hull = stdin.readline().strip().split()
        x, y = int(x), int(y)
        if is_hull == 'Y':
            points.append((x, y))
    points.sort()
    # print(points)

    m = len(points)

    diffs = []
    for i in range(m):
        diffs.append((points[i][0] - points[0][0], points[i][1] - points[0][1], i))
    # print(diffs)

    diffs[1:] = sorted(diffs[1:], key=cmp_to_key(compare))
    # print(diffs)

    start = 1
    for i in range(2, m):
        a = diffs[i - 1]
        b = diffs[i]
        if a[0] * b[1] != a[1] * b[0]:
            if start == 1:
                # 1 ~ i-1까지 정렬
                diffs[1:i] = sorted(diffs[1:i], key=cmp_to_key(compare_x))
            start = i
    diffs[start:] = sorted(diffs[start:], key=cmp_to_key(compare_x_reverse))

    print(m)
    for x, y, idx in diffs:
        print(points[idx][0], points[idx][1], flush=False)


if __name__ == "__main__":
    solve()
