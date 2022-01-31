from sys import stdin


def main():
    t = int(stdin.readline())
    for _ in range(t):
        s = stdin.readline().rstrip()
        zeros = s.count('0')
        ones = s.count('1')
        if zeros == ones:
            print(zeros - 1)
        else:
            print(min(zeros, ones))


if __name__ == '__main__':
    main()
