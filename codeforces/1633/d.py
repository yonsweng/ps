from sys import stdin


def main():
    ops = [9999] * 1001
    ops[1] = 0
    for i in range(1, 1000):
        for x in range(1, i + 1):
            if i + i // x <= 1000:
                ops[i + i // x] = min(ops[i + i // x], ops[i] + 1)

    t = int(stdin.readline())
    for _ in range(t):
        n, k = map(int, stdin.readline().split())
        b = [0] + list(map(int, stdin.readline().split()))
        c = [0] + list(map(int, stdin.readline().split()))

        items = [
            (ops[bi], ci)
            for bi, ci in zip(b[1:], c[1:])
        ]

        d = {0: 0}
        for wi, ci in items:
            da = {}
            for key, v in d.items():
                if key + wi <= k:
                    da[key + wi] = max(da.get(key + wi, 0), v + ci)
            for key, v in da.items():
                d[key] = max(d.get(key, 0), v)

        print(max(d.values()))


if __name__ == '__main__':
    main()
