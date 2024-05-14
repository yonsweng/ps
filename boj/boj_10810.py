from sys import stdin


def main():
    n, m = map(int, stdin.readline().split())
    balls = [0] * n

    for _ in range(m):
        i, j, k = map(int, stdin.readline().split())

        for l in range(i - 1, j):
            balls[l] = k

    print(" ".join(map(str, balls)))


if __name__ == "__main__":
    main()
