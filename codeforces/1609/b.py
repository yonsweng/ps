from sys import stdin


def read_input():
    n, q = map(int, stdin.readline().split())
    s = stdin.readline().rstrip()
    return n, q, s


def solve(n, q, s):
    cnt = s.count('abc')
    s = list(s)

    for _ in range(q):
        i, c = stdin.readline().rstrip().split()
        i = int(i) - 1

        if s[i] == 'a' and c != 'a' and i + 2 < n and s[i+1] == 'b' and s[i+2] == 'c':
            cnt -= 1
        if s[i] == 'b' and c != 'b' and i - 1 >= 0 and i + 1 < n and s[i-1] == 'a' and s[i+1] == 'c':
            cnt -= 1
        if s[i] == 'c' and c != 'c' and i - 2 >= 0 and s[i-2] == 'a' and s[i-1] == 'b':
            cnt -= 1
        if s[i] != 'a' and c == 'a' and i + 2 < n and s[i+1] == 'b' and s[i+2] == 'c':
            cnt += 1
        if s[i] != 'b' and c == 'b' and i - 1 >= 0 and i + 1 < n and s[i-1] == 'a' and s[i+1] == 'c':
            cnt += 1
        if s[i] != 'c' and c == 'c' and i - 2 >= 0 and s[i-2] == 'a' and s[i-1] == 'b':
            cnt += 1

        s[i] = c
        print(cnt)


def main():
    # t = int(stdin.readline())
    for _ in range(1):
        input = read_input()
        solve(*input)
        # print(answer)


if __name__ == '__main__':
    main()
