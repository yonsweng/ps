from sys import stdin
from math import gcd


def read_input():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    return n, a


def solve(n, a):
    gcd_even = a[0]
    for ai in a[2:n:2]:
        gcd_even = gcd(gcd_even, ai)
    gcd_odd = a[1]
    for ai in a[3:n:2]:
        gcd_odd = gcd(gcd_odd, ai)
    if gcd_even == gcd_odd:
        return 0
    good = True
    for ai in a[0:n:2]:
        if ai % gcd_odd == 0:
            good = False
            break
    if good:
        return gcd_odd
    for ai in a[1:n:2]:
        if ai % gcd_even == 0:
            return 0
    return gcd_even


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
