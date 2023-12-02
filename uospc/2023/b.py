from sys import stdin


def main():
    n = int(stdin.readline())
    a = stdin.readline().rstrip()

    u, o, s, p, c = 0, 0, 0, 0, 0
    for i in range(n):
        if a[i] == "u":
            u += 1
        elif a[i] == "o":
            o += 1
        elif a[i] == "s":
            s += 1
        elif a[i] == "p":
            p += 1
        elif a[i] == "c":
            c += 1

    ans = min(u, o, s, p, c)
    print(ans)


if __name__ == "__main__":
    main()
