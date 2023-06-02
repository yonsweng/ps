from sys import stdin


def solve():
    n = int(stdin.readline())
    cnt = [0] * 10001
    for _ in range(n):
        a = int(stdin.readline())
        cnt[a] += 1

    for i in range(1, 10001):
        for _ in range(cnt[i]):
            print(i, flush=False)


if __name__ == "__main__":
    solve()
