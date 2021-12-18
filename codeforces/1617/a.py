from sys import stdin
from string import ascii_lowercase


def read_input():
    S = stdin.readline().rstrip()
    T = stdin.readline().rstrip()
    return S, T


def solve(S, T):
    answer = 0

    if T == 'abc':
        others = []
        for alphabet in ascii_lowercase:
            if alphabet != 'a' and alphabet != 'b' and alphabet != 'c':
                others.append(alphabet * S.count(alphabet))
        others = ''.join(others)
        if S.count('a') > 0:
            answer = S.count('a') * 'a' + S.count('c') * 'c' + S.count('b') * 'b' + others
        else:
            answer = S.count('b') * 'b' + S.count('c') * 'c' + others
    else:
        answer = [S.count(alphabet) * alphabet for alphabet in ascii_lowercase]
        answer = ''.join(answer)

    return answer


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
