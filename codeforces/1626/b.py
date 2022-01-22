from sys import stdin


def exists_over_10(x):
    for i in range(len(x) - 2, -1, -1):
        if int(x[i]) + int(x[i + 1]) >= 10:
            return i
    return -1


def main():
    t = int(stdin.readline())
    for _ in range(t):
        x = stdin.readline().rstrip()
        i = exists_over_10(x)
        if i != -1:
            print(x[:i] + str(int(x[i]) + int(x[i + 1])) + x[i + 2:])
        else:
            print(str(int(x[0]) + int(x[1])) + x[2:])


if __name__ == '__main__':
    main()
