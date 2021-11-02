from sys import stdin


def read_input():
    n = int(stdin.readline().rstrip())
    a = list(map(int, stdin.readline().split()))
    return n, a


def solve(n, a):
    a.sort()
    acc = 0
    answer = -1000000000000000
    for ai in a:
        curr_min = ai + acc
        answer = max(curr_min, answer)
        acc -= curr_min
    return answer


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
