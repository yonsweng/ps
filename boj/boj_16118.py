from heapq import heappop, heappush
from sys import stdin


def solve():
    N, M = map(int, stdin.readline().split())
    adj = [{} for _ in range(N + 1)]
    for _ in range(M):
        a, b, d = map(int, stdin.readline().split())
        adj[a][b] = d * 2
        adj[b][a] = d * 2

    fox_dist = [float("inf")] * (N + 1)
    fox_dist[1] = 0

    fox_queue = [(0, 1)]  # (distance, node)
    while fox_queue:
        dist, current = heappop(fox_queue)

        if dist > fox_dist[current]:
            continue

        for neighbor, weight in adj[current].items():
            new_dist = dist + weight
            if new_dist < fox_dist[neighbor]:
                fox_dist[neighbor] = new_dist
                heappush(fox_queue, (new_dist, neighbor))

    wolf_dist = [[float("inf")] * 2 for _ in range(N + 1)]
    wolf_dist[1][0] = 0

    wolf_queue = [(0, 1, 0)]  # (distance, node, parity: 0=odd, 1=even)
    while wolf_queue:
        dist, current, parity = heappop(wolf_queue)

        if dist > wolf_dist[current][parity]:
            continue

        for neighbor, weight in adj[current].items():
            if parity == 0:  # odd time: add half of the distance
                new_dist = dist + weight // 2
                new_parity = 1  # next move will be even
            else:  # even time: add twice the distance
                new_dist = dist + weight * 2
                new_parity = 0  # next move will be odd

            if new_dist < wolf_dist[neighbor][new_parity]:
                wolf_dist[neighbor][new_parity] = new_dist
                heappush(wolf_queue, (new_dist, neighbor, new_parity))

    answer = 0
    for i in range(2, N + 1):
        if fox_dist[i] < min(wolf_dist[i][0], wolf_dist[i][1]):
            answer += 1

    print(answer)


if __name__ == "__main__":
    solve()
