from sys import stdin
from math import gcd


def read_input():
    n = int(stdin.readline())                     # read an integer.
    a = list(map(int, stdin.readline().split()))  # read several integers of a line.
    return n, a


def solve(n, a):
    if all(ai == 0 for ai in a):
        return ' '.join(map(str, list(range(1, n+1))))

    ones = []
    p, q = 0, 1
    while p < 30:
        cnt = 0
        for ai in a:
            cnt += 1 if ai & q != 0 else 0
        ones.append(cnt)
        p += 1
        q *= 2

    g = ones[0]
    for ones_i in ones[1:]:
        g = gcd(g, ones_i)

    answer = []
    for d in range(1, g+1):
        if g % d == 0:
            answer.append(d)

    return ' '.join(map(str, answer))


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
