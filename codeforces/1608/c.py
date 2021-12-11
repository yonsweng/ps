from sys import stdin


def read_input():
    n = int(stdin.readline())                     # read an integer.
    a = list(map(int, stdin.readline().split()))  # read several integers of a line.
    b = list(map(int, stdin.readline().split()))  # read several integers of a line.
    return n, a, b


def solve(n, a, b):
    answer = [1] * n

    ab = [(ai, bi, i) for i, (ai, bi) in enumerate(zip(a, b))]

    ab.sort(reverse=True)

    min_b = ab[0][1]
    for ai, bi, i in ab:
        if bi < min_b:
            answer[i] = 0
            min_b = bi
    good = False
    for ai, bi, i in ab[::-1]:
        if answer[i] == 1:
            good = True
        if good:
            answer[i] = 1

    return ''.join(map(str, answer))


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
