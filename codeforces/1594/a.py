from sys import stdin


def read_input():
    n = int(stdin.readline())                     # read an integer.
    return (n, )


def solve(n):
    answer = f'{-n + 1} {n}'
    return answer


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
