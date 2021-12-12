from sys import stdin


def read_input():
    n = int(stdin.readline())                     # read an integer.
    a = list(map(int, stdin.readline().split()))  # read several integers of a line.
    return n, a


def solve(n, a):
    answer = 1
    prev = -1
    for ai in a:
        if ai == 0:
            if prev == 0:
                return -1
        else:
            if prev != 1:
                answer += 1
            else:
                answer += 5
        prev = ai
    return answer


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
