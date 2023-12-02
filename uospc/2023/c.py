from sys import stdin


def main():
    n, k = map(int, stdin.readline().split())
    s = stdin.readline().rstrip()

    t = s[: k - 1]
    if (n - k + 1) % 2 == 1:
        t = t[::-1]
    ans = s[k - 1 :] + t
    print(ans)


if __name__ == "__main__":
    main()
