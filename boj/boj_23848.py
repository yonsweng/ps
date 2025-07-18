from sys import stdin


def solve():
    N = int(stdin.readline().strip())

    a = 0
    for k in range(3, 40):
        for r in range(2, 1000000):
            b = (r ** k - 1) // (r - 1)
            if b > N:
                break
            if N % b == 0:
                a = N // b
                break
        if a > 0:
            break

    if a == 0:
        print(-1)
        return

    seq = []
    cur = a
    for _ in range(k):
        seq.append(cur)
        cur *= r

    print(k)
    print(*seq)


if __name__ == "__main__":
    solve()
