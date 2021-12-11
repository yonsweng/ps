from sys import stdin


def read_input():
    n, a, b = map(int, stdin.readline().split())     # read two integers of a line.
    return n, a, b


def solve(n, a, b):
    if a < b:
        top = b + 1
        bot = b

        bots = [i for i in range(1, bot + 1)]
        tops = [i for i in range(bot + 1, bot + top + 1)]

        answer = []
        for i in range(n):
            if i % 2 == 0:
                if i // 2 < len(tops):
                    answer.append(tops[i // 2])
                else:
                    answer.append(i + 1)
            else:
                if i // 2 < len(bots):
                    answer.append(bots[i // 2])
                else:
                    answer.append(i + 1)
    elif a > b:
        top = a
        bot = a + 1

        bots = [i for i in range(n - top, n - top - bot, -1)]
        tops = [i for i in range(n, n - top, -1)]

        answer = []
        for i in range(n):
            if i % 2 == 0:
                if i // 2 < len(bots):
                    answer.append(bots[i // 2])
                else:
                    answer.append(n - i)
            else:
                if i // 2 < len(tops):
                    answer.append(tops[i // 2])
                else:
                    answer.append(n - i)
    else:
        top = a + 1
        bot = a + 1

        bots = [i for i in range(1, bot + 1)]
        tops = [i for i in range(bot + 1, bot + top + 1)]

        answer = []
        for i in range(n):
            if i % 2 == 0:
                if i // 2 < len(bots):
                    answer.append(bots[i // 2])
                else:
                    answer.append(i + 1)
            else:
                if i // 2 < len(tops):
                    answer.append(tops[i // 2])
                else:
                    answer.append(i + 1)

    if top + bot > n or abs(a - b) > 1:
        return -1

    return ' '.join(map(str, answer))


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
