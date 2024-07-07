from sys import stdin


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def counter_clockwise_direction(d):
    if d == 0:
        return 3
    else:
        return d - 1
    

def is_valid_position(i, j, N, M):
    if 0 <= i < N and 0 <= j < M:
        return True
    return False


def solve():
    N, M = map(int, stdin.readline().split())
    r, c, d = map(int, stdin.readline().split())

    board = []
    for _ in range(N):
        row = list(map(int, stdin.readline().split()))
        board.append(row)

    count = 0
    while True:
        if board[r][c] == 0:
            board[r][c] = 2
            count += 1

        for _ in range(4):
            d = counter_clockwise_direction(d)
            ni = r + di[d]
            nj = c + dj[d]
            if is_valid_position(ni, nj, N, M) and board[ni][nj] == 0:
                r, c = ni, nj
                break
        else:
            ni = r - di[d]
            nj = c - dj[d]
            if is_valid_position(ni, nj, N, M) and board[ni][nj] != 1:
                r, c = ni, nj
            else:
                break

    print(count)


if __name__ == '__main__':
    solve()
