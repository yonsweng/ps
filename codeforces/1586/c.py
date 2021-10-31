from sys import stdin

def read_input():
    n, m = map(int, stdin.readline().split())

    a = ['.' * (m + 1)]
    for _ in range(n):
        ai = '.' + stdin.readline().rstrip()
        a.append(ai)

    return n, m, a


def solve(n, m, a):
    s = [0] * (m + 1)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i-1][j] == 'X' and a[i][j-1] == 'X':
                s[j] += 1

    for j in range(2, m + 1):
        s[j] += s[j-1]

    q = int(stdin.readline())

    for _ in range(q):
        u, v = map(int, stdin.readline().split())
        answer = 'YES' if s[v] - s[u] == 0 else 'NO'
        print(answer)


def main():
    input = read_input()
    solve(*input)


if __name__ == '__main__':
    main()
