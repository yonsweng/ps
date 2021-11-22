from sys import stdin


def read_input():
    x, y = map(int, stdin.readline().split())     # read two integers of a line.
    return x, y


def solve(x, y):
    if (x + y) % 2 == 1:
        return '-1 -1'

    answer = (x + y) // 2
    x = x // 2
    y = answer - x
    return f'{x} {y}'


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
