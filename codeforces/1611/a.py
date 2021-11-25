from sys import stdin


def read_input():
    n = int(stdin.readline())                     # read an integer.
    return n,


def all_odd(n):
    for ni in n:
        if (ord(ni) - ord('0')) % 2 == 0:
            return False
    return True


def solve(n):
    n = str(n)
    if all_odd(n):
        return -1
    elif (ord(n[-1]) - ord('0')) % 2 == 0:
        return 0
    elif (ord(n[0]) - ord('0')) % 2 == 0:
        return 1
    else:
        return 2


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
