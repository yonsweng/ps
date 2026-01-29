from sys import stdin


def solve():
    h, w = map(int, stdin.readline().split())
    grid = [list(stdin.readline().strip()) for _ in range(h)]

    wing = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w - 2, -1, -1):
            if grid[i][j] == "." and grid[i][j + 1] == ".":
                wing[i][j] = wing[i][j + 1] + 1

    result = -1
    for j in range(w - 2, -1, -1):
        lower, upper = 1, w - j - 1
        while lower <= upper:
            b = (lower + upper) // 2
            indices = []
            valid = False
            i = 0
            while i < h:
                if grid[i][j] == "#":
                    indices = []
                elif wing[i][j] >= b:
                    if len(indices) == 2:
                        valid = True
                        result = max(result, (i - indices[0] + 1) + 3 * b)
                    else:
                        indices.append(i)
                        i += 1

                i += 1

            if valid:
                lower = b + 1
            else:
                upper = b - 1

    print(result)


if __name__ == "__main__":
    solve()
