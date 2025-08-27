from sys import stdin


def solve():
    K, N, M = map(int, stdin.readline().split())

    drivers = [[0, 0, 0] for _ in range(N)]  # [checkpoints, time]
    for i in range(M):
        X, Y = map(int, stdin.readline().split())
        if Y == (drivers[X-1][0] % K) + 1:
            drivers[X-1][0] += 1
            drivers[X-1][1] = i

    for i in range(N):
        drivers[i][2] = i + 1

    drivers.sort(key=lambda x: (-x[0], x[1]))

    print(" ".join(str(driver[2]) for driver in drivers))


if __name__ == "__main__":
    solve()
