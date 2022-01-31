from sys import stdin
from math import ceil


def main():
    t = int(stdin.readline())
    for _ in range(t):
        hc, dc = map(int, stdin.readline().split())
        hm, dm = map(int, stdin.readline().split())
        k, w, a = map(int, stdin.readline().split())

        yes = False
        for kw in range(k+1):
            ka = k - kw

            tc = ceil((hc + ka * a) / dm)
            tm = ceil(hm / (dc + kw * w))

            if tc >= tm:
                yes = True
                break

        if yes:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
