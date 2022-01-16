from sys import stdin
from collections import deque


DIRECTION = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def read_input():
    n, m = map(int, stdin.readline().split())
    return n, m


def solve(n, m):
    grid = [[0] * m for _ in range(n)]
    s = set([((n-1)//2, (m-1)//2), ((n-1)//2, m//2), (n//2, (m-1)//2), (n//2, m//2)])
    q = deque()
    for i, j in s:
        grid[i][j] = n//2 + m//2
        q.append((i, j))
    while len(q) > 0:
        i, j = q.popleft()
        for di, dj in DIRECTION:
            if 0<=i+di<n and 0<=j+dj<m and grid[i+di][j+dj] == 0:
                grid[i+di][j+dj] = grid[i][j] + 1
                q.append((i+di, j+dj))
    arr = []
    for i in range(n):
        for j in range(m):
            arr.append(grid[i][j])
    return ' '.join(map(str, sorted(arr)))


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
