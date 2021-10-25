from sys import stdin


def read_input():
    s = stdin.readline().rstrip()
    return (s, )


def solve(s):
    answer = 0

    answer = min(map(ord, s))
    a = chr(answer)

    flag = False
    b = []
    for si in s:
        if flag or si != a:
            b.append(si)
        elif si == a:
            flag = True

    return a + ' ' + ''.join(b)


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
