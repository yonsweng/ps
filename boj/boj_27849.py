from sys import stdin


def solve():
    n, t = map(int, stdin.readline().split())

    answer = 0
    l = 0
    for _ in range(n):
        d, b = map(int, stdin.readline().split())
        prev_l = l
        l = min(t, d + b - 1 + max(0, l - d + 1))
        answer += l - max(prev_l, d - 1)

    print(answer)


if __name__ == "__main__":
    solve()
