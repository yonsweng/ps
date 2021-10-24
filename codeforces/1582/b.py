from sys import stdin


def read_input():
    n = map(int, stdin.readline().split())     # read two integers of a line.
    a = list(map(int, stdin.readline().split()))
    return n, a


def solve(n, a):
    zero, one = 0, 0
    for ai in a:
        if ai == 0:
            zero += 1
        elif ai == 1:
            one += 1

    return one * (2 ** zero)


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
