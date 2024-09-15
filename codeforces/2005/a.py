from sys import stdin


def solve():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        cnt_a = n // 5 + (1 if n % 5 > 0 else 0)
        cnt_e = n // 5 + (1 if n % 5 > 1 else 0)
        cnt_i = n // 5 + (1 if n % 5 > 2 else 0)
        cnt_o = n // 5 + (1 if n % 5 > 3 else 0)
        cnt_u = n // 5 + (1 if n % 5 > 4 else 0)
        print("a" * cnt_a + "e" * cnt_e + "i" * cnt_i + "o" * cnt_o + "u" * cnt_u)


if __name__ == "__main__":
    solve()
