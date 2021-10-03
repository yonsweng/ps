from sys import stdin


def read_input():
    n, x = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    return n, x, a


def solve(n, x, a):
    b = a[:]
    b.sort()

    for i in range(n-x, x):
        if a[i] != b[i]:
            return 'NO'

    return 'YES'


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
