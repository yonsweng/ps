from sys import stdin
from bisect import bisect_left


def read_input():
    N, K = map(int, stdin.readline().split())
    B = [0] + list(map(int, stdin.readline().split()))
    return N, K, B


def solve(N, K, B):
    S = [0] * (N + 1)
    for i in range(1, N + 1):
        S[i] = S[i - 1] + B[i]

    answer = N + 1

    for i in range(1, N + 1):
        for j in range(i, N + 1):
            section1 = S[j] - S[i - 1]

            if section1 == K:
                answer = min(answer, j - i + 1)
                continue

            for k in range(j + 2, N + 1):
                x = K - section1 + S[k - 1]
                l = bisect_left(S, x, lo=k)
                if l <= N and S[l] == x:
                    answer = min(answer, (j - i + 1) + (l - k + 1))

    if answer == N + 1:
        return -1
    else:
        return answer


def main():
    t = int(stdin.readline())

    for x in range(1, t + 1):
        input = read_input()
        answer = solve(*input)
        print(f'Case #{x}: {answer}')


if __name__ == '__main__':
    main()
