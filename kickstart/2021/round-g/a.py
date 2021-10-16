from sys import stdin


def read_input():
    N, D, C, M = map(int, stdin.readline().split())     # read two integers of a line.
    S = stdin.readline().rsplit()
    return N, D, C, M, S


def solve(N, D, C, M, S):
    S = list(S[0])
    n_dogs = S.count('D')
    dogs_cnt = 0

    if n_dogs == 0:
        return 'YES'

    for s in S:
        if s == 'D':
            if D == 0:
                return 'NO'

            dogs_cnt += 1
            if dogs_cnt == n_dogs:
                return 'YES'

            D -= 1
            C += M
        else:
            if C == 0:
                return 'NO'

            C -= 1

    return 'YES'


def main():
    t = int(stdin.readline())

    for x in range(1, t + 1):
        input = read_input()
        answer = solve(*input)
        print(f'Case #{x}: {answer}')


if __name__ == '__main__':
    main()
