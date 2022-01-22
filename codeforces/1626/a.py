from sys import stdin


def main():
    t = int(stdin.readline())
    for _ in range(t):
        s = stdin.readline().rstrip()
        cnt = {}
        for si in s:
            cnt[si] = cnt.get(si, 0) + 1
        for si, c in cnt.items():
            print(si * c, end='')
        print()


if __name__ == '__main__':
    main()
