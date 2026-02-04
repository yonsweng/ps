from sys import stdin


def solve():
    N, K = map(int, stdin.readline().split())
    T = [int(stdin.readline()) for _ in range(N)]

    diffs = []
    for i in range(N - 1):
        diffs.append(T[i + 1] - T[i] - 1)

    diffs.sort()

    result = T[-1] - T[0] + 1
    for diff in diffs[N - K :]:
        result -= diff

    print(result)


if __name__ == "__main__":
    solve()
