from sys import stdin


def solve():
    while True:
        w = float(stdin.readline().strip())
        if w < 0:
            break
        print(
            "Objects weighing %.2f on Earth will weigh %.2f on the moon."
            % (w, w * 0.167)
        )


if __name__ == "__main__":
    solve()
