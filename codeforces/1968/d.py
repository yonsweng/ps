from sys import stdin


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n, k, pb, ps = map(int, stdin.readline().split())
        p = [0] + list(map(int, stdin.readline().split()))
        a = [0] + list(map(int, stdin.readline().split()))

        kk = k
        k = min(k, n)

        b = [0, pb] + [0] * (k - 1)
        s = [0, ps] + [0] * (k - 1)

        for i in range(2, k + 1):
            b[i] = p[b[i-1]]
            s[i] = p[s[i-1]]

        tb = [0] * (k + 1)
        ts = [0] * (k + 1)
        for i in range(1, k + 1):
            tb[i] = tb[i-1] + a[b[i]]
            ts[i] = ts[i-1] + a[s[i]]

        ans_b, ans_s = 0, 0

        for i in range(1, k + 1):
            ans_b = max(ans_b, tb[i] + a[b[i]] * (kk - i))
            ans_s = max(ans_s, ts[i] + a[s[i]] * (kk - i))

        if ans_b > ans_s:
            print("Bodya", flush=False)
        elif ans_b < ans_s:
            print("Sasha", flush=False)
        else:
            print("Draw", flush=False)


if __name__ == "__main__":
    main()