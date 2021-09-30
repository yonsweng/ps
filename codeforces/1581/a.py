from sys import stdin


def read_input():
    n = int(stdin.readline())                     # read an integer.
    return n


def modFact(n, p):
    if n >= p:
        return 0

    result = 1
    for i in range(1, n + 1):
        if i == 2:
            continue
        result = (result * i) % p

    return result


def solve(n):
    answer = modFact(2*n, 1000000007)
    return answer


def main():
    t = int(stdin.readline())

    for _ in range(t):
        n = read_input()
        answer = solve(n)
        print(answer)


if __name__ == '__main__':
    main()
