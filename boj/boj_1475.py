from sys import stdin


def solve():
    N = int(stdin.readline().strip())

    cnt = {}
    while N > 0:
        num = N % 10
        if num == 9:
            num = 6
        if num in cnt:
            cnt[num] += 1
        else:
            cnt[num] = 1
        N //= 10

    cnt[6] = (cnt.get(6, 0) + 1) // 2

    max_cnt = 0
    for num, count in cnt.items():
        if count > max_cnt:
            max_cnt = count

    print(max_cnt)


if __name__ == "__main__":
    solve()
