from sys import stdin


def solve():
    N = int(stdin.readline())
    cows = [[int(x) for x in stdin.readline().strip()] for _ in range(N)]

    count = 0
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            if cows[i][j] == 1:
                count += 1
                for k in range(i + 1):
                    for l in range(j + 1):
                        cows[k][l] = 1 - cows[k][l]
    print(count)


if __name__ == "__main__":
    solve()
