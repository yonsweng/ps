from sys import stdin


def read_input():
    n, a, b = map(int, stdin.readline().split())
    return n, a, b


def solve(n, a, b):
    l, r = [a], [b]
    c = []

    for i in range(1, n + 1):
        if i == a or i == b:
            continue
        if i < a and i > b:
            return -1
        if i < a:
            r.append(i)
        elif i > b:
            l.append(i)
        else:
            c.append(i)

    if len(l) > n // 2 or len(r) > n // 2:
        return -1

    return ' '.join(map(str, l)) + ' ' + ' '.join(map(str, c)) + (' ' if len(c) > 0 else '') + ' '.join(map(str, r))


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
