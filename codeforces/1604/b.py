from sys import stdin


def read_input():
    n = int(stdin.readline())                     # read an integer.
    a = list(map(int, stdin.readline().split()))  # read several integers of a line.
    return n, a


def is_all_increasing(a):
    prev = a[0]

    for ai in a[1:]:
        if ai <= prev:
            return False
        prev = ai

    return True


def solve(n, a):
    if n % 2 == 0:
        answer = 'YES'
    else:
        if is_all_increasing(a):
            answer = 'NO'
        else:
            answer = 'YES'

    return answer


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
