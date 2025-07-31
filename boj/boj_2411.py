from collections import deque
from sys import stdin


def solve():
    N, M, A, B = map(int, stdin.readline().split())
    board = [[0] * (M + 1) for _ in range(N + 1)]

    items = [tuple(map(int, stdin.readline().split())) for _ in range(A)]

    for _ in range(B):
        x, y = map(int, stdin.readline().split())
        board[x][y] = -1

    items.sort(key=lambda x: x[0] + x[1])

    for i in range(1, A):
        # Calculate the diagonal sums for the current and previous items
        prev_diagonal_sum = items[i - 1][0] + items[i - 1][1]
        curr_diagonal_sum = items[i][0] + items[i][1]
        
        # Check if the current and previous items are on the same diagonal but not in the same row
        if prev_diagonal_sum == curr_diagonal_sum and items[i - 1][0] != items[i][0]:
            print(0)
            return
        
    items.append((N, M))

    q = deque([(1, 1)])
    inq = {(1, 1)}
    a = 0
    board[1][1] = 1
    for x, y in items:
        while q:
            cx, cy = q.popleft()
            inq.remove((cx, cy))
            if (cx, cy) == (x, y):
                a += 1
                q = deque([(cx, cy)])
                inq = {(cx, cy)}
                break
            for dx, dy in [(0, 1), (1, 0)]:
                nx, ny = cx + dx, cy + dy
                if nx <= x and ny <= y and board[nx][ny] != -1:
                    board[nx][ny] += board[cx][cy]
                    if (nx, ny) not in inq:
                        q.append((nx, ny))
                        inq.add((nx, ny))
        else:
            print(0)
            return
        
    print(board[N][M])


if __name__ == "__main__":
    solve()
