from sys import stdin


def read_input():
    a, b, c = map(int, stdin.readline().split())
    return a, b, c


def solve(a, b, c):
    a_prime = 2 * b - c
    if a_prime > 0 and a_prime % a == 0:
        return 'YES'

    if (a + c) % 2 == 0:
        b_prime = (a + c) // 2
        if b_prime > 0 and b_prime % b == 0:
            return 'YES'

    c_prime = 2 * b - a
    if c_prime > 0 and c_prime % c == 0:
        return 'YES'

    return 'NO'


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
