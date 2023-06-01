from sys import stdin


def dfs(board, visited, i, j):
    n = len(board)
    if i < 0 or i >= n or j < 0 or j >= n:
        return 0
    if board[i][j] == "0" or visited[i][j]:
        return 0
    visited[i][j] = True
    return (
        1
        + dfs(board, visited, i - 1, j)
        + dfs(board, visited, i + 1, j)
        + dfs(board, visited, i, j - 1)
        + dfs(board, visited, i, j + 1)
    )


def solve():
    n = int(stdin.readline())
    board = [stdin.readline().rstrip() for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    answer = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == "1" and not visited[i][j]:
                answer.append(dfs(board, visited, i, j))
    print(len(answer))
    for a in sorted(answer):
        print(a)


if __name__ == "__main__":
    solve()
