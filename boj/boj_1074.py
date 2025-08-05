from sys import stdin


def find_z_order(N, r, c):
    if N == 1:
        return 0
    mid = N // 2
    if r < mid and c < mid:  # Top-left quadrant
        return find_z_order(mid, r, c)
    elif r < mid and c >= mid:  # Top-right quadrant
        return (mid * mid) + find_z_order(mid, r, c - mid)
    elif r >= mid and c < mid:  # Bottom-left quadrant
        return (2 * mid * mid) + find_z_order(mid, r - mid, c)
    else:  # Bottom-right quadrant
        return (3 * mid * mid) + find_z_order(mid, r - mid, c - mid)


def solve():
    N, r, c = map(int, stdin.readline().split())

    answer = find_z_order(2 ** N, r, c)
    print(answer)


if __name__ == "__main__":
    solve()
