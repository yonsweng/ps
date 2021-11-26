from sys import stdin


def read_input():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    return n, a


def solve(n, a):
    d = {1: (0, 0)}
    a.sort()
    for ai in a:
        max_s = 0
        max_c = 0
        for k, (s, c) in d.items():
            if ai % k == 0:
                if max_s < s or (max_s == s and max_c < c):
                    max_s = s
                    max_c = c
        d[ai] = (max_s + ai, max_c + 1)

    max_s = 0
    max_c = 0
    for k, (s, c) in d.items():
        if max_s < s or (max_s == s and max_c > c):
            max_s = s
            max_c = c

    return max_s + (n - max_c)


def main():
    for _ in range(1):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
