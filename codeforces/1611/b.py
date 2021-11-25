from sys import stdin


def read_input():
    a, b = map(int, stdin.readline().split())
    return a, b


def solve(a, b):
    return min(min(a, b), (a + b) // 4)


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
