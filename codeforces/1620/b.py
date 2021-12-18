from sys import stdin


def read_input():
    answer = 0
    w, h = map(int, stdin.readline().split())     # read two integers of a line.
    for _ in range(2):
        x = list(map(int, stdin.readline().split()))
        answer = max(answer, h * (x[-1] - x[1]))
    for _ in range(2):
        x = list(map(int, stdin.readline().split()))
        answer = max(answer, w * (x[-1] - x[1]))
    print(answer)


def solve(a, b, c, d, e):
    answer = 0
    return answer


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        # answer = solve(*input)
        # print(answer)


if __name__ == '__main__':
    main()
