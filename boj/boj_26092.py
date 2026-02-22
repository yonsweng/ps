from math import sqrt
from sys import stdin


def solve():
    a, b = map(int, stdin.readline().split())

    c, d = 2, 2
    while True:
        if a == 1 or b == 1:
            break

        if a == b:
            break

        if a >= b:
            div = False
            while c <= sqrt(a):
                if a % c == 0:
                    a //= c
                    div = True
                    break
                c += 1
            if not div:
                a = 1
        else:
            div = False
            while d <= sqrt(b):
                if b % d == 0:
                    b //= d
                    div = True
                    break
                d += 1
            if not div:
                b = 1

    print(min(a, b))


if __name__ == "__main__":
    solve()
