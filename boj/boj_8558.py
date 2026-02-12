from sys import stdin


def solve():
    n = int(stdin.read().strip())
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % 10
    print(result)


if __name__ == "__main__":
    solve()
