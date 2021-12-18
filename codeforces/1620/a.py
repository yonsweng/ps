from sys import stdin


def read_input():
    a = stdin.readline().rstrip()
    return a,


def solve(a):
    answer = 'YES' if a.count('N') != 1 else 'NO'
    return answer


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
