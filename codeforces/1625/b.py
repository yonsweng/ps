from sys import stdin


def read_input():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    return n, a


def solve(n, a):
    answer = -1

    c = {}
    for i, ai in enumerate(a):
        if ai in c:
            answer = max(answer, n - (i - c[ai]))
        c[ai] = i

    return answer


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
