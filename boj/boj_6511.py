from sys import stdin


def solve():
    while True:
        n, m, c = map(int, stdin.readline().split())
        if n == 0 and m == 0 and c == 0:
            break

        k = (m - 7) * (n - 7)
        if k % 2 == 0:
            print(k // 2)
        else:
            if c == 0:
                print(k // 2)
            else:
                print(k // 2 + 1)


if __name__ == "__main__":
    solve()
