from sys import stdin


def read_input():
    x, y = map(int, stdin.readline().split())
    return x, y


def solve(x, y):
    if x == y:
        n = x
    elif x < y:
        if y < 3 * x:
            n = (x + y) // 2
        else:
            n = y - (y % x) // 2
    else:
        n = x + y

    assert(n % x == y % n)
    return n


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
