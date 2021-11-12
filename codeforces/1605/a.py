from sys import stdin


def read_input():
    a1, a2, a3 = map(int, stdin.readline().split())     # read two integers of a line.
    return a1, a2, a3


def solve(a1, a2, a3):
    if abs(a1 + a3 - 2 * a2) % 3 == 0:
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
