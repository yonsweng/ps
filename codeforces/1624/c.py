from sys import stdin


def read_input():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    return n, a


def reduce(a, n):
    while a > n:
        a //= 2
    return a


def solve(n, a):
    cnt = [0] * (n + 1)
    for ai in a:
        ai = reduce(ai, n)
        cnt[ai] += 1

    for i in range(n, 0, -1):
        if cnt[i] == 0:
            return 'NO'
        if cnt[i] > 1:
            cnt[i//2] += cnt[i] - 1
            cnt[i] = 1

    return 'YES'


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
