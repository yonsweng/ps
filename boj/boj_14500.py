from sys import stdin


def rotate(tetromino):
    tetromino = [(c, -r) for r, c in tetromino]
    min_r, min_c = min(tetromino)
    tetromino = [(r - min_r, c - min_c) for r, c in tetromino]
    return tetromino


def flip_horizontal(tetromino):
    tetromino = [(-r, c) for r, c in tetromino]
    min_r, min_c = min(tetromino)
    tetromino = [(r - min_r, c - min_c) for r, c in tetromino]
    return tetromino


def flip_vertical(tetromino):
    tetromino = [(r, -c) for r, c in tetromino]
    min_r, min_c = min(tetromino)
    tetromino = [(r - min_r, c - min_c) for r, c in tetromino]
    return tetromino


def main():
    tetrominoes = [
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (0, 1), (1, 0), (1, 1)],
        [(0, 0), (1, 0), (2, 0), (2, 1)],
        [(0, 0), (1, 0), (1, 1), (2, 1)],
        [(0, 0), (0, 1), (0, 2), (1, 1)],
    ]

    n, m = map(int, stdin.readline().split())
    board = [list(map(int, stdin.readline().split())) for _ in range(n)]

    def check(r, c):
        if 0 <= r < n and 0 <= c < m:
            return True
        return False

    def get_sum(r, c, tetromino):
        value = 0
        for dr, dc in tetromino:
            nr, nc = r + dr, c + dc
            if check(nr, nc):
                value += board[nr][nc]
            else:
                return 0
        return value

    def get_max_sum(tetromino):
        max_sum = 0
        for r in range(n):
            for c in range(m):
                sum_value = get_sum(r, c, tetromino)
                if sum_value > max_sum:
                    max_sum = sum_value
        return max_sum

    max_sum = 0
    for tetromino in tetrominoes:
        for _ in range(4):
            tetromino_flipped_horizontal = flip_horizontal(tetromino)
            tetromino_flipped_vertical = flip_vertical(tetromino)
            s1 = max(max_sum, get_max_sum(tetromino))
            s2 = max(max_sum, get_max_sum(tetromino_flipped_horizontal))
            s3 = max(max_sum, get_max_sum(tetromino_flipped_vertical))
            max_sum = max(max_sum, s1, s2, s3)
            tetromino = rotate(tetromino)

    print(max_sum)


if __name__ == "__main__":
    main()
