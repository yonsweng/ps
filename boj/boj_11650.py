from sys import stdin

n = int(stdin.readline())
points = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
points.sort()
for point in points:
    print(*point, flush=False)
