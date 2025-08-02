from sys import stdin


def solve():
    """
    Solves a cost minimization problem involving two types of transportation: truck and helicopter.

    Input (read from stdin):
        - First line: integer N, the number of delivery locations.
        - Second line: N space-separated integers, the positions of the delivery locations.
        - Third line: two integers, truck and heli, representing the cost per unit distance for truck and the fixed cost for helicopter, respectively.

    Algorithm:
        - Uses dynamic programming to compute the minimum cost to deliver to all locations, considering two options at each step:
            1. Deliver using only trucks.
            2. Use a helicopter for the last segment.
        - Maintains cumulative position sums and cost tables for both options.

    Output:
        - Prints the minimum total cost to deliver to all locations.
    """
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
