from sys import stdin


def read_input():
    n, l, r, k = map(int, stdin.readline().split())     # read two integers of a line.
    a = list(map(int, stdin.readline().split()))  # read several integers of a line.
    return n, l, r, k, a


def solve(n, l, r, k, a):
    answer = 0
    accu = 0

    a.sort()
    for ai in a:
        if l <= ai <= r and accu + ai <= k:
            answer += 1
            accu += ai

    return answer


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
