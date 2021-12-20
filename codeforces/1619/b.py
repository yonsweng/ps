from sys import stdin
from math import sqrt, floor


def read_input():
    n = int(stdin.readline())
    return n,


def calc_cube_root(n):
    b = 1
    while b ** 3 <= n:
        b += 1
    return b - 1


def calc_hexa_root(n):
    b = 1
    while b ** 6 <= n:
        b += 1
    return b - 1


def solve(n):
    square_root = floor(sqrt(n))
    cube_root = calc_cube_root(n)
    hexa_root = calc_hexa_root(n)
    answer = square_root + cube_root - hexa_root
    return answer


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
