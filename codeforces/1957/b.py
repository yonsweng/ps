from sys import stdin


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n, k = map(int, stdin.readline().split())

        if n == 1:
            print(k, flush=False)
            continue

        q = 1
        while q <= k:
            q *= 2
        q //= 2

        if 2 * q - 1 == k:
            print(' '.join(map(str, [k] + [0] * (n - 1))), flush=False)
            continue

        print(' '.join(map(str, [q - 1, k - (q - 1)] + [0] * (n - 2))), flush=False)


if __name__ == "__main__":
    main()
