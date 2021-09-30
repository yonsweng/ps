from sys import stdin


def read_input():
    n, m, k = map(int, stdin.readline().split())     # read two integers of a line.
    return n, m, k


def solve(n, m, k):
    if k == 0 or k == 1:
        return 'NO'
    elif k == 2:
        if n == 1 and m == 0:
            return 'YES'
        else:
            return 'NO'
    elif k == 3:
        if m == n * (n - 1) // 2:
            return 'YES'
        else:
            return 'NO'
    else:
        if m >= n - 1 and m <= n * (n - 1) // 2:
            return 'YES'
        else:
            return 'NO'


def main():
    t = int(stdin.readline())

    for _ in range(t):
        n, m, k = read_input()
        answer = solve(n, m, k)
        print(answer)


if __name__ == '__main__':
    main()
