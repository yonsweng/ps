from sys import stdin


def read_input():
    a = stdin.readline()                          # read (a line + '\n') as an str.
    b = int(stdin.readline())                     # read an integer.
    c, d = map(int, stdin.readline().split())     # read two integers of a line.
    e = list(map(int, stdin.readline().split()))  # read several integers of a line.
    return a, b, c, d, e


def solve(a, b, c, d, e):
    answer = 0
    return answer


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
