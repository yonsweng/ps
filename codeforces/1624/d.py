from sys import stdin


def read_input():
    n, k = map(int, stdin.readline().split())
    s = stdin.readline().rstrip()
    return n, k, s


def solve(n, k, s):
    cnt = {}
    for si in s:
        cnt[si] = cnt.get(si, 0) + 1

    mok, r = 0, 0
    for si, v in cnt.items():
        mok += v // 2
        r += v % 2

    answer = 2 * (mok // k)
    r += 2 * (mok % k)
    answer += bool(r >= k)

    return answer


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
