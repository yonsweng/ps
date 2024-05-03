from sys import stdin


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        x = [0, 0] + list(map(int, stdin.readline().split()))

        a = [0] * (n + 1)
        a[1] = x[2] + 1
        a[2] = x[2]

        for i in range(3, n + 1):
            if x[i] < a[i-1]:
                a[i] = x[i]
            else:
                a[i-1] += a[i-2] * ((x[i] - a[i-1]) // a[i-2] + 1)
                a[i] = x[i]

        print(' '.join(map(str, a[1:])), flush=False)


if __name__ == "__main__":
    main()