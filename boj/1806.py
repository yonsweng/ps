from sys import stdin
from bisect import bisect_left


def read_input():
    N, S = map(int, stdin.readline().split())
    A = list(map(int, stdin.readline().split()))
    return N, S, A


def solve(N, S, A):
    B = [0] * (len(A) + 1)
    B[1] = A[0]
    for i, Ai in enumerate(A[1:], 2):
        B[i] = B[i - 1] + Ai

    # print(B)
    answer = N + 1

    for i in range(1, len(B)):
        j = bisect_left(B, S + B[i - 1], lo=i)
        if j <= N:
            answer = min(answer, j - i + 1)

    if answer == N + 1:
        answer = 0

    return answer


def main():
    input = read_input()
    answer = solve(*input)
    print(answer)


if __name__ == "__main__":
    main()
