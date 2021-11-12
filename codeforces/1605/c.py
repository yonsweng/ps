from sys import stdin


def read_input():
    n = int(stdin.readline().rstrip())
    s = stdin.readline().rstrip()
    return n, s


def solve(n, s):
    INF = 9999999
    answer = INF
    cnt = {}

    for c in s:
        cnt[c] = cnt.get(c, 0) + 1
        na = cnt.get('a', 0)
        nb = cnt.get('b', 0)
        nc = cnt.get('c', 0)
        if na < nb or na < nc:
            cnt = {}
        elif na > nb and na > nc and na >= 2:
            answer = min(answer, na + nb + nc)
            cnt = {'a': 1}

    if answer == INF:
        if s.find('abbacca') != -1 or s.find('accabba') != -1:
            return 7

    return answer if answer != INF else -1


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
