from sys import stdin
from math import gcd


def read_input():
    n = int(stdin.readline())
    return n,


def solve(n):
    b = 2
    while True:
        a = n - b - 1
        if gcd(a, b) == 1:
            return f'{a} {b} 1'
        b += 1


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
