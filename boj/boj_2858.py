from sys import stdin


def solve():
    R, B = map(int, stdin.readline().split())

    for L in range(3, R + 1):
        if (R + B) % L == 0:
            W = (R + B) // L
            if W >= 3 and 2 * (L + W) - 4 == R:
                if L <= W:
                    L, W = W, L
                print(L, W)
                return


if __name__ == "__main__":
    solve()
 