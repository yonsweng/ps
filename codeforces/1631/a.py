from sys import stdin


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        a = list(map(int, stdin.readline().split()))
        b = list(map(int, stdin.readline().split()))
        for i in range(n):
            if a[i] > b[i]:
                a[i], b[i] = b[i], a[i]
        print(max(a) * max(b))


if __name__ == '__main__':
    main()
