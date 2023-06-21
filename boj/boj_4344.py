from sys import stdin


def solve():
    c = int(stdin.readline())
    for _ in range(c):
        n, *scores = map(int, stdin.readline().split())
        sum_scores = sum(scores)
        print(
            f"{int(len([s for s in scores if s * n > sum_scores]) / n * 100000 + 0.5) / 1000:.3f}%"
        )


if __name__ == "__main__":
    solve()
