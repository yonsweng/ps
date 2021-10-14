from sys import stdin


def read_input():
    n = stdin.readline().rstrip()
    return (n, )


def solve(n):
    answer = 99
    for i in range(len(n) - 1, 0, -1):
        if n[i] == '0':
            for j in range(i - 1, -1, -1):
                if n[j] == '0' or n[j] == '5':
                    answer = min(answer, (i - j - 1) + (len(n) - i - 1))
        elif n[i] == '5':
            for j in range(i - 1, -1, -1):
                if n[j] == '2' or n[j] == '7':
                    answer = min(answer, (i - j - 1) + (len(n) - i - 1))
    return answer


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
