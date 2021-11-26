from sys import stdin


def read_input():
    n, m = map(int, stdin.readline().split())     # read two integers of a line.
    return n, m


def solve(n, m):
    all_or = 0
    for _ in range(m):
        l, r, x = map(int, stdin.readline().split())     # read two integers of a line.
        all_or |= x

    pos = 1
    answer = 0
    while pos <= all_or:
        if all_or & pos != 0:
            answer = (pos + answer) % 1000000007
        pos *= 2

    answer = (answer * pow(2, n - 1, 1000000007)) % 1000000007

    return answer


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
