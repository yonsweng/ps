from sys import stdin


def solve():
    N = int(stdin.readline().strip())
    pos = [0] + list(map(int, stdin.readline().strip().split()))
    truck, heli = map(int, stdin.readline().strip().split())

    pos.sort()
    acc = [0] * (N + 1)
    for i in range(1, N + 1):
        acc[i] = acc[i - 1] + pos[i]

    cost = [[0, 0] for _ in range(N + 1)]
    for i in range(1, N + 1):
        cost[i][0] = float('inf')
        for j in range(i):
            cost[i][0] = min(
                cost[i][0],
                cost[j][1] + truck * (acc[i] - acc[j] - (i - j) * pos[j]),
            )

        cost[i][1] = float('inf')
        for j in range(i):
            cost[i][1] = min(
                cost[i][1],
                min(cost[j][0], cost[j][1]) + truck * ((i - j - 1) * pos[i] - (acc[i-1] - acc[j])) + heli,
            )

    print(min(cost[N][0], cost[N][1]))


if __name__ == "__main__":
    solve()
