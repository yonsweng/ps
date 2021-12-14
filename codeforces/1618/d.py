from sys import stdin
from math import gcd


def read_input():
    n, k = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    return n, k, a


def solve(n, k, a):
    a.sort(reverse=True)
    answer = 0
    for i in range(k):
        answer += a[i+k] // a[i]
    for ai in a[2*k:]:
        answer += ai
    return answer


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
