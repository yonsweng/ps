from sys import stdin
from math import gcd


def read_input():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    return n, a


def solve(n, a):
    b = [False] * (10 ** 6 + 1)
    for ai in a:
        b[ai] = True

    l, r = 10 ** 6 - 1, 10 ** 6
    while l > 1:
        while l > 2 and not b[l]:
            l -= 1
        while r > l + 1 and not b[r]:
            r -= 1
        if b[l] and b[r]:
            b[gcd(l, r)] = True
        l -= 1
        r -= 1

    return sum(b) - n


def main():
    for _ in range(1):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
