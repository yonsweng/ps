from sys import stdin
import bisect


def read_input():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    return n, a


def reverse_insort(a, x, lo=0, hi=None):
    """Insert item x in list a, and keep it reverse-sorted assuming a
    is reverse-sorted.

    If x is already in a, insert it to the right of the rightmost x.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x > a[mid]: hi = mid
        else: lo = mid+1
    return lo - 1


def solve(n, a):
    answer = []

    if n == 2:
        for _ in range(min(a)):
            answer.append((1, 2))
        return answer

    a = sorted([[ai, i] for i, ai in enumerate(a, 1)], reverse=True)

    while a[1][0] != 0:
        j = reverse_insort(a, [a[1][0], 0], lo=1)
        i = reverse_insort(a, [a[0][0], 0], hi=j)
        answer.append((a[i][1], a[j][1]))
        a[i][0] -= 1
        a[j][0] -= 1

    return answer


def main():
    t = int(stdin.readline())

    for _ in range(t):
        n, a = read_input()
        answer = solve(n, a)

        print(len(answer))
        for i, j in answer:
            print(i, j)


if __name__ == '__main__':
    main()
