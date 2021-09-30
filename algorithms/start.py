from sys import stdin


def read_input():
    a = stdin.readline()                          # read (a line + '\n') as an str.
    b = int(stdin.readline())                     # read an integer.
    c, d = stdin.readline().split()               # read words of a line.
    e, f = map(int, stdin.readline().split())     # read two integers of a line.
    g = list(map(int, stdin.readline().split()))  # read several integers of a line.
    return a, b, c, d, e, f, g


def solve(a, b, c, d, e, f, g):
    answer = 0
    return answer


def main():
    input = read_input()
    answer = solve(*input)
    print(answer)


if __name__ == '__main__':
    main()
