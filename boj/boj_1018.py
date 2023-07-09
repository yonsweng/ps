n, m = map(int, input().split())
board = [input() for _ in range(n)]

answer = 99
for i in range(n - 7):
    for j in range(m - 7):
        cnt1 = 0
        cnt2 = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != "W":
                        cnt1 += 1
                    if board[k][l] != "B":
                        cnt2 += 1
                else:
                    if board[k][l] != "B":
                        cnt1 += 1
                    if board[k][l] != "W":
                        cnt2 += 1
        answer = min(answer, min(cnt1, cnt2))

print(answer)
