from sys import stdin


def main():
    t = int(stdin.readline())
    for _ in range(t):
        l, r, k = map(int, stdin.readline().split())
        if l == r:
            if l == 1:
                print('NO')
            else:
                print('YES')
        elif r % 2 == 1 and l % 2 == 1:
            if r - l + 1 <= 2 * k:
                print('YES')
            else:
                print('NO')
        else:
            if r - l <= 2 * k:
                print('YES')
            else:
                print('NO')


if __name__ == '__main__':
    main()
