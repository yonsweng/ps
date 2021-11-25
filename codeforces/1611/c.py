from sys import stdin


def read_input():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    return n, a


def get_position_of_n(a, n):
    for i, ai in enumerate(a):
        if ai == n:
            return i
    return -1


def solve(n, a):
    position_of_n = get_position_of_n(a, n)
    if position_of_n == 0 or position_of_n == n - 1:
        answer = []

        if position_of_n == 0:
            answer.append(n)
            for ai in a[-1:0:-1]:
                answer.append(ai)
        else:
            for ai in a[-2::-1]:
                answer.append(ai)
            answer.append(n)

        return ' '.join(map(str, answer))
    else:
        return -1


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
