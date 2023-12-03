from sys import stdin
from bisect import bisect_left


def main():
    n = stdin.readline().rstrip()
    p = [[] for _ in range(10)]
    for i, ni in enumerate(n):
        p[int(ni)].append(i)

    fail = False
    for i in range(1, 10**8):
        k = 0
        for j in str(i):
            j = int(j)
            r = bisect_left(p[j], k)
            if r < len(p[j]):
                k = p[j][r] + 1
            else:
                fail = True
                break
        if fail:
            break
    print(i)


if __name__ == "__main__":
    main()
