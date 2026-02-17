from sys import stdin


def solve():
    n = int(stdin.readline())

    for _ in range(3):
        a = [0] + list(map(int, stdin.readline().split()))

        s = [a[0]]
        for ai in a[1:]:
            s.append(s[-1] + ai)

        m = [float("inf")] * (n + 1)
        m[0] = 0

        for i in range(1, n + 1):
            for j in range(i):
                m[i] = min(m[i], s[i] - m[j])

        if 2 * m[-1] == s[-1]:
            print("D")
        elif 2 * m[-1] < s[-1]:
            print("A")
        else:
            print("B")


if __name__ == "__main__":
    solve()
