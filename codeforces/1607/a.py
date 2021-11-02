from sys import stdin


def read_input():
    k = stdin.readline().rstrip()
    s = stdin.readline().rstrip()
    return k, s


def solve(k, s):
    answer = 0

    d = {}
    for i, key in enumerate(k):
        d[key] = i

    for i in range(len(s) - 1):
        answer += abs(d[s[i]] - d[s[i+1]])

    return answer


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
