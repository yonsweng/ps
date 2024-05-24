from sys import stdin


def main():
    n, m = map(int, stdin.readline().split())
    a = [i for i in range(n+1)]
    for _ in range(m):
        i, j = map(int, stdin.readline().split())
        a[i], a[j] = a[j], a[i]
    print(' '.join(map(str, a[1:])))


if __name__ == "__main__":
    main()
