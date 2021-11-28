from sys import stdin


def read_input():
    n = int(stdin.readline())                     # read an integer.
    a = list(map(int, stdin.readline().split()))  # read several integers of a line.
    return n, a


def solve(n, a):
    cnt = 0
    for i in range(n):
        while a[i] >= 2:
            if a[i] % 2 == 0:
                cnt += 1
                a[i] //= 2
            else:
                break

    argmax = 0
    for i, ai in enumerate(a[1:], 1):
        if ai > a[argmax]:
            argmax = i

    a[argmax] *= 2 ** cnt

    return sum(a)


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
