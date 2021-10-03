from sys import stdin
import math


def read_input():
    n, H = map(int, stdin.readline().split())     # read two integers of a line.
    a = list(map(int, stdin.readline().split()))
    return n, H, a


def solve(n, H, a):
    a.sort(reverse=True)

    x = a[0]
    y = a[1]

    m = math.ceil(H / (x + y))
    if (m-1) * (x+y) + x >= H:
        return 2 * m - 1
    else:
        return 2 * m


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
