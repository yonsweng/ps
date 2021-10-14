from sys import stdin
from math import gcd


def read_input():
    n = int(stdin.readline().rstrip())
    a = list(map(int, stdin.readline().rstrip().split()))
    return n, a


def solve(n, a):
    m = min(a)
    d = list(map(lambda ai: ai - m, a))
    d = [di for di in d if di != 0]
    if len(d) == 0:
        return -1
    g = d[0]
    for di in d[1:]:
        g = gcd(g, di)
    return g


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
