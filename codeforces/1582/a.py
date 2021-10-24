from sys import stdin


def read_input():
    a, b, c = map(int, stdin.readline().split())     # read two integers of a line.
    return a, b, c


def solve(a, b, c):
    if c % 2 == 0:
        if (a + 2 * b) % 2 == 1:
            answer = 1
        elif a == 0 and b == 1:
            answer = 2
        else:
            answer = 0
    else:
        if a == 0 and b == 0:
            answer = 3
        elif a == 1 and b == 0:
            answer = 2
        elif (a + 2 * b) % 2 == 1:
            answer = 0
        else:
            answer = 1

    return answer


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
