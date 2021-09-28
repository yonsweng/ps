from sys import stdin


def read_input():
    return stdin.readline().rstrip()  # read (a line + '\n') as an str.


def solve(s):
    a, b, c, = 0, 0, 0
    for d in s:
        if d == 'A':
            a += 1
        elif d == 'B':
            b += 1
        else:
            c += 1

    if a + c == b:
        return 'YES'
    else:
        return 'NO'


def main():
    t = int(stdin.readline())

    for _ in range(t):
        s = read_input()
        answer = solve(s)
        print(answer)


if __name__ == '__main__':
    main()
