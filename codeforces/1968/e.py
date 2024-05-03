from sys import stdin


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())

        for i in range(1, n-1):
            print(i, i, flush=False)
        print(n-1, n, flush=False)
        print(n, n, flush=False)


if __name__ == "__main__":
    main()
