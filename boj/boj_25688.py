from collections import deque
from sys import stdin


def solve():
    board = [list(map(int, stdin.readline().split())) for _ in range(5)]
    r, c = map(int, stdin.readline().split())

    dp = [[[99] * 64 for _ in range(5)] for _ in range(5)]
    inq = set()
    q = deque([(r, c, 0)])  # (row, col, visited)

    dp[r][c][0] = 0
    inq.add((r, c, 0))

    answer = -1

    while q:
        row, col, visited = q.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc

            if 0 <= nr < 5 and 0 <= nc < 5 and board[nr][nc] != -1:
                if board[nr][nc] == 0:
                    nvisited = visited
                else:
                    nvisited = visited | (1 << (board[nr][nc] - 1))

                if dp[nr][nc][nvisited] > dp[row][col][visited] + 1:
                    dp[nr][nc][nvisited] = dp[row][col][visited] + 1

                    if nvisited == 63:
                        answer = dp[nr][nc][nvisited]
                        break

                    if (nr, nc, nvisited) not in inq:
                        q.append((nr, nc, nvisited))
                        inq.add((nr, nc, nvisited))

        if answer != -1:
            break

    print(answer)


if __name__ == "__main__":
    solve()
