from collections import deque


def main():
    n, m = map(int, input().split())
    board = [list(map(int, input())) for _ in range(n)]
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    q = deque([(0, 0, 0)])
    while q:
        x, y, z = q.popleft()
        if x == n - 1 and y == m - 1:
            print(visited[x][y][z])
            return
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append((nx, ny, z))
            if board[nx][ny] == 1 and z == 0:
                visited[nx][ny][1] = visited[x][y][z] + 1
                q.append((nx, ny, 1))
    print(-1)


if __name__ == "__main__":
    main()
