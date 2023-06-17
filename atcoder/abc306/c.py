from sys import stdin


def solve():
    n = int(stdin.readline().rstrip())
    a = list(map(int, stdin.readline().rstrip().split()))
    m = {}
    f = {}
    for i, ai in enumerate(a, 1):
        if ai in m:
            m[ai] += 1
        else:
            m[ai] = 1
        if m[ai] == 2:
            f[ai] = i

    l = []
    for k, v in f.items():
        l.append((v, k))

    l.sort()
    answer = []
    for _, k in l:
        answer.append(k)

    print(" ".join(map(str, answer)))


if __name__ == "__main__":
    solve()
