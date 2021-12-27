from sys import stdin


def read_input():
    n = int(stdin.readline())
    p = list(map(int, stdin.readline().split()))
    s = stdin.readline().rstrip()
    return n, p, s


def solve(n, p, s):
    sp = [(si, pi, i) for i, (si, pi) in enumerate(zip(s, p))]
    sp.sort()

    q = [0] * n
    for j, (si, pi, i) in enumerate(sp, 1):
        q[i] = j

    return ' '.join(map(str, q))


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
