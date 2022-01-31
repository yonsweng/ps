from sys import stdin


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())

        if n % 7 == 0:
            print(n)
        else:
            for m in range(n - n % 10, n - n % 10 + 10):
                if m % 7 == 0:
                    print(m)
                    break


if __name__ == '__main__':
    main()
