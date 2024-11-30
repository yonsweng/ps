from sys import stdin
from math import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


def solve():
    t = int(stdin.readline())
    for _ in range(t):
        a, b = map(int, stdin.readline().split())
        m = lcm(a, b)
        print(m)


if __name__ == "__main__":
    solve()
