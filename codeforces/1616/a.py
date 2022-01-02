from sys import stdin


def read_input():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    return n, a


def solve(n, a):
    answer = 0
    h = {}
    for ai in a:
        h[abs(ai)] = h.get(abs(ai), 0) + 1
    for ai, cnt in h.items():
        if ai == 0:
            answer += 1
        else:
            if cnt == 1:
                answer += 1
            else:
                answer += 2
    return answer


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
