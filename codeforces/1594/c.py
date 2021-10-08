from sys import stdin


def read_input():
    n, c = stdin.readline().split()
    n = int(n)
    s = stdin.readline().rstrip()
    return n, c, s


def solve(n, c, s):
    if all(si == c for si in s):
        return []
    for i in range(n, n // 2, -1):
        if s[i-1] == c:
            return [str(i)]
    return [str(n-1), str(n)]


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(len(answer))
        if len(answer):
            print(' '.join(answer))


if __name__ == '__main__':
    main()
