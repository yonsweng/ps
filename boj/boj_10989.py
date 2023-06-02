from sys import stdin


def solve():
    n = int(stdin.readline())
    cnt = [0] * 10001
    for _ in range(n):
        a = int(stdin.readline())
        cnt[a] += 1

    flush_cnt = 0
    for i in range(1, 10001):
        for _ in range(cnt[i]):
            print(i, flush=False)
            flush_cnt += 1
            if flush_cnt % 500 == 0:
                print(end="", flush=True)


if __name__ == "__main__":
    solve()
