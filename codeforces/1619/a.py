from sys import stdin


def read_input():
    s = stdin.readline().rstrip()
    return s,


def solve(s):
    if len(s) % 2 == 1:
        return 'NO'
    for i in range(len(s) // 2):
        if s[i] != s[i + len(s) // 2]:
            return 'NO'
    return 'YES'


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
