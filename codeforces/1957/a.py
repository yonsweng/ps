from sys import stdin


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        a = list(map(int, stdin.readline().split()))

        cnt = {}
        for ai in a:
            cnt[ai] = cnt.get(ai, 0) + 1

        ans = 0
        for c in cnt.values():
            ans += c // 3

        print(ans)


if __name__ == "__main__":
    main()
