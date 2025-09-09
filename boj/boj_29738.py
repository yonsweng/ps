from sys import stdin


def solve():
    T = int(stdin.readline().strip())
    for t in range(1, T + 1):
        N = int(stdin.readline().strip())
        if N <= 25:
            result = "World Finals"
        elif N <= 1000:
            result = "Round 3"
        elif N <= 4500:
            result = "Round 2"
        else:
            result = "Round 1"
        print(f"Case #{t}: {result}")


if __name__ == "__main__":
    solve()
