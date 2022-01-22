from sys import stdin


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n, k = map(int, stdin.readline().split())
        a = list(map(int, stdin.readline().split()))
        b = list(map(int, stdin.readline().split()))
        ab = [(ai, bi) for ai, bi in zip(a, b)]
        ab.sort()
        for ai, bi in ab:
            if ai <= k:
                k += bi
        print(k)


if __name__ == '__main__':
    main()
