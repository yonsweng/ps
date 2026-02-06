from sys import stdin


def solve():
    N = int(stdin.readline().strip())
    T, D = [], [1000]
    for _ in range(N):
        cmd, val = stdin.readline().strip().split()
        val = int(val)
        if cmd == "T":
            T.append(val)
        else:
            D.append(val)

    T.sort(reverse=True)
    D.sort(reverse=True)

    t, d, r = 0, 0, 1
    while len(T) > 0 or len(D) > 0:
        if len(T) == 0:
            Ti = float("inf")
        else:
            Ti = T[-1]
        if len(D) == 0:
            Dj = float("inf")
        else:
            Dj = D[-1]

        t1 = Ti - t
        t2 = (Dj - d) * r

        if t1 < t2:
            t = Ti
            d = d + t1 / r
            T.pop()
        else:
            t = t + t2
            d = Dj
            D.pop()
        r = r + 1

    print(int(t + 0.5))


if __name__ == "__main__":
    solve()
