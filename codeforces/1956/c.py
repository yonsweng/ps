from sys import stdin


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())

        s = 0
        for i in range(1, n + 1):
            s += i * (i * 2 - 1)

        m = 2 * n

        print(s, m, flush=False)

        for i in range(n, 0, -1):
            print(f"1 {i} {' '.join(map(str, range(1, n + 1)))}", flush=False)
            print(f"2 {i} {' '.join(map(str, range(1, n + 1)))}", flush=False)


if __name__ == '__main__':
    main()
