from sys import stdin


def main():
    n = int(stdin.readline())

    # n combination 5
    ans = n * (n - 1) * (n - 2) * (n - 3) * (n - 4) // (5 * 4 * 3 * 2 * 1)
    print(ans)


if __name__ == "__main__":
    main()
