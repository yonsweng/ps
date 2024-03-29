from sys import stdin


def read_input():
    n, m = map(int, stdin.readline().split())
    return n, m


def solve(n, m):
    if n == m == 1:
        return 0
    answer = min(2, min(n, m))
    return answer


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
