from sys import stdin
from collections import deque


def read_input():
    n = int(stdin.readline())
    p = list(map(int, stdin.readline().split()))
    return n, p


def solve(n, p):
    answer = deque()

    for pi in p:
        if len(answer) == 0 or pi < answer[0]:
            answer.appendleft(pi)
        else:
            answer.append(pi)

    return ' '.join(map(str, answer))


def main():
    t = int(stdin.readline())

    for _ in range(t):
        n, p = read_input()
        answer = solve(n, p)
        print(answer)


if __name__ == '__main__':
    main()
