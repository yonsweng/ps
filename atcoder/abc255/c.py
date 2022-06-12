from sys import stdin


def main():
    x, a, d, n = map(int, stdin.readline().rstrip().split())

    if d == 0:
        print(abs(x - a))
    elif d > 0:
        if x <= a:
            print(a - x)
        elif x >= a + (n - 1) * d:
            print(x - (a + (n - 1) * d))
        else:
            print(min((x - a) % d, d - (x - a) % d))
    else:
        if x >= a:
            print(x - a)
        elif x <= a + (n - 1) * d:
            print(a + (n - 1 ) * d - x)
        else:
            print(min(abs((x - a) % d), abs(d) - abs((x - a) % d)))


if __name__ == '__main__':
    main()
