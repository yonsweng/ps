from sys import stdin


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        b = stdin.readline().strip()

        r = list(sorted(set(b)))
        idx = {v: i for i, v in enumerate(r)}
        s = "".join(r[len(r) - 1 - idx[v]] for v in b)
        print(s, flush=False)


if __name__ == "__main__":
    main()
