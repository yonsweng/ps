from itertools import product


def dfs(board, visited, color, row, col, same_colors):
    if visited[row][col] or board[row][col] != color:
        return

    same_colors.append((row, col))
    visited[row][col] = True

    dfs(board, visited, color, row-1, col, same_colors)
    dfs(board, visited, color, row, col+1, same_colors)
    dfs(board, visited, color, row+1, col, same_colors)
    dfs(board, visited, color, row, col-1, same_colors)


def eat(board, macarons_to_eat):
    for row, col in macarons_to_eat:
        board[row][col] = 0

    for col in range(1, 7):
        tmp_col = [board[row][col] for row in range(6, 0, -1) if board[row][col] != 0]
        tmp_col = tmp_col + [0] * (6 - len(tmp_col))
        for row, color in zip(range(6, 0, -1), tmp_col):
            board[row][col] = color


def put(board, col, color):
    for row in range(6, 0, -1):
        if board[row][col] == 0:
            board[row][col] = color
            break

    while True:
        macarons_to_eat = []
        visited = [[False] * 8 for _ in range(8)]

        for row, col in product(range(1, 7), range(1, 7)):
            if visited[row][col] or board[row][col] == 0:
                continue

            same_colors = []
            dfs(board, visited, board[row][col], row, col, same_colors)

            if len(same_colors) >= 3:
                macarons_to_eat += same_colors

        if len(macarons_to_eat) == 0:
            break

        eat(board, macarons_to_eat)


def solution(macarons):
    answer = []
    board = [[0] * 8 for _ in range(8)]

    for macaron in macarons:
        pos, color = macaron[0], macaron[1]
        put(board, pos, color)
        answer = [''.join(map(str, row[1:-1])) for row in board[1:-1]]
        print(answer)

    answer = [''.join(map(str, row[1:-1])) for row in board[1:-1]]
    return answer


macaron = [[1,1],[2,1],[1,2],[3,3],[6,4],[3,1],[3,3],[3,3],[3,4],[2,1]]
result = solution(macaron)
print(result)
