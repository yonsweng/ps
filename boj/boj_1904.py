from sys import stdin


def solve():
    N = int(stdin.readline().strip())

    result = [0, 1, 2]
    for i in range(3, N + 1):
        result.append((result[i - 1] + result[i - 2]) % 15746)

    print(result[N])


if __name__ == "__main__":
    solve()
