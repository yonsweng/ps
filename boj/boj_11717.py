from sys import stdin


def grundy(board, y1, y2, x1, x2, g):
    if y1 > y2 or x1 > x2:
        return 0

    if g[y1][y2][x1][x2] != -1:
        return g[y1][y2][x1][x2]

    s = set()
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            if board[y][x] == "X":
                continue
            s.add(
                grundy(board, y1, y - 1, x1, x - 1, g)
                ^ grundy(board, y + 1, y2, x1, x - 1, g)
                ^ grundy(board, y1, y - 1, x + 1, x2, g)
                ^ grundy(board, y + 1, y2, x + 1, x2, g)
            )

    mex = 0
    for si in sorted(s):
        if si == mex:
            mex += 1
        else:
            break

    g[y1][y2][x1][x2] = mex
    return mex


def main():
    h, w = map(int, stdin.readline().rstrip().split())
    board = [stdin.readline().rstrip() for _ in range(h)]
    g = [[[[-1] * w for _ in range(w)] for _ in range(h)] for _ in range(h)]

    print("First" if grundy(board, 0, h - 1, 0, w - 1, g) else "Second")


if __name__ == "__main__":
    main()
