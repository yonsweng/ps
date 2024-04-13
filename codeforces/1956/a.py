from sys import stdin


def main():
    t = int(stdin.readline())
    for _ in range(t):
        k, q = map(int, stdin.readline().split())
        a = list(map(int, stdin.readline().split()))
        n = list(map(int, stdin.readline().split()))
        for i in range(q):
            print(min(a[0] - 1, n[i]), end=' ')
        print()


if __name__ == '__main__':
    main()
