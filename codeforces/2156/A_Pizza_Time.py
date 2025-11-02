from sys import stdin


def solve():
    t = int(stdin.readline().strip())
    for _ in range(t):
        n = int(stdin.readline().strip())
        total_hao = 0
        while n > 2:
            hao = n // 3
            n -= 2 * hao
            total_hao += hao
        print(total_hao)


if __name__ == "__main__":
    solve()
