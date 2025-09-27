from sys import stdin


def solve():
    for _ in range(2):
        T, F, S, P, C = map(int, stdin.readline().strip().split())
        total_points = T * 6 + F * 3 + S * 2 + P * 1 + C * 2
        print(total_points, end=' ')


if __name__ == "__main__":
    solve()
