from sys import stdin


def solve():
    N, K = map(int, stdin.readline().split())
    count = 0
    for i in range(1, N + 1):
        if N % i == 0:
            count += 1
            if count == K:
                print(i)
                return
    print(0)


if __name__ == "__main__":
    solve()
