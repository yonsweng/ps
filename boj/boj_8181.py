from sys import stdin


def solve():
    t = int(stdin.readline().strip())
    for _ in range(t):
        n, m = map(int, stdin.readline().strip().split())

        a = [
            list(map(int, stdin.readline().strip().split()))
            for _ in range(n)
        ]

        b = [
            list(map(int, stdin.readline().strip().split()))
            for _ in range(n)
        ]

        xy = [(-1, -1)] * 2000001
        for i in range(n):
            for j in range(m):
                xy[b[i][j] + 1000000] = (i, j)

        x = [-1] * n
        y = [-1] * m
        nie = False
        for i in range(n):
            for j in range(m):
                to_x, to_y = xy[a[i][j] + 1000000]
                if to_x == -1 or to_y == -1:
                    nie = True
                    break
                if x[i] != -1 and x[i] != to_x:
                    nie = True
                    break
                if y[j] != -1 and y[j] != to_y:
                    nie = True
                    break
                x[i] = to_x
                y[j] = to_y
            if nie:
                break

        if not nie:
            print("TAK", flush=False)
        else:
            print("NIE", flush=False)


if __name__ == "__main__":
    solve()
