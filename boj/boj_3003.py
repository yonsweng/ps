from sys import stdin


def solve():
    pieces = list(map(int, stdin.readline().split()))
    chess = [1, 1, 2, 2, 2, 8]
    for i in range(6):
        print(chess[i] - pieces[i], end=" ")


if __name__ == "__main__":
    solve()
