from sys import stdin


def read_input():
    n = int(stdin.readline())     # read two integers of a line.
    a = list(map(int, stdin.readline().split()))  # read several integers of a line.
    return n, a


def solve(n, a):
    answer = 0
    x = [0] * (n+1)
    b = [(ai, i) for i, ai in enumerate(a, 1)]
    b.sort(reverse=True)

    j = -1
    for ai, i in b:
        answer += abs(j) * ai * 2

        x[i] = j
        j = -j if j < 0 else -j - 1

    return str(answer) + '\n' + ' '.join(map(str, x))


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
