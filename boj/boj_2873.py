from sys import stdin


def main():
    r, c = map(int, stdin.readline().split())
    board = [list(map(int, stdin.readline().split())) for _ in range(r)]

    answer = []
    if r % 2 == 1:
        for i in range(r):
            if i == r - 1:
                answer.append("R" * (c - 1))
            elif i % 2 == 0:
                answer.append("R" * (c - 1) + "D")
            else:
                answer.append("L" * (c - 1) + "D")
    elif c % 2 == 1:
        for i in range(c):
            if i == c - 1:
                answer.append("D" * (r - 1))
            elif i % 2 == 0:
                answer.append("D" * (r - 1) + "R")
            else:
                answer.append("U" * (r - 1) + "R")
    else:
        min_xy = (0, 1)
        for i in range(r):
            for j in range(c):
                if (i + j) % 2 == 1:
                    if board[min_xy[0]][min_xy[1]] > board[i][j]:
                        min_xy = (i, j)

        # avoid the min_xy and visit all cells and arrive at (r-1, c-1)
        for i in range(min_xy[0] // 2):
            answer.append("R" * (c - 1) + "D" + "L" * (c - 1) + "D")
        for i in range(min_xy[1] // 2):
            answer.append("DRUR")
        if min_xy[0] % 2 == 0:  # min_xy is in the even row
            answer.append("DR")
        else:
            answer.append("RD")
        for i in range((c - 1 - min_xy[1]) // 2):
            answer.append("RURD")
        for i in range((r - 1 - min_xy[0]) // 2):
            answer.append("D" + "L" * (c - 1) + "D" + "R" * (c - 1))

    answer = "".join(answer)
    print(answer)


if __name__ == "__main__":
    main()
