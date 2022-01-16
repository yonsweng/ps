from sys import stdin


def read_input():
    n, l = map(int, stdin.readline().split())
    x = list(map(int, stdin.readline().split()))
    return n, l, x


def solve(n, l, x):
    x.sort()
    answer = 0
    p = 1
    while x[-1] != 0:
        cnt = [0, 0]
        for i, xi in enumerate(x):
            cnt[xi % 2] += 1
            x[i] //= 2
        if cnt[0] < cnt[1]:
            answer += p
        p *= 2

    return answer


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
