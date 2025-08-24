from sys import stdin


def solve():
    N = int(stdin.readline().strip())
    paper = [list(map(int, stdin.readline().strip().split())) for _ in range(N)]
    # 색종이의 개수를 세기 위한 변수
    white = 0
    blue = 0

    # 색종이를 나누는 함수
    def divide_paper(x, y, size):
        nonlocal white, blue
        color = paper[x][y]
        for i in range(x, x + size):
            for j in range(y, y + size):
                if paper[i][j] != color:
                    # 색종이가 섞여있다면 4등분
                    divide_paper(x, y, size // 2)
                    divide_paper(x, y + size // 2, size // 2)
                    divide_paper(x + size // 2, y, size // 2)
                    divide_paper(x + size // 2, y + size // 2, size // 2)
                    return
        if color == 0:
            white += 1
        else:
            blue += 1

    divide_paper(0, 0, N)
    print(white)
    print(blue)


if __name__ == "__main__":
    solve()
