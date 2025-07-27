from sys import stdin


def solve():
    a = []
    for _ in range(5):
        a.append(int(stdin.readline().strip()))
    a.sort()
    print(sum(a) // 5)
    print(a[2])  # Print the median value


if __name__ == "__main__":
    solve()
