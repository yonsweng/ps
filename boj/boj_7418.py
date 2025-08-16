from sys import setrecursionlimit, stdin

setrecursionlimit(10**3)

INF = float('inf')


def print_solution(s, state, i, j):
    if i > j:
        return
    if i == j:
        if s[i] in '()':
            print('()', end='')
        else:
            print('[]', end='')
        return
    k = state[i][j]
    if k == 0:
        print(s[i], end='')
        print_solution(s, state, i + 1, j - 1)
        print(s[j], end='')
        return
    print_solution(s, state, i, k)
    print_solution(s, state, k + 1, j)


def solve():
    s = ' ' + stdin.readline().strip()
    
    n = len(s) - 1
    a = [[0] * (n + 1) for _ in range(n + 1)]
    state = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        a[i][i] = 2

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            a[i][j] = INF
            if (s[i] == '(' and s[j] == ')') or (s[i] == '[' and s[j] == ']'):
                a[i][j] = a[i + 1][j - 1] + 2
            for k in range(i, j):
                if a[i][j] > a[i][k] + a[k + 1][j]:
                    a[i][j] = a[i][k] + a[k + 1][j]
                    state[i][j] = k

    print_solution(s, state, 1, n)


if __name__ == "__main__":
    solve()
