from sys import stdin


def read_input():
    n = int(stdin.readline())                     # read an integer.
    a = stdin.readline().rstrip()                          # read (a line + '\n') as an str.
    b = stdin.readline().rstrip()                          # read (a line + '\n') as an str.
    # c, d = stdin.readline().split()               # read words of a line.
    # e, f = map(int, stdin.readline().split())     # read two integers of a line.
    # g = list(map(int, stdin.readline().split()))  # read several integers of a line.
    return n, a, b


def solve(n, a, b):
    for i in range(n):
        if a[i] == '1' and b[i] == '1':
            return 'NO'
    return 'YES'


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
