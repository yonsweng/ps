from sys import stdin


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n, m = map(int, stdin.readline().split())
        a = stdin.readline().strip()
        b = stdin.readline().strip()

        i, j = 0, 0
        while i < n and j < m:
            if a[i] == b[j]:
                i += 1
            j += 1

        print(i, flush=False)


if __name__ == "__main__":
    main()