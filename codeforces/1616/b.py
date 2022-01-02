from sys import stdin


def read_input():
    n = int(stdin.readline())
    s = stdin.readline().rstrip()
    return n, s


def solve(n, s: str):
    pivot = 1

    for i in range(n - 1):
        if s[i] < s[i + 1]:
            break

        if s[i] == s[i + 1] and s[i] == s[0]:
            break

        pivot += 1

    return s[:pivot] + s[:pivot][::-1]


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
