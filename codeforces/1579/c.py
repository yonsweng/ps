from sys import stdin


def read_input():
    n, m, k = map(int, stdin.readline().split())
    a = ['.' * (m + 2)]
    for _ in range(1, n + 1):
        a.append('.' + stdin.readline().rstrip() + '.')
    return n, m, k, a


def solve(n, m, k, a):
    check = [[False] * (m + 2) for _ in range(n + 1)]
    for i in range(n, 0, -1):
        for j in range(1, m + 1):
            if a[i][j] == '*':
                d = 0
                while a[i-d-1][j-d-1] == '*' and a[i-d-1][j+d+1] == '*':
                    d += 1
                if d >= k:
                    d = 0
                    check[i][j] = True
                    while a[i-d-1][j-d-1] == '*' and a[i-d-1][j+d+1] == '*':
                        check[i-d-1][j-d-1] = check[i-d-1][j+d+1] = True
                        d += 1

    for i in range(n, 0, -1):
        for j in range(1, m + 1):
            if a[i][j] == '*' and check[i][j] == False:
                return 'NO'

    return 'YES'


def main():
    t = int(stdin.readline())

    for _ in range(t):
        n, m, k, a = read_input()
        answer = solve(n, m, k, a)
        print(answer)


if __name__ == '__main__':
    main()
