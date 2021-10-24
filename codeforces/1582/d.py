from sys import stdin


def gcd(n,m):
    while m:
        n, m = m, n % m
    return n


def read_input():
    n = int(stdin.readline().rstrip())
    a = list(map(int, stdin.readline().split()))
    return n, a


def solve(n, a):
    b = [0] * n

    for i in range(0, n-1, 2):
        g = gcd(abs(a[i+1]), abs(a[i]))
        b[i] = a[i+1] // g
        b[i+1] = -a[i] // g

    if n % 2 == 1:
        g = gcd(abs(a[-1]), abs(a[-2]))
        if a[-1] * b[-2] > 0:
            b[-2] += a[-1] // g
            b[-1] = -a[-2] // g
        else:
            b[-2] -= a[-1] // g
            b[-1] = a[-2] // g

    return ' '.join(map(str, b))


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
