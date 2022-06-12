from sys import stdin


def main():
    r, c = map(int, stdin.readline().rstrip().split())

    a = [[0] * 3 for _ in range(3)]
    a[1][1], a[1][2] = map(int, stdin.readline().rstrip().split())
    a[2][1], a[2][2] = map(int, stdin.readline().rstrip().split())

    print(a[r][c])


if __name__ == '__main__':
    main()
