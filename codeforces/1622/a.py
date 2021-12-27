from sys import stdin


def read_input():
    a, b, c = map(int, stdin.readline().split())
    return a, b, c


def solve(a, b, c):
    if a == b + c or b == a + c or c == a + b:
        return 'YES'
    elif (a == b and c % 2 == 0) or (b == c and a % 2 == 0) or (c == a and b % 2 == 0):
        return 'YES'
    else:
        return 'NO'


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
