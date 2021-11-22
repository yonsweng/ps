from sys import stdin


def read_input():
    a, b, x = map(int, stdin.readline().split())
    return a, b, x


def solve(a, b, x):
    if a == x or b == x:
        return 'YES'

    while (a >= x or b >= x) and a > 0 and b > 0:
        if a > b:
            if a % b == x % b:
                return 'YES'
            a = a % b
        else:
            if b % a == x % a:
                return 'YES'
            b = b % a

    return 'NO'


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
