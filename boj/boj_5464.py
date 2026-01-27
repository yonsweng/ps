from collections import deque
from sys import stdin


def solve():
    N, M = map(int, stdin.readline().split())
    rates = [int(stdin.readline()) for _ in range(N)]
    weights = [int(stdin.readline()) for _ in range(M)]

    spaces = [0] * N
    cars = {}
    queue = deque()

    dollars = 0

    for _ in range(2 * M):
        order = int(stdin.readline().strip())
        if order > 0:
            try:
                empty_index = spaces.index(0)
            except ValueError:
                queue.append(order)
                continue
            dollars += rates[empty_index] * weights[order - 1]
            spaces[empty_index] = order
            cars[order] = empty_index
        else:
            space_index = cars[-order]
            spaces[space_index] = 0
            del cars[-order]
            if queue:
                next_car = queue.popleft()
                dollars += rates[space_index] * weights[next_car - 1]
                spaces[space_index] = next_car
                cars[next_car] = space_index

    print(dollars)


if __name__ == "__main__":
    solve()
