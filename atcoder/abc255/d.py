from sys import stdin
from bisect import bisect_left, bisect_right


def main():
    n, q = map(int, stdin.readline().rstrip().split())
    a = [0] + list(map(int, stdin.readline().rstrip().split()))

    a.sort()
    a.append(1000000001)

    s = [0] * (n + 1)
    t = [0] * (n + 2)
    for i in range(1, n + 1):
        s[i] = s[i-1] + (a[i] - a[i-1]) * (i - 1)
    for i in range(n - 1, 0, -1):
        t[i] = t[i+1] + (a[i+1] - a[i]) * (n - i)

    # print('a:', a)
    # print('s:', s)
    # print('t:', t)

    # print(bisect_right(a, 2))
    # print(bisect_right(a, 5))
    # print(bisect_right(a, 8))
    # print(bisect_right(a, 11))
    # print(bisect_right(a, 12))

    for _ in range(q):
        x = int(stdin.readline().rstrip())
        m = bisect_right(a, x) - 1

        # print(m)
        left = s[m] + m * (x - a[m])
        right = t[m+1] + (n - m) * (a[m+1] - x)
        # print(left, right)
        print(left + right)


if __name__ == '__main__':
    main()
