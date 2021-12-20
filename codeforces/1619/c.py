from sys import stdin


def read_input():
    a, s = map(int, stdin.readline().split())
    return a, s


def pos_num(v, p):
    return v // p % 10


def solve(a, s):
    b = 0

    pa, ps = 1, 1
    while pa <= a or ps <= s:
        if pos_num(a, pa) > pos_num(s, ps):
            if pos_num(s, ps * 10) == 1:
                b += (pos_num(s, ps * 10) * 10 + pos_num(s, ps) - pos_num(a, pa)) * pa
                ps *= 10
            else:
                return -1
        else:
            b += (pos_num(s, ps) - pos_num(a, pa)) * pa
        pa *= 10
        ps *= 10

    return b


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
