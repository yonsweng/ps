from sys import stdin


def solve():
    N, L = map(int, stdin.readline().strip().split())
    pools = [
        (x, y)
        for x, y in (map(int, stdin.readline().strip().split()) for _ in range(N))
    ]

    pools.sort()

    current_position = 0
    total_jump_count = 0
    for pool in pools:
        s, e = pool
        if current_position < s:
            jump_count = (e - s + L - 1) // L
            total_jump_count += jump_count
            current_position = s + jump_count * L
        elif current_position < e:
            jump_count = (e - current_position + L - 1) // L
            total_jump_count += jump_count
            current_position += jump_count * L

    print(total_jump_count)


if __name__ == "__main__":
    solve()
