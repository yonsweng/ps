import heapq
from sys import stdin


def dist(location1, location2):
    return abs(location1[0] - location2[0]) + abs(location1[1] - location2[1])


def calc_duration(space, shark_size, shark_location, N):
    # Do BFS with priority queue
    visited = set()
    queue = [(0, shark_location)]
    heapq.heapify(queue)
    while queue:
        dist, (x, y) = heapq.heappop(queue)
        if 0 < space[x][y] < shark_size:
            return dist, space[x][y], (x, y)
        for d in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < N and 0 <= ny < N and space[nx][ny] <= shark_size and (nx, ny) not in visited:
                visited.add((nx, ny))
                heapq.heappush(queue, (dist + 1, (nx, ny)))
    return float("inf"), None, None


def solve():
    N = int(stdin.readline().strip())
    space = []
    for _ in range(N):
        space.append(list(map(int, stdin.readline().strip().split())))

    state_locations = {1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 9: set()}
    for i in range(N):
        for j in range(N):
            state = space[i][j]
            if state != 0:
                state_locations[state].add((i, j))

    duration = 0
    shark_location = state_locations[9].pop()
    shark_size = 2
    shark_ate = 0
    while True:
        space[shark_location[0]][shark_location[1]] = 0
        current_duration, next_state, next_location = calc_duration(space, shark_size, shark_location, N)
        if current_duration == float("inf"):
            break

        duration += current_duration
        shark_location = next_location
        state_locations[next_state].discard(next_location)
        if not state_locations[next_state]:
            del state_locations[next_state]
        shark_ate += 1
        if shark_ate == shark_size:
            shark_size += 1
            shark_ate = 0

    print(duration)


if __name__ == "__main__":
    solve()
