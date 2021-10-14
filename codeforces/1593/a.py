from sys import stdin


def read_input():
    a, b, c = map(int, stdin.readline().split())     # read two integers of a line.
    return a, b, c


def solve(a, b, c):
    if a == b and b == c:
        return '1 1 1'
    m = max(max(a, b), c)
    if a == b and b == m:
        a = 1
        b = 1
        c = m - c + 1
    elif a == c and c == m:
        a = 1
        c = 1
        b = m - b + 1
    elif b == c and c == m:
        b = 1
        c = 1
        a = m - a + 1
    else:
        a = m - a + 1 if m != a else 0
        b = m - b + 1 if m != b else 0
        c = m - c + 1 if m != c else 0
    return ' '.join((str(a), str(b), str(c)))


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
