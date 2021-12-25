from sys import stdin


def read_input():
    n = int(stdin.readline())
    A = stdin.readline().rstrip()
    B = stdin.readline().rstrip()
    return n, A, B


def solve(n, A, B):
    a, b, c, d = 0, 0, 0, 0
    for Ai, Bi in zip(A, B):
        if Ai == Bi == '0':
            a += 1
        elif Ai == '0' and Bi == '1':
            b += 1
        elif Ai == '1' and Bi == '0':
            c += 1
        else:
            d += 1

    if A == B:
        return 0
    elif c + d == 0:
        return -1
    elif b == c and d - a == 1:
        return min(b + c, a + d)
    elif b == c:
        return b + c
    elif d - a == 1:
        return a + d
    else:
        return -1


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
