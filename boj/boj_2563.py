def main():
    n = int(input())
    board = [[0] * 100 for _ in range(100)]
    for _ in range(n):
        x, y = map(int, input().split())
        for i in range(10):
            for j in range(10):
                board[x + i][y + j] = 1

    print(sum(sum(row) for row in board))


if __name__ == "__main__":
    main()
