from sys import stdin


def main():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))

    c = [0] * 29
    for bi in b:
        p = 0
        while bi > 0:
            c[p] += bi % 2
            bi //= 2
            p += 1

    ans1 = 0
    for ai in a:
        pp = 1
        for i in range(29):
            ans1 = (ans1 + pp * (ai % 2) * c[i]) % 1999
            ai //= 2
            pp = pp * 2 % 1999

    ans2 = 2**29 - 1

    a_min = [[-1, -1] for _ in range(29)]
    a_max = [[-1, -1] for _ in range(29)]
    b_min = [[-1, -1] for _ in range(29)]
    b_max = [[-1, -1] for _ in range(29)]

    for k in range(29):
        mask = 2 ** (k + 1) - 1
        for ai in a:
            ai = ai & mask
            if ai & (2**k) == 0:
                if a_min[k][0] == -1:
                    a_min[k][0] = ai
                else:
                    a_min[k][0] = min(a_min[k][0], ai)
                if a_max[k][0] == -1:
                    a_max[k][0] = ai
                else:
                    a_max[k][0] = max(a_max[k][0], ai)
            else:
                if a_min[k][1] == -1:
                    a_min[k][1] = ai
                else:
                    a_min[k][1] = min(a_min[k][1], ai)
                if a_max[k][1] == -1:
                    a_max[k][1] = ai
                else:
                    a_max[k][1] = max(a_max[k][1], ai)
        for bi in b:
            bi = bi & mask
            if bi & (2**k) == 0:
                if b_min[k][0] == -1:
                    b_min[k][0] = bi
                else:
                    b_min[k][0] = min(b_min[k][0], bi)
                if b_max[k][0] == -1:
                    b_max[k][0] = bi
                else:
                    b_max[k][0] = max(b_max[k][0], bi)
            else:
                if b_min[k][1] == -1:
                    b_min[k][1] = bi
                else:
                    b_min[k][1] = min(b_min[k][1], bi)
                if b_max[k][1] == -1:
                    b_max[k][1] = bi
                else:
                    b_max[k][1] = max(b_max[k][1], bi)

    ans2 = 0
    for k in range(29):
        mask = 1 << k
        if a_min[k][0] != -1 and b_min[k][0] != -1:
            mask &= a_min[k][0] + b_min[k][0]
        if a_min[k][1] != -1 and b_min[k][1] != -1:
            mask &= a_min[k][1] + b_min[k][1]
        if a_max[k][0] != -1 and b_max[k][1] != -1:
            mask &= a_max[k][0] + b_max[k][1]
        if a_max[k][1] != -1 and b_max[k][0] != -1:
            mask &= a_max[k][1] + b_max[k][0]
        ans2 |= mask

    print(ans1, ans2)


if __name__ == "__main__":
    main()
