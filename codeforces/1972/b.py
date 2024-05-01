from sys import stdin


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        s = stdin.readline().strip()

        # count the number of 'U' in s
        u = s.count('U')
        if u % 2 == 0:
            print("NO", flush=False)
        else:
            print("YES", flush=False)


if __name__ == "__main__":
    main()