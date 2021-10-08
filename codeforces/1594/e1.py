from sys import stdin


def read_input():
    k = int(stdin.readline())
    return (k, )


def solve(k):
    return 6 * pow(4, 2 ** k - 2, 1000000007) % 1000000007


def main():
    # t = int(stdin.readline())

    # for _ in range(t):
    input = read_input()
    answer = solve(*input)
    print(answer)


if __name__ == '__main__':
    main()
