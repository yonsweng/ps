from sys import stdin


def move_pawn(i: int, j: int, board: list, is_black: bool):
    directions = [(1, -1), (1, 1)] if is_black else [(-1, -1), (-1, 1)]
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < 8 and 0 <= nj < 8 and board[ni][nj] == 0:
            board[ni][nj] = 1


def move_knight(i: int, j: int, board: list):
    directions = [
        (-2, -1),
        (-2, 1),
        (-1, -2),
        (-1, 2),
        (1, -2),
        (1, 2),
        (2, -1),
        (2, 1),
    ]
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < 8 and 0 <= nj < 8 and board[ni][nj] == 0:
            board[ni][nj] = 1


def move_bishop(i: int, j: int, board: list):
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for di, dj in directions:
        ni, nj = i + di, j + dj
        while 0 <= ni < 8 and 0 <= nj < 8:
            if board[ni][nj] == 2:
                break
            board[ni][nj] = 1
            ni += di
            nj += dj


def move_rook(i: int, j: int, board: list):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for di, dj in directions:
        ni, nj = i + di, j + dj
        while 0 <= ni < 8 and 0 <= nj < 8:
            if board[ni][nj] == 2:
                break
            board[ni][nj] = 1
            ni += di
            nj += dj


def move_queen(i: int, j: int, board: list):
    move_bishop(i, j, board)
    move_rook(i, j, board)


def move_king(i: int, j: int, board: list):
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < 8 and 0 <= nj < 8 and board[ni][nj] == 0:
            board[ni][nj] = 1


def count_unoccupied_squares(fen_description: str) -> int:
    board = [[0] * 8 for _ in range(8)]
    rows = fen_description.split("/")
    pieces = []

    # First pass: mark all piece positions
    for i, row in enumerate(rows):
        j = 0
        for char in row:
            if char.isdigit():
                j += int(char)
                continue
            board[i][j] = 2
            pieces.append((i, j, char))
            j += 1

    # Second pass: calculate moves for each piece
    for i, j, char in pieces:
        if char == "P":
            move_pawn(i, j, board, False)
        elif char == "p":
            move_pawn(i, j, board, True)
        elif char == "N" or char == "n":
            move_knight(i, j, board)
        elif char == "B" or char == "b":
            move_bishop(i, j, board)
        elif char == "R" or char == "r":
            move_rook(i, j, board)
        elif char == "Q" or char == "q":
            move_queen(i, j, board)
        elif char == "K" or char == "k":
            move_king(i, j, board)

    unoccupied_count = 0
    for i in range(8):
        for j in range(8):
            if not board[i][j]:
                unoccupied_count += 1
    return unoccupied_count


def solve():
    while True:
        fen_description = stdin.readline().strip()
        if fen_description == "":
            break

        answer = count_unoccupied_squares(fen_description)
        print(answer)


if __name__ == "__main__":
    solve()
