from sys import stdin


def read_input():
    n = int(stdin.readline())                     # read an integer.
    a = list(map(int, stdin.readline().split()))  # read several integers of a line.
    return n, a


def solve(n, a):
    for i, ai in enumerate(a, 1):
        indivisible = False
        for d in range(2, min(i+2, 30)):
            if ai % d != 0:
                indivisible = True
                break
        if not indivisible:
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
